import os, re, simplejson, boto3
from flask import Flask, request
from twilio.rest import Client

app = Flask(__name__)


@app.route('/parse_email', methods=['POST'])
def email():

	#Retrieve email headers and extract fax number
	email_headers = simplejson.loads(request.values.get('envelope'))
	to_email = email_headers['to'][0].split('@')
	
	#Retrieve attachment and save it to the root directory
	attachment = None
	num_attachments = int(request.form.get('attachments', 0))
	if(num_attachments > 0):
		for num in range(1, (num_attachments + 1)):
  			attachment = request.files.get(('attachment%d' % num))
  			attachment.save(attachment.filename)
  			media_url = upload_file(attachment.filename)
  			send_fax(to_email[0], media_url)
		return "OK"
	else:
		return "No attachments found"
	

def send_fax(to, media_url):
	#Send fax via Twilio API
	username = os.environ['TWILIO_ACCOUNT_SID']
	password = os.environ['TWILIO_AUTH_TOKEN']
	from_ = os.environ['TWILIO_NUMBER']

	#Validate the destination number is valid, and send the fax
	if(re.match('[+]\d+',to)):
		client = Client(username, password)
		fax = client.fax.faxes.create(
				from_ = from_, 
				to = to, 
				media_url = media_url
			)
		return 'OK'
	else:
		return 'Failed'

def upload_file(filename):	
	#Upload file to S3 bucket and set public access to read
	s3 = boto3.client('s3')
	bucket_name = os.environ['S3_FAX_BUCKET']
	file_url = 'https://' + bucket_name + '.s3.us-east-2.amazonaws.com/' + filename
	s3.upload_file(filename, bucket_name, filename)
	s3.put_object_acl(ACL='public-read', Bucket=bucket_name, Key=filename)

	return file_url


if __name__ == "__main__":
    app.run(debug=True)

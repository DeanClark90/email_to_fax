# Email to Fax Sample APP
Sample app provides details on how you can utilize the SendGrid Parse Webhook, to receive receive the contents of an email, store the attachment in an S3 bucket and send it as a fax using Twilio.
## Requirements
* A Twilio, account, you can sign up here: https://www.twilio.com/try-twilio 
* A SendGrid account, you can sign up here: https://signup.sendgrid.com/
* For details on setting up the SendGrid Parse Webhook please see https://sendgrid.com/docs/for-developers/parsing-email/setting-up-the-inbound-parse-webhook/ 

# Setting Up
We assume that before you begin, you will have Python and pip installed on your system and available at the command line.

Before you can run this project, you will need to set four system environment variables. These are:

    TWILIO_ACCOUNT_SID : Get it from your Twilio Console.
    TWILIO_AUTH_TOKEN : Same as above.
    TWILIO_NUMBER : A Twilio number that you own, that can be used for making calls and sending messages. You can find a list of phone numbers you control (and buy another one, if necessary) in the console.
    S3_FAX_BUCKET : AWS S3 Bucket where the files will be stored

For Mac and Linux, environment variables can be set by opening a terminal window and typing the following three commands - replace all the characters after the = with values from your Twilio account:

    export TWILIO_ACCOUNT_SID=ACXXXXXXXXX
    export TWILIO_AUTH_TOKEN=XXXXXXXXX
    export TWILIO_PHONE_NUMBER=+1XXXXXXXXX
    export S3_FAX_BUCKET=BUCKET_NAME

On Windows, the easiest way to set permanent environment variables (as of Windows 8) is using the setx command. Note that there is no =, just the key and value separated by a space:

    setx TWILIO_ACCOUNT_SID ACXXXXXXXXX
    setx TWILIO_AUTH_TOKEN XXXXXXXXX
    setx TWILIO_PHONE_NUMBER +1XXXXXXXXXX
    setx S3_FAX_BUCKET=BUCKET_NAME
    
# Running the Application

Clone this repository. Navigate to the folder with the source code on your machine in a terminal window.
From there we recommend creating a virtualenv and activating it to avoid installing dependencies globaly on your computer.

    virtualenv -p python3 env source env/bin/activate
    Install dependencies:
    pip install -r requirements.txt
    Run the web app: 
    python emailApp.py

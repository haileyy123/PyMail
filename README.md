# Py Mail  
A simple open source email server and temporary email site written in python

## Usage Instructions

1. Download This Repository
2. Install python from https://www.python.org/
3. Open Command Prompt/Terminal and navigate to the project directory
4. Run `pip install -r requirements.txt`
5. Run `python main.py` to start the PyMail server.

## Open Up The Server To The World

1. Navigate to your router's settings page on your default gateway, this is normally 192.168.0.1 or 192.168.1.1
2. Login
3. Forward ports 25 and 80 on TCP/UDP on the device running PyMail's local ipv4

Anyone will now be able to visit your PyMail website.

## Linking your domain to PyMail to receive emails
This lets people visit your webiste using your domain and lets you receive emails.  

1. Buy a domain if you dont have one already, you can get a cheap one for £2 from dynadot https://www.dynadot.com/
2. Once you have your domain, go to the DNS settings.
3. create a new subdomain called `mail` set the record type to `A` and set the target host to your public ipv4.
4. set the record type for your main domain to `MX` set the priority to `10` and set the host to `mail.yourdomain.com`

you will now be able to visit your website py going to mail.yourdomain.com and receive emails that get sent to any email address @yourdomain.com

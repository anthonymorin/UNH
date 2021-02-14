
import smtplib
#import secrets

carriers = {
	'att':    '@mms.att.net',
	'tmobile':' @tmomail.net',
	'verizon':  '@vtext.com',
	'sprint':   '@page.nextel.com'
}

def SendText(message, phoneNumber, emailAddress, emailPW, carrier = 'tmobile', mailserver = "smtp.gmail.com", mailServerPort = 587):
	"""Sends a text message to the specified phone number, using the provided settings

	Args:
		message (str): The message to send
		phoneNumber (str): The phone number.  Format is '000-000-000'
		emailAddress (str): the email address the message will be sent from over SMTP
		emailPW (str): The password to the email address.  
			Gmail will require you to make an app-specific password.  
			See https://support.google.com/mail/?p=InvalidSecondFactor for more info
		carrier (str, optional): The carrier of the phone number.  
			Tested carriers are 'tmobile'.  
			Supported carriers are 'att', 'tmobile', 'verizon', 'sprint'. 
			Defaults to 'tmobile'.
		mailserver (str, optional): The SMTP server to use. Defaults to "smtp.gmail.com".
		mailServerPort (int, optional): The port of the SMTP server to use. Defaults to 587.
	"""
    #the destination phone number formatted as an email address, according to the carrier's format
	to_number = f'{phoneNumber}.{carriers[carrier]}'

	# Establish a secure session with the mailserver's outgoing SMTP server using the provided email account
	server = smtplib.SMTP(mailserver, mailServerPort)
	server.starttls()
	server.login(emailAddress, emailPW)

	#carrier specific message formatting
	if carrier == 'tmobile':
		message = f"From: {emailAddress}\r\nTo: {to_number}\r\nSubject: Python Message\r\n{message}"

	# Send text message through SMS gateway of destination number
	server.sendmail(emailAddress, to_number, message)
		
##test
#SendText("This is probably the last test", secrets.phoneNumber, secrets.email, secrets.pw)
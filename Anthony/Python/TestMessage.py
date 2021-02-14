
import smtplib
#import secrets

carriers = {
	'att':    '@mms.att.net',
	'tmobile':' @tmomail.net',
	'verizon':  '@vtext.com',
	'sprint':   '@page.nextel.com'
}

def SendText(message, phoneNumber, emailAddress, emailPW, carrier = 'tmobile'):
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
	"""
        # Replace the number with your own, or consider using an argument\dict for multiple people.
	to_number = phoneNumber + '{}'.format(carriers[carrier])
	auth = (emailAddress, emailPW)

	# Establish a secure session with gmail's outgoing SMTP server using your gmail account
	server = smtplib.SMTP( "smtp.gmail.com", 587 )
	server.starttls()
	server.login(auth[0], auth[1])

	#carrier specific message formatting
	if carrier == 'tmobile':
		message = f"From: {auth[0]}\r\nTo: {to_number}\r\nSubject: Python Message\r\n{message}"

	# Send text message through SMS gateway of destination number
	server.sendmail( auth[0], to_number, message)
		
##test
#SendText("This is probably the last test", secrets.phoneNumber, secrets.email, secrets.pw)
# Extra Package
# from sms import send_sms
# from sendsms import api
# from sendsms.message import SmsMessage


class SMS_helper():
	"""All Backend Apps's View will Use this class so that 
	they got the Confirmation Helper class Attributes"""

	def __init__(self, arg):
		#super('', self).__init__()
		self.arg = arg



	# SMS API PROCESS START
	#------------------------------
	def sms_send(self, message, sender, receiver):

		self.message  = message
		self.sender   = sender
		self.receiver = receiver

		import os
		from django.conf import settings
		from twilio.rest import Client

		# print('---------', os.environ)
		# account_sid = os.environ.get(settings.TWILIO_ACCOUNT_SID)
		# auth_token  = os.environ.get(settings.TWILIO_AUTH_TOKEN)
		# print('---------', account_sid, auth_token)
		# client      = Client(account_sid, auth_token)
		# print('---------', settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
		client      = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

		if self.sender != '' and self.receiver != '':
			self.response = client.messages.create(from_=self.sender, body=self.message, to=self.receiver)
			
			if self.response == 1:
				return 'success'
			else:
				return 'failed'
		else:
			pass
	# Find your Account SID and Auth Token at twilio.com/console
	# and set the environment variables. See http://twil.io/secure
	#--------------------
	# SMS API PROCESS END






	# SMS API PROCESS START
	#------------------------------
	'''These wrappers are provided to make sending SMS extra quick, 
	to help test SMS sending during development, and to provide 
	additional SMS gateways'''
	# pip install django-sms (***NEEDED***)
	

	# def sms_send(self, message, sender, receiver):

	# 	self.message  = message
	# 	self.sender   = sender
	# 	self.receiver = receiver

	# 	if self.sender != '' and self.receiver != '':
	# 		self.response = send_sms(self.message, self.sender, [self.receiver], fail_silently=False)
			
	# 		if self.response == 1:
	# 			return 'success'
	# 		else:
	# 			return 'failed'
	# 	else:
	# 		pass
	#--------------------
	# SMS API PROCESS END
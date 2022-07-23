# Buildin Package
from django.core.mail import send_mail


class Email_helper():
	"""All Backend Apps's View will Use this class so that 
	they got the Confirmation Helper class Attributes"""

	def __init__(self, arg):
		#super('', self).__init__()
		self.arg = arg



	# GMAIL EMAIL API PROCESS START
	#------------------------------
	'''We need to add two factor sequirity from own gmail sequirity 
	and then have to add pass for custom app(127.0.0.1 or own domain)'''
	def mail_seld(self, subject, message, sender, receiver):

		self.subject  = subject
		self.message  = message
		self.sender   = sender
		self.receiver = receiver

		if self.sender != '' and self.receiver != '':
			self.response = send_mail(self.subject, self.message, self.sender, [self.receiver], fail_silently=False,)
			return 'success'
		else:
			pass
	#----------------------------
	# GMAIL EMAIL API PROCESS END









	# SEND GRID EMAIL API PROCESS START
	#------------------------------------
	# def mail_seld(self, subject, message, sender, receiver):
		
	# 	'''SETTINGS CODE START'''
	# 	EMAIL_HOST = 'smtp.sendgrid.net'
	# 	EMAIL_HOST_USER = 'apikey'
	# 	EMAIL_HOST_PASSWORD = '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'
	# 	EMAIL_PORT = 587
	# 	EMAIL_USE_TLS = True
	# 	'''SETTINGS CODE END'''

	# 	self.subject  = subject
	# 	self.message  = message
	# 	self.sender   = sender
	# 	self.receiver = receiver

	# 	if self.sender != '' and self.receiver != '':
	# 		self.response = send_mail(self.subject, self.message, self.sender, [self.receiver], fail_silently=False,)
	# 		return 'success'
	# 	else:
	# 		pass





		# OTHER WAY TO SEND EMAIL
		# -----------------------
		# import sendgrid
		# import os
		# from sendgrid.helpers.mail import Email, Mail, Content

		# self.sg = sendgrid.SendGridAPIClient(apikey='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')
		# self.from_email = Email(self.sender)
		# self.to_email = Email(self.receiver)
		# self.content = Content("text/plain", self.message)
		# self.mail = Mail(self.from_email, self.subject, self.to_email, self.content)
		# self.response = self.sg.client.mail.send.post(request_body=self.mail.get())
		# self.result1 self.response.status_code
		# self.result2 self.response.body
		# self.result3 self.response.headers
		# print(self.response)
		# return self.response
	
	#--------------------------------
	# SEND GRID EMAIL API PROCESS END
class View_origin():
	"""All Apps will extend this class so that they 
	got the View Global Prime class Attributes"""

	"""Importing Build-In Packages For View"""
	from django.core.paginator import Paginator
	
	"""Importing User Define Packages For View"""
	from package.view_helper import View_helper as vh
	from package.confirmation_helper import Confirmation_helper as ch
	from package.email_helper import Email_helper as eh
	from package.sms_helper import SMS_helper as sh
	from package.barcode_helper import Barcode_helper as bh
	from package.qrcode_helper import Qrcode_helper as qh



	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg
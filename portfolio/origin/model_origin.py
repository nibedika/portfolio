class Model_origin():
	"""All Apps will extend this class so that they 
	got the Model Global Prime class Attributes"""

	"""Importing Build-In Packages For View"""
	from django.db.models import Q as Q_set
	
	"""Importing User Define Packages For View"""
	from package.model_helper import Model_helper as mh




	""" Importing Models For Globally Reading Data """
	''' -------------- Backend Models ------------ '''
	from apps.access_apps.backend_access.models import User as backendUser

	from apps.backend_apps.setting.models import Website_cl as websiteDB
	from apps.backend_apps.privilege.models import Admin_cl as privilegeDB
	from apps.backend_apps.message.models import Cl as msgDB
	from apps.backend_apps.business_contact.models import Cl as contactDB
	

	''' -------------- Frontend Models ----------- '''




	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg
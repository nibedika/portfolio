# Buildin Package
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST

# View Prime Class Import 
from origin.view_origin import View_origin as vo

# Model Prime Class Import 
from origin.model_origin import Model_origin as mo


# App's Model Import
from apps.frontend_apps.resume.models import Cl as resumeDB
from apps.frontend_apps.portfolio.models import Cl as portfolioDB
from apps.frontend_apps.service.models import Cl as serviceDB
from apps.frontend_apps.blog.models import Cl as blogDB


# Create your views here.
class Frontend_access(vo, mo):

	def __init__(self, arg):
		super(vo, mo, self).__init__()
		self.arg = arg



	def web_home(request):
		
		# COMMON INFO FETCHING START
		# BUSINESS ::
		businessWhere    = mo.Q_set(account_type='account', status='active', trash=False)
		businessInfo     = mo.mh.fetch_data(mo.mh, mo.backendUser, businessWhere).last()

		# WEBSITE ::
		try:
			websiteWhere = mo.Q_set(user_id=businessInfo, status='active', trash=False)
			websiteInfo  = mo.mh.get_data(mo.mh, mo.websiteDB, websiteWhere)
		except:
			websiteInfo  = ''
		# COMMON INFO FETCHING END

		# EXPERIENCE RESUME ::
		experienceWhere  = mo.Q_set(resume_type='work', status='active', trash=False)
		experienceInfo   = mo.mh.fetch_data(mo.mh, resumeDB, experienceWhere)

		# EDUCATION RESUME ::
		educationWhere   = mo.Q_set(resume_type='education', status='active', trash=False)
		educationInfo    = mo.mh.fetch_data(mo.mh, resumeDB, educationWhere)

		# PORTFOLIO ::
		portfolioWhere   = mo.Q_set(status='active', trash=False)
		portfolioInfo    = mo.mh.fetch_data(mo.mh, portfolioDB, portfolioWhere)

		# SERVICE ::
		serviceWhere     = mo.Q_set(status='active', trash=False)
		serviceInfo      = mo.mh.fetch_data(mo.mh, serviceDB, serviceWhere)

		# BLOG ::
		blogWhere    = mo.Q_set(status='active', trash=False)
		blogInfo     = mo.mh.fetch_data(mo.mh, blogDB, blogWhere)

		return render(request, 'web_home.html', {'active': 'home', 'businessData': businessInfo, 'websiteData': websiteInfo, 'experienceData': experienceInfo, 'educationData': educationInfo, 'portfolioData': portfolioInfo, 'serviceData': serviceInfo, 'blogData': blogInfo})





	def portfolio_detail(request, portfolioId):

		# COMMON INFO FETCHING START
		# BUSINESS ::
		businessWhere    = mo.Q_set(account_type='account', status='active', trash=False)
		businessInfo     = mo.mh.fetch_data(mo.mh, mo.backendUser, businessWhere).last()

		# WEBSITE ::
		try:
			websiteWhere = mo.Q_set(user_id=businessInfo, status='active', trash=False)
			websiteInfo  = mo.mh.get_data(mo.mh, mo.websiteDB, websiteWhere)
		except:
			websiteInfo  = ''
		# COMMON INFO FETCHING END

		# PORTFOLIO ::
		portfolioWhere = mo.Q_set(id=portfolioId, status='active', trash=False)
		portfolioInfo  = mo.mh.get_data(mo.mh, portfolioDB, portfolioWhere)

		return render(request, 'web_portfolio_detail.html', {'businessData': businessInfo, 'websiteData': websiteInfo, 'portfolioData': portfolioInfo})





	def blog_detail(request, blogId):

		# COMMON INFO FETCHING START
		# BUSINESS ::
		businessWhere    = mo.Q_set(account_type='account', status='active', trash=False)
		businessInfo     = mo.mh.fetch_data(mo.mh, mo.backendUser, businessWhere).last()

		# WEBSITE ::
		try:
			websiteWhere = mo.Q_set(user_id=businessInfo, status='active', trash=False)
			websiteInfo  = mo.mh.get_data(mo.mh, mo.websiteDB, websiteWhere)
		except:
			websiteInfo  = ''
		# COMMON INFO FETCHING END

		# BLOG ::
		blogWhere = mo.Q_set(id=blogId, status='active', trash=False)
		blogInfo  = mo.mh.get_data(mo.mh, blogDB, blogWhere)

		return render(request, 'web_blog_detail.html', {'businessData': businessInfo, 'websiteData': websiteInfo, 'blogData': blogInfo})
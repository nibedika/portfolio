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
from apps.frontend_apps.portfolio.models import Cl as portfolioDB


# Create your views here.
class Portfolio():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg



	def portfolio_add(request, confirmation):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			menuWhere       = mo.Q_set(username=sessionUsername, status='active', trash=False)
			menuInfo        = mo.mh.get_data(mo.mh, mo.backendUser, menuWhere)
			
			# For Owner & Business Admin's Only
			privilegeWhere  = mo.Q_set(admin_id=menuInfo, status='active', trash=False)
			privilegeInfo   = mo.mh.fetch_data(mo.mh, mo.privilegeDB, privilegeWhere)
			
			navMsgWhere     = mo.Q_set(receiver=menuInfo, status='unseen', trash=False)
			navMsgInfo      = mo.mh.fetch_data(mo.mh, mo.msgDB, navMsgWhere)
			
			contactWhere    = mo.Q_set(user_id=menuInfo, status='unseen', trash=False)
			contactInfo     = mo.mh.fetch_data(mo.mh, mo.contactDB, contactWhere)
			# COMMON INFO FETCHING END

			if len(confirmation) > 3:
				pageConfirmation = vo.vh.value_decrypter(vo.vh, confirmation)
			else:
			 	pageConfirmation = confirmation

			# Add Start Here ------------->
			if request.method == 'POST' and request.POST.get('portfolio_add'):

				# Data entry block start 
				data = portfolioDB(
					portfolio_id    = vo.vh.unique_custom_id(mo.mh, 'BP'),
					user_id         = menuInfo,
					portfolio_topic = request.POST.get('portfolio_topic'),
					portfolio_title = request.POST.get('portfolio_title'),
					portfolio_txt   = request.POST.get('portfolio_txt'),
					portfolio_img   = vo.vh.file_processor(vo.vh, request.FILES.get('portfolio_img'), 'portfolio_img', 'user/portfolio_img/'),
				)

				if menuInfo:
					msg = {
						'pattern' : 'success',
						'content' : 'Successfully Saved.',
						'style'   : 'success'
					}
					#confirmation = vo.ch.message(vo.ch, 'success', msg)
					confirmation = vo.ch.message(vo.ch, mo.mh.add_data(mo.mh, data), msg)
					return redirect('portfolio_add', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
				else:
					msg = {
						'pattern' : 'warning',
						'content' : 'Information Missing ! Try again.',
						'style'   : 'warning'
					}
					confirmation = vo.ch.message(vo.ch, 'warning', msg)
					return render(request, 'portfolio_add.html', {'activeAside': 'portfolio', 'activeMenu': 'portfolio_add', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'confirm': confirmation})
				# Data entry block end
			
			elif request.method == 'GET':
				return render(request, 'portfolio_add.html', {'activeAside': 'portfolio', 'activeMenu': 'portfolio_add', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'confirm': pageConfirmation})

			return render(request, 'portfolio_add.html', {'activeAside': 'portfolio', 'activeMenu': 'portfolio_add', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'confirm': pageConfirmation})
		else:
			return redirect('sign_up')





	def portfolio_all(request, confirmation):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			menuWhere       = mo.Q_set(username=sessionUsername, status='active', trash=False)
			menuInfo        = mo.mh.get_data(mo.mh, mo.backendUser, menuWhere)
			
			# For Owner & Business Admin's Only
			privilegeWhere  = mo.Q_set(admin_id=menuInfo, status='active', trash=False)
			privilegeInfo   = mo.mh.fetch_data(mo.mh, mo.privilegeDB, privilegeWhere)
			
			navMsgWhere     = mo.Q_set(receiver=menuInfo, status='unseen', trash=False)
			navMsgInfo      = mo.mh.fetch_data(mo.mh, mo.msgDB, navMsgWhere)
			
			contactWhere    = mo.Q_set(user_id=menuInfo, status='unseen', trash=False)
			contactInfo     = mo.mh.fetch_data(mo.mh, mo.contactDB, contactWhere)
			# COMMON INFO FETCHING END

			if len(confirmation) > 3:
				pageConfirmation = vo.vh.value_decrypter(vo.vh, confirmation)
			else:
			 	pageConfirmation = confirmation
			
			portfolioWhere    = mo.Q_set(user_id=menuInfo, trash=False)
			portfolioInfo     = mo.mh.fetch_data(mo.mh, portfolioDB, portfolioWhere)

			return render(request, 'portfolio_all.html', {'activeAside': 'portfolio', 'activeMenu': 'portfolio_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'portfolioData': portfolioInfo, 'confirm': pageConfirmation})
		else:
			return redirect('sign_up')





	def portfolio_view(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			menuWhere       = mo.Q_set(username=sessionUsername, status='active', trash=False)
			menuInfo        = mo.mh.get_data(mo.mh, mo.backendUser, menuWhere)
			
			# For Owner & Business Admin's Only
			privilegeWhere  = mo.Q_set(admin_id=menuInfo, status='active', trash=False)
			privilegeInfo   = mo.mh.fetch_data(mo.mh, mo.privilegeDB, privilegeWhere)
			
			navMsgWhere     = mo.Q_set(receiver=menuInfo, status='unseen', trash=False)
			navMsgInfo      = mo.mh.fetch_data(mo.mh, mo.msgDB, navMsgWhere)
			
			contactWhere    = mo.Q_set(user_id=menuInfo, status='unseen', trash=False)
			contactInfo     = mo.mh.fetch_data(mo.mh, mo.contactDB, contactWhere)
			# COMMON INFO FETCHING END

			portfolioWhere    = mo.Q_set(id=id, trash=False)
			portfolioInfo     = mo.mh.get_data(mo.mh, portfolioDB, portfolioWhere)

			return render(request, 'portfolio_view.html', {'activeAside': 'portfolio', 'activeMenu': 'portfolio_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'portfolioData': portfolioInfo})
		else:
			return redirect('sign_up')





	def portfolio_edit(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			menuWhere       = mo.Q_set(username=sessionUsername, status='active', trash=False)
			menuInfo        = mo.mh.get_data(mo.mh, mo.backendUser, menuWhere)
			
			# For Owner & Business Admin's Only
			privilegeWhere  = mo.Q_set(admin_id=menuInfo, status='active', trash=False)
			privilegeInfo   = mo.mh.fetch_data(mo.mh, mo.privilegeDB, privilegeWhere)
			
			navMsgWhere     = mo.Q_set(receiver=menuInfo, status='unseen', trash=False)
			navMsgInfo      = mo.mh.fetch_data(mo.mh, mo.msgDB, navMsgWhere)
			
			contactWhere    = mo.Q_set(user_id=menuInfo, status='unseen', trash=False)
			contactInfo     = mo.mh.fetch_data(mo.mh, mo.contactDB, contactWhere)
			# COMMON INFO FETCHING END

			portfolioWhere    = mo.Q_set(id=id, trash=False)
			portfolioInfo     = mo.mh.get_data(mo.mh, portfolioDB, portfolioWhere)

			# Update Start Here ------------->
			if request.method == 'POST' and request.POST.get('portfolio_edit'):

				if request.FILES.get('portfolio_img') != None and request.FILES.get('portfolio_img') != '':
					portfolioFile = vo.vh.file_processor(vo.vh, request.FILES.get('portfolio_img'), 'portfolio_img', 'user/portfolio_img/')
				else:
					portfolioFile = portfolioInfo.portfolio_img

				# Data entry block start 
				where       = mo.Q_set(id=id, trash=False)
				pre_update  = portfolioDB.objects.select_related().filter(where)
				post_update = pre_update.update(
					portfolio_topic = request.POST.get('portfolio_topic'),
					portfolio_title = request.POST.get('portfolio_title'),
					portfolio_txt   = request.POST.get('portfolio_txt'),
					status          = request.POST.get('status'),
					portfolio_img   = portfolioFile
			    )

				msg = {
					'pattern' : 'success',
					'content' : 'Information Successfully Updated',
					'style'   : 'success'
				}

				confirmation = vo.ch.message(vo.ch, 'success', msg)
				return redirect('portfolio_all', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
				# Data entry block end

			elif request.method == 'GET':
				return render(request, 'portfolio_edit.html', {'activeAside': 'portfolio', 'activeMenu': 'portfolio_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'portfolioData': portfolioInfo})
			
			return render(request, 'portfolio_edit.html', {'activeAside': 'portfolio', 'activeMenu': 'portfolio_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'portfolioData': portfolioInfo})
		else:
			return redirect('sign_up')





	def portfolio_delete(request, id):
		if request.session.has_key('username'):

			if request.method == 'GET':
				where       = mo.Q_set(id=id)
				pre_update  = mo.mh.update_data(mo.mh, portfolioDB, where)
				post_update = pre_update.update(
					trash   = True,
			    )

				msg = {
					'pattern' : 'danger',
					'content' : 'Information Successfully Deleted',
					'style'   : 'danger'
				}

				confirmation = vo.ch.message(vo.ch, 'danger', msg)
				return redirect('portfolio_all', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
			else:
				pass
		else:
			return redirect('sign_up')

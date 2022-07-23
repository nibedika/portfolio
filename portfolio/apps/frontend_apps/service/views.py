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
from apps.frontend_apps.service.models import Cl as serviceDB


# Create your views here.
class Service():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg



	def service_add(request, confirmation):
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
			if request.method == 'POST' and request.POST.get('service_add'):

				# Data entry block start 
				data = serviceDB(
					service_id    = vo.vh.unique_custom_id(vo.vh, 'BS'),
					user_id       = menuInfo,
					service_title = request.POST.get('service_title'),
					service_txt   = request.POST.get('service_txt'),
					service_icon  = vo.vh.file_processor(vo.vh, request.FILES.get('service_icon'), 'service_icon', 'user/service_icon/'),
				)

				if menuInfo:
					msg = {
						'pattern' : 'success',
						'content' : 'Successfully Saved.',
						'style'   : 'success'
					}
					#confirmation = vo.ch.message(vo.ch, 'success', msg)
					confirmation = vo.ch.message(vo.ch, mo.mh.add_data(mo.mh, data), msg)
					return redirect('service_add', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
				else:
					msg = {
						'pattern' : 'warning',
						'content' : 'Information Missing ! Try again.',
						'style'   : 'warning'
					}
					confirmation = vo.ch.message(vo.ch, 'warning', msg)
					return render(request, 'service_add.html', {'activeAside': 'service', 'activeMenu': 'service_add', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'confirm': confirmation})
				# Data entry block end
			
			elif request.method == 'GET':
				return render(request, 'service_add.html', {'activeAside': 'service', 'activeMenu': 'service_add', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'confirm': pageConfirmation})

			return render(request, 'service_add.html', {'activeAside': 'service', 'activeMenu': 'service_add', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'confirm': pageConfirmation})
		else:
			return redirect('sign_up')





	def service_all(request, confirmation):
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
			
			serviceWhere    = mo.Q_set(user_id=menuInfo, trash=False)
			serviceInfo     = mo.mh.fetch_data(mo.mh, serviceDB, serviceWhere)

			return render(request, 'service_all.html', {'activeAside': 'service', 'activeMenu': 'service_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'confirm': pageConfirmation, 'serviceData': serviceInfo})
		else:
			return redirect('sign_up')





	def service_view(request, id):
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

			serviceWhere    = mo.Q_set(id=id, trash=False)
			serviceInfo     = mo.mh.get_data(mo.mh, serviceDB, serviceWhere)

			return render(request, 'service_view.html', {'activeAside': 'service', 'activeMenu': 'service_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'serviceData': serviceInfo})
		else:
			return redirect('sign_up')





	def service_edit(request, id):
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

			serviceWhere    = mo.Q_set(id=id, trash=False)
			serviceInfo     = mo.mh.get_data(mo.mh, serviceDB, serviceWhere)

			# Update Start Here ------------->
			if request.method == 'POST' and request.POST.get('service_edit'):

				if request.FILES.get('service_icon') != None and request.FILES.get('service_icon') != '':
					serviceIcon = vo.vh.file_processor(vo.vh, request.FILES.get('service_icon'), 'service_icon', 'user/service_icon/')
				else:
					serviceIcon = serviceInfo.service_icon

				# Data entry block start 
				where       = mo.Q_set(id=id, trash=False)
				pre_update  = serviceDB.objects.select_related().filter(where)
				post_update = pre_update.update(
					service_title = request.POST.get('service_title'),
					service_txt   = request.POST.get('service_txt'),
					status        = request.POST.get('status'),
					service_icon  = serviceIcon
			    )
				
				msg = {
					'pattern' : 'success',
					'content' : 'Information Successfully Updated',
					'style'   : 'success'
				}

				confirmation = vo.ch.message(vo.ch, 'success', msg)
				return redirect('service_all', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
				# Data entry block end

			elif request.method == 'GET':
				return render(request, 'service_edit.html', {'activeAside': 'service', 'activeMenu': 'service_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'serviceData': serviceInfo})
			
			return render(request, 'service_edit.html', {'activeAside': 'service', 'activeMenu': 'service_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'serviceData': serviceInfo})
		else:
			return redirect('sign_up')





	def service_delete(request, id):
		if request.session.has_key('username'):

			if request.method == 'GET':
				where       = mo.Q_set(id=id)
				pre_update  = mo.mh.update_data(mo.mh, serviceDB, where)
				post_update = pre_update.update(
					trash   = True,
			    )

				msg = {
					'pattern' : 'danger',
					'content' : 'Information Successfully Deleted',
					'style'   : 'danger'
				}

				confirmation = vo.ch.message(vo.ch, 'danger', msg)
				return redirect('service_all', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
			else:
				pass
		else:
			return redirect('sign_up')

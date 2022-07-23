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
from apps.backend_apps.familiar.models import Cl as familiarDB



# Create your views here.
class Familiar(vo, mo):

	def __init__(self, arg):
		super(vo, mo, self).__init__()
		self.arg = arg




	def familiar_add(request, confirmation):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			menuWhere       = mo.Q_set(username=sessionUsername, status='active', trash=False)
			menuInfo        = mo.mh.get_data(mo.mh, mo.backendUser, menuWhere)
			
			# For Admin's Only
			privilegeWhere  = mo.Q_set(admin_id=menuInfo, status='active', trash=False)
			privilegeInfo   = mo.mh.fetch_data(mo.mh, mo.privilegeDB, privilegeWhere)
			
			navMsgWhere     = mo.Q_set(receiver=menuInfo, status='unseen', trash=False)
			navMsgInfo      = mo.mh.fetch_data(mo.mh, mo.msgDB, navMsgWhere)
			
			contactWhere    = mo.Q_set(user_id=menuInfo, status='unseen', trash=False)
			contactInfo     = mo.mh.fetch_data(mo.mh, mo.contactDB, contactWhere)
			# COMMON INFO FETCHING END

			if len(confirmation) > 3:
				pageConfirmation   = vo.vh.value_decrypter(vo.vh, confirmation)
			else:
			 	pageConfirmation   = confirmation

			if request.method == 'POST' and request.POST.get('familiar_add'):
			    
				if request.FILES.get('attached_file') != None:
					familiarImg = vo.vh.file_processor(vo.vh, request.FILES.get('attached_file'), 'familiar', 'business/familiar/')
				else:
					familiarImg = ' '

				# Data entry block start 
				data = familiarDB(
					familiar_id       = vo.vh.unique_custom_id(mo.mh, 'BF'),
					user_id           = menuInfo,
					name              = request.POST.get('name'),
					contact_no        = request.POST.get('contact_no'),
					address           = request.POST.get('address'),
					contact_person    = request.POST.get('contact_person'),
					contact_person_no = request.POST.get('contact_person_no'),
					description       = request.POST.get('description'),
					remark            = request.POST.get('remark'),
					photo             = familiarImg
				)

				if menuInfo:
					msg = {
						'pattern' : 'success',
						'content' : 'Successfully Saved.',
						'style'   : 'success'
					}
					#confirmation = vo.ch.message(vo.ch, 'success', msg)
					confirmation = vo.ch.message(vo.ch, mo.mh.add_data(mo.mh, data), msg)
					return redirect('familiar_add', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
				else:
					msg = {
						'pattern' : 'warning',
						'content' : 'Information Missing ! Try again.',
						'style'   : 'warning'
					}
					confirmation = vo.ch.message(vo.ch, 'warning', msg)
					return render(request, 'familiar_add.html', {'activeAside': 'familiar', 'activeMenu': 'familiar_add', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'confirm': pageConfirmation})
				# Data entry block end

			elif request.method == 'GET':
				return render(request, 'familiar_add.html', {'activeAside': 'familiar', 'activeMenu': 'familiar_add', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'confirm': pageConfirmation})

			return render(request, 'familiar_add.html', {'activeAside': 'familiar', 'activeMenu': 'familiar_add', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'confirm': pageConfirmation})
		else:
			return redirect('sign_up')





	def familiar_all(request, confirmation):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			menuWhere       = mo.Q_set(username=sessionUsername, status='active', trash=False)
			menuInfo        = mo.mh.get_data(mo.mh, mo.backendUser, menuWhere)
			
			# For Admin's Only
			privilegeWhere  = mo.Q_set(admin_id=menuInfo, status='active', trash=False)
			privilegeInfo   = mo.mh.fetch_data(mo.mh, mo.privilegeDB, privilegeWhere)
			
			navMsgWhere     = mo.Q_set(receiver=menuInfo, status='unseen', trash=False)
			navMsgInfo      = mo.mh.fetch_data(mo.mh, mo.msgDB, navMsgWhere)
			
			contactWhere    = mo.Q_set(user_id=menuInfo, status='unseen', trash=False)
			contactInfo     = mo.mh.fetch_data(mo.mh, mo.contactDB, contactWhere)
			# COMMON INFO FETCHING END
			
			familiarWhere = mo.Q_set(user_id=menuInfo, trash=False)
			familiarInfo  = mo.mh.fetch_data(mo.mh, familiarDB, familiarWhere)

			if len(confirmation) > 3:
				pageConfirmation   = vo.vh.value_decrypter(vo.vh, confirmation)
			else:
			 	pageConfirmation   = confirmation

			return render(request, 'familiar_all.html', {'activeAside': 'familiar', 'activeMenu': 'familiar_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'familiarData': familiarInfo, 'confirm': pageConfirmation})
		else:
			return redirect('sign_up')





	def familiar_view(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			menuWhere       = mo.Q_set(username=sessionUsername, status='active', trash=False)
			menuInfo        = mo.mh.get_data(mo.mh, mo.backendUser, menuWhere)
			
			# For Admin's Only
			privilegeWhere  = mo.Q_set(admin_id=menuInfo, status='active', trash=False)
			privilegeInfo   = mo.mh.fetch_data(mo.mh, mo.privilegeDB, privilegeWhere)
			
			navMsgWhere     = mo.Q_set(receiver=menuInfo, status='unseen', trash=False)
			navMsgInfo      = mo.mh.fetch_data(mo.mh, mo.msgDB, navMsgWhere)
			
			contactWhere    = mo.Q_set(user_id=menuInfo, status='unseen', trash=False)
			contactInfo     = mo.mh.fetch_data(mo.mh, mo.contactDB, contactWhere)
			# COMMON INFO FETCHING END

			familiarWhere = mo.Q_set(id=id)
			familiarInfo  = mo.mh.get_data(mo.mh, familiarDB, familiarWhere)

			return render(request, 'familiar_view.html', {'activeAside': 'familiar', 'activeMenu': 'familiar_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'familiarData': familiarInfo})
		else:
			return redirect('sign_up')





	def familiar_edit(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			menuWhere       = mo.Q_set(username=sessionUsername, status='active', trash=False)
			menuInfo        = mo.mh.get_data(mo.mh, mo.backendUser, menuWhere)
			
			# For Admin's Only
			privilegeWhere  = mo.Q_set(admin_id=menuInfo, status='active', trash=False)
			privilegeInfo   = mo.mh.fetch_data(mo.mh, mo.privilegeDB, privilegeWhere)
			
			navMsgWhere     = mo.Q_set(receiver=menuInfo, status='unseen', trash=False)
			navMsgInfo      = mo.mh.fetch_data(mo.mh, mo.msgDB, navMsgWhere)
			
			contactWhere    = mo.Q_set(user_id=menuInfo, status='unseen', trash=False)
			contactInfo     = mo.mh.fetch_data(mo.mh, mo.contactDB, contactWhere)
			# COMMON INFO FETCHING END

			familiarWhere = mo.Q_set(id=id)
			familiarInfo  = mo.mh.get_data(mo.mh, familiarDB, familiarWhere)

			if request.FILES.get('attached_file') != None:
				familiarImg = vo.vh.file_processor(vo.vh, request.FILES.get('attached_file'), 'familiar', 'business/familiar/')
			else:
				familiarImg = familiarInfo.photo

			if request.method == 'POST' and request.POST.get('familiar_update'):

				where       = mo.Q_set(id=id)
				pre_update  = mo.mh.update_data(mo.mh, familiarDB, where)
				post_update = pre_update.update(
					name              = request.POST.get('name'),
					contact_no        = request.POST.get('contact_no'),
					address           = request.POST.get('address'),
					contact_person    = request.POST.get('contact_person'),
					contact_person_no = request.POST.get('contact_person_no'),
					remark            = request.POST.get('remark'),
					description       = request.POST.get('description'),
					photo             = familiarImg,
					status            = request.POST.get('status')
			    )

				msg = {
					'pattern' : 'success',
					'content' : 'Information Successfully Updated',
					'style'   : 'success'
				}

				confirmation = vo.ch.message(vo.ch, 'success', msg)
				return redirect('familiar_all', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
			
			elif request.method == 'GET':
				return render(request, 'familiar_edit.html', {'activeAside': 'familiar', 'activeMenu': 'familiar_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'familiarData': familiarInfo})
			
			return render(request, 'familiar_edit.html', {'activeAside': 'familiar', 'activeMenu': 'familiar_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'familiarData': familiarInfo})
		else:
			return redirect('sign_up')





	def familiar_delete(request, id):
		if request.session.has_key('username'):

			if request.method == 'GET':
				where       = mo.Q_set(id=id)
				pre_update  = mo.mh.update_data(mo.mh, familiarDB, where)
				post_update = pre_update.update(
					trash   = True,
			    )

				msg = {
					'pattern' : 'danger',
					'content' : 'Information Successfully Deleted',
					'style'   : 'danger'
				}

				confirmation = vo.ch.message(vo.ch, 'danger', msg)
				return redirect('familiar_all', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
			else:
				pass
		else:
			return redirect('sign_up')

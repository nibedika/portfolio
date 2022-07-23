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


# Create your views here.
class Resume():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg



	def resume_add(request, confirmation):
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
			if request.method == 'POST' and request.POST.get('resume_add'):

				# Data entry block start 
				data = resumeDB(
					resume_id      = vo.vh.unique_custom_id(vo.vh, 'BR'),
					user_id        = menuInfo,
					resume_type    = request.POST.get('resume_type'),
					duration       = request.POST.get('duration'),
					resume_title   = request.POST.get('resume_title'),
					resume_txt     = request.POST.get('resume_txt'),
					institute      = request.POST.get('institute'),
					institute_logo = vo.vh.file_processor(vo.vh, request.FILES.get('institute_logo'), 'institute_logo', 'user/institute_logo/'),
					url            = request.POST.get('url'),
				)

				if menuInfo:
					msg = {
						'pattern' : 'success',
						'content' : 'Successfully Saved.',
						'style'   : 'success'
					}
					#confirmation = vo.ch.message(vo.ch, 'success', msg)
					confirmation = vo.ch.message(vo.ch, mo.mh.add_data(mo.mh, data), msg)
					return redirect('resume_add', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
				else:
					msg = {
						'pattern' : 'warning',
						'content' : 'Information Missing ! Try again.',
						'style'   : 'warning'
					}
					confirmation = vo.ch.message(vo.ch, 'warning', msg)
					return render(request, 'resume_add.html', {'activeAside': 'resume', 'activeMenu': 'resume_add', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'confirm': confirmation})
				# Data entry block end
			
			elif request.method == 'GET':
				return render(request, 'resume_add.html', {'activeAside': 'resume', 'activeMenu': 'resume_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'confirm': pageConfirmation})

			return render(request, 'resume_add.html', {'activeAside': 'resume', 'activeMenu': 'resume_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'confirm': pageConfirmation})
		else:
			return redirect('sign_up')





	def resume_all(request, confirmation):
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
			
			resumeWhere    = mo.Q_set(user_id=menuInfo, trash=False)
			resumeInfo     = mo.mh.fetch_data(mo.mh, resumeDB, resumeWhere)

			return render(request, 'resume_all.html', {'activeAside': 'resume', 'activeMenu': 'resume_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'resumeData': resumeInfo, 'confirm': pageConfirmation})
		else:
			return redirect('sign_up')





	def resume_view(request, id):
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

			resumeWhere    = mo.Q_set(id=id, trash=False)
			resumeInfo     = mo.mh.get_data(mo.mh, resumeDB, resumeWhere)

			return render(request, 'resume_view.html', {'activeAside': 'resume', 'activeMenu': 'resume_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'resumeData': resumeInfo})
		else:
			return redirect('sign_up')





	def resume_edit(request, id):
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

			resumeWhere     = mo.Q_set(id=id, trash=False)
			resumeInfo      = mo.mh.get_data(mo.mh, resumeDB, resumeWhere)

			# Update Start Here ------------->
			if request.method == 'POST' and request.POST.get('resume_edit'):

				if request.FILES.get('institute_logo') != None and request.FILES.get('institute_logo') != '':
					instituteLogo = vo.vh.file_processor(vo.vh, request.FILES.get('institute_logo'), 'institute_logo', 'user/institute_logo/')
				else:
					instituteLogo = resumeInfo.institute_logo

				# Data entry block start 
				where       = mo.Q_set(id=id, trash=False)
				pre_update  = resumeDB.objects.select_related().filter(where)
				post_update = pre_update.update(
					resume_type    = request.POST.get('resume_type'),
					duration       = request.POST.get('duration'),
					resume_title   = request.POST.get('resume_title'),
					resume_txt     = request.POST.get('resume_txt'),
					institute      = request.POST.get('institute'),
					institute_logo = instituteLogo,
					url            = request.POST.get('url'),
					status         = request.POST.get('status'),
			    )

				msg = {
					'pattern' : 'success',
					'content' : 'Information Successfully Updated',
					'style'   : 'success'
				}

				confirmation = vo.ch.message(vo.ch, 'success', msg)
				return redirect('resume_all', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
				# Data entry block end

			elif request.method == 'GET':
				return render(request, 'resume_edit.html', {'activeAside': 'resume', 'activeMenu': 'resume_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'resumeData': resumeInfo})
			
			return render(request, 'resume_edit.html', {'activeAside': 'resume', 'activeMenu': 'resume_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'resumeData': resumeInfo})
		else:
			return redirect('sign_up')





	def resume_delete(request, id):
		if request.session.has_key('username'):

			if request.method == 'GET':
				where       = mo.Q_set(id=id)
				pre_update  = mo.mh.update_data(mo.mh, resumeDB, where)
				post_update = pre_update.update(
					trash   = True,
			    )

				msg = {
					'pattern' : 'danger',
					'content' : 'Information Successfully Deleted',
					'style'   : 'danger'
				}

				confirmation = vo.ch.message(vo.ch, 'danger', msg)
				return redirect('resume_all', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
			else:
				pass
		else:
			return redirect('sign_up')


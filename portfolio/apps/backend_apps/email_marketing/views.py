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
from apps.backend_apps.email_marketing.models import Email_list as emailListDB
from apps.backend_apps.email_marketing.models import Cl as emailMarketingDB




# Create your views here.
class Email_marketing(vo, mo):

	def __init__(self, arg):
		super(vo, mo, self).__init__()
		self.arg = arg


	def email_list(request, confirmation):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			menuWhere       = mo.Q_set(username=sessionUsername, status='active', trash=False)
			menuInfo        = mo.mh.get_data(mo.mh, mo.backendUser, menuWhere)
			
			# For Business Admin's Only
			privilegeWhere  = mo.Q_set(admin_id=menuInfo, status='active', trash=False)
			privilegeInfo   = mo.mh.fetch_data(mo.mh, mo.privilegeDB, privilegeWhere)
			
			navMsgWhere     = mo.Q_set(receiver=menuInfo, status='unseen', trash=False)
			navMsgInfo      = mo.mh.fetch_data(mo.mh, mo.msgDB, navMsgWhere)
			
			contactWhere    = mo.Q_set(user_id=menuInfo, status='unseen', trash=False)
			contactInfo     = mo.mh.fetch_data(mo.mh, mo.contactDB, contactWhere)
			# COMMON INFO FETCHING END

			emailListWhere  = mo.Q_set(user_id=menuInfo, trash=False)
			emailListInfo   = mo.mh.fetch_data(mo.mh, emailListDB, emailListWhere)

			if len(confirmation) > 3:
				pageConfirmation = vo.vh.value_decrypter(vo.vh, confirmation)
			else:
			 	pageConfirmation = confirmation

			if request.method == 'POST' and request.POST.get('email_list_add'):

				slugValue  = request.POST.get('email')

				emailInfo  = ''
				try:
					emailWhere = mo.Q_set(email=slugValue, trash=False)
					emailInfo  = mo.mh.get_data(mo.mh, emailListDB, emailWhere)
				except:
					emailInfo  = ''

				# Data entry block start 
				data = emailListDB(
					list_id = vo.vh.unique_custom_id(mo.mh, 'EML'),
					user_id = menuInfo,
					email   = request.POST.get('email'),
					name    = request.POST.get('name'),
					remark  = request.POST.get('remark'),
				)

				if emailInfo != '':
					msg = {
						'pattern' : 'warning',
						'content' : 'Information Already Exists ! Try Another.',
						'style'   : 'warning'
					}
					confirmation = vo.ch.message(vo.ch, 'warning', msg)
					return render(request, 'email_list.html', {'activeAside': 'email_marketing', 'activeMenu': 'email_list', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'emailListData': emailListInfo, 'confirm': confirmation})
				else:
					msg = {
						'pattern' : 'success',
						'content' : 'Successfully Saved.',
						'style'   : 'success'
					}
					#confirmation = vo.ch.message(vo.ch, 'success', msg)
					confirmation = vo.ch.message(vo.ch, mo.mh.add_data(mo.mh, data), msg)
					return redirect('email_list', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
				# Data entry block end

			elif request.method == 'GET':
				return render(request, 'email_list.html', {'activeAside': 'email_marketing', 'activeMenu': 'email_list', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'emailListData': emailListInfo, 'confirm': pageConfirmation})

			return render(request, 'email_list.html', {'activeAside': 'email_marketing', 'activeMenu': 'email_list', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'emailListData': emailListInfo, 'confirm': pageConfirmation})
		else:
			return redirect('sign_up')



	def email_edit(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			menuWhere       = mo.Q_set(username=sessionUsername, status='active', trash=False)
			menuInfo        = mo.mh.get_data(mo.mh, mo.backendUser, menuWhere)
			
			# For Business Admin's Only
			privilegeWhere  = mo.Q_set(admin_id=menuInfo, status='active', trash=False)
			privilegeInfo   = mo.mh.fetch_data(mo.mh, mo.privilegeDB, privilegeWhere)
			
			navMsgWhere     = mo.Q_set(receiver=menuInfo, status='unseen', trash=False)
			navMsgInfo      = mo.mh.fetch_data(mo.mh, mo.msgDB, navMsgWhere)
			
			contactWhere    = mo.Q_set(user_id=menuInfo, status='unseen', trash=False)
			contactInfo     = mo.mh.fetch_data(mo.mh, mo.contactDB, contactWhere)
			# COMMON INFO FETCHING END

			emailListWhere  = mo.Q_set(id=id)
			emailListInfo   = mo.mh.get_data(mo.mh, emailListDB, emailListWhere)

			if request.method == 'POST' and request.POST.get('email_update'):

				slugValue = request.POST.get('email')

				emailInfo  = ''
				try:
					emailWhere = mo.Q_set(email=slugValue, trash=False)
					emailInfo  = mo.mh.get_data(mo.mh, emailListDB, emailWhere)
				except:
					emailInfo  = ''

				if emailInfo != '' and emailListInfo.email != slugValue:
					msg = {
						'pattern' : 'warning',
						'content' : 'Information Already Exists ! Try Another.',
						'style'   : 'warning'
					}
					confirmation = vo.ch.message(vo.ch, 'warning', msg)
					return render(request, 'email_list.html', {'activeAside': 'email_marketing', 'activeMenu': 'email_list', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'confirm': confirmation})
				else:
					where       = mo.Q_set(id=id)
					pre_update  = mo.mh.update_data(mo.mh, emailListDB, where)
					post_update = pre_update.update(
						email   = request.POST.get('email'),
						name    = request.POST.get('name'),
						remark  = request.POST.get('remark'),
					)

					msg = {
						'pattern' : 'success',
						'content' : 'Information Successfully Updated',
						'style'   : 'success'
					}
					confirmation = vo.ch.message(vo.ch, 'success', msg)
					return redirect('email_list', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
			
			elif request.method == 'GET':
				return render(request, 'email_edit.html', {'activeAside': 'email_marketing', 'activeMenu': 'email_list', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'emailListData': emailListInfo})
			
			return render(request, 'email_edit.html', {'activeAside': 'email_marketing', 'activeMenu': 'email_list', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'emailListData': emailListInfo})
		else:
			return redirect('sign_up')




	def email_delete(request, id):
		if request.session.has_key('username'):

			if request.method == 'GET':
				where       = mo.Q_set(id=id)
				pre_update  = mo.mh.update_data(mo.mh, emailListDB, where)
				post_update = pre_update.update(
					trash   = True,
			    )

				msg = {
					'pattern' : 'danger',
					'content' : 'Information Successfully Deleted',
					'style'   : 'danger'
				}

				confirmation = vo.ch.message(vo.ch, 'danger', msg)
				return redirect('email_list', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
			else:
				pass
		else:
			return redirect('sign_up')





#####################################################################################





	def marketing_email_send(request, confirmation):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			menuWhere       = mo.Q_set(username=sessionUsername, status='active', trash=False)
			menuInfo        = mo.mh.get_data(mo.mh, mo.backendUser, menuWhere)
			
			# For Business Admin's Only
			privilegeWhere  = mo.Q_set(admin_id=menuInfo, status='active', trash=False)
			privilegeInfo   = mo.mh.fetch_data(mo.mh, mo.privilegeDB, privilegeWhere)
			
			navMsgWhere     = mo.Q_set(receiver=menuInfo, status='unseen', trash=False)
			navMsgInfo      = mo.mh.fetch_data(mo.mh, mo.msgDB, navMsgWhere)
			
			contactWhere    = mo.Q_set(user_id=menuInfo, status='unseen', trash=False)
			contactInfo     = mo.mh.fetch_data(mo.mh, mo.contactDB, contactWhere)
			# COMMON INFO FETCHING END

			# EMAIL LIST
			emailListWhere  = mo.Q_set(user_id=menuInfo, trash=False)
			emailListInfo   = mo.mh.fetch_data(mo.mh, emailListDB, emailListWhere)

			if len(confirmation) > 3:
				pageConfirmation = vo.vh.value_decrypter(vo.vh, confirmation)
			else:
			 	pageConfirmation = confirmation


			if request.method == 'POST' and request.POST.get('marketing_email_send'):

				emailListIn = request.POST.getlist('email_list[]')

				# Data entry block start.....
				emailNum = len(list(set(emailListIn)))
				for index in range(emailNum):
					emailWhere = mo.Q_set(list_id=emailListIn[index], trash=False)
					emailInfo  = mo.mh.get_data(mo.mh, emailListDB, emailWhere)
					
					# Email Sending Start
					subject    = 'Promotional Email'
					message    = request.POST.get('text')
					sender     = 'Inventory Site'
					receiver   = emailInfo.email
					
					emailSend  = vo.eh.mail_seld(vo.eh, subject, message, sender, receiver)
					# Email Sending End

					if emailSend == 'success':
						data = emailMarketingDB(
							email_id       = vo.vh.unique_custom_id(mo.mh, 'EME'),
							user_id        = menuInfo,
							sender_email   = menuInfo.email,
							receiver_email = emailInfo,
							text           = request.POST.get('text'),
							#file          = vo.vh.file_processor(vo.vh, request.FILES.get('attached_file'), 'email-marketing', 'common/email-marketing/')
						)
						mo.mh.add_data(mo.mh, data)
				# Data entry block end.....

				if menuInfo:
					msg = {
						'pattern' : 'success',
						'content' : 'Successfully Saved.',
						'style'   : 'success'
					}
					confirmation = vo.ch.message(vo.ch, 'success', msg)
					return redirect('marketing_email_send', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
				else:
					msg = {
						'pattern' : 'warning',
						'content' : 'Information Missing ! Try again.',
						'style'   : 'warning'
					}
					confirmation = vo.ch.message(vo.ch, 'warning', msg)
					return render(request, 'marketing_email_send.html', {'activeAside': 'email_marketing', 'activeMenu': 'marketing_email_add', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'emailListData': emailListInfo, 'confirm': confirmation})
				# Data entry block end

			elif request.method == 'GET':
				return render(request, 'marketing_email_send.html', {'activeAside': 'email_marketing', 'activeMenu': 'marketing_email_add', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'emailListData': emailListInfo, 'confirm': pageConfirmation})

			return render(request, 'marketing_email_send.html', {'activeAside': 'email_marketing', 'activeMenu': 'marketing_email_add', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'emailListData': emailListInfo, 'confirm': pageConfirmation})
		else:
			return redirect('sign_up')





	def marketing_email_all(request, confirmation):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			menuWhere       = mo.Q_set(username=sessionUsername, status='active', trash=False)
			menuInfo        = mo.mh.get_data(mo.mh, mo.backendUser, menuWhere)
			
			# For Business Admin's Only
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

			emailMarketingWhere = mo.Q_set(trash=False)
			emailMarketingInfo  = mo.mh.fetch_data(mo.mh, emailMarketingDB, emailMarketingWhere)
			
			# page             = request.GET.get('page')
			# paginator        = vo.Paginator(email_marketingInfo, 20).get_page(page)

			return render(request, 'marketing_email_all.html', {'activeAside': 'email_marketing', 'activeMenu': 'marketing_email_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'emailMarketingData': emailMarketingInfo, 'confirm': pageConfirmation})
		else:
			return redirect('sign_up')





	def marketing_email_delete(request, id):
		if request.session.has_key('username'):

			if request.method == 'GET':
				where       = mo.Q_set(id=id)
				pre_update  = mo.mh.update_data(mo.mh, emailMarketingDB, where)
				post_update = pre_update.update(
					trash   = True,
			    )

				msg = {
					'pattern' : 'danger',
					'content' : 'Information Successfully Deleted',
					'style'   : 'danger'
				}

				confirmation = vo.ch.message(vo.ch, 'danger', msg)
				return redirect('marketing_email_all', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
			else:
				pass
		else:
			return redirect('sign_up')
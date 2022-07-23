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
from apps.backend_apps.sms_marketing.models import Contact_list as contactListDB
from apps.backend_apps.sms_marketing.models import Cl as smsMarketingDB




# Create your views here.
class SMS_marketing(vo, mo):

	def __init__(self, arg):
		super(vo, mo, self).__init__()
		self.arg = arg


	def contact_list(request, confirmation):
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

			contactListWhere  = mo.Q_set(user_id=menuInfo, trash=False)
			contactListInfo   = mo.mh.fetch_data(mo.mh, contactListDB, contactListWhere)

			if len(confirmation) > 3:
				pageConfirmation = vo.vh.value_decrypter(vo.vh, confirmation)
			else:
			 	pageConfirmation = confirmation

			if request.method == 'POST' and request.POST.get('contact_list_add'):

				slugValue = request.POST.get('contact')

				contactInfo  = ''
				try:
					contactWhere = mo.Q_set(contact=slugValue, trash=False)
					contactInfo  = mo.mh.get_data(mo.mh, contactListDB, contactWhere)
				except:
					contactInfo  = ''

				# Data entry block start 
				data = contactListDB(
					list_id = vo.vh.unique_custom_id(mo.mh, 'SMC'),
					user_id = menuInfo,
					contact = request.POST.get('contact'),
					name    = request.POST.get('name'),
					remark  = request.POST.get('remark'),
				)

				if contactInfo != '':
					msg = {
						'pattern' : 'warning',
						'content' : 'Information Already Exists ! Try Another.',
						'style'   : 'warning'
					}
					confirmation = vo.ch.message(vo.ch, 'warning', msg)
					return render(request, 'contact_list.html', {'activeAside': 'sms_marketing', 'activeMenu': 'contact_list', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'contactListData': contactListInfo, 'confirm': confirmation})
				else:
					msg = {
						'pattern' : 'success',
						'content' : 'Successfully Saved.',
						'style'   : 'success'
					}
					#confirmation = vo.ch.message(vo.ch, 'success', msg)
					confirmation = vo.ch.message(vo.ch, mo.mh.add_data(mo.mh, data), msg)
					return redirect('contact_list', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
				# Data entry block end

			elif request.method == 'GET':
				return render(request, 'contact_list.html', {'activeAside': 'sms_marketing', 'activeMenu': 'contact_list', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'contactListData': contactListInfo, 'confirm': pageConfirmation})

			return render(request, 'contact_list.html', {'activeAside': 'sms_marketing', 'activeMenu': 'contact_list', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'contactListData': contactListInfo, 'confirm': pageConfirmation})
		else:
			return redirect('sign_up')



	def contact_edit(request, id):
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

			contactListWhere  = mo.Q_set(id=id)
			contactListInfo   = mo.mh.get_data(mo.mh, contactListDB, contactListWhere)

			if request.method == 'POST' and request.POST.get('contact_update'):

				slugValue = request.POST.get('contact')

				contactInfo  = ''
				try:
					contactWhere = mo.Q_set(contact=slugValue, trash=False)
					contactInfo  = mo.mh.get_data(mo.mh, contactListDB, contactWhere)
				except:
					contactInfo  = ''

				if contactInfo != '' and contactListInfo.contact != slugValue:
					msg = {
						'pattern' : 'warning',
						'content' : 'Information Already Exists ! Try Another.',
						'style'   : 'warning'
					}
					confirmation = vo.ch.message(vo.ch, 'warning', msg)
					return render(request, 'contact_list.html', {'activeAside': 'sms_marketing', 'activeMenu': 'contact_list', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'confirm': confirmation})
				else:
					where       = mo.Q_set(id=id)
					pre_update  = mo.mh.update_data(mo.mh, contactListDB, where)
					post_update = pre_update.update(
						contact = request.POST.get('contact'),
						name    = request.POST.get('name'),
						remark  = request.POST.get('remark'),
					)

					msg = {
						'pattern' : 'success',
						'content' : 'Information Successfully Updated',
						'style'   : 'success'
					}
					confirmation = vo.ch.message(vo.ch, 'success', msg)
					return redirect('contact_list', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
			
			elif request.method == 'GET':
				return render(request, 'contact_edit.html', {'activeAside': 'sms_marketing', 'activeMenu': 'contact_list', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'contactListData': contactListInfo})
			
			return render(request, 'contact_edit.html', {'activeAside': 'sms_marketing', 'activeMenu': 'contact_list', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'contactListData': contactListInfo})
		else:
			return redirect('sign_up')




	def contact_delete(request, id):
		if request.session.has_key('username'):

			if request.method == 'GET':
				where       = mo.Q_set(id=id)
				pre_update  = mo.mh.update_data(mo.mh, contactListDB, where)
				post_update = pre_update.update(
					trash   = True,
			    )

				msg = {
					'pattern' : 'danger',
					'content' : 'Information Successfully Deleted',
					'style'   : 'danger'
				}

				confirmation = vo.ch.message(vo.ch, 'danger', msg)
				return redirect('contact_list', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
			else:
				pass
		else:
			return redirect('sign_up')





#####################################################################################





	def marketing_sms_send(request, confirmation):
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

			# CONTACT LIST
			contactListWhere  = mo.Q_set(user_id=menuInfo, trash=False)
			contactListInfo   = mo.mh.fetch_data(mo.mh, contactListDB, contactListWhere)

			if len(confirmation) > 3:
				pageConfirmation = vo.vh.value_decrypter(vo.vh, confirmation)
			else:
			 	pageConfirmation = confirmation


			if request.method == 'POST' and request.POST.get('marketing_sms_send'):

				contactListIn = request.POST.getlist('contact_list[]')

				# Data entry block start.....
				contactNum = len(list(set(contactListIn)))
				for index in range(contactNum):
					contactWhere = mo.Q_set(list_id=contactListIn[index], trash=False)
					contactInfo  = mo.mh.get_data(mo.mh, contactListDB, contactWhere)
					
					# sms Sending Start
					message  = request.POST.get('text')
					# sender   = menuInfo.contact_no.replace(" ", "")
					sender   = '+17813324693'
					receiver = contactInfo.contact.replace(" ", "")
					
					smsSend  = vo.sh.sms_send(vo.sh, message, sender, receiver)
					# sms Sending End

					if smsSend == 'success':
						data = smsMarketingDB(
							sms_id           = vo.vh.unique_custom_id(mo.mh, 'SMS'),
							user_id          = menuInfo,
							sender_contact   = sender,
							receiver_contact = contactInfo,
							text             = request.POST.get('text')
						)
						# mo.mh.add_data(mo.mh, data)
				# Data entry block end.....

				if menuInfo:
					msg = {
						'pattern' : 'success',
						'content' : 'Successfully Saved.',
						'style'   : 'success'
					}
					confirmation = vo.ch.message(vo.ch, 'success', msg)
					return redirect('marketing_sms_send', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
				else:
					msg = {
						'pattern' : 'warning',
						'content' : 'Information Missing ! Try again.',
						'style'   : 'warning'
					}
					confirmation = vo.ch.message(vo.ch, 'warning', msg)
					return render(request, 'marketing_sms_send.html', {'activeAside': 'sms_marketing', 'activeMenu': 'marketing_sms_add', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'contactListData': contactListInfo, 'confirm': confirmation})
				# Data entry block end

			elif request.method == 'GET':
				return render(request, 'marketing_sms_send.html', {'activeAside': 'sms_marketing', 'activeMenu': 'marketing_sms_add', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'contactListData': contactListInfo, 'confirm': pageConfirmation})

			return render(request, 'marketing_sms_send.html', {'activeAside': 'sms_marketing', 'activeMenu': 'marketing_sms_add', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'contactListData': contactListInfo, 'confirm': pageConfirmation})
		else:
			return redirect('sign_up')





	def marketing_sms_all(request, confirmation):
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

			smsMarketingWhere = mo.Q_set(trash=False)
			smsMarketingInfo  = mo.mh.fetch_data(mo.mh, smsMarketingDB, smsMarketingWhere)
			
			# page             = request.GET.get('page')
			# paginator        = vo.Paginator(sms_marketingInfo, 20).get_page(page)

			return render(request, 'marketing_sms_all.html', {'activeAside': 'sms_marketing', 'activeMenu': 'marketing_sms_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'smsMarketingData': smsMarketingInfo, 'confirm': pageConfirmation})
		else:
			return redirect('sign_up')





	def marketing_sms_delete(request, id):
		if request.session.has_key('username'):

			if request.method == 'GET':
				where       = mo.Q_set(id=id)
				pre_update  = mo.mh.update_data(mo.mh, smsMarketingDB, where)
				post_update = pre_update.update(
					trash   = True,
			    )

				msg = {
					'pattern' : 'danger',
					'content' : 'Information Successfully Deleted',
					'style'   : 'danger'
				}

				confirmation = vo.ch.message(vo.ch, 'danger', msg)
				return redirect('marketing_sms_all', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
			else:
				pass
		else:
			return redirect('sign_up')
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
from apps.backend_apps.additional_cost.models import Field_cl as additionalCostFieldDB
from apps.backend_apps.additional_cost.models import Cl as additionalCostDB



# Create your views here.
class Additional_cost(vo, mo):

	def __init__(self, arg):
		super(vo, mo, self).__init__()
		self.arg = arg



	def additional_cost_field_add(request, confirmation):
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
				pageConfirmation = vo.vh.value_decrypter(vo.vh, confirmation)
			else:
			 	pageConfirmation = confirmation

			additionalCostFieldWhere = mo.Q_set(user_id=menuInfo, trash=False)
			additionalCostFieldInfo  = mo.mh.fetch_data(mo.mh, additionalCostFieldDB, additionalCostFieldWhere)

			if request.method == 'POST' and request.POST.get('additional_cost_field_add'):

				slugValue     = request.POST.get('title').replace(' ' , '_').lower()

				fieldInfo  = ''
				try:
					fieldWhere = mo.Q_set(slug=slugValue, trash=False)
					fieldInfo  = mo.mh.get_data(mo.mh, additionalCostFieldDB, fieldWhere)
				except:
					fieldInfo  = ''

				# Data entry block start 
				data = additionalCostFieldDB(
					field_id = vo.vh.unique_custom_id(mo.mh, 'CCF'),
					user_id  = menuInfo,
					title    = request.POST.get('title'),
					slug     = slugValue,
				)

				if fieldInfo != '':
					msg = {
						'pattern' : 'warning',
						'content' : 'Information Missing ! Try again.',
						'style'   : 'warning'
					}
					confirmation = vo.ch.message(vo.ch, 'warning', msg)
					return render(request, 'additional_cost_field_add.html', {'activeAside': 'additional_cost', 'activeMenu': 'additional_cost_field_add', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'additionalCostFieldData': additionalCostFieldInfo, 'confirm': confirmation})
				else:
					msg = {
						'pattern' : 'success',
						'content' : 'Successfully Saved.',
						'style'   : 'success'
					}
					#confirmation = vo.ch.message(vo.ch, 'success', msg)
					confirmation = vo.ch.message(vo.ch, mo.mh.add_data(mo.mh, data), msg)
					return redirect('additional_cost_field_add', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
				# Data entry block end

			elif request.method == 'GET':
				return render(request, 'additional_cost_field_add.html', {'activeAside': 'additional_cost', 'activeMenu': 'additional_cost_field_add', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'additionalCostFieldData': additionalCostFieldInfo, 'confirm': pageConfirmation})

			return render(request, 'additional_cost_field_add.html', {'activeAside': 'additional_cost', 'activeMenu': 'additional_cost_field_add', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'additionalCostFieldData': additionalCostFieldInfo, 'confirm': pageConfirmation})
		else:
			return redirect('sign_up')

			



	def additional_cost_field_edit(request, id):
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

			additionalCostFieldWhere = mo.Q_set(id=id)
			additionalCostFieldInfo  = mo.mh.get_data(mo.mh, additionalCostFieldDB, additionalCostFieldWhere)

			if request.method == 'POST' and request.POST.get('additional_cost_field_update'):

				slugValue     = request.POST.get('title').replace(' ' , '_')

				fInfo  = ''
				try:
					fWhere = mo.Q_set(slug=slugValue, trash=False)
					fInfo  = mo.mh.get_data(mo.mh, additionalCostFieldDB, fWhere)
				except:
					fInfo  = ''

				if fInfo != '':
					msg = {
						'pattern' : 'warning',
						'content' : 'Information Missing ! Try again.',
						'style'   : 'warning'
					}
					confirmation = vo.ch.message(vo.ch, 'warning', msg)
					return render(request, 'additional_cost_field_add.html', {'activeAside': 'additional_cost', 'activeMenu': 'additional_cost_field_add', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'additionalCostFieldData': additionalCostFieldInfo, 'confirm': confirmation})
				else:
					where       = mo.Q_set(id=id)
					pre_update  = mo.mh.update_data(mo.mh, additionalCostFieldDB, where)
					post_update = pre_update.update(
						title   = request.POST.get('title'),
						status  = request.POST.get('status')
					)

					msg = {
						'pattern' : 'success',
						'content' : 'Information Successfully Updated',
						'style'   : 'success'
					}
					confirmation = vo.ch.message(vo.ch, 'success', msg)
					return redirect('additional_cost_field_add', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
			
			elif request.method == 'GET':
				return render(request, 'additional_cost_field_edit.html', {'activeAside': 'additional_cost', 'activeMenu': 'additional_cost_field_add', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'additionalCostFieldData': additionalCostFieldInfo})
			
			return render(request, 'additional_cost_field_edit.html', {'activeAside': 'additional_cost', 'activeMenu': 'additional_cost_field_add', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'additionalCostFieldData': additionalCostFieldInfo})
		else:
			return redirect('sign_up')





	def additional_cost_field_delete(request, id):
		if request.session.has_key('username'):

			if request.method == 'GET':
				where       = mo.Q_set(id=id)
				pre_update  = mo.mh.update_data(mo.mh, additionalCostFieldDB, where)
				post_update = pre_update.update(
					trash   = True,
			    )

				msg = {
					'pattern' : 'danger',
					'content' : 'Information Successfully Deleted',
					'style'   : 'danger'
				}

				confirmation = vo.ch.message(vo.ch, 'danger', msg)
				return redirect('additional_cost_field_add', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
			else:
				pass
		else:
			return redirect('sign_up')





	def additional_cost_add(request, confirmation):
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
				pageConfirmation = vo.vh.value_decrypter(vo.vh, confirmation)
			else:
			 	pageConfirmation = confirmation

			# additional_cost FIELD ::
			fieldWhere = mo.Q_set(user_id=menuInfo, status='active', trash=False)
			fieldInfo  = mo.mh.fetch_data(mo.mh, additionalCostFieldDB, fieldWhere)

			if request.method == 'POST' and request.POST.get('additional_cost_add'):

				# FIELD ::
				additionalCostFieldWhere = mo.Q_set(field_id=request.POST.get('field_id'), trash=False)
				additionalCostFieldInfo  = mo.mh.get_data(mo.mh, additionalCostFieldDB, additionalCostFieldWhere)

				# Data entry block start 
				data = additionalCostDB(
					cost_id     = vo.vh.unique_custom_id(mo.mh, 'BC'),
					user_id     = menuInfo,
					field_id    = additionalCostFieldInfo,
					amount      = request.POST.get('amount'),
					description = request.POST.get('description'),
					spend_by    = request.POST.get('spend_by'),
				)

				if menuInfo:
					msg = {
						'pattern' : 'success',
						'content' : 'Successfully Saved.',
						'style'   : 'success'
					}
					#confirmation = vo.ch.message(vo.ch, 'success', msg)
					confirmation = vo.ch.message(vo.ch, mo.mh.add_data(mo.mh, data), msg)
					return redirect('additional_cost_add', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
				else:
					msg = {
						'pattern' : 'warning',
						'content' : 'Information Missing ! Try again.',
						'style'   : 'warning'
					}
					confirmation = vo.ch.message(vo.ch, 'warning', msg)
					return render(request, 'additional_cost_add.html', {'activeAside': 'additional_cost', 'activeMenu': 'additional_cost_add', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'confirm': confirmation, 'fieldData': fieldInfo})
				# Data entry block end

			elif request.method == 'GET':
				return render(request, 'additional_cost_add.html', {'activeAside': 'additional_cost', 'activeMenu': 'additional_cost_add', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'confirm': pageConfirmation, 'fieldData': fieldInfo})

			return render(request, 'additional_cost_add.html', {'activeAside': 'additional_cost', 'activeMenu': 'additional_cost_add', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'confirm': pageConfirmation, 'fieldData': fieldInfo})
		else:
			return redirect('sign_up')





	def additional_cost_all(request, confirmation):
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
				pageConfirmation = vo.vh.value_decrypter(vo.vh, confirmation)
			else:
			 	pageConfirmation = confirmation

			additionalCostWhere = mo.Q_set(user_id=menuInfo, trash=False)
			additionalCostInfo  = mo.mh.fetch_data(mo.mh, additionalCostDB, additionalCostWhere)
			
			# page             = request.GET.get('page')
			# paginator        = vo.Paginator(additional_costInfo, 20).get_page(page)

			return render(request, 'additional_cost_all.html', {'activeAside': 'additional_cost', 'activeMenu': 'additional_cost_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'additionalCostData': additionalCostInfo, 'confirm': pageConfirmation})
		else:
			return redirect('sign_up')





	def additional_cost_view(request, id):
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

			additionalCostWhere = mo.Q_set(id=id)
			additionalCostInfo  = mo.mh.get_data(mo.mh, additionalCostDB, additionalCostWhere)

			return render(request, 'additional_cost_view.html', {'activeAside': 'additional_cost', 'activeMenu': 'additional_cost_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'additionalCostData': additionalCostInfo})
		else:
			return redirect('sign_up')

			



	def additional_cost_edit(request, id):
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

			# additional_cost FIELD ::
			fieldWhere = mo.Q_set(user_id=menuInfo, status='active', trash=False)
			fieldInfo  = mo.mh.fetch_data(mo.mh, additionalCostFieldDB, fieldWhere)

			additionalCostWhere = mo.Q_set(id=id)
			additionalCostInfo  = mo.mh.get_data(mo.mh, additionalCostDB, additionalCostWhere)

			if request.method == 'POST' and request.POST.get('additional_cost_update'):

				# FIELD ::
				additionalCostFieldWhere = mo.Q_set(field_id=request.POST.get('field_id'), trash=False)
				additionalCostFieldInfo  = mo.mh.get_data(mo.mh, additionalCostFieldDB, additionalCostFieldWhere)

				where       = mo.Q_set(id=id)
				pre_update  = mo.mh.update_data(mo.mh, additionalCostDB, where)
				post_update = pre_update.update(
					field_id    = additionalCostFieldInfo,
					amount      = request.POST.get('amount'),
					description = request.POST.get('description'),
					spend_by    = request.POST.get('spend_by'),
					status      = request.POST.get('status')
			    )

				msg = {
					'pattern' : 'success',
					'content' : 'Information Successfully Updated',
					'style'   : 'success'
				}

				confirmation = vo.ch.message(vo.ch, 'success', msg)
				return redirect('additional_cost_all', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
			
			elif request.method == 'GET':
				return render(request, 'additional_cost_edit.html', {'activeAside': 'additional_cost', 'activeMenu': 'additional_cost_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'additionalCostData': additionalCostInfo, 'fieldData': fieldInfo})
			
			return render(request, 'additional_cost_edit.html', {'activeAside': 'additional_cost', 'activeMenu': 'additional_cost_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'additionalCostData': additionalCostInfo, 'fieldData': fieldInfo})
		else:
			return redirect('sign_up')





	def additional_cost_delete(request, id):
		if request.session.has_key('username'):

			if request.method == 'GET':
				where       = mo.Q_set(id=id)
				pre_update  = mo.mh.update_data(mo.mh, additionalCostDB, where)
				post_update = pre_update.update(
					trash   = True,
			    )

				msg = {
					'pattern' : 'danger',
					'content' : 'Information Successfully Deleted',
					'style'   : 'danger'
				}

				confirmation = vo.ch.message(vo.ch, 'danger', msg)
				return redirect('additional_cost_all', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
			else:
				pass
		else:
			return redirect('sign_up')

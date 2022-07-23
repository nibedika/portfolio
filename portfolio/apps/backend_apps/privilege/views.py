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




# Create your views here.
class Privilege(vo, mo):

	def __init__(self, arg):
		super(vo, mo, self).__init__()
		self.arg = arg



	def privilege_all(request):
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

			userWhere = mo.Q_set(admin_auth=menuInfo, trash=False)
			userInfo  = mo.mh.fetch_data(mo.mh, mo.backendUser, userWhere)

			return render(request, 'privilege_all.html', {'activeAside': 'privilege', 'activeMenu': 'privilege_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'userData': userInfo})
		else:
			return redirect('sign_up')





	def generate_privilege(request, userId):
		if request.session.has_key('username'):

			userWhere = mo.Q_set(user_id=userId, trash=False)
			userInfo  = mo.mh.get_data(mo.mh, mo.backendUser, userWhere)

			componentList = ['supplier', 'godown', 'category', 'subcategory', 'brand', 'product', 'purchase', 'stock', 'offer', 'client', 'sale', 'employee', 'additional_cost', 'report', 'email_marketing', 'sms_marketing', 'message', 'contact', 'setting', 'privilege']

			for i in componentList:
				privilegeWhere  = mo.Q_set(admin_id=userInfo, component=i, trash=False)
				privilegeInfo   = mo.mh.fetch_data(mo.mh, mo.privilegeDB, privilegeWhere)

				if not privilegeInfo:
					# Data entry block start 
					data = mo.privilegeDB(
						privilege_id  = vo.vh.unique_custom_id(mo.mh, 'CP'),
						auth_id       = userInfo.admin_auth,
						admin_id      = userInfo,
						component     = i,
						position      = 0,
						view_action   = False,
						edit_action   = False,
						delete_action = False,
						status        = 'inactive',
					)
					mo.mh.add_data(mo.mh, data)

			return redirect('privilege_all')
		else:
			return redirect('sign_up')





	def set_privilege(request, userId):
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

			userWhere = mo.Q_set(user_id=userId, trash=False)
			userInfo  = mo.mh.get_data(mo.mh, mo.backendUser, userWhere)

			userPrivilegeWhere  = mo.Q_set(auth_id=menuInfo, admin_id=userInfo, trash=False)
			userPrivilegeInfo   = mo.mh.fetch_data(mo.mh, mo.privilegeDB, userPrivilegeWhere, order_by='position')


			if request.method == 'POST' and request.POST.get('set_privilege'):

				moduleListIn    = request.POST.getlist('module[]')
				positionListIn  = request.POST.getlist('position[]')
				componentListIn = request.POST.getlist('component[]')
				viewListIn      = request.POST.getlist('view[]')
				editListIn      = request.POST.getlist('edit[]')
				deleteListIn    = request.POST.getlist('delete[]')


				# Data entry block start..... 
				componentNum = len(list(componentListIn))
				for index in range(componentNum):

					if moduleListIn[index] == 'True':
						statusIn = 'active'

						if viewListIn[index] == 'True':
							viewIn = True
						else:
							viewIn = False

						if editListIn[index] == 'True':
							editIn = True
						else:
							editIn = False

						if deleteListIn[index] == 'True':
							deleteIn = True
						else:
							deleteIn = False
					else:
						statusIn = 'inactive'
						viewIn   = False
						editIn   = False
						deleteIn = False

					

					#print('>>>>>>>>', viewIn)
					#print('>>>>>>>>', editIn)
					#print('>>>>>>>>', deleteIn)

					# HANDELING PRIVILEGE ITEM UPDATE START .....
					where       = mo.Q_set(auth_id=menuInfo, admin_id=userInfo, component=componentListIn[index], trash=False)
					pre_update  = mo.mh.update_data(mo.mh, mo.privilegeDB, where)
					post_update = pre_update.update(
						position      = positionListIn[index],
						view_action   = viewIn,
						edit_action   = editIn,
						delete_action = deleteIn,
						status        = statusIn,
				    )
					# HANDELING PRIVILEGE ITEM UPDATE END .....

				return redirect('set_privilege', userId=userId)

			return render(request, 'set_privilege.html', {'activeAside': 'privilege', 'activeMenu': 'privilege_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'userData': userInfo, 'userPrivilegeData': userPrivilegeInfo})
		else:
			return redirect('sign_up')
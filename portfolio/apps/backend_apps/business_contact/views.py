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
class Business_contact(vo, mo):

	def __init__(self, arg):
		super(vo, mo, self).__init__()
		self.arg = arg




	def business_contact_view(request, contactId):
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


			# Update Message Status Start ...
			where       = mo.Q_set(contact_id=contactId, trash=False)
			pre_update  = mo.mh.update_data(mo.mh, mo.contactDB, where)
			post_update = pre_update.update(
				status   = 'seen',
		    )
			# Update Message Status End ...

			businessContactWhere = mo.Q_set(contact_id=contactId, user_id=menuInfo, trash=False)
			businessContactInfo  = mo.mh.get_data(mo.mh, mo.contactDB, businessContactWhere)

			return render(request, 'business_contact_view.html', {'activeAside': 'business_contact', 'activeMenu': 'business_contact_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'businessContactData': businessContactInfo})
		else:
			return redirect('sign_up')





	def business_contact_all(request, confirmation):
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

			businessContactWhere = mo.Q_set(user_id=menuInfo, trash=False)
			businessContactInfo  = mo.mh.fetch_data(mo.mh, mo.contactDB, businessContactWhere)
			
			# page        = request.GET.get('page')
			# paginator   = vo.Paginator(business_contactInfo, 20).get_page(page)

			if len(confirmation) > 3:
				pageConfirmation   = vo.vh.value_decrypter(vo.vh, confirmation)
			else:
			 	pageConfirmation   = confirmation

			return render(request, 'business_contact_all.html', {'activeAside': 'business_contact', 'activeMenu': 'business_contact_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'businessContactData': businessContactInfo, 'confirm': pageConfirmation})
		else:
			return redirect('sign_up')

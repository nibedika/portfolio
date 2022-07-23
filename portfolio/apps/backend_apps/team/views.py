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
from apps.backend_apps.team.models import Member_cl as memberDB
from apps.backend_apps.team.models import Cl as teamDB



# Create your views here.
class Team(vo, mo):

	def __init__(self, arg):
		super(vo, mo, self).__init__()
		self.arg = arg



	def member_add(request, confirmation):
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

			if request.method == 'POST' and request.POST.get('member_add'):
			    
				if request.FILES.get('attached_file') != None:
					memberImg = vo.vh.file_processor(vo.vh, request.FILES.get('attached_file'), 'member', 'common/member/')
				else:
					memberImg = ' '

				# Data entry block start 
				data = memberDB(
					member_id    = vo.vh.unique_custom_id(mo.mh, 'BM'),
					user_id      = menuInfo,
					name         = request.POST.get('name'),
					email        = request.POST.get('email'),
					contact_no   = request.POST.get('contact_no'),
					address      = request.POST.get('address'),
					description  = request.POST.get('description'),
					remark       = request.POST.get('remark'),
					designation  = request.POST.get('designation'),
					salary       = request.POST.get('salary'),
					joining_date = request.POST.get('joining_date'),
					image        = memberImg
				)

				if menuInfo:
					msg = {
						'pattern' : 'success',
						'content' : 'Successfully Saved.',
						'style'   : 'success'
					}
					#confirmation = vo.ch.message(vo.ch, 'success', msg)
					confirmation = vo.ch.message(vo.ch, mo.mh.add_data(mo.mh, data), msg)
					return redirect('member_add', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
				else:
					msg = {
						'pattern' : 'warning',
						'content' : 'Information Missing ! Try again.',
						'style'   : 'warning'
					}
					confirmation = vo.ch.message(vo.ch, 'warning', msg)
					return render(request, 'member_add.html', {'activeAside': 'member', 'activeMenu': 'member_add', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'confirm': confirmation})
				# Data entry block end

			elif request.method == 'GET':
				return render(request, 'member_add.html', {'activeAside': 'member', 'activeMenu': 'member_add', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'confirm': pageConfirmation})

			return render(request, 'member_add.html', {'activeAside': 'member', 'activeMenu': 'member_add', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'confirm': pageConfirmation})
		else:
			return redirect('sign_up')





	def member_all(request, confirmation):
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

			memberWhere = mo.Q_set(user_id=menuInfo, trash=False)
			memberInfo  = mo.mh.fetch_data(mo.mh, memberDB, memberWhere)
			
			# page      = request.GET.get('page')
			# paginator = vo.Paginator(memberInfo, 20).get_page(page)

			return render(request, 'member_all.html', {'activeAside': 'member', 'activeMenu': 'member_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'memberData': memberInfo, 'confirm': pageConfirmation})
		else:
			return redirect('sign_up')





	def member_view(request, id):
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

			memberWhere = mo.Q_set(id=id)
			memberInfo  = mo.mh.get_data(mo.mh, memberDB, memberWhere)

			return render(request, 'member_view.html', {'activeAside': 'member', 'activeMenu': 'member_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'memberData': memberInfo})
		else:
			return redirect('sign_up')

			



	def member_edit(request, id):
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

			memberWhere = mo.Q_set(id=id)
			memberInfo  = mo.mh.get_data(mo.mh, memberDB, memberWhere)

			if request.method == 'POST' and request.POST.get('member_update'):

				if request.FILES.get('attached_file') != None:
					memberImg = vo.vh.file_processor(vo.vh, request.FILES.get('attached_file'), 'member', 'common/member/')
				else:
					memberImg = memberInfo.image

				where       = mo.Q_set(id=id)
				pre_update  = mo.mh.update_data(mo.mh, memberDB, where)
				post_update = pre_update.update(
					name         = request.POST.get('name'),
					email        = request.POST.get('email'),
					contact_no   = request.POST.get('contact_no'),
					address      = request.POST.get('address'),
					description  = request.POST.get('description'),
					remark       = request.POST.get('remark'),
					designation  = request.POST.get('designation'),
					salary       = request.POST.get('salary'),
					joining_date = request.POST.get('joining_date'),
					leaving_date = request.POST.get('leaving_date'),
					image        = memberImg,
					status       = request.POST.get('status')
			    )

				msg = {
					'pattern' : 'success',
					'content' : 'Information Successfully Updated',
					'style'   : 'success'
				}

				confirmation = vo.ch.message(vo.ch, 'success', msg)
				return redirect('member_all', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
			
			elif request.method == 'GET':
				return render(request, 'member_edit.html', {'activeAside': 'member', 'activeMenu': 'member_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'memberData': memberInfo})
			
			return render(request, 'member_edit.html', {'activeAside': 'member', 'activeMenu': 'member_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'memberData': memberInfo})
		else:
			return redirect('sign_up')





	def member_delete(request, id):
		if request.session.has_key('username'):

			if request.method == 'GET':
				where       = mo.Q_set(id=id)
				pre_update  = mo.mh.update_data(mo.mh, memberDB, where)
				post_update = pre_update.update(
					trash   = True,
			    )

				msg = {
					'pattern' : 'danger',
					'content' : 'Information Successfully Deleted',
					'style'   : 'danger'
				}

				confirmation = vo.ch.message(vo.ch, 'danger', msg)
				return redirect('member_all', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
			else:
				pass
		else:
			return redirect('sign_up')





	def team_add(request, confirmation):
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


			# MEMBER ::
			memberWhere       = mo.Q_set(user_id=menuInfo, status='active', trash=False)
			memberInfo        = mo.mh.fetch_data(mo.mh, memberDB, memberWhere)

			if len(confirmation) > 3:
				pageConfirmation = vo.vh.value_decrypter(vo.vh, confirmation)
			else:
			 	pageConfirmation = confirmation

			if request.method == 'POST' and request.POST.get('team_add'):
				
				# MEMBER ::
				memberWhere = mo.Q_set(member_id=request.POST.get('team_head'), status='active', trash=False)
				member      = mo.mh.get_data(mo.mh, memberDB, memberWhere)

				# Data entry block start 
				data = teamDB(
					team_id     = vo.vh.unique_custom_id(mo.mh, 'BT'),
					user_id     = menuInfo,
					team_head   = member,
					team_name   = request.POST.get('team_name'),
					description = request.POST.get('description'),
					remark      = request.POST.get('remark'),
				)

				if menuInfo:
					msg = {
						'pattern' : 'success',
						'content' : 'Successfully Saved.',
						'style'   : 'success'
					}
					#confirmation = vo.ch.message(vo.ch, 'success', msg)
					confirmation = vo.ch.message(vo.ch, mo.mh.add_data(mo.mh, data), msg)
					return redirect('team_add', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
				else:
					msg = {
						'pattern' : 'warning',
						'content' : 'Information Missing ! Try again.',
						'style'   : 'warning'
					}
					confirmation = vo.ch.message(vo.ch, 'warning', msg)
					return render(request, 'team_add.html', {'activeAside': 'team', 'activeMenu': 'team_add', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'confirm': confirmation, 'memberData': memberInfo})
				# Data entry block end

			elif request.method == 'GET':
				return render(request, 'team_add.html', {'activeAside': 'team', 'activeMenu': 'team_add', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'confirm': pageConfirmation, 'memberData': memberInfo})

			return render(request, 'team_add.html', {'activeAside': 'team', 'activeMenu': 'team_add', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'confirm': pageConfirmation, 'memberData': memberInfo})
		else:
			return redirect('sign_up')





	def team_all(request, confirmation):
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

			teamWhere = mo.Q_set(user_id=menuInfo, status='active', trash=False)
			teamInfo  = mo.mh.fetch_data(mo.mh, teamDB, teamWhere)
			
			# page        = request.GET.get('page')
			# paginator   = vo.Paginator(teamInfo, 20).get_page(page)

			if len(confirmation) > 3:
				pageConfirmation   = vo.vh.value_decrypter(vo.vh, confirmation)
			else:
			 	pageConfirmation   = confirmation

			return render(request, 'team_all.html', {'activeAside': 'team', 'activeMenu': 'team_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'teamData': teamInfo, 'confirm': pageConfirmation})
		else:
			return redirect('sign_up')





	def team_view(request, id):
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

			teamWhere = mo.Q_set(id=id)
			teamInfo  = mo.mh.get_data(mo.mh, teamDB, teamWhere)

			return render(request, 'team_view.html', {'activeAside': 'team', 'activeMenu': 'team_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'teamData': teamInfo})
		else:
			return redirect('sign_up')





	def team_edit(request, id):
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

			teamWhere   = mo.Q_set(id=id)
			teamInfo    = mo.mh.get_data(mo.mh, teamDB, teamWhere)
			
			# MEMBER ::
			memberWhere = mo.Q_set(status='active', trash=False)
			memberInfo  = mo.mh.fetch_data(mo.mh, memberDB, memberWhere)

			if request.method == 'POST' and request.POST.get('team_update'):

				# MEMBER ::
				mWhere = mo.Q_set(team_head=request.POST.get('team_head'), trash=False)
				member      = mo.mh.get_data(mo.mh, memberDB, mWhere)

				where       = mo.Q_set(id=id)
				pre_update  = mo.mh.update_data(mo.mh, teamDB, where)
				post_update = pre_update.update(
					team_head   = member,
					team_name   = request.POST.get('team_name'),
					description = request.POST.get('description'),
					remark      = request.POST.get('remark'),
					status      = request.POST.get('status'),
			    )

				msg = {
					'pattern' : 'success',
					'content' : 'Information Successfully Updated',
					'style'   : 'success'
				}

				confirmation = vo.ch.message(vo.ch, 'success', msg)
				return redirect('team_all', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
			
			elif request.method == 'GET':
				return render(request, 'team_edit.html', {'activeAside': 'team', 'activeMenu': 'team_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'teamData': teamInfo})
			
			return render(request, 'team_edit.html', {'activeAside': 'team', 'activeMenu': 'team_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'teamData': teamInfo})
		else:
			return redirect('sign_up')





	def team_delete(request, id):
		if request.session.has_key('username'):

			if request.method == 'GET':
				where       = mo.Q_set(id=id)
				pre_update  = mo.mh.update_data(mo.mh, teamDB, where)
				post_update = pre_update.update(
					trash   = True,
			    )

				msg = {
					'pattern' : 'danger',
					'content' : 'Information Successfully Deleted',
					'style'   : 'danger'
				}

				confirmation = vo.ch.message(vo.ch, 'danger', msg)
				return redirect('team_all', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
			else:
				pass
		else:
			return redirect('sign_up')

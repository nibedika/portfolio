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
class Backend_access(vo, mo):

	def __init__(self, arg):
		super(vo, mo, self).__init__()
		self.arg = arg


	def sign_up(request):

		try:
			userWhere = mo.Q_set(status='active', trash=False)
			userInfo  = mo.mh.fetch_data(mo.mh, mo.backendUser, userWhere)
		except:
			userInfo  = ''

		if request.method == 'POST' and request.POST.get('sign_up'):

			authId    = request.POST.get('admin_auth')

			try:
				authWhere = mo.Q_set(username=authId, status='active', trash=False)
				authInfo  = mo.mh.get_data(mo.mh, mo.backendUser, authWhere)
			except:
				authInfo  = None

			data = mo.backendUser(
				user_id         = vo.vh.unique_custom_id(mo.mh, 'BU'),
				name            = request.POST.get('name'),
				username        = request.POST.get('username'),
				email           = request.POST.get('email'),
				password        = request.POST.get('password'),
				confirmed_pass  = request.POST.get('confirmed_pass'),
				birthday        = request.POST.get('birthday'),
				gender          = request.POST.get('gender'),
				account_type    = request.POST.get('account_type'),
				admin_auth      = authInfo,
				designation     = request.POST.get('designation')
			)

			# Username and Email existance check start
			username          = request.POST.get('username')
			email             = request.POST.get('email')
			usernameWhere     = mo.Q_set(username=username)
			usernameExixtance = mo.mh.exists_data(mo.mh, mo.backendUser, usernameWhere)
			emailWhere        = mo.Q_set(email=email)
			emailExixtance    = mo.mh.exists_data(mo.mh, mo.backendUser, emailWhere)
			# Username and Email existance check end

			# Data entry block start 
			if usernameExixtance == False and emailExixtance == False:

				emailCode = vo.vh.unique_email_code(vo.vh)
				subject   = 'Email Verification'
				message   = 'Your email verification code is  - ' + emailCode
				sender    = 'Management Site'
				receiver  = email

				msg = {
					'pattern' : 'success',
					'content' : 'Congrats ! You are way to join Management Site.',
					'style'   : 'success'
				}

				emailSend    = vo.eh.mail_seld(vo.eh, subject, message, sender, receiver)
				confirmation = vo.ch.message(vo.ch, mo.mh.add_data(mo.mh, data), msg)

				return redirect('email_verify', emailCode=(vo.vh.value_encrypter(vo.vh, emailCode)), email=(vo.vh.value_encrypter(vo.vh, email)), confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
			else:
				msg = {
					'pattern' : 'warning',
					'content' : 'Username or email is already in use. Try another !',
					'style'   : 'warning'
				}
				confirmation = vo.ch.message(vo.ch, 'warning', msg)
				return render(request, 'sign_up.html', {'userData': userInfo, 'confirm': confirmation})
			# Data entry block end

		elif request.method == 'GET':
			return render(request, 'sign_up.html', {'userData': userInfo, 'confirm': ''})

		return render(request, 'sign_up.html', {'userData': userInfo, 'confirm': ''})





	def email_verify(request, emailCode, email, confirmation):

		idCode = vo.vh.value_decrypter(vo.vh, emailCode)
		idEmail = vo.vh.value_decrypter(vo.vh, email)
		idConfirmation = vo.vh.value_decrypter(vo.vh, confirmation)

		if request.method == 'POST' and request.POST.get('email_verify') and idCode != None  and idEmail != None:

			# Identity Verification check start
			email_code = request.POST.get('email_code')
			# Identity Verification check end

			# Data entry block start 
			if idCode == email_code:

				where              = mo.Q_set(email=idEmail, status='active', trash=False)
				pre_email_verify   = mo.mh.update_data(mo.mh, mo.backendUser, where)
				post_email_verify  = pre_email_verify.update(
					email_verified = True
			    )

				return redirect('sign_in')
			else:
				msg = {
					'pattern' : 'warning',
					'content' : 'Invalid Information !',
					'style'   : 'warning'
				}
				confirmation = vo.ch.message(vo.ch, 'warning', msg)
				return render(request, 'mail_verify.html', {'confirm': confirmation})
			# Data entry block end 

		elif request.method == 'GET':
			return render(request, 'mail_verify.html', {'confirm': idConfirmation})

		return render(request, 'mail_verify.html', {'confirm': idConfirmation})





	def sign_in(request):
		if request.method == 'POST' and request.POST.get('sign_in'):

			signinUsername = request.POST.get('username')
			signinPassword = request.POST.get('password')

			userWhere     = mo.Q_set(username=signinUsername, password=signinPassword, email_verified=True, status='active', trash=False)
			userExixtance = mo.mh.exists_data(mo.mh, mo.backendUser, userWhere)

			if userExixtance == True:
				where    = mo.Q_set(username=signinUsername, password=signinPassword, email_verified=True, status='active', trash=False)
				userInfo = mo.mh.fetch_data(mo.mh, mo.backendUser, where)

				if userInfo[0].username == signinUsername and userInfo[0].confirmed_pass == signinPassword:

					# data = mo.backendSession(
					# 	re_user_id  = userInfo[0].re_user_id,
					# 	username    = userInfo[0].username,
					# 	email       = userInfo[0].email,
					# 	ip          = vbp.sh.get_ip(vbp.sh, request),
					# 	browser     = vbp.sh.get_browser(vbp.sh, request),
					# 	os          = vbp.sh.get_os(vbp.sh, request),
					# 	device      = vbp.sh.get_device(vbp.sh, request),
					# 	device_type = vbp.sh.get_device_type(vbp.sh, request),
					# 	brand       = vbp.sh.get_brand(vbp.sh, request),
					# 	status      = 'active',
					# 	trash       = False
					# )

					request.session['username'] = signinUsername
					#session_start = mo.mh.add_data(mo.mh, data)

					return redirect('home')
				else:
					msg = {
						'pattern' : 'warning',
						'content' : 'Invalid username or password !',
						'style'   : 'warning'
					}
					confirmation = vo.ch.message(vo.ch, 'warning', msg)
					return render(request, 'sign_in.html', {'confirm': confirmation})
			else:
				msg = {
					'pattern' : 'warning',
					'content' : 'User is not exist !',
					'style'   : 'warning'
				}
				confirmation = vo.ch.message(vo.ch, 'warning', msg)
				return render(request, 'sign_in.html', {'confirm': confirmation})

		elif request.method == 'GET':
			return render(request, 'sign_in.html')
		
		return render(request, 'sign_in.html')





	def home(request):
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

			# member ::
			memberWhere = mo.Q_set(user_id=menuInfo, trash=False)
			memberInfo  = mo.mh.fetch_data(mo.mh, memberDB, memberWhere)

			# team ::
			teamWhere = mo.Q_set(user_id=menuInfo, trash=False)
			teamInfo  = mo.mh.fetch_data(mo.mh, teamDB, teamWhere)

			return render(request, 'home.html', {'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'memberData': memberInfo, 'saleItemData': 'saleItemInfo', 'salePrice': 'salePrice', 'teamData': teamInfo, 'contactData': contactInfo})
		else:
			return redirect('sign_up')





	def sign_out(request):
		if request.session.has_key('username'):
			try:
				sessionUsername = request.session['username']
				userWhere       = mo.Q_set(username=sessionUsername, status='active', trash=False)
				menuInfo        = mo.mh.get_data(mo.mh, mo.backendUser, userWhere)

				# data = mo.backendSession(
				# 	re_user_id  = menuInfo[0].re_user_id,
				# 	username    = menuInfo[0].username,
				# 	email       = menuInfo[0].email,
				# 	ip          = vbp.sh.get_ip(vbp.sh, request),
				# 	browser     = vbp.sh.get_browser(vbp.sh, request),
				# 	os          = vbp.sh.get_os(vbp.sh, request),
				# 	device      = vbp.sh.get_device(vbp.sh, request),
				# 	device_type = vbp.sh.get_device_type(vbp.sh, request),
				# 	brand       = vbp.sh.get_brand(vbp.sh, request),
				# 	status      = 'inactive',
				# 	trash       = False
				# )

				# session_end = mo.mh.add_data(mo.mh, data)

				del request.session['username']
				return redirect('sign_up')
			except:
				return redirect('sign_up')
		else:
			return redirect('sign_up')



 

	def password_recovery_surface(request):

		if request.method == 'POST' and request.POST.get('password_recovery_info'):

			# Username and Email existance check start
			username          = request.POST.get('username')
			email             = request.POST.get('email')

			usernameWhere     = mo.Q_set(username=username, status='active', trash=False)
			usernameExixtance = mo.mh.exists_data(mo.mh, mo.backendUser, usernameWhere)

			emailWhere        = mo.Q_set(email=email, status='active', trash=False)
			emailExixtance    = mo.mh.exists_data(mo.mh, mo.backendUser, emailWhere)
			# Username and Email existance check end

			userWhere         = mo.Q_set(username=username, email=email, status='active', trash=False)
			userInfo          = mo.mh.get_data(mo.mh, mo.backendUser, userWhere)
 
			# Data entry block start 
			if usernameExixtance == True and emailExixtance == True and username == userInfo.username and email == userInfo.email:

				emailCode = vo.vh.unique_email_code(vo.vh)
				subject   = 'E-commerce password recovery'
				message   = 'Your password recovery code is  - ' + emailCode
				sender    = 'E-commerce Site'
				receiver  = email

				msg = {
					'pattern' : 'success',
					'content' : 'Congrats ! You are way to recovery E-commerce password.',
					'style'   : 'success'
				}

				emailSend    = vcp.eh.mail_seld(vcp.eh, subject, message, sender, receiver)
				confirmation = vo.ch.message(vo.ch, 'success', msg)
				return redirect('password_recovery_code', emailCode=(vo.vh.value_encrypter(vo.vh, emailCode)), email=(vo.vh.value_encrypter(vo.vh, email)), confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
			else:
				msg = {
					'pattern' : 'warning',
					'content' : 'Username or email is not valid. Try again !',
					'style'   : 'warning'
				}
				confirmation = vo.ch.message(vo.ch, 'warning', msg)
				return render(request, 'password_recovery_surface.html', {'confirm': confirmation})
			# Data entry block end 
		elif request.method == 'GET':
			return render(request, 'password_recovery_surface.html')

		return redirect('sign_up')





	def password_recovery_code(request, emailCode, email, confirmation):

		idCode = vo.vh.value_decrypter(vo.vh, emailCode)
		idEmail = vo.vh.value_decrypter(vo.vh, email)
		idConfirmation = vo.vh.value_decrypter(vo.vh, confirmation)

		if request.method == 'POST' and request.POST.get('password_recovery_code') and idCode != None  and idEmail != None:

			# Identity Verification check start
			email_code = request.POST.get('email_code')
			# Identity Verification check end

			# Data entry block start 
			if idCode == email_code:
				return redirect('password_recovery',  email=(vo.vh.value_encrypter(vo.vh, email)), confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
			else:
				msg = {
					'pattern' : 'warning',
					'content' : 'Invalid Information !',
					'style'   : 'warning'
				}
				confirmation = vo.ch.message(vo.ch, 'warning', msg)
				return render(request, 'password_recovery_code.html', {'confirm': confirmation})
			# Data entry block end 

		elif request.method == 'GET':
			return render(request, 'password_recovery_code.html', {'confirm': idConfirmation})
		
		return render(request, 'password_recovery_code.html', {'confirm': idConfirmation})





	def password_recovery(request, email, confirmation):

		idEmail = vo.vh.value_decrypter(vo.vh, email)

		if request.method == 'POST' and request.POST.get('password_recovery'):

			# Data entry block start 
			where       = mo.Q_set(email=idEmail, status='active', trash=False)
			pre_update  = mo.mh.update_data(mo.mh, mo.backendUser, where)
			post_update = pre_update.update(
				password         = request.POST.get('password'),
				confirmed_pass   = request.POST.get('password')
		    )
			# Data entry block end 

			return redirect('sign_up')

		elif request.method == 'GET':
			return render(request, 'password_recovery.html')

		return render(request, 'password_recovery.html')





	def account_setting(request):
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

			if request.method == 'POST' and request.POST.get('update'):

				username = request.session['username']

				if request.FILES.get('profile_img') != None:
					newProfileImg = vo.vh.file_processor(vo.vh, request.FILES.get('profile_img'), 'profile-img', 'account-img/profile-img/')
				else:
					newProfileImg = menuInfo.profile_img

				if request.FILES.get('display_pic') != None:
					displayPic = vo.vh.file_processor(vo.vh, request.FILES.get('display_pic'), 'display_pic', 'account-img/display-pic/')
				else:
					displayPic = menuInfo.display_pic

				if request.FILES.get('logo') != None:
					newLogo = vo.vh.file_processor(vo.vh, request.FILES.get('logo'), 'logo', 'account-img/logo/')
				else:
					newLogo = menuInfo.logo

				if request.FILES.get('banner') != None:
					newBanner = vo.vh.file_processor(vo.vh, request.FILES.get('banner'), 'banner', 'account-img/banner/')
				else:
					newBanner = menuInfo.banner

				# Data entry block start 
				where       = mo.Q_set(username=username)
				pre_update  = mo.mh.update_data(mo.mh, mo.backendUser, where)
				post_update = pre_update.update(
					name            = request.POST.get('name'),
					designation     = request.POST.get('designation'),
					gender          = request.POST.get('gender'),
					contact_no      = request.POST.get('contact_no'),
					address         = request.POST.get('address'),
					city            = request.POST.get('city'),
					country         = request.POST.get('country'),
					available_in    = request.POST.get('available_in'),
					available_for   = request.POST.get('available_for'),
					intro           = request.POST.get('intro'),
					profile_img     = newProfileImg,
					display_pic     = displayPic,
					logo            = newLogo,
					banner          = newBanner,
					website         = request.POST.get('website'),
					facebook_link   = request.POST.get('facebook_link'),
					instagram_link  = request.POST.get('instagram_link'),
					whatsup_link    = request.POST.get('whatsup_link'),
					twitter_link    = request.POST.get('twitter_link'),
					google_link     = request.POST.get('google_link'),
					youtube_link    = request.POST.get('youtube_link'),
					linkedin_link   = request.POST.get('linkedin_link'),
					pinterest_link  = request.POST.get('pinterest_link'),
					tumblr_link     = request.POST.get('tumblr_link'),
					other_link      = request.POST.get('other_link'),
					info_verified   = True,
			    )
				# Data entry block end 

				return redirect('account_setting')

			elif request.method == 'GET':
				return render(request, 'account_setting.html', {'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo})

			return render(request, 'account_setting.html', {'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo})
		else:
			return redirect('sign_up')





	def all_account(request):
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

			try:
				if menuInfo.account_type == 'account':
					userWhere = mo.Q_set(admin_auth=menuInfo, trash=False)
					userInfo  = mo.mh.fetch_data(mo.mh, mo.backendUser, userWhere)
				else:
					userInfo  = ' '
			except:
				userInfo  = ' '
			

			if request.method == 'POST' and request.POST.get('change_status'):

				status = request.POST.get('status')
				userId = request.POST.get('userId')
				# print('Data : ', status, userId)

				# Data update block start 
				where       = mo.Q_set(username=userId)
				pre_update  = mo.mh.update_data(mo.mh, mo.backendUser, where)
				post_update = pre_update.update(
					status  = status
			    )
				# Data update block end 

				return JsonResponse({
					'status' : status,
					'userId' : userId,
				})

			elif request.method == 'GET':
				return render(request, 'all_account.html', {'activeAside': 'all_account', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'userData': userInfo})

			return render(request, 'all_account.html', {'activeAside': 'all_account', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'userData': userInfo})
		else:
			return redirect('sign_up')

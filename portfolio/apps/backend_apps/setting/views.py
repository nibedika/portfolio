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
from apps.backend_apps.setting.models import Rules_cl as rulesDB
from apps.backend_apps.setting.models import Website_cl as websiteDB



# Create your views here.
class Setting(vo, mo):

	def __init__(self, arg):
		super(vo, mo, self).__init__()
		self.arg = arg



	def rules_setting(request, confirmation):
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

			rulesWhere = mo.Q_set(trash=False)
			rulesInfo  = mo.mh.fetch_data(mo.mh, rulesDB, rulesWhere)
			
			# page      = request.GET.get('page')
			# paginator = vo.Paginator(rulesInfo, 20).get_page(page)

			if request.method == 'POST' and request.POST.get('business_rules_add'):

				# Data entry block start 
				data = rulesDB(
					rules_id      = vo.vh.unique_custom_id(mo.mh, 'BR'),
					user_id       = menuInfo,
					preference    = request.POST.get('preference'),
					conditions    = request.POST.get('conditions'),
					authorised_by = request.POST.get('authorised_by')
				)

				if menuInfo:
					msg = {
						'pattern' : 'success',
						'content' : 'Successfully Saved.',
						'style'   : 'success'
					}
					#confirmation = vo.ch.message(vo.ch, 'success', msg)
					confirmation = vo.ch.message(vo.ch, mo.mh.add_data(mo.mh, data), msg)
					return redirect('rules_setting', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
				else:
					msg = {
						'pattern' : 'warning',
						'content' : 'Information Missing ! Try again.',
						'style'   : 'warning'
					}
					confirmation = vo.ch.message(vo.ch, 'warning', msg)
					return render(request, 'rules_add.html', {'activeAside': 'setting', 'activeMenu': 'business_rules_add', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'rulesData': rulesInfo, 'confirm': confirmation})
				# Data entry block end

			elif request.method == 'GET':
				return render(request, 'rules_add.html', {'activeAside': 'setting', 'activeMenu': 'business_rules_add', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'rulesData': rulesInfo, 'confirm': pageConfirmation})

			return render(request, 'rules_add.html', {'activeAside': 'setting', 'activeMenu': 'business_rules_add', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'rulesData': rulesInfo, 'confirm': pageConfirmation})
		else:
			return redirect('sign_up')





	def rules_view(request, id):
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

			rulesWhere = mo.Q_set(id=id)
			rulesInfo  = mo.mh.get_data(mo.mh, rulesDB, rulesWhere)

			return render(request, 'rules_view.html', {'activeAside': 'business_rules', 'activeMenu': 'rules_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'rulesData': rulesInfo})
		else:
			return redirect('sign_up')

			



	def rules_edit(request, id):
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

			rulesWhere = mo.Q_set(id=id)
			rulesInfo  = mo.mh.get_data(mo.mh, rulesDB, rulesWhere)

			if request.method == 'POST' and request.POST.get('rules_update'):

				where       = mo.Q_set(id=id)
				pre_update  = mo.mh.update_data(mo.mh, rulesDB, where)
				post_update = pre_update.update(
					preference    = request.POST.get('preference'),
					conditions    = request.POST.get('conditions'),
					authorised_by = request.POST.get('authorised_by'),
					status        = request.POST.get('status')
				)

				msg = {
					'pattern' : 'success',
					'content' : 'Information Successfully Updated',
					'style'   : 'success'
				}

				confirmation = vo.ch.message(vo.ch, 'success', msg)
				return redirect('rules_all', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
			
			elif request.method == 'GET':
				return render(request, 'rules_edit.html', {'activeAside': 'setting', 'activeMenu': 'rules_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'rulesData': rulesInfo})
			
			return render(request, 'rules_edit.html', {'activeAside': 'setting', 'activeMenu': 'rules_all', 'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'contactData': contactInfo, 'rulesData': rulesInfo})
		else:
			return redirect('sign_up')





	def rules_delete(request, id):
		if request.session.has_key('username'):

			if request.method == 'GET':
				where       = mo.Q_set(id=id)
				pre_update  = mo.mh.update_data(mo.mh, rulesDB, where)
				post_update = pre_update.update(
					trash   = True,
			    )

				msg = {
					'pattern' : 'danger',
					'content' : 'Information Successfully Deleted',
					'style'   : 'danger'
				}

				confirmation = vo.ch.message(vo.ch, 'danger', msg)
				return redirect('rules_setting', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
			else:
				pass
		else:
			return redirect('sign_up')





	def website_setting(request, confirmation):
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

			try:
				websiteWhere = mo.Q_set(trash=False)
				websiteInfo  = mo.mh.fetch_data(mo.mh, websiteDB, websiteWhere).last()
			except:
				websiteInfo  = ''


			if request.method == 'POST' and request.POST.get('update'):

				if request.FILES.get('slider_img1') != None:
					sliderImg1 = vo.vh.file_processor(vo.vh, request.FILES.get('slider_img1'), 'slider_img1', 'account-img/website/slider-img1')
				else:
					sliderImg1 = websiteInfo.slider_img1

				if request.FILES.get('slider_img2') != None:
					sliderImg2 = vo.vh.file_processor(vo.vh, request.FILES.get('slider_img2'), 'slider_img2', 'account-img/website/slider-img2')
				else:
					sliderImg2 = websiteInfo.slider_img2
					
				if request.FILES.get('slider_img3') != None:
					sliderImg3 = vo.vh.file_processor(vo.vh, request.FILES.get('slider_img3'), 'slider_img3', 'account-img/website/slider-img3')
				else:
					sliderImg3 = websiteInfo.slider_img3
					
				if request.FILES.get('about_img') != None:
					aboutImg = vo.vh.file_processor(vo.vh, request.FILES.get('about_img'), 'about_img', 'account-img/website/about-img')
				else:
					aboutImg = websiteInfo.about_img
					
				if request.FILES.get('cv_file') != None:
					cvFile = vo.vh.file_processor(vo.vh, request.FILES.get('cv_file'), 'cv_file', 'account-img/website/cv-file')
				else:
					cvFile = websiteInfo.cv_file


				if websiteInfo:
					# Data entry block start 
					where       = mo.Q_set(trash=False)
					pre_update  = mo.mh.update_data(mo.mh, websiteDB, where)
					post_update = pre_update.update(
						slider_img1 = sliderImg1,
						slider_txt1 = request.POST.get('slider_txt1'),
						slider_img2 = sliderImg2,
						slider_txt2 = request.POST.get('slider_txt2'),
						slider_img3 = sliderImg3,
						slider_txt3 = request.POST.get('slider_txt3'),
						cv_file     = cvFile,
						about_img   = aboutImg,
						about_txt   = request.POST.get('about_txt'),
					)
					# Data entry block end 
					msg = {
						'pattern' : 'success',
						'content' : 'Successfully Updated.',
						'style'   : 'success'
					}
					confirmation = vo.ch.message(vo.ch, 'success', msg)
					return redirect('website_setting', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
				else:
					# Data entry block start 
					data = websiteDB(
						website_id  = vo.vh.unique_custom_id(mo.mh, 'BW'),
						user_id     = menuInfo,
						slider_img1 = sliderImg1,
						slider_txt1 = request.POST.get('slider_txt1'),
						slider_img2 = sliderImg2,
						slider_txt2 = request.POST.get('slider_txt2'),
						slider_img3 = sliderImg3,
						slider_txt3 = request.POST.get('slider_txt3'),
						cv_file     = cvFile,
						about_img   = aboutImg,
						about_txt   = request.POST.get('about_txt'),
					)

					if menuInfo:
						msg = {
							'pattern' : 'success',
							'content' : 'Successfully Saved.',
							'style'   : 'success'
						}
						confirmation = vo.ch.message(vo.ch, mo.mh.add_data(mo.mh, data), msg)
						return redirect('website_setting', confirmation=(vo.vh.value_encrypter(vo.vh, confirmation)))
					else:
						msg = {
							'pattern' : 'warning',
							'content' : 'Information Missing ! Try again.',
							'style'   : 'warning'
						}
						confirmation = vo.ch.message(vo.ch, 'warning', msg)
						return render(request, 'website_setting.html', {'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'websiteData': websiteInfo, 'contactData': contactInfo, 'confirm': pageConfirmation})
					# Data entry block end

			elif request.method == 'GET':
				return render(request, 'website_setting.html', {'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'websiteData': websiteInfo, 'contactData': contactInfo, 'confirm': pageConfirmation})

			return render(request, 'website_setting.html', {'menuData': menuInfo, 'privilegeData': privilegeInfo, 'navMsgData': navMsgInfo, 'websiteData': websiteInfo, 'contactData': contactInfo, 'confirm': pageConfirmation})
		else:
			return redirect('sign_up')
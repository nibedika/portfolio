# Buildin Package
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST

# View Prime Class Import 
from origin.view_origin import View_origin as vo

# Model Prime Class Import 
from origin.model_origin import Model_origin as mo



# Create your views here.
class User_contact(vo, mo):

	def __init__(self, arg):
		super(vo, mo, self).__init__()
		self.arg = arg




	def user_contact_add(request, userId, confirmation):

		receiverWhere = mo.Q_set(user_id=userId, status='active', trash=False)
		receiverInfo  = mo.mh.get_data(mo.mh, mo.backendUser, receiverWhere)

		if len(confirmation) > 3:
			pageConfirmation = vo.vh.value_decrypter(vo.vh, confirmation)
		else:
		 	pageConfirmation = confirmation

		if request.method == 'POST' and request.POST.get('user_contact_add'):

			if request.FILES.get('attached_file') != None:
				messageFile = vo.vh.file_processor(vo.vh, request.FILES.get('attached_file'), 'user_contact', 'user/user_contact/')
			else:
				messageFile = ''

			# Data entry block start 
			data = mo.contactDB(
				contact_id = vo.vh.unique_custom_id(mo.mh, 'UC'),
				user_id    = receiverInfo,
				name       = request.POST.get('name'),
				email      = request.POST.get('email'),
				subject    = request.POST.get('subject'),
				text       = request.POST.get('text'),
				file       = messageFile
			)

			if receiverInfo:
				msg = {
					'pattern' : 'success',
					'content' : 'Successfully Send.',
					'style'   : 'success'
				}
				#confirmation = vo.ch.message(vo.ch, 'success', msg)
				confirmation = vo.ch.message(vo.ch, mo.mh.add_data(mo.mh, data), msg)
				return redirect('web')
			else:
				msg = {
					'pattern' : 'warning',
					'content' : 'Information Missing ! Try again.',
					'style'   : 'warning'
				}
				confirmation = vo.ch.message(vo.ch, 'warning', msg)
				return redirect('web')
			# Data entry block end

		elif request.method == 'GET':
			pass

import json
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.db.models import Q as Q_set

from package.internal.model_helper import Model_helper as mh


from apps.frontend_apps.office_apps.businessman.product.models import Businessman as businessmanProduct


class Ajax_helper(mh):
	"""All Model Prime import this class so that they got the 
	Model Helper class and Backend Apps's Model will Use this 
	class attributes through Pirme """

	def __init__(self, arg):
		#super('', self).__init__()
		self.arg = arg



	def getData(self, table, condition):
		# self.table     = table
		# self.condition = condition
		# self.result    = self.table.objects.get(self.condition)
		# print(self.result)
		pass



	#@require_POST
	def fetchData(request):
		if request.session.has_key('username') and request.is_ajax() == True:

			content = request.POST.get('data')
			#receive = json.loads(content)
			#table  = receive.table

			try:
				
				where  = Q_set(id=1)
				result = mh.get_data(mh, businessmanProduct, where)

				#dump = json.dumps(result)
				#print(result)
				#return HttpResponse(result, content_type='application/json')
				#result = json.dumps(result)


				return JsonResponse({
					'status' : 'ok',
					'name'   : content,
				})
			except:
				pass

			#content = request.POST.get('data')
			#receive = json.loads(content)
			#return content

			#table     = table
			#condition = condition

			#table  = self.receive.table
			#print(table)
			#where  = Q_set()
			#result = mh.fetch_data(mh, table, where)
			#print(self.result)

		else:
			pass



	def fetchLimit(self, table, condition, first, last, order_by='-id'):
		# self.table     = table
		# self.condition = condition
		# self.first     = first
		# self.last      = last
		# self.order_by  = order_by
		# self.result    = self.table.objects.filter(self.condition).order_by(self.order_by)[self.first:self.last]
		# print(self.result)
		pass



	def fetchOne(self, table, condition, order_by='-id'):
		# self.table     = table
		# self.condition = condition
		# self.order_by  = order_by
		# self.result    = self.table.objects.filter(self.condition).order_by(self.order_by)[:1]
		# print(self.result)
		pass




	def fetchJoinData(self, table, condition, order_by='-id'):
		# self.table     = table
		# self.condition = condition
		# self.order_by  = order_by
		# self.result    = self.table.objects.select_related(self.condition).order_by(self.order_by)
		# print(self.result)
		pass




	def deleteData(self, table, condition):
		# self.table     = table
		# self.condition = condition
		# self.result    = self.table.objects.filter(self.condition).delete()
		# print('danger')
		pass
		






	# def addData(self):
	# 	self.table   = table
	# 	self.data   = data
	# 	self.result = self.data.save()

	# 	data = postUpload(
	# 		post_id    = vgp.vh.unique_custom_id(mgp.mh, 'post'),
	# 		re_user_id = userInfo.re_user_id,
	# 		author	   = userInfo,
	# 		username   = sessionUsername,
	# 		text       = request.POST.get('text'),
	# 		file       = vgp.vh.file_processor(vgp.vh, request.FILES.get('file'), 'post', 'frontend/upload/post/'),
	# 		status     = 'public',
	# 	)

	# 	self.result = mh.add_data(mh, data)

	# 	print('success')




	def updateData(self, table, condition):
		# self.table     = table
		# self.condition = condition
		# self.result    = self.table.objects.select_related().filter(self.condition)
		# print(self.result)
		pass



	def countData(self, table, condition):
		# self.table     = table
		# self.condition = condition
		# self.result    = self.table.objects.filter(self.condition).count()
		# print(self.result)
		pass



	def existsData(self, table, condition):
		# self.table     = table
		# self.condition = condition
		# if self.table.objects.filter(self.condition).exists():
		# 	print(True)
		# else:
		# 	print(False)
		pass


class Model_helper():
	"""All Model Prime import this class so that they got the 
	Model Helper class and Backend Apps's Model will Use this 
	class attributes through Pirme """

	def __init__(self, arg):
		#super('', self).__init__()
		self.arg = arg



	def get_data(self, table, condition):
		self.table     = table
		self.condition = condition
		self.result    = self.table.objects.get(self.condition)
		return self.result



	def fetch_data(self, table, condition, order_by='-id'):
		self.table     = table
		self.condition = condition
		self.order_by  = order_by
		self.result    = self.table.objects.filter(self.condition).order_by(self.order_by)
		return self.result



	def fetch_like_data(self, table, like_cond, condition, order_by='-id'):
		self.table     = table
		self.like_cond = like_cond
		self.condition = condition
		self.order_by  = order_by
		self.result    = self.table.objects.filter(self.condition).filter(self.like_cond).order_by(self.order_by)
		return self.result



	def fetch_limit(self, table, condition, first, last, order_by='-id'):
		self.table     = table
		self.condition = condition
		self.first     = first
		self.last      = last
		self.order_by  = order_by
		self.result    = self.table.objects.filter(self.condition).order_by(self.order_by)[self.first:self.last]
		return self.result



	def fetch_last(self, table, condition):
		self.table     = table
		self.condition = condition
		self.order_by  = order_by
		self.result    = self.table.objects.filter(self.condition).last()
		return self.result
		


	def fetch_distinct(self, table, group_by, condition):
		self.table     = table
		self.group_by  = group_by
		self.condition = condition
		self.result    = self.table.objects.filter(self.condition).values_list(self.group_by, flat=True).distinct()
		return self.result
		


	def count_data(self, table, condition):
		self.table     = table
		self.condition = condition
		self.result    = self.table.objects.filter(self.condition).count()
		return self.result



	def exists_data(self, table, condition):
		self.table     = table
		self.condition = condition
		if self.table.objects.filter(self.condition).exists():
			return True
		else:
			return False



	def add_data(self, data):
		self.data   = data
		self.result = self.data.save()
		return 'success'



	def update_data(self, table, condition):
		self.table     = table
		self.condition = condition
		self.result    = self.table.objects.select_related().filter(self.condition)
		return self.result



	def delete_data(self, table, condition):
		self.table     = table
		self.condition = condition
		self.result    = self.table.objects.filter(self.condition).delete()
		return 'danger'

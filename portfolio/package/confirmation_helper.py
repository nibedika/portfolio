
class Confirmation_helper():
	"""All Model Prime import this class so that they got the 
	Confirmation Helper class and Backend Apps's View will Use this 
	class attributes through Pirme """

	def __init__(self, arg):
		#super('', self).__init__()
		self.arg = arg
		


	def message(self, return_type, msg):

		self.return_type = return_type
		self.msg         = msg

		self.pattern = {
			'success' : 'SUCCESS',
			'info'    : 'INFO',
			'warning' : 'WARNING',
			'danger'  : 'DANGER'
		}

		self.content = {
			'success' : 'Successfully Done !',
			'info'    : 'Information Fetched !',
			'warning' : 'Warning !',
			'danger'  : 'Action Denied !'
		}

		self.style = {
			'success' : 'success',
			'info'    : 'info',
			'warning' : 'warning',
			'danger'  : 'danger'
		}


		if len(self.msg)>0:

			if self.msg.get('pattern'):
				self.pattern[self.return_type] = self.msg.get('pattern')

			if self.msg.get('content'):
				self.content[self.return_type] = self.msg.get('content')

			if self.msg.get('style'):
				self.style[self.return_type]   = self.msg.get('style')

		return_msg_items = self.pattern[self.return_type].upper(), self.content[self.return_type], self.style[self.return_type];
		return list(return_msg_items)
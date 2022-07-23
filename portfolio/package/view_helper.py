
class View_helper():
	"""All View Prime import this class so that they got the 
	Model Helper class and Backend Apps's View will Use this 
	class attributes through Pirme """

	def __init__(self, arg):
		#super('', self).__init__()
		self.arg = arg
		


	def unique_custom_id(self, prefix):
		import time
		self.prefix = prefix.upper()
		self.miliTime = int(round(time.time() * 1000))
		self.result = str(self.prefix) + str(self.miliTime)
		return self.result



	def unique_email_code(self):
		import time
		self.miliTime = int(round(time.time() * 1000))
		self.result = str(self.miliTime)
		return self.result



	def incremented_invoice_no(self, prefix, count):
		from datetime import date
		today 		  = str(date.today())
		dateStr 	  = today.replace("-", "")
		self.prefix   = str(prefix.upper())
		self.count    = str(count + 1)
		self.zeroFill = self.count.zfill(6)
		self.result   = self.prefix + dateStr + self.zeroFill
		return self.result



	def value_encrypter(self, value):
		import time
		import random
		import string
		self.miliTime = int(round(time.time() * 1000))
		self.timeStr  = str(self.miliTime)
		self.letters  = string.ascii_lowercase
		self.randStr  = ''.join(random.choice(self.letters) for i in range(12))

		from django.core import signing
		self.value  = value
		self.result = str(signing.dumps(self.value)) + str(self.randStr) + str(self.timeStr)
		return self.result



	def value_decrypter(self, value):
		from django.core import signing
		self.strVal = str(value)[-25:]
		self.val    = value.replace(self.strVal, '')
		self.result = signing.loads(self.val)
		return self.result



	def file_processor(self, file, filename, folder):
		import time
		import os
		from django.conf import settings
		from django.core.files.storage import FileSystemStorage

		self.file     = file
		self.filename = filename
		self.random   = str(int(round(time.time() * 1000)))
		self.ext      = os.path.splitext(self.file.name)[1]
		self.folder   = os.path.join(settings.MEDIA_ROOT, folder)

		if self.file != None or self.file != '':
			if self.ext.lower() in ['.jpg', '.jpeg', '.png', '.pdf', '.mp3', '.mp4']:

				self.fileName = self.filename + self.random + self.ext
				fs = FileSystemStorage(location=self.folder)

				if fs.exists(self.fileName):
					fs.delete(self.fileName)
				else:
					self.resultFile = fs.save(self.fileName, self.file)
					return self.fileName
		else:
			pass


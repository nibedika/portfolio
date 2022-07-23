# additional imports
from django.shortcuts import render
import qrcode
from io import BytesIO
from django.core.files import File
from django.core.files.storage import FileSystemStorage


class Qrcode_helper():
    """All View Prime import this class so that they got the 
    Model Helper class and Backend Apps's View will Use this 
    class attributes through Pirme """
    # pip install qrcode==5.1 (***REQUIRED***)

    def __init__(self, arg):
        #super('', self).__init__()
        self.arg = arg

    

    def qrcode_processor(self, filename, data, folder): 

        import os
        from django.conf import settings

        self.fileName = filename + '.png'
        self.folder   = os.path.join(settings.MEDIA_ROOT, folder)

        fs = FileSystemStorage(location=self.folder)
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=6,
            border=6,
        )
        qr.add_data(data)
        qr.make(fit=True)

        io  = BytesIO()
        img = qr.make_image().save(io)

        if fs.exists(self.fileName):
            fs.delete(self.fileName)
            self.resultFile = fs.save(self.fileName, io)
            return self.fileName
        else:
            self.resultFile = fs.save(self.fileName, io)
            return self.fileName

# additional imports
import barcode 
from barcode.writer import ImageWriter
from io import BytesIO
from io import StringIO
from django.core.files import File
from django.core.files.storage import FileSystemStorage


class Barcode_helper():
    """All View Prime import this class so that they got the 
    Model Helper class and Backend Apps's View will Use this 
    class attributes through Pirme """
    # pip install python-barcode (***REQUIRED***)

    def __init__(self, arg):
        #super('', self).__init__()
        self.arg = arg

    

    def barcode_processor(self, filename, folder): 

        import os
        from django.conf import settings

        self.fileName = filename + '.png'
        self.folder   = os.path.join(settings.MEDIA_ROOT, folder)


        # overriding save() # code128
        COD128 = barcode.get_barcode_class('code128')
        io     = BytesIO()
        code   = COD128(f'{filename}', writer=ImageWriter()).write(io)
        fs     = FileSystemStorage(location=self.folder)

        if fs.exists(self.fileName):
            fs.delete(self.fileName)
            self.resultFile = fs.save(self.fileName, File(io))
            return self.fileName
        else:
            self.resultFile = fs.save(self.fileName, File(io))
            return self.fileName



        # overriding save() # code39
        # COD39   = barcode.get_barcode_class('code39')
        # io      = BytesIO()
        # options = {'text_distance': 2}
        # code    = COD39(str(filename), writer=ImageWriter(), add_checksum=False).write(io, options)
        # fs      = FileSystemStorage(location=self.folder)

        # if fs.exists(self.fileName):
        #     fs.delete(self.fileName)
        # else:
        #     self.resultFile = fs.save(self.fileName, File(io))
        #     return self.fileName
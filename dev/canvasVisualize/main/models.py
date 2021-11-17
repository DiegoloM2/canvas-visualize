from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe

from urllib.request import urlopen

from .upload import upload, open




media_url = "https://cvisualize-code.s3.eu-west-2.amazonaws.com/media"
bucket_name = "cvisualize-code"


class Visualization(models.Model):
    title = models.CharField(max_length = 100, unique = True, blank = False)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete =models.CASCADE)
    codeLocation = models.CharField(max_length = 200)
    created = models.DateField(auto_now = True)
    
    def get(self):
        code = open(bucket_name, f"code/{self.codeLocation}")
        return {
            "id":self.id,
            "title":self.title,
            "creator":self.creator, 
            "code":mark_safe(code),
            "created": self.created, 
            "codeLocation":self.codeLocation
        }
    
    def upload(self, code, imgPreview):
        self.codeLocation = f"visualization_{self.id}.js"
        upload(code, bucket_name, f"code/{self.codeLocation}")
        upload(imgPreview, bucket_name, f"images/visualizationPreviews/{self.title}.txt")
        self.save()


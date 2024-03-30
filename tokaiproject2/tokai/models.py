from django.db import models
# from django.contrib.auth.models import User

# class Tokai(models.Model):
#     title = models.CharField(max_length=100)
#     text = models.TextField(default='default_text_value') 
#     thumbnail = models.ImageField(default='default_thumbnail.jpg')

class FileUpload(models.Model):
    files = models.FileField(upload_to='videos/')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.files)

    class Meta:
        db_table = 'tokai_fileupload'



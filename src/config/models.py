from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class  Links(models.Model):
    STATUS_CHOICES = (
        ('Publish', 'انتشار'),
        ('Draft', 'پیش نویس')
    )
    LinkName = models.CharField(null=True, max_length=100, verbose_name='نام لینک')
    LinkAddress = models.CharField(null=True, max_length=1000, verbose_name='آدرس لینک')
    LinkStatus = models.CharField(null=True, max_length=10, choices=STATUS_CHOICES, verbose_name='وضعیت')
    
    def __str__(self):
        return self.LinkName
    
class  Header(models.Model):
    STATUS_CHOICES = (
        ('Publish', 'انتشار'),
        ('Draft', 'پیش نویس')
    )
    HeaderDescription = RichTextField(null=True, verbose_name='توضیحات بالای سایت')
    HeaderStatus = models.CharField(null=True, max_length=10, choices=STATUS_CHOICES, verbose_name='وضعیت')
    
    def __str__(self):
        return "توضیحات بالای صفحه"
    
class  Sub(models.Model):
    STATUS_CHOICES = (
    ('Publish', 'انتشار'),
    ('Draft', 'پیش نویس')
    )
    SubDescription = RichTextField(null=True, verbose_name='توضیحات متن سایت')
    SubStatus = models.CharField(null=True, max_length=10, choices=STATUS_CHOICES, verbose_name='وضعیت')
    def __str__(self):
        return "توضیحات"
    
class Media(models.Model):
    STATUS_CHOICES = (
        ('Publish', 'انتشار'),
        ('Draft', 'پیش نویس')
    )
    MediaTitle = models.CharField(max_length=100, verbose_name="تیتر ویدئو")
    MediaAddress = models.CharField(null=True, max_length=100, verbose_name="لینک ویدئو")
    MediaPage = models.CharField(null=True, max_length=100, verbose_name="لینک صفحه")
    MediaBody = RichTextUploadingField(null=True, default='Body', verbose_name="متن")
    MediaStatus = models.CharField(null=True, max_length=10, choices=STATUS_CHOICES, verbose_name='وضعیت')
    #User
    
    def __str__(self):
        return self.MediaTitle
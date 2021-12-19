from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    STATUS_CHOICES = (
        ('Publish', 'انتشار'),
        ('Draft', 'پیش نویس')
    )
    ArticleTitle = models.CharField(max_length=100, verbose_name="تیتر مقاله")
    ArticleSlug = models.SlugField(null=True, verbose_name="آدرس کوتاه")
    ArtileThumbnail = models.ImageField(null=True, verbose_name="تصویر مقاله")
    ArticleDiscription = models.TextField(null=True, verbose_name='توضیح کوتاه')
    ArticleBody = RichTextUploadingField(null=True, default='Body', verbose_name="متن مقاله")
    ArticleDate = models.DateTimeField(default=timezone.now, verbose_name="تاریخ")
    ArticleStatus = models.CharField(null=True, max_length=10, choices=STATUS_CHOICES, verbose_name='وضعیت')
    #User
    
    def __str__(self):
        return self.ArticleTitle

class Aboutme(models.Model):
    AboutmeImage = models.ImageField(null=True, verbose_name='تصویر')
    AboutmeBody = RichTextUploadingField(null=True, verbose_name='توضیحات')
    
    def __str__(self):
        return 'درباره من'

class Projects(models.Model):
    STATUS_CHOICES = (
        ('Publish', 'انتشار'),
        ('Draft', 'پیش نویس')
    )
    ProjectName = models.CharField(null=True, max_length=100, verbose_name='نام پروژه')
    ProjectImage = models.ImageField(null=True, verbose_name='تصویر پروژه')
    ProjectDescription = RichTextUploadingField(null=True, verbose_name='توضیحات پروژه')
    ProjectDate = models.DateTimeField(default=timezone.now, verbose_name="تاریخ")
    ProjectStatus = models.CharField(null=True, max_length=10, choices=STATUS_CHOICES, verbose_name='وضعیت')
    
    def __str__(self):
        return self.ProjectName

class Contact(models.Model):
    ContactDescription = RichTextField(null=True, verbose_name='تویحات')
    
    def __str__(self):
        return "ارتباط با من"

class Support(models.Model):
    STATUS_CHOICES = (
        ('Publish', 'انتشار'),
        ('Draft', 'پیش نویس')
    )
    SupportImage = models.ImageField(null=True, verbose_name='تصویر')
    SupportDescription = RichTextUploadingField(null=True, verbose_name='توضیحات ')
    ArticleStatus = models.CharField(null=True, max_length=10, choices=STATUS_CHOICES, verbose_name='وضعیت')
    
    def __str__(self):
        return "حمایت مالی"
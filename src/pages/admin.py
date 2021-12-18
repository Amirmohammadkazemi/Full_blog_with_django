from django.contrib import admin
from . import models
from .models import Article, Aboutme, Projects, Contact, Support
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('ArticleTitle', 'ArticleDate', 'ArticleStatus')
    list_filter = ('ArticleTitle', 'ArticleDate', 'ArticleStatus')
    search_fields = ('ArticleTitle', 'ArticleDate', 'ArticleStatus')
    ordering = ('-ArticleDate', '-ArticleStatus', 'ArticleTitle')
    
    
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('ProjectName', 'ProjectStatus')
    list_filter = ('ProjectName', 'ProjectStatus')


admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Aboutme)
admin.site.register(models.Projects, ProjectAdmin)
admin.site.register(models.Contact)
admin.site.register(models.Support)
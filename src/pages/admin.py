from django.contrib import admin
from . import models
from .models import Article, Aboutme, Projects, Contact, Support, Category

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('ArticleTitle', 'ArticleDate', 'ArticleStatus', 'category_name')
    list_filter = ('ArticleTitle', 'ArticleDate', 'ArticleStatus')
    search_fields = ('ArticleTitle', 'ArticleDate', 'ArticleStatus')
    ordering = ('-ArticleDate', '-ArticleStatus', 'ArticleTitle')

    def category_name(self, obj):
        return [category for category in obj.ArticleCategory.all()]
    category_name.short_description='دسته بندی'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('CategoryTitle', 'ParentCategory')
    search_fields = ('CategoryTitle', 'ParentCategory')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('ProjectName', 'ProjectStatus')
    list_filter = ('ProjectName', 'ProjectStatus')

admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Aboutme)
admin.site.register(models.Projects, ProjectAdmin)
admin.site.register(models.Contact)
admin.site.register(models.Support)
admin.site.register(models.Category, CategoryAdmin)

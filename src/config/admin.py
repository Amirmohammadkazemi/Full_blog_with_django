from django.contrib import admin
from. import models
from .models import Links, Media

# Register your models here.
class LinksAdmin(admin.ModelAdmin):
    list_display = ('LinkName', 'LinkAddress', 'LinkStatus')

class MediaAdmin(admin.ModelAdmin):
    list_display = ('MediaTitle', 'MediaStatus')

admin.site.register(models.Links, LinksAdmin)
admin.site.register(models.Header)
admin.site.register(models.Sub)
admin.site.register(models.Media, MediaAdmin)
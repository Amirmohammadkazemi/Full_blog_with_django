from django.contrib import admin
from. import models
from .models import Links, Header, Sub

# Register your models here.
class LinksAdmin(admin.ModelAdmin):
    list_display = ('LinkName', 'LinkAddress', 'LinkStatus')

admin.site.register(models.Links, LinksAdmin)
admin.site.register(models.Header)
admin.site.register(models.Sub)
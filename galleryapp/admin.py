from django.contrib import admin
from galleryapp.models import *

class ImageAdmin(admin.ModelAdmin):
    readonly_fields =('date_upload', 'date_update')

admin.site.register(Image, ImageAdmin)
admin.site.register(Notes)
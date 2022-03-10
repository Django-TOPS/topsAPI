from django.contrib import admin
from .models import studInfo

class studinfoAdmin(admin.ModelAdmin):
    list_display=['firstname','lastname','email','mobile']

admin.site.register(studInfo,studinfoAdmin)


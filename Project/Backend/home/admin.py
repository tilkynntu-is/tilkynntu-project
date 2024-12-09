from django.contrib import admin
from .models import *

class ReportAdmin(admin.ModelAdmin):
    list_display = ['title']
    filter_horizontal = ['tags']

# Register your models here.
admin.site.register(Report, ReportAdmin)
admin.site.register(Image)
admin.site.register(Tag)
admin.site.register(Rating)
admin.site.register(Comment)

from django.contrib import admin
from Binfo.models import Blood
# Register your models here.
class BloodAdmin(admin.ModelAdmin):
    list_display=['First_Name','BloodGroup']
admin.site.register(Blood,BloodAdmin)

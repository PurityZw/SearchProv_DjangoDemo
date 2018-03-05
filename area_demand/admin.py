from django.contrib import admin
from area_demand.models import AreaInfo

# Register your models here.
class AreaInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'atitle']


admin.site.register(AreaInfo, AreaInfoAdmin)

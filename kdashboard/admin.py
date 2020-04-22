from django.contrib import admin
from .models import Dashboards#, AccessToDashboard


# Register your models here.
@admin.register(Dashboards)
class dashboards_admin(admin.ModelAdmin):
    #list_display = ('id', 'dashboard_name')

    #fields = ('user','dashboard_name')
    fields = ('dashboard_name',)




     #list_display = ('user_id', 'dashboard_id')

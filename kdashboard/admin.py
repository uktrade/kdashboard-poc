from django.contrib import admin
from .models import Dashboards#, AccessToDashboard


# Register your models here.
@admin.register(Dashboards)
class dashboards_admin(admin.ModelAdmin):
    #list_display = ('id', 'dashboard_name')
    ###inlines = [dashboards_inline,]
    fields = ('user','dashboard_name')


# @admin.register(AccessToDashboard)
# class dashboards_admin(admin.ModelAdmin):
#     list_display = ('dashboard_user', 'dashboard_name')
#
#     def dashboard_name(self, obj):
#         return (obj.dashboard_item.dashboard_name)

# @admin.register(Dashboards_Inline)
# class dashboards_inline(admin.TublarInline):
#     model = Dashboards.user.through

     #list_display = ('user_id', 'dashboard_id')

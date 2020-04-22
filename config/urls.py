from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from core.admin_views import admin_login_view
from core.views import login_redirect_view

from kdashboard.views import staff_lookup, dashboards, home_page

urlpatterns = [
    path('auth/', include('authbroker_client.urls', namespace='authbroker')),
    path('admin/login/', admin_login_view, name='admin-login-view'),
    #url(r'^$', RedirectView.as_view(pattern_name='staff_lookup')),
    path('admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(pattern_name='home_page')),
    path('home/', home_page.as_view(), name='home_page'),
    path('search/', staff_lookup.as_view(), name='staff_lookup'),
    path('dashboards/', dashboards.as_view(), name='dashboards'),
    path('login/redirect/', login_redirect_view, name='login-redirect'),
]

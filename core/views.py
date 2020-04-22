from django.shortcuts import reverse, redirect
from django.utils.http import is_safe_url
from django.conf import settings

from .middleware import SESSION_LOGIN_REDIRECT_KEY


def login_redirect_view(request):
    """Figure out where to redirect the user after logging in"""
    #breakpoint()
    url = request.session.get(SESSION_LOGIN_REDIRECT_KEY)

    if url and is_safe_url(url, settings.ALLOWED_HOSTS, request.is_secure()):
        next_url = url
    else:
        next_url = reverse('dashboards')

    return redirect(next_url)

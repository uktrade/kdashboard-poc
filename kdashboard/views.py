from django.shortcuts import render
import requests

from .forms import (
    StaffLookupForm, DashboardsForm)

from django.views.generic.edit import FormView
from django.template.loader import render_to_string
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from core.helpers import get_dashboards, check_user_exists


class home_page(View):
    template_name = 'home-page.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class staff_lookup(FormView):
    template_name = 'staff-lookup.html'
    form_class = StaffLookupForm
    success_url = reverse_lazy('dashboards')

    def form_valid(self, form):
        user = form.cleaned_data['searchname']
        #breakpoint()
        #kibana_url = get_dashboards(user)


        return super().form_valid(form)
        #return redirect('/dashboards/?' + urlencode(context))


class dashboards(LoginRequiredMixin, FormView):
    template_name = 'dashboards.html'
    form_class = DashboardsForm
    login_url = '/auth/login/'
    #redirect_field_name = '/dashboards/'

    def get_form_kwargs(self, **kwargs):
        #breakpoint()
        kwargs = super(dashboards, self).get_form_kwargs(**kwargs)
        #kwargs['email'] = self.request.user.email
        kwargs['userid'] = self.request.user.user_id

        return kwargs


    def form_valid(self, form):
        dashboard_id = form.cleaned_data['dashboard']

        #breakpoint()
        kibana_url = get_dashboards(dashboard_id, self.request.user.email)

        user_exists = check_user_exists(self.request.user.email, self.request.user.user_id)
        if not user_exists:
            template = render_to_string("sorry-no-user.html")
            return HttpResponse(template)


        return redirect(kibana_url)

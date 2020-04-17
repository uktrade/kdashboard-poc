from django.shortcuts import render
import requests

from .forms import (
    StaffLookupForm, DashboardsForm)

from django.views.generic.edit import FormView
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import redirect

from core.helpers import get_dashboards


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

        #return redirect(kibana_url)
        #context = {'user': user}

        return super().form_valid(form)
        #return redirect('/dashboards/?' + urlencode(context))


class dashboards(FormView):
    template_name = 'dashboards.html'
    form_class = DashboardsForm

    def get_form_kwargs(self, **kwargs):
        #breakpoint()
        kwargs = super(dashboards, self).get_form_kwargs(**kwargs)
        kwargs['email'] = self.request.user.email
    
        return kwargs


    def form_valid(self, form):
        dashboard_id = form.cleaned_data['dashboard']

        #breakpoint()
        kibana_url = get_dashboards(dashboard_id, self.request.user.email)

        return redirect(kibana_url)

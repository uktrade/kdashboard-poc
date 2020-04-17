from django import forms

from .models import Dashboards#, AccessToDashboard
from user.models import User

from govuk_forms.forms import GOVUKForm
from govuk_forms import widgets


class StaffLookupForm(GOVUKForm):
    searchname = forms.CharField(
        label='Name:',
        max_length=60,
        widget=widgets.TextInput())


def get_dashboard_list(email):
    #breakpoint()

    #return Dashboards.objects.filter(user__id=1).values_list('id', 'dashboard_name')
    return Dashboards.objects.filter(user__email=email).values_list('id', 'dashboard_name')
    #return AccessToDashboard.objects.filter(dashboard_user_id=2).values_list('dashboard_item__id', 'dashboard_item__dashboard_name')


class DashboardsForm(GOVUKForm):
    def __init__(self, *args, **kwargs):
        email = kwargs.pop('email')
        super().__init__(*args, **kwargs)
        #breakpoint()
        self.fields['dashboard'].choices = get_dashboard_list(email)

    dashboard = forms.ChoiceField(
        label='Which dashboard:',
        choices=[],
        widget=widgets.Select())

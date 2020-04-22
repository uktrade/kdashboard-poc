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


def get_dashboard_list(userid):
    #breakpoint()

    return Dashboards.objects.filter(user__user_id=userid).values_list('id', 'dashboard_name')



class DashboardsForm(GOVUKForm):
    def __init__(self, *args, **kwargs):
        #email = kwargs.pop('email')
        userid = kwargs.pop('userid')
        super().__init__(*args, **kwargs)
        #breakpoint()
        self.fields['dashboard'].choices = get_dashboard_list(userid)

    dashboard = forms.ChoiceField(
        label='Which dashboard:',
        choices=[],
        widget=widgets.Select())

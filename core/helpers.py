import requests

from django.conf import settings

from kdashboard.models import Dashboards
from user.models import User


def transform_email(email):

    #breakpoint()
    url_remail = email.replace('.','-').replace('@','-')


    return url_remail


def get_dashboards(dashboard_id, email):
    #breakpoint()
    route_url = settings.KIBANA_URL
    params = (('dashboard', settings.MASTER_DASHBOARD_TOKEN),)

    #breakpoint()

    dashboard_name = Dashboards.objects.get(id=dashboard_id).dashboard_name



    # breakpoint()
    url_email = transform_email(email)

    #kibana_url = settings.KIBANA_DOMAIN + '/s/' + url_email + '/app/kibana#/dashboards?title='+ dashboard_name#'[Logs]%20Web%20Traffic'
    kibana_url = settings.KIBANA_DOMAIN + '/s/' + 'user-a-space' + '/app/kibana#/dashboards?title='+ dashboard_name#'[Logs]%20Web%20Traffic'


    return kibana_url


def create_kibana_user(email, userid):
    #breakpoint()
    headers = {
        'Content-Type': 'application/json',
        }
    data = {
        "password" : str(userid),
        "roles" : [ "monitor_default" ],
        "email" : email}
    response = requests.post(
        settings.ELASTIC_DOMAIN + '/_security/user/' + email,
        headers=headers,
        json=data,
        auth=(settings.ELASTIC_USER, settings.ELASTIC_PASSWORD))

    print (response)

def check_user_exists(email, userid):
    #breakpoint()
    #email = "testuser2@mail.com"
    user_exists = False
    response = requests.get(
         settings.ELASTIC_DOMAIN + '/_security/user',
         #params=params,
         auth=(settings.ELASTIC_USER, settings.ELASTIC_PASSWORD))

    elastic_users = response.json()

    for kibana_user in elastic_users:
        #if kibana_user in User.objects.values_list('email', flat=True):
        if kibana_user == email:
            print('User exists')
            user_exists = True

    if user_exists is False:
            create_kibana_user(email, userid)

    return user_exists

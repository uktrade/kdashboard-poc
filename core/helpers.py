import requests

from django.conf import settings

from kdashboard.models import Dashboards


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

    # response = requests.get(
    #     route_url + '/dashboards/export',
    #     params=params,
    #     auth=(settings.KIBANA_ADMIN_USER, settings.KIBANA_ADMIN_PASSWORD))
    #
    # dashboard_titles = response.json()

    # for object in dashboard_titles['objects']:
    #     print(object['attributes']['title'])

    # breakpoint()
    url_email = transform_email(email)

    kibana_url = settings.KIBANA_DOMAIN + '/s/' + url_email + '/app/kibana#/dashboards?title='+ dashboard_name#'[Logs]%20Web%20Traffic'
    kibana_url = settings.KIBANA_DOMAIN + '/s/' + 'user-a-space' + '/app/kibana#/dashboards?title='+ dashboard_name#'[Logs]%20Web%20Traffic'


    return kibana_url


import sys
import time
import requests
from bs4 import BeautifulSoup


def sleep_until_ready(host):
    """ Waits until the host is up."""
    now = time.time()
    while True:
        try:
            requests.get(host + 'available_languages')
            return
        except Exception:
            time.sleep(1)
            sys.stdout.write('\rWaiting for {} seconds to boot up'.format(int(time.time() - now)))
            sys.stdout.flush()


def check_configuration(host, dashboard_enabled):
    """ Verifies that the dashboard is correctly enabled/disabled """
    r = requests.get(host + 'dashboard/login')
    if dashboard_enabled:
        return r.status_code == 200
    else:
        return r.status_code == 404


def monitor_all_endpoints(host):
    """ Enables the monitoring of all endpoints."""
    url_login = host + 'dashboard/login'
    url_rules = host + 'dashboard/rules'

    # Login to the dashboard
    client = requests.session()
    html = client.get(url_login)
    parsed_html = BeautifulSoup(html.text, "html.parser")
    token = parsed_html.body.find(id='csrf_token')['value']
    login_data = dict(csrf_token=token, name='admin', password='admin', submit='Login')
    client.post(url_login, data=login_data, headers=dict(Referer=url_login))

    # Turn on monitoring for all rules
    html = client.get(url_rules)
    parsed_html = BeautifulSoup(html.text, "html.parser")
    token = parsed_html.body.find(id='csrf_token')['value']
    rules_data = {'csrf_token': token}
    for endpoint in parsed_html.findAll('table')[0].findAll('tr')[1:]:
        rules_data[endpoint.find('label')['for']] = 'on'

    client.post(url_rules, data=rules_data, headers=dict(Referer=url_rules))


def measure_execution_time(host, page, n, method='get', data=None):
    """ Call a certain page n times and returns the execution time (in ms) """
    result = []
    for i in range(n):
        try:
            r = requests.Request(method, host + page, data=data).prepare()
            s = requests.Session()
            now = time.time()
            s.send(r)
            duration = (time.time() - now) * 1000
            result.append(duration)
        except Exception as e:
            print('Exception for page {}: {}'.format(page, e))
    print('Measuring page "{}": {} ms'.format(page, sum(result)/len(result)))
    return result


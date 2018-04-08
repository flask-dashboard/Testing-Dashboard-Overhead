
import sys
import time
import requests
from bs4 import BeautifulSoup
from .util import save_result


def sleep_until_ready(hosts):
    """ Waits until all the hosts are up."""
    now = time.time()
    for host in hosts:
        host_up = False
        while not host_up:
            try:
                requests.get(host + 'available_languages')
                host_up = True
            except Exception:
                time.sleep(1)
                sys.stdout.write('\rWaiting for {} seconds to boot all hosts up'.format(int(time.time() - now)))
                sys.stdout.flush()
    print('')


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


def measure_time(index, builders, page, args=None):
    result = [str(index)]
    page2 = page
    if args:
        page2 = page + args
    for builder in builders:
        try:
            r = requests.Request('get', builder._host + page2).prepare()
            s = requests.Session()
            now = time.time()
            response = s.send(r)
            duration = (time.time() - now) * 1000
            result.append(str(duration))
            if response.status_code != 200:
                print(response.text)
        except Exception as e:
            print('Exception for page {}: {}'.format(page, e))
            raise
    return ','.join(result)


def test_endpoint(builders, page, n=500, args=None):
    title = ['id']
    for builder in builders:
        title.append(builder._name)
    result = [','.join(title)]

    for i in range(10):  # init endpoint by calling it 10 times
        measure_time(i, builders, page, args)

    for i in range(n):
        sys.stdout.write('\r{}/{}: {}'.format(i+1, n, page))
        sys.stdout.flush()
        result.append(measure_time(i, builders, page, args))
    print('')

    save_result(result, page)

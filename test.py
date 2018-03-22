"""
Run this script for making a number of requests to the webservice
"""

import sys
import requests
import time
from util import parse_args, save_result
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


def monitor_all_endpoints(host):
    """ Enables the monitoring of all endpoints."""
    url_login = host + 'dashboard/login'
    url_rules = host + 'dashboard/rules'

    client = requests.session()
    html = client.get(url_login)

    parsed_html = BeautifulSoup(html.text, "html.parser")
    token = parsed_html.body.find(id='csrf_token')['value']
    login_data = dict(csrf_token=token, name='admin', password='admin', submit='Login')

    client.post(url_login, data=login_data, headers=dict(Referer=url_login))
    html = client.get(url_rules)

    parsed_html = BeautifulSoup(html.text, "html.parser")
    token = parsed_html.body.find(id='csrf_token')['value']
    rules_data = {'csrf_token':token, 'checkbox-api.available_languages':'on'}

    r = client.post(url_rules, json=rules_data, headers=dict(Referer=url_rules))
    print(r.text[:5000])
    print(r.status_code)


def measure_execution_time(host, page, n=100):
    """ Call a certain page n times and returns the execution time (in ms) """
    data = []
    for _ in range(n):
        now = time.time()
        try:
            urllib2.urlopen(host + page, timeout=1)
        except Exception:
            print('Can\'t open url {}{}'.format(host, page) )
        data.append((time.time() - now) * 1000)
    return data

if __name__ == '__main__':
    host, name = parse_args()
    sleep_until_ready(host)
    print('\nHost is up.')
    if name == 'with_dashboard':
        print('Enabling monitoring of all endpoints...')
        monitor_all_endpoints(host)
        print('All endpoints are now monitored.')
    print('Testing the overhead now...')
    data = measure_execution_time(host, page='available_languages')
    save_result(data, name + '.txt')
    print('Results saved.')

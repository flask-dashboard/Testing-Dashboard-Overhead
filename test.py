"""
Run this script for making a number of requests to the webservice
"""

import sys
import requests
import time
import sqlite3
import urllib2
from util import parse_args, save_result


def sleep_until_ready(host):
    """ Waits until the host is up."""
    now = time.time()
    while True:
        try:
            urllib2.urlopen(host + 'available_languages', timeout=1)
            return
        except Exception:
            time.sleep(1)
            sys.stdout.write('\rWaiting for {} seconds to boot up'.format(time.time() - now))
            sys.stdout.flush()


def monitor_all_endpoints(db):
    """ Enables the monitoring of all endpoints."""
    try:
        conn = sqlite3.connect(db)
        c = conn.cursor()
        c.execute("UPDATE rules SET monitor = 1")
        conn.commit()
        conn.close()
    except Exception as e:
        print('Could not enable the monitoring of all endpoints.')
        print(e)


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
    print('Host is up.\nEnabling monitoring of all endpoints...')
    monitor_all_endpoints('/Zeeguu-API/flask_monitoringdashboard.db')
    print('All endpoints are now monitored.\nTesting the overhead now...')
    data = measure_execution_time(host, page='available_languages')
    save_result(data, name + '.txt')
    print('Results saved.')

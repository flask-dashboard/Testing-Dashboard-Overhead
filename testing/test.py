
import sys
import time
import urllib2


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


def measure_execution_time(host, page, n=100):
    """ Call a certain page n times and returns the execution time (in ms) """
    data = []
    for _ in range(n):
        now = time.time()
        try:
            urllib2.urlopen(host + page, timeout=1)
        except Exception:
            print('Can\'t open url {}{}'.format(host, page))
        data.append((time.time() - now) * 1000)
    return data


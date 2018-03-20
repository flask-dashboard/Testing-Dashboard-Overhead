"""
Run this script for making a number of requests to the webservice
"""

import sys
import requests
import time
import urllib2


def parse_host():
    """ Returns the host (as a string) from the script argument. """
    try:
        return sys.argv[1]
    except Exception as e:
        print('Got exception: {}'.format(e))
        print('Usage: {} {{Host}}'.format(sys.argv[0]))
        print('Given: {} {}'.format(sys.argv[0], sys.argv[1]))
        sys.exit(1)


def sleep_until_ready(host):
    """ Waits until the host is up."""
    now = time.time()
    while True:
        try:
            urllib2.urlopen(host + 'available_languages', timeout=1)
            return
        except Exception:
            time.sleep(1)
            print('Waiting for {} seconds to boot up'.format(time.time() - now))


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
    host = parse_host()
    sleep_until_ready(host)
    print('Ready for the real testing')

    page = 'available_languages'
    data = measure_execution_time(host, page)
    print(data)

    with open('{}.txt'.format(host), 'w') as file:
        for line in data:
            file.write(line + '\n')
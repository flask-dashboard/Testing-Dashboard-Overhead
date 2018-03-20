"""
Run this script for making a number of requests to the webservice
"""

import sys
import os
import requests
import time
import urllib2


def parse_args():
    """ Returns the host (as a string) and the name from the script arguments. """
    try:
        return sys.argv[1], sys.argv[2]
    except Exception as e:
        print('Got exception: {}'.format(e))
        print('Usage: {} {{Host}} {{Name}}'.format(sys.argv[0]))
        print('Given: {} {} {}'.format(sys.argv[0], sys.argv[1], sys.argv[2]))
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
            print('Can\'t open url {}{}'.format(host, page) )
        data.append((time.time() - now) * 1000)
    return data

if __name__ == '__main__':
    host, name = parse_args()
    sleep_until_ready(host)
    print('Ready for the real testing')

    page = 'available_languages'
    data = measure_execution_time(host, page)

    try:
        os.makedirs('output')
    except Exception as e:
        print(e)

    with open('output/{}.txt'.format(name), 'w') as file:
        for line in data:
            file.write(str(line) + '\n')
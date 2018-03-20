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
    while True:
        try:
            urllib2.urlopen(host + 'available_languages', timeout=1)
            return
        except Exception:
            time.sleep(1)
            print('Waiting until host is up')


if __name__ == '__main__':
    host = parse_host()
    sleep_until_ready(host)
    print('Ready for the real testing')
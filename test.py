"""
Run this script for making a number of requests to the webservice
"""

import sys
import requests
import time


if __name__ == '__main__':
    try:
        num_requests = int(sys.argv[1])
    except Exception as e:
        print('Got exception: {}'.format(e))
        print('Usage: {} {{NUM_REQUESTS}}'.format(sys.argv[0]))
        print('Given: {} {}'.format(sys.argv[0], sys.argv[1]))
        sys.exit(1)

    for i in range(num_requests):
        start = time.time()
        r = requests.get(url='http://localhost:5000/')
        print('{}/{} status-code: {} time: {}'.format(i, num_requests, r.status_code, time.time() - start))

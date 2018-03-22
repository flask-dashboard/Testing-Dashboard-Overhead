"""
Run this script for making a number of requests to the webservice
"""

from .util import parse_args, save_result
from .test import sleep_until_ready, measure_execution_time

if __name__ == '__main__':
    host, name = parse_args()
    sleep_until_ready(host)
    print('Ready for testing the webservice')

    data = measure_execution_time(host, page='available_languages')
    save_result(data, name + '.txt')

"""
Run this script for making a number of requests to the webservice
"""

from .util import parse_args
from .test import sleep_until_ready, check_configuration, monitor_all_endpoints
from .test_procedure import test_procedure


if __name__ == '__main__':
    host, name = parse_args()
    sleep_until_ready(host)

    dashboard_enabled = name != "without_dashboard"
    if not check_configuration(host, dashboard_enabled):
        raise Exception('Incorrectly configured {}'.format(name))

    if dashboard_enabled:
        monitor_all_endpoints(host)

    print('Ready for testing the webservice')
    test_procedure(host=host, name=name)
    print('Done with testing webservice: {}'.format(name))

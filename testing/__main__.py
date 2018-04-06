"""
Run this script for making a number of requests to the webservice
"""

from .util import parse_args
from .test import sleep_until_ready, check_configuration, monitor_all_endpoints
from .test_procedure import test_procedure


if __name__ == '__main__':
    hosts, names = parse_args()
    sleep_until_ready(hosts)

    # Verify that the dashboard is correctly enabled/disabled
    for i in range(len(hosts)):
        dashboard_enabled = names[i] != "without_dashboard"
        if not check_configuration(hosts[i], dashboard_enabled):
            raise Exception('Incorrectly configured {}'.format(names[i]))

        if dashboard_enabled:
            monitor_all_endpoints(hosts[i])

    print('Ready for testing the webservice')
    test_procedure(hosts=hosts, names=names)

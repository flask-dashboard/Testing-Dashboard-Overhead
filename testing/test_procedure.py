"""
This file determines which endpoints (and how often) are tested
"""

from .test import test_endpoint
from .init_session import init_sessions


class Builder(object):
    """ Easier usage of the test_and_save function """

    def __init__(self, host, name):
        self._host = host
        self._name = name


def test_procedure(hosts, names):
    """ The actual test procedure """

    builders = [Builder(hosts[i], names[i]) for i in range(len(hosts))]

    test_endpoint(builders, 'available_languages')
    test_endpoint(builders, 'available_native_languages')
    test_endpoint(builders, 'ping')
    init_sessions(names)
    test_endpoint(builders, 'user_articles', args='/recommended?session=12345')
    test_endpoint(builders, 'recommended_feeds', args='/4?session=12345')
    test_endpoint(builders, 'user_article', args='?session=12345&url=http%3A%2F%2Fwww.nu.nl')
    test_endpoint(builders, 'create_default_exercises', args='?session=12345')

"""
This file determines which endpoints (and how often) are tested
"""

from .util import save_result
from .test import measure_execution_time
from .init_session import init_session


def test_and_save(host, name, page, n=100, args=None):
    """ Shorthand for testing and storing the result"""
    page2 = page
    if args:
        page2 = page2 + args
    data = measure_execution_time(host=host, page=page2, n=n)
    save_result(data, name=name, page=page)


def test_procedure(host, name):
    """ The actual test procedure """

    test_and_save(host, name, 'available_languages')
    test_and_save(host, name, 'available_native_languages')
    test_and_save(host, name, 'ping')
    init_session(name)
    test_and_save(host, name, 'user_articles', args='/recommended?session=12345')
    test_and_save(host, name, 'user_article', args='?session=12345&url=http%3A%2F%2Fwww.nu.nl')

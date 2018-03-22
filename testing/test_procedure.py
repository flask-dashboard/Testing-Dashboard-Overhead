"""
This file determines which endpoints (and how often) are tested
"""

from .util import save_result
from .test import measure_execution_time


def test_and_save(host, name, page, n=100):
    """ Shorthand for testing and storing the result"""
    data = measure_execution_time(host=host, page=page, n=n)
    save_result(data, name=name + '.txt', page=page)


def test_procedure(host, name):
    """ The actual test procedure """

    test_and_save(host, name, 'available_languages')

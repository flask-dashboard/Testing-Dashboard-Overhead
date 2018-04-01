"""
This file determines which endpoints (and how often) are tested
"""

from .util import save_result
from .test import measure_execution_time
from .init_session import init_session


class Builder(object):
    """ Easier usage of the test_and_save function """

    def __init__(self, host, name):
        self._host = host
        self._name = name

    def test_and_save(self, page, n=100, args=None, method='get', data=None):
        """ Shorthand for testing and storing the result"""
        page2 = page
        if args:
            page2 = page2 + args
        result = measure_execution_time(host=self._host, page=page2, n=n, method=method, data=data)
        save_result(result, name=self._name, page=page)


def test_procedure(host, name):
    """ The actual test procedure """

    build = Builder(host, name)

    build.test_and_save('available_languages', n=1
                        )
    # build.test_and_save('available_native_languages')
    # build.test_and_save('ping')
    init_session(name)
    # build.test_and_save('user_articles', args='/recommended?session=12345')
    # build.test_and_save('user_article', args='?session=12345&url=http%3A%2F%2Fwww.nu.nl')
    data = {
        'context': 'The sentence in which a certain word occurs.',
        'url': 'articleURL=1234',
        'word': 'sentence',
        'title': 'title of the article'
    }
    build.test_and_save('get_possible_translations', args='/en/nl?session=12345', method='post', n=1, data=data)

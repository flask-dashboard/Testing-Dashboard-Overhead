"""
This file contains a number of helper functions
"""

import os
import sys


def parse_args():
    """ Returns the host (as a string) and the name from the script arguments. """
    try:
        return [sys.argv[1], sys.argv[3], sys.argv[5]], \
               [sys.argv[2], sys.argv[4], sys.argv[6]]
    except Exception as e:
        print('Got exception: {}'.format(e))
        print('Usage: {} {{Host-1}} {{Container-name-1}} {{Host-2}} {{Container-name-2}} {{Host-3}} '
              '{{Container-name-3}}'.format(sys.argv[0]))
        print('Given: {} {} {} {} {} {}'.format(sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4],
                                                sys.argv[5], sys.argv[6]))
        sys.exit(1)


def make_directory(name):
    """ Creates a directory if it doesn't exists """
    try:
        os.makedirs(name)
    except Exception:
        pass


def save_result(data, page):
    """ Saves the result in a file """
    make_directory('output')

    with open('output/{}.csv'.format(page), 'w') as file:
        for line in data:
            file.write(str(line) + '\n')

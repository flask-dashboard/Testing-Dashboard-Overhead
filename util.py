"""
This file contains a number of helper functions
"""

import sys
import os


def parse_args():
    """ Returns the host (as a string) and the name from the script arguments. """
    try:
        return sys.argv[1], sys.argv[2]
    except Exception as e:
        print('Got exception: {}'.format(e))
        print('Usage: {} {{Host}} {{Name}}'.format(sys.argv[0]))
        print('Given: {} {} {}'.format(sys.argv[0], sys.argv[1], sys.argv[2]))
        sys.exit(1)


def make_directory(name):
    """ Creates a directory if it doesn't exists """
    try:
        os.makedirs(name)
    except Exception as e:
        print(e)


def save_result(data, name):
    """ Saves the result in a file """
    make_directory('output')

    try:
        os.remove('output/{}'.format(name))
    except Exception as e:
        print(e)
        
    with open('output/{}'.format(name), 'w') as file:
        for line in data:
            file.write(str(line) + '\n')
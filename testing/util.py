"""
This file contains a number of helper functions
"""

import os
import sys


def parse_args():
    """ Returns the host (as a string) and the name from the script arguments. """
    if len(sys.argv) >= 3 and len(sys.argv) % 2 == 1:
        hosts = []
        names = []
        for i in range(1, len(sys.argv), 2):
            hosts.append(sys.argv[i])
            names.append(sys.argv[i+1])
        return hosts, names
    else:
        print('Usage: {} {{Host}} {{Container-name}} [more hosts and names]'.format(sys.argv[0]))
        sys.exit(1)


def make_directory(name):
    """ Creates a directory if it doesn't exists """
    try:
        os.makedirs(name)
    except Exception:
        pass
        # Don't print the exception, as it is due to a folder that already exists


def unique_filename(prefix='', postfix=''):
    """ Checks whether the filename: 'prefix + postfix' is available.
    If not, it adds a counter, such that the name is unique """
    index = 0
    while os.path.isfile(prefix + str(index) + postfix):
        index = index+1
    return prefix + str(index) + postfix


def save_result(data, page):
    """ Saves the result in a file """
    make_directory('output')

    filename = unique_filename('output/{}-'.format(page), '.csv')

    with open(filename, 'w') as file:
        for line in data:
            file.write(str(line) + '\n')

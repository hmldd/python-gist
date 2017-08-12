#!/usr/bin/env python
# coding:utf-8


import getopt
import sys


def main(argv):
    # Default params value
    start = 1
    number = 10

    # Get cli params
    try:
        opts, args = getopt.getopt(argv, "hs:n:", ["start=", "number="])
        for opt, arg in opts:
            if opt == '-h':
                print_help()
            elif opt in ("-s", "--start"):
                start = arg
            elif opt in ("-n", "--number"):
                number = arg
    except getopt.GetoptError:
        print_help(2)

    # Use params
    print('Start from: ' + str(start))
    print('Number is: ' + str(number))


def print_help(code=0):
    print('script.py -s <start:1> -n <number:10>')
    sys.exit(code)


if __name__ == '__main__':
    main(sys.argv[1:])
    sys.exit()

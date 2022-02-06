#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
"""
Author: Urska
Purpose: Say hello
"""

import argparse

def get_args():
    """Get the command-line arguments"""

    parser = argparse.ArgumentParser(description = 'Say hello')
    parser.add_argument('-n', '--name', metavar='name', default='World', help = 'Name to greet')
    return parser.parse_args()

def main():
    """Print greeting"""

    args = get_args()
    print('Hello, ' + args.name + '!')

if __name__ == '__main__':
    main()

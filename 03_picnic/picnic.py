#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
"""
Author : Urska <Urska@localhost>
Date   : 2022-03-03
Purpose: Shopping list for a picnic
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='food',
                        help='Food for picnic',
                        nargs='+')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Print shopping list"""

    args = get_args()
    food_list = args.str

    template = 'You are bringing {}.'
    length = len(food_list)

    if args.sorted:
        food_list.sort()

    food = ''
    if length == 1:
        food = food_list[0]
    elif length == 2:
        food = ' and '.join(food_list)
    else:
        food_list[-1] =  'and ' + food_list[-1]
        food = ', '.join(food_list)

    print(template.format(food))



# --------------------------------------------------
if __name__ == '__main__':
    main()

#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
"""
Crow's Nest
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Crow''s Nest -- choose the correct article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        help='A word')
    parser.add_argument('-s',
                        '--side',
                        help='Side of ship',
                        metavar='side',
                        type=str,
                        default='larboard')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Warn the Captain"""

    args = get_args()
    word = args.word
    side = args.side

    if not word.isalpha():
        print('Enter a valid word.')
        return

    article = 'an' if word[0].lower() in 'aeiou' else 'a'
    article = article.title() if word[0].isupper() else article


    print(f'Ahoy, Captain, {article} {word} off the {side} bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()

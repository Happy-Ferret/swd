# -*- coding: utf-8 -*-

import argparse


def calculate(first_word, second_word, text):
    # TODO: Implement
    return 0


def main():
    '''
    Main entry point for CLI part.
    Parses arguments and runs `calculate` against them.
    '''
    parser = argparse.ArgumentParser(
        description='''
            calculates shortest distance between two words in a piece of text.
        ''',
    )
    parser.add_argument(
        '-s', action='store_true', default=False,
        help='Third argument is string.',
    )
    parser.add_argument('first_word', help='First word.')
    parser.add_argument('second_word', help='Second word.')
    parser.add_argument(
        'text', nargs='+', help='Text piece as string or path to file.',
    )

    args = parser.parse_args()
    text = ''.join(args.text) if args.s else open(args.text[0])

    print(calculate(args.first_word, args.second_word, text))


if __name__ == '__main__':
    main()

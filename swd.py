# -*- coding: utf-8 -*-

import argparse
import io


class NoOccurenceException(Exception):
    '''One of the supplied words was not in the text.'''


def __read_words(f):
    '''
    Reads file(-like) object word by word, with buffer,
    but without reading the whole thing into memory at once.

    Also strips punctuation and any other non-alphanum chars
    on the way.

    Note: Wouldn't it be nice if different objects in the `io`
    module were composable? Unfortunately, no banana this time.
    '''
    word = ''
    while True:
        buf = f.read(10240)
        if not buf:
            if word:
                yield word
            return

        for pos, ch in enumerate(buf):
            if not ch.isalnum():
                if word:
                    yield word
                word = ''
                continue
            word += ch


def calculate(first_word, second_word, text):
    '''
    Calculates shortest words distance (i.e. number of words) between
    `first_word` and `second_word` in the given `text`.
    '''
    if isinstance(text, str):
        text = io.StringIO(text)

    i = None
    j = None
    distance = None
    for pos, word in enumerate(__read_words(text)):
        if word == first_word:
            i = pos
        if word == second_word:
            j = pos
        if i is not None and j is not None:
            d = abs(j - i)
            if distance is None or d < distance:
                distance = d

    if distance is None:
        raise NoOccurenceException()
    # Since first index actually points *at* the word,
    # not after it, subtract it here.
    return distance - 1


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
    text = ' '.join(args.text) if args.s else open(args.text[0])

    print(calculate(args.first_word, args.second_word, text))


if __name__ == '__main__':
    main()

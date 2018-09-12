# -*- coding: utf-8 -*-

import io

import pytest

import swd


@pytest.mark.parametrize('expected,first_word,second_word,text', [(
    2, 'motivation', 'development',
    (
        'We do value and reward motivation in our development team. '
        'Development is a key skill for a DevOp.',
    ),
), (
    4, 'first', 'second',
    'My first example for swd. With second sentence, to make sense.',
), (
    2, 'test', 'latter',
    'Having this test and that test, pick the latter one.',
), (
    3, 'Having', 'this',
    'Having many these, pick this this over that this.',
), (
    1, 'test', 'this',
    'Now, having wrong test and right test, take this, not this.',
), (
    2, 'sentence', 'punct',
    'This will test matching at the end of sentence. Ie. with punct.',
), (
    1, 'Perhaps', 'swap',
    'Can we swap args? Perhaps.',
)])
def test_calculate_str(expected, first_word, second_word, text):
    '''Checks that calculate provides correct answers.'''
    assert swd.calculate(first_word, second_word, text) == expected


def test_calculate_file():
    '''Checks that calculate works with text IO objects.'''
    assert swd.calculate('The', 'one', io.StringIO('The simple one')) == 1


@pytest.mark.parametrize('first_word,second_word', [
    ('first', 'second'),
    ('third', 'fourth'),
    ('fifth', 'NaN'),
])
def test_calculate_no_occurence(first_word, second_word):
    '''Checks that calculate throws on no occurences.'''
    with pytest.raises(swd.NoOccurenceException):
        swd.calculate(
            first_word, second_word, 'Sentence that is first and fourth only.'
        )

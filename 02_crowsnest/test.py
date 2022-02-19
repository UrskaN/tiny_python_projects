#!/usr/bin/env python3
"""tests for crowsnest.py"""

import os
from subprocess import getstatusoutput, getoutput

prg = './crowsnest.py'

consonant_words = [
    'brigantine', 'clipper', 'dreadnought', 'frigate', 'galleon', 'haddock',
    'junk', 'ketch', 'longboat', 'mullet', 'Narwhal', 'porpoise', 'quay',
    'regatta', 'submarine', 'tanker', 'vessel', 'whale', 'xebec', 'yatch',
    'zebrafish'
]
vowel_words = ['aviso', 'eel', 'iceberg', 'octopus', 'upbound']
sides = ['starboard', 'larboard', 'port']
junk_input = ['9879', '.?kjh', 'df56']

template = 'Ahoy, Captain, {} {} off the {} bow!'
default_side = 'larboard'

# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_consonant():
    """brigantine -> a brigantine"""

    for word in consonant_words:
        out = getoutput(f'{prg} {word.lower()}')
        assert out.strip() == template.format('a', word.lower(), default_side)


# --------------------------------------------------
def test_consonant_upper():
    """brigantine -> A Brigatine"""

    for word in consonant_words:
        out = getoutput(f'{prg} {word.title()}')
        assert out.strip() == template.format('A', word.title(), default_side)


# --------------------------------------------------
def test_vowel():
    """octopus -> an octopus"""

    for word in vowel_words:
        out = getoutput(f'{prg} {word.lower()}')
        assert out.strip() == template.format('an', word.lower(), default_side)


# --------------------------------------------------
def test_vowel_upper():
    """octopus -> an Octopus"""

    for word in vowel_words:
        out = getoutput(f'{prg} {word.title()}')
        assert out.strip() == template.format('An', word.title(), default_side)


# --------------------------------------------------
def test_side():
    """starboard"""
    word = 'narhwal'

    for side in sides:
        for option in ['-s', '--side']:
            rv, out = getstatusoutput(f'{prg} {word} {option} {side}')
            assert rv == 0
            assert out.strip() == template.format('a', word, side)


# --------------------------------------------------
def test_alphabetic():
    """284kl -> Enter a valid word"""

    for junk in junk_input:
        out = getoutput(f'{prg} {junk}')
        assert out.strip() == 'Enter a valid word.'


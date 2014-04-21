import os
import collections

import nose.tools as n
n.assert_dict_equal.__self__.maxDiff = None
import lxml.etree

import libsheetmusic.main as main

def test_cases():
    '''
    Function names are case insensitive.
    With this in mind, the functions dict
    should contain no duplicates.
    '''
    observed = dict(collections.Counter(k.upper() for k in main.functions().keys()))
    expected = {k.upper():1 for k in main.functions().keys()}
    n.assert_dict_equal(observed, expected)

def test_diatonic_scale():
    observed = main.functions()['diatonic_scale']('C4')
    expected = [['C4', 'D4', 'E4', 'F4', 'G4', 'A5', 'B5', ]]
    n.assert_list_equal(observed[0], expected[0])
    n.assert_list_equal(observed, expected)

def test_major_sixth_interval():
    observed = main.functions()['major_sixth_interval']('C2')
    expected = 'A3'
    n.assert_equal(observed, expected)

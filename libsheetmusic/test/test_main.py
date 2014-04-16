import os
import collections

import nose.tools as n
n.assert_dict_equal.__self__.maxDiff = None
import lxml.etree

import libsheetmusic.main as main

def test_functions():
    fn = os.path.join('spellbook','plugin.xml')
    xml = lxml.etree.parse(fn).getroot()
    from_xml = set(xml.xpath('//function/@name'))
    from_python = set(main.functions())
    n.assert_set_equal(from_xml, from_python)

def test_cases():
    '''
    Function names are case insensitive.
    With this in mind, the functions dict
    should contain no duplicates.
    '''
    observed = dict(collections.Counter(k.upper() for k in main.functions().keys()))
    expected = {k.upper():1 for k in main.functions().keys()}
    n.assert_dict_equal(observed, expected)

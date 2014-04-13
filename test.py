import sys
sys.path.append('spellbook')
import os

import nose.tools as n
import lxml.etree

from sheetmusic import sheetmusic_functions as f

def test_xml():
    fn = os.path.join('spellbook','plugin.xml')
    xml = lxml.etree.parse(fn).getroot()
    from_xml = set(xml.xpath('//function/@name'))
    from_python = set(f.keys())
    n.assert_set_equal(from_xml, from_python)

def test_to_integer():
    n.assert_equal(f['to_integer']('B3'), 34)

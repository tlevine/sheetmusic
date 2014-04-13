import sys
sys.path.append('spellbook')
import os

import nose.tools as n
import lxml.etree

import sheetmusic

def test_correspondance():
    fn = os.path.join('spellbook','plugin.xml')
    xml = lxml.etree.parse(fn).getroot()
    from_xml = set(xml.xpath('//function/@name'))
    from_python = set(sheetmusic.sheetmusic_functions.keys())
    n.assert_set_equal(from_xml, from_python)

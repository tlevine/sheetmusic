import sys
sys.path.append('spellbook')
import os

import lxml.etree

import sheetmusic

def test_correspondance():
    fn = os.path.join('spellbook','plugin.xml')
    lxml.etree.parse(fn).getroot()

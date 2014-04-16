import nose.tools as n
import lxml.etree

import libspreadsheet.main as main

def test_functions():
    fn = os.path.join('spellbook','plugin.xml')
    xml = lxml.etree.parse(fn).getroot()
    from_xml = set(xml.xpath('//function/@name'))
    from_python = set(main.functions())
    n.assert_set_equal(from_xml, from_python)

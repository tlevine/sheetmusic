import nose.tools as n
import mingus.containers as c

import libsheetmusic.spreadsheet as ss

def test_from_integer():
    n.assert_equal(ss.from_integer(23), c.Note(23))

def test_to_integer():
    n.assert_equal(ss.to_integer(c.Note(23)), 23)

def test_from_scientific():
    n.assert_equal(ss.from_scientific('A4'), c.Note('A-4'))

def test_to_scientific():
    n.assert_equal(ss.to_scientific(c.Note('A-4')), 'A4')

def test_range_apply():
    original = [[1,2],[3,4],[5,6]]
    observed = ss.range_apply(lambda x:x*10, original)
    expected = [[10,20],[30,40],[50,60]]
    n.assert_list_equal(observed, expected)

def test_from_range_ref():
    import libsheetmusic.test.MockGnumeric as MockGnumeric
    observed = ss.from_range_ref(MockGnumeric, MockGnumeric.RangeRef())
    expected = [[MockGnumeric.Cell._cell_text]*4]*6

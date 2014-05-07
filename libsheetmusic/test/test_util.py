import nose.tools as n
import mingus.containers as c

import libsheetmusic.util as util

def test_from_integer():
    n.assert_equal(util.from_integer(23), c.Note(23))

def test_to_integer():
    n.assert_equal(util.to_integer(c.Note(23)), 23)

def test_from_scientific():
    n.assert_equal(util.from_scientific('A4'), c.Note('A-4'))

def test_to_scientific():
    n.assert_equal(util.to_scientific(c.Note('A-4')), 'A4')

def test_from_range_ref():
    import libsheetmusic.test.MockGnumeric as MockGnumeric
    observed = util.from_range_ref(MockGnumeric, MockGnumeric.RangeRef())
    expected = [[MockGnumeric.Cell._cell_text]*4]*6

def test_range_apply():
    original = [[1,2],[3,4],[5,6]]
    observed = util.range_apply(lambda x:x*10, original)
    expected = [[10,20],[30,40],[50,60]]
    n.assert_list_equal(observed, expected)

def test_merge():
    a = {'one':1, 'two': 2}
    b = {'three': 3, 'four': 4}
    n.assert_dict_equal(util.merge(a,b), {'one': 1, 'two':2, 'three': 3, 'four': 4})
    n.assert_dict_equal(a, {'one':1, 'two': 2})
    n.assert_dict_equal(b, {'three': 3, 'four': 4})

def test_transpose():
    observed = util.transpose([[1,2,3],[4,5,6],[7,8,9]])
    expected = [[1,4,7],[2,5,8],[3,6,9]]
    n.assert_list_equal(observed, expected)

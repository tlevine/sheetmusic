import nose.tools as n

import libsheetmusic.util as util

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

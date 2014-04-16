import nose.tools as n

import libsheetmusic.util as util

def test_range_apply():
    original = [[1,2],[3,4],[5,6]]
    observed = util.range_apply(lambda x:x*10, original)
    expected = [[10,20],[30,40],[50,60]]
    n.assert_list_equal(observed, expected)

def test_merge():
    raise NotImplementedError

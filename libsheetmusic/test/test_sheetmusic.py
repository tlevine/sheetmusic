import mingus.containers as c
import nose.tools as n

import libsheetmusic.sheetmusic as s

def test_bars_D_4_4():
    observed = list(s.bars('D', (4, 4), ['C-4', 'E-4', 'G-4']))
    expected = [c.Bar('D', (4, 4))]
    expected[0] + 'C-4'
    expected[0] + 'E-4'
    expected[0] + 'G-4'
    
    n.assert_list_equal(observed, expected)

def test_bars_C_2_2():
    observed = list(s.bars('C', (2, 2), ['C-4', 'E-4', 'G-4']))
    expected = [c.Bar('C', (2, 2))] * 2
    expected[0] + 'C-4'
    expected[0] + 'E-4'
    expected[1] + 'G-4'
    
    n.assert_list_equal(observed, expected)

@n.nottest
def test_track():
    observed = list(s.bars('C', (2, 2), ['C-4', 'E-4', 'G-4']))
    expected = c.Track()
    bar = c.Bar('C', (2, 2))
    bar + 'C-4'
    bar + 'E-4'
    expected += bar
    bar = c.Bar('C', (2, 2))
    bar + 'G-4'
    expected += bar
    
    n.assert_list_equal(observed, expected)

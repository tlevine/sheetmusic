import nose.tools as n
import mingus.containers as c

import sheetmusic.music as music

def test_scale():
    observed = music.scale('lydian', c.Note('G',3))
    expected = [map(c.Note, ['G-3', 'A-4', 'B-4', 'C#-4', 'D-4', 'E-4', 'F#-4'])]
    n.assert_list_equal(observed[0], expected[0])
    n.assert_list_equal(observed, expected)

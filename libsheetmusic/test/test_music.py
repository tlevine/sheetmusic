import nose.tools as n
import mingus.containers as c

import libsheetmusic.music as music

def test_scale():
    observed = music.scale('lydian', c.Note('G',3))
    expected = [map(c.Note, ['G-3', 'A-4', 'B-4', 'C#-4', 'D-4', 'E-4', 'F#-4'])]
    n.assert_list_equal(observed[0], expected[0])
    n.assert_list_equal(observed, expected)

def test_chord():
    observed = music.chord('augmented_major_seventh', c.Note('C-5'))
    expected = [[c.Note(x)] for x in ['C-5', 'E-5', 'G#-5', 'B-6']]
    n.assert_list_equal(observed, expected)

def test_arpeggio():
    observed = music.chord('augmented_major_seventh', c.Note('C-5'))
    expected = [[c.Note(x) for x in ['C-5', 'E-5', 'G#-5', 'B-6']]]
    n.assert_list_equal(observed, expected)

def test_progression():
    observed = music.progression([['I','IV','V']], c.Note('C-3'))
    expected_str = [['C-3', 'E-3', 'G-3'], ['F-3', 'A-4', 'C-4'], ['G-3', 'B-4', 'D-4']]
    expected = [[c.Note(j) for j in i] for i in expected_str]
    n.assert_list_equal(observed, expected)

def test_keyed_interval():
    raise NotImplementedError

def test_nonkeyed_interval():
    raise NotImplementedError

def test_next_note():
    n.assert_equal(_next_note(c.Note('D-4'), 'E'), c.Note('E-4'))
    n.assert_equal(_next_note(c.Note('D-4'), 'C'), c.Note('C-5'))
    n.assert_equal(_next_note(c.Note('D-2'), 'E'), c.Note('E-2'))

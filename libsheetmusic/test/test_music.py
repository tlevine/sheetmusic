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
    n.assert_equal(music.keyed_interval('sixth', c.Note('G-4'), 'A'), c.Note('E-5'))
    n.assert_equal(music.keyed_interval('sixth', c.Note('G-4'), 'Ab'), c.Note('Eb-5'))
    n.assert_equal(music.keyed_interval('second', c.Note('D-2'), 'Ab'), c.Note('E-2'))

def test_nonkeyed_interval():
    n.assert_equal(music.keyed_interval('major_sixth', c.Note('G-4')), c.Note('E-5'))
    n.assert_equal(music.keyed_interval('minor_sixth', c.Note('G-4')), c.Note('Eb-5'))
    n.assert_equal(music.keyed_interval('major_second', c.Note('D-2')), c.Note('E-2'))

def test_next_note():
    n.assert_equal(_next_note(c.Note('D-4'), 'E'), c.Note('E-4'))
    n.assert_equal(_next_note(c.Note('D-4'), 'C'), c.Note('C-5'))
    n.assert_equal(_next_note(c.Note('D-2'), 'E'), c.Note('E-2'))

def test_ascending():
    note_names = ['D', 'G', 'A', 'C']
    n.assert_list_equal(_ascending(c.Note('C-3'), note_names), map(c.Note, ['D-3', 'G-3', 'A-4', 'C-4']))
    n.assert_list_equal(_ascending(c.Note('F-5'), note_names), map(c.Note, ['D-6', 'G-6', 'A-7', 'C-7']))

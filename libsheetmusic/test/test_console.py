import nose.tools as n
n.assert_list_equal.__self__.maxDiff = None
import mingus.containers as c

import libsheetmusic.console as console

def test_to_track_sparse():
    key = 'C'
    upper = 4
    lower = 4
    range_values = [
        ['D2', '', 'F#2', 'G2', 'A3', 'B3', 'C#3', 'D3'], # Column 1
        ['D3', '', 'F#3', 'G3', 'A4', 'B4', 'C#4', 'D4'], # Column 2
        ['D4', '', 'F#4', 'G4', 'A5', 'B5', 'C#5', 'D5'], # Column 3
    ]
    observed = console.to_track(range_values, key, upper, lower)
    expected = c.Track()
    expected.add_notes(c.NoteContainer(map(c.Note, ['D-2','D-3','D-4'])))
    expected.add_notes(c.NoteContainer(map(c.Note, ['E-2','E-3','E-4'])))
    expected.add_notes(c.NoteContainer(map(c.Note, ['F#-2','F#-3','F#-4'])))
    expected.add_notes(c.NoteContainer(map(c.Note, ['G-2','G-3','G-4'])))
    expected.add_notes(c.NoteContainer(map(c.Note, ['A-3','A-4','A-5'])))
    expected.add_notes(c.NoteContainer(map(c.Note, ['B-3','B-4','B-5'])))
    expected.add_notes(c.NoteContainer(map(c.Note, ['C#-3','C#-4','C#-5'])))
    expected.add_notes(c.NoteContainer(map(c.Note, ['D-3','D-4','D-5'])))
    n.assert_equal(list(observed), list(expected))

def test_to_track_dense():
    key = 'C'
    upper = 4
    lower = 4
    range_values = [
        ['D2', 'E2', 'F#2', 'G2', 'A3', 'B3', 'C#3', 'D3'], # Column 1
        ['D3', 'E3', 'F#3', 'G3', 'A4', 'B4', 'C#4', 'D4'], # Column 2
        ['D4', 'E4', 'F#4', 'G4', 'A5', 'B5', 'C#5', 'D5'], # Column 3
    ]
    observed = console.to_track(range_values, key, upper, lower)
    expected = c.Track()
    expected.add_notes(c.NoteContainer(map(c.Note, ['D-2','D-3','D-4'])))
    expected.add_notes(None)
    expected.add_notes(c.NoteContainer(map(c.Note, ['F#-2','F#-3','F#-4'])))
    expected.add_notes(c.NoteContainer(map(c.Note, ['G-2','G-3','G-4'])))
    expected.add_notes(c.NoteContainer(map(c.Note, ['A-3','A-4','A-5'])))
    expected.add_notes(c.NoteContainer(map(c.Note, ['B-3','B-4','B-5'])))
    expected.add_notes(c.NoteContainer(map(c.Note, ['C#-3','C#-4','C#-5'])))
    expected.add_notes(c.NoteContainer(map(c.Note, ['D-3','D-4','D-5'])))
    n.assert_equal(list(observed), list(expected))

import functools

import mingus.containers as c
import mingus.extra.LilyPond as LilyPond
from mingus.midi import MidiFileOut

import libsheetmusic.util as u

def sheetmusic(Gnumeric, range_ref, key = 'C', upper = 4, lower = 4, header = False):
    partial_bars = functools.partial(bars, key, (upper, lower))
    cells = u.from_range_ref(Gnumeric, range_ref)
    for column in cells:
        track = build_track(header, partial_bars, column)
        return LilyPond.to_png(track, '/tmp/track.png')

def build_track(header, partial_bars, column):
    '''
    header :: bool
    column :: [Note]
    '''

    if header:
        instrument = column[0]
        notes = column[1:]
    else:
        instrument = None
        notes = column

    track = c.Track(instrument)
    for bar in partial_bars(notes):
        track += bar
    return track

def bars(key, meter, notes):
    '''
    Group the notes into bars.
    '''
    upper, lower = meter
    left = notes[:lower]
    right = notes[lower:]

    if len(left) > 0:
        bar = c.Bar(key, meter)
        bar.place_notes(left, upper)
        yield bar
        for bar in bars(key, meter, right):
            yield bar

def to_midi(Gnumeric, fn, range_ref_or_cell):
    if 'RangeRef' in str(type(range_ref_or_cell)):
        MidiFileOut.write_Composition(fn, to_composition(u.from_range_ref(Gnumeric, range_ref_or_cell)))
    else:
        MidiFileOut.write_Note(fn, from_scientific(range_ref_or_cell))

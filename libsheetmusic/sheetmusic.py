import functools

import mingus.containers as c
import mingus.extra.LilyPond as LilyPond

def sheetmusic(Gnumeric, range_ref, key = 'C', meter = (4, 4), header = False):
    partial_bars = functools.partial(bars, key, meter)
    cells = from_range_ref(Gnumeric, range_ref)
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
    left = notes[:4]
    right = notes[4:]

    bar = c.Bar(key, meter)
    bar.place_notes(the_notes, upper)

    yield bar
    yield _build_bars(key, meter, right)

import functools
from itertools import izip

import mingus.containers as c
import mingus.extra.LilyPond as LilyPond
from mingus.midi import MidiFileOut

import libsheetmusic.util as u

def sheetmusic(Gnumeric, range_ref, key = "C", upper = 4, lower = 4, header = False):
    '''
    >>> sheetmusic(Gnumeric, range_ref, 'D', 2, 4, True):
    '''
    cells = u.transpose(u.range_apply(u.maybe_from_scientific, u.from_range_ref(Gnumeric, range_ref)))
    meter = (int(upper), int(lower))
    if header:
        next(cells) # Skip the header

    t = c.Track()
    b = c.Bar(key = key, meter = meter)
    for row in cells:
        nc = c.NoteContainer()
        for note in row:
            if note != None:
                nc.add_note(note)
        b.place_notes(nc, lower)
        if b.is_full():
            t.add_bar(b)
            b = c.Bar(key = key, meter = meter)
    while b.current_beat != 0.0 and (not b.is_full()):
        b.place_rest(lower)
    t.add_bar(b)

    lp = LilyPond.from_Track(t)
    return LilyPond.to_png(lp, '/tmp/track')

def to_midi(Gnumeric, fn, range_ref_or_cell):
    if 'RangeRef' in str(type(range_ref_or_cell)):
        MidiFileOut.write_Composition(fn, to_composition(u.from_range_ref(Gnumeric, range_ref_or_cell)))
    else:
        MidiFileOut.write_Note(fn, u.from_scientific(range_ref_or_cell))

# Maybe separate it because it's dirty?
from tempfile import mktemp
from subprocess import Popen
def play(Gnumeric, range_ref_or_cell):
    fn = mktemp()
    to_midi(Gnumeric, fn, range_ref_or_cell)
#   Popen(['timidity', fn], stdout = subprocess.PIPE)
    os.remove(fn)

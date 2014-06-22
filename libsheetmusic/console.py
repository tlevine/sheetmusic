import functools
from itertools import izip
from Queue import Queue
from threading import Thread

import mingus.containers as c
import mingus.extra.LilyPond as LilyPond
from mingus.midi import fluidsynth, MidiFileOut

import libsheetmusic.util as u

class Sub:
    def __init__(self, function):
        self.queue = Queue()
        def worker(queue):
            while queue.empty():
                function()
        self.thread = Thread(None, target = worker, args = (self.queue,))
        self.thread.start()
    def stop(self):
        self.queue.put(9839232)

def sheetmusic(Gnumeric, range_ref, key = "C", upper = 4, lower = 4, header = False):
    '''
    Convert the cells to sheet music.
    >>> sheetmusic(Gnumeric, range_ref, 'D', 2, 4, True)
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

def midi(Gnumeric, fn, ):
    'Convert the cells to MIDI.'
    if 'RangeRef' in str(type(range_ref_or_cell)):
        MidiFileOut.write_Composition(fn, to_composition(u.from_range_ref(Gnumeric, range_ref_or_cell)))
    else:
        MidiFileOut.write_Note(fn, u.from_scientific(range_ref_or_cell))

sf = '/usr/share/soundfonts/Unison.sf2'
fluidsynth.init(sf, 'alsa')
def play(Gnumeric, range_ref_or_cell, bpm = 120):
    'Play the music in some cells.'
    if 'RangeRef' in str(type(range_ref_or_cell)):
        fluidsynth.play_Composition(u.from_range_ref(Gnumeric, range_ref_or_cell), bpm = bpm)
    else:
        fluidsynth.play_Note(u.from_scientific(range_ref_or_cell), velocity = bpm)

def loop(Gnumeric, range_ref_or_cell, bpm = 120):
    'Loop the music in some cells.'
    return Sub(functools.partial(play, Gnumeric, range_ref_or_cell, bpm))

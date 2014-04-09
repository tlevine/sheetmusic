import re

import mingus.containers as containers
import mingus.core.chords as chords
import mingus.core.intervals as intervals

def pretty(func):
    '''
    Given a function of type (int -> int),
    make it into a function of type (scientific -> scientific).
    '''
    def wrapper(scientific_notation):
        m = re.match(r'^([^0-9]+)([0-9]+)$', scientific_notation)
        if not m:
            raise ValueError('%s is not in scientific notation' % scientific_notation)
        note_within_octave = m.group(1)
        octave = int(m.group(2))
        input_int = int(containers.Note(note_within_octave, octave))
        output_int = func(input_int)
        note = containers.Note(output_int)
        return note.name + str(note.octave)

def interval(up, thenote, theinterval):
    h

def main():
    functions = {}
    functions.update({name:getattr(intervals,name) for name in dir(intervals) if re.match(r'^(major|minor).*', name)})
    return functions

sheetmusic_functions = main()

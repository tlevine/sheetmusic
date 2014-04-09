import re

import mingus.containers as containers
import mingus.core.chords as chords
import mingus.core.intervals as intervals

def pretty(func):
    '''
    Given a function of type (int -> int),
    make it into a function of type (scientific -> scientific).
    '''
    def wrapper(scientific_notation, *args, **kwargs):
        m = re.match(r'^([^0-9]+)([0-9]+)$', scientific_notation)
        if not m:
            raise ValueError('%s is not in scientific notation' % scientific_notation)
        note_within_octave = m.group(1)
        octave = int(m.group(2))
        input_int = int(containers.Note(note_within_octave, octave))
        output_int = func(input_int, *args, **kwargs)
        note = containers.Note(output_int)
        return note.name + str(note.octave)
    return wrapper

@pretty
def interval(note, halfsteps):
    '''
    :param note: Integer representation of the note, like 57 for A4
    :param halfsteps: Integer of half steps in the interval, negative
                      for decreasing intervals
    '''
    return note + halfsteps

class Foo:
    def __add__(self, n):
        return 8

def main():
    functions = {'foo': Foo}
    return functions

sheetmusic_functions = main()

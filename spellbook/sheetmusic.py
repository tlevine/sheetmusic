import re

import mingus.containers as containers
import mingus.core.chords as chords
import mingus.core.intervals as intervals

def parse_scientific(scientific_notation):
    m = re.match(r'^([^0-9]+)([0-9]+)$', scientific_notation)
    if not m:
        raise ValueError('%s is not in scientific notation' % scientific_notation)
    note_within_octave = m.group(1)
    octave = int(m.group(2))
    return containers.Note(note_within_octave, octave)

def pretty(func):
    '''
    Given a function of type (int -> int),
    make it into a function of type (scientific -> scientific).
    '''
    def wrapper(scientific_notation, *args, **kwargs):
        input_int = int(parse_scientific(scientific_notation))
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

def integer(note):
    '''
    :param note: Scientific representation of the note, like A4
    '''
    return int(parse_scientific(note))

def main():
    functions = {
        'integer': integer,
    }
    return functions

sheetmusic_functions = main()

import re

import mingus.containers as containers

def from_scientific(scientific_note):
    m = re.match(r'^([^0-9]+)([0-9]+)$', str(scientific_note))
    if not m:
        raise ValueError('%s is not in scientific notation' % scientific_note)
    note_within_octave = m.group(1)
    octave = int(m.group(2))
    return containers.Note(note_within_octave, octave)

def to_scientific(integral_note):
    note = containers.Note(int(integral_note))
    return note.name + str(note.octave)

def range_apply(func, list_list):
    return [[func(cell) for cell in column] for column in list_list]

def to_integer(scientific_note):
    '''
    :param scientific_note: Scientific representation of the note, like A4

    Returns an integer so you can feed this into spreadsheet functions
    '''
    return int(scientific_note)

def from_integer(integral_note):
    '''
    :param integral_note: Integral representation of a note, like 42

    Returns the note in scientific notation so you can feed this into
    other sheetmusic functions
    '''
    return containers.Note(integral_note)

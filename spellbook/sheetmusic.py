import re

import mingus.containers as containers
import mingus.core.chords as chords
import mingus.core.scales as scales
import mingus.core.intervals as intervals
import mingus.core.progressions as progressions

import mingus.extra.LilyPond as LilyPond

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

def pretty(func):
    '''
    Given a function of type (int -> int),
    make it into a function of type (scientific -> scientific).
    '''
    def wrapper(scientific_note, *args, **kwargs):
        input_int = int(from_scientific(scientific_note))
        output_int = func(input_int, *args, **kwargs)
        return to_scientific(output_int)
    return wrapper

@pretty
def interval(note, halfsteps):
    '''
    :param note: Integer representation of the note, like 57 for A4
    :param halfsteps: Integer of half steps in the interval, negative
                      for decreasing intervals
    '''
    return note + halfsteps

def to_integer(scientific_note):
    '''
    :param note: Scientific representation of the note, like A4
    '''
    return int(from_scientific(str(scientific_note)))

def from_integer(integral_note):
    return to_scientific(containers.Note(int(integral_note)))

def scale(func_name, scientific_note):
    'http://code.google.com/p/mingus/wiki/tutorialScales'
    note = from_scientific(scientific_note)
    results = _ascending(note, map(containers.Note, getattr(scales, func_name)(note.name)))
    return [[to_scientific(result) for result in results]]

def _chord(func_name, scientific_note, *args, **kwargs):
    'http://code.google.com/p/mingus/wiki/tutorialChords'
    note = from_scientific(scientific_note)
    results = _ascending(note, map(containers.Note, getattr(chords, func_name)(note.name, *args, **kwargs)))
    return [to_scientific(result) for result in results]

def chord(*args, **kwargs):
    return [[x] for x in _chord(*args, **kwargs)]

def arpeggio(*args, **kwargs):
    return [_chord(*args,**kwargs)]

def _ascending(note, results):
    results = list(results)
    if results[0].name >= note.name:
        octave = note.octave
    else:
        octave = note.octave + 1

    for result in results:
        result.octave = octave

    def correct_octaves(smaller, larger):
        if larger <= smaller:
            larger.octave = larger.octave + 1

    smaller = None
    for result in results:
        if smaller == None:
            smaller = result
            continue
        larger = result
        correct_octaves(smaller, result)
    return results

def progression(the_progression, root):
    '''
    >>> progression(['I','IV','V'], 'C3')
    [['C3', 'E3', 'G3'], ['F3', 'A4', 'C4'], ['G3', 'B4', 'D4']]
    '''
    root_note = from_scientific(root)
    chords = progressions.to_chord(the_progression, root.name)
    return [_ascending(root, chord) for chord in chords]

def sheetmusic(range_ref, key = 'C', meter = (4, 4)):
    # Gnumeric.functions['column'](range_ref)
    for column in cells:
        bar = containers.Bar(key, meter)
        for cell in column:
            bar += from_scientific(cell)
        LilyPond.to_png(bar, '/tmp/bar.png')

def main():
    functions = {
        'to_integer': to_integer,
        'from_integer': from_integer,
        'interval': interval,
        'chord': chord,
        'scale': scale,
        'progression': progression,
        'sheetmusic': sheetmusic,
    }
    return functions

sheetmusic_functions = main()

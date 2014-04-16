import re

import mingus.containers as containers
import mingus.core.chords as chords
import mingus.core.scales as scales
import mingus.core.intervals as intervals
import mingus.core.progressions as progressions

def scale(func_name, note):
    'http://code.google.com/p/mingus/wiki/tutorialScales'
    return [_ascending(note, map(containers.Note, getattr(scales, func_name)(note.name)))]

def chord(*args, **kwargs):
    return [[x] for x in _chord(*args, **kwargs)]

def arpeggio(*args, **kwargs):
    return [_chord(*args,**kwargs)]

def progression(the_progression, root_note):
    '''
    >>> progression(['I','IV','V'], 'C3')
    [['C3', 'E3', 'G3'], ['F3', 'A4', 'C4'], ['G3', 'B4', 'D4']]
    '''
    chords = progressions.to_chords(the_progression, root_note.name)
    return [_ascending(root_note, chord) for chord in chords]

def _chord(func_name, note, *args, **kwargs):
    'http://code.google.com/p/mingus/wiki/tutorialChords'
    return _ascending(note, map(containers.Note, getattr(chords, func_name)(note.name, *args, **kwargs)))

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

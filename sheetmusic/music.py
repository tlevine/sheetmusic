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

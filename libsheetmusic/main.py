import functools

import libspreadsheet.music as m

def scale_functions():
    scale_names = [
        'aeolian',
        'chromatic',
        'diatonic',
        'diminished',
        'dorian',
        'harmonic_minor',
        'ionian',
        'locrian',
        'lydian',
        'melodic_minor',
        'mixolydian',
        'natural_minor',
        'phrygian',
        'whole_note'
    ]
    return {name + '_scale': functools.partial(m.scale, name) for name in scale_names}

def chord_functions():
    chord_names = [
        'I', 'I7', 'II', 'II7', 'III', 'III7', 'IV', 'IV7', 'V', 'V7', 'VI', 'VI7', 'VII', 'VII7',
        'augmented_major_seventh', 'augmented_minor_seventh', 'augmented_triad',
        'diminished_seventh', 'diminished_triad',
        'dominant', 'dominant7', 'dominant_flat_five', 'dominant_flat_ninth', 'dominant_ninth',
        'dominant_seventh', 'dominant_sharp_ninth', 'dominant_sixth','dominant_thirteenth',
        'eleventh', 'first_inversion',
        'half_diminished_seventh', 'hendrix_chord',
        'ii', 'ii7', 'iii', 'iii7', 'invert', 'lydian_dominant_seventh',
        'major_ninth', 'major_seventh', 'major_sixth', 'major_thirteenth', 'major_triad',
        'mediant', 'mediant7', 'minor_eleventh', 'minor_major_seventh', 'minor_ninth',
        'minor_seventh', 'minor_seventh_flat_five', 'minor_sixth', 'minor_thirteenth',
        'minor_triad', 'notes', 'second_inversion', 'seventh', 'sevenths', 'sixth_ninth',
        'subdominant', 'subdominant7', 'submediant', 'submediant7', 'subtonic', 'subtonic7',
        'supertonic', 'supertonic7',
        'suspended_fourth_ninth', 'suspended_fourth_triad', 'suspended_second_triad',
        'suspended_seventh', 'suspended_triad', 'third_inversion',
        'tonic', 'tonic7', 'triad', 'triads', 'vi', 'vi7', 'vii', 'vii7',
    ]
    result = {name + '_chord': functools.partial(m.chord, name) for name in chord_names}
    result.update({name + '_arpeggio': functools.partial(m.arpeggio, name) for name in chord_names})

def progression(the_progression, root_note):

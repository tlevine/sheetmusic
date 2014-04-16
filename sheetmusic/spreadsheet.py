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

def range_apply(func, list_list):
    return [[func(cell) for cell in cells] for column in list_list]

def
    note = from_scientific(scientific_note)


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

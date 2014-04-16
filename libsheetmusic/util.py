def merge(a, b):
    '''
    (dict,dict) -> dict
    Combine two dictionaries without side-effects.
    '''
    result = dict(a)
    result.update(b)
    return result

def range_apply(func, list_list):
    return [[func(cell) for cell in column] for column in list_list]


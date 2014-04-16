import functools
import Gnumeric

from_range_ref = functools.partial(sheetmusic.spreadsheet.from_range_ref, Gnumeric)

def main():
    functions = {
     #  'to_integer': to_integer,
        'from_range_ref': from_range_ref,
     #  'interval': interval,
     #  'chord': chord,
     #  'scale': scale,
     #  'progression': progression,
     #  'sheetmusic': sheetmusic,
    }
    return functions

sheetmusic_functions = main()

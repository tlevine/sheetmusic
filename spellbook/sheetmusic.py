import re

import mingus.core.chords as chords
import mingus.core.intervals as intervals

def main():
    functions = {}
    functions.update({name:getattr(intervals,name) for name in dir(intervals) if re.match(r'^(major|minor).*', name)})
    return functions

sheetmusic_functions = main()

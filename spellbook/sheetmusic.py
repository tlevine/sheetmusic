
import mingus.extra.LilyPond as LilyPond
from mingus.midi import fluidsynth
fluidsynth.init


def sheetmusic(range_ref, key = 'C', meter = (4, 4)):
    for column in cells:
        bar = containers.Bar(key, meter)
        for cell in column:
            bar += from_scientific(cell)
        LilyPond.to_png(bar, '/tmp/bar.png')

try:
    import Gnumeric
except ImportError:
    pass
else:
    def range_values(range_ref):
        workbook_index = 0 # Let's just hope that's always the case
        workbook = Gnumeric.workbooks()[workbook_index]
        sheet_index = int(Gnumeric.functions['sheet'](range_ref)) - 1
        sheet = workbook.sheets()[sheet_index]
        begin, end = range_ref.get_tuple()
        rows = map(int, Gnumeric.functions['row'](range_ref)[0])
        columns = [int(x[0]) for x in Gnumeric.functions['column'](range_ref)]
        return [[sheet.cell_fetch(int(column-1), int(row-1)).get_entered_text() for row in rows] for column in columns]

def from_integer(range_ref):
    return str(type(range_ref))

def from_range_ref(range_ref):
    workbook_index = 0 # Let's just hope that's always the case
    workbook = Gnumeric.workbooks()[workbook_index]
    sheet_index = int(Gnumeric.functions['sheet'](range_ref)) - 1
    sheet = workbook.sheets()[sheet_index]
    begin, end = range_ref.get_tuple()
    print(Gnumeric.functions['row'](range_ref))
    print(Gnumeric.functions['column'](range_ref))
    rows = map(int, Gnumeric.functions['row'](range_ref)[0])
    columns = [int(x[0]) for x in Gnumeric.functions['column'](range_ref)]
    return [[sheet.cell_fetch(int(column-1), int(row-1)).get_entered_text() for row in rows] for column in columns]

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

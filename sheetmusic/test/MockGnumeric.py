class Cell:
    _cell_text = 'The rendered text'
    def get_rendered_text(self, ):
        return self._cell_text

class Sheet:
    def cell_fetch(self, column, row):
        return Cell()

class Workbook:
    def sheets(self):
        return (Sheet(), Sheet(), Sheet(), )

class RangeRef:
    def get_tuple():
        raise NotImplementedError

workbooks = lambda: (Workbook(),)

functions = {
    'sheet': lambda _: 1.0,
    'column': lambda _: [[1.0], [2.0], [3.0], [4.0]],
    'row': lambda _: [[1.0, 2.0, 3.0, 4.0, 5.0, 6.0]],
}

from functools import partial

import libsheetmusic.console as c

import Gnumeric

play = partial(c.play, Gnumeric)
loop = partial(c.loop, Gnumeric)
midi = partial(c.midi, Gnumeric)
sheetmusic = partial(c.sheetmusic, Gnumeric)
bold = partial(c.bold, Gnumeric)
init = c.init
show_track = partial(c.show_track, Gnumeric)
show_rendered_text = partial(c.show_rendered_text, Gnumeric)

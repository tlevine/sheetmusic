import mingus.extra.LilyPond as LilyPond

def sheetmusic(Gnumeric, range_ref, key = 'C', meter = (4, 4), header = False):
    cells = from_range_ref(Gnumeric, range_ref)
    upper, lower = meter
    for column in cells:
        if header:
            track = containers.Track() #column header
        else:
            track = containers.Track()
        bar = containers.Bar(key, meter)
        for cell in column:
            if b.is_full():
                track += bar
                bar = containers.Bar(key, meter)
            else:
                bar += from_scientific(cell)
        LilyPond.to_png(bar, '/tmp/bar.png')

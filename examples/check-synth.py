#!/usr/bin/env python2
import mingus.containers as c
from mingus.midi import fluidsynth, MidiFileOut

sf = '/usr/share/soundfonts/Unison.sf2'
fluidsynth.init(sf, 'alsa')

bar = c.Bar()
bar + c.Note('A',4)
bar + c.Note('B',4)
bar + c.Note('C',4)
bar + c.Note('D',4)
print(bar)

for _ in range(10):
    print('Play')
    fluidsynth.play_Bar(bar)

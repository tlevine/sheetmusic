from mingus.midi import fluidsynth, MidiFileOut
sf = '/usr/share/soundfonts/Unison.sf2'
fluidsynth.init(sf, 'alsa')

# Maybe separate it because it's dirty?
from tempfile import mktemp
from subprocess import Popen
def play(Gnumeric, range_ref_or_cell):
    fn = mktemp()
    to_midi(Gnumeric, fn, range_ref_or_cell)
#   Popen(['timidity', fn], stdout = subprocess.PIPE)
    os.remove(fn)

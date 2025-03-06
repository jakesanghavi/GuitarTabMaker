# GuitarTabMaker

GuitarTabMaker is a Python tool that allows you to quickly transcribe your guitar songs into tab format. It is also compatible with [Acousterr](https://www.acousterr.com/).

## Usage
Below is an example of how to use `GuitarTabMaker` to generate a tab:

```python
from guitar_tab_maker import TabMaker

t = TabMaker(bpm=275, capo=None, info="Intro part shapes: A, C#m/G#, F#m, D, picking: t4, i3, m1")

sequences = []
sequences += ['D7', 'z1', 'G6', 'D7', 'z1', 'B5', 'z1', 'G6', 'D7', 'G6']*1
sequences += ['D6', 'z1', 'G6', 'D6', 'z1', 'B5', 'z1', 'G6', 'D6', 'G6']*1
sequences += ['D4', 'z1', 'G2', 'D4', 'z1', 'B2', 'z1', 'G2', 'D4', 'G2']*1
sequences += ['D2', 'z1', 'G2', 'D2', 'z1', 'B2', 'z1', 'G2', 'D2', 'G2']*1

t.add_line(sequences)
sequences = []

sequences += ['D0', 'z1', 'G2', 'D0', 'z1', 'B5', 'z1', 'G2', 'D0', 'G2']*2
sequences += ['D4', 'z1', 'G2', 'D4', 'z1', 'B2', 'z1', 'G2', 'D4', 'G2']*1
sequences += ['D2', 'z1', 'G2', 'D2', 'z1', 'B2', 'z1', 'G2', 'D2', 'G2']*1

t.add_line(sequences)

t.save_tab("Orange_Juice_Noah_Kahan")
```

## Output Example
The above script generates a guitar tab:

```
(/) Slide Up  (\) Slide Down  (h) Hammer On  (p) Pull Off  (b) Bend (r) Release (v) Vibrato (x) Muted
Tabs for Song :
BPM : 275

^This number isn't perfect, but it's close. Play along with the song to get a better feel.
Notes : Intro part shapes: A, C#m/G#, F#m, D, picking: t4, i3, m1

E|--------------------------------------------------------------------------------------------------
B|-------------5-----------------------5-----------------------2-----------------------2------------
G|------6----------6-----6------6----------6-----6------2----------2-----2------2----------2-----2--
D|--7------7----------7-----6------6----------6-----4------4----------4-----2------2----------2-----
A|--------------------------------------------------------------------------------------------------
E|--------------------------------------------------------------------------------------------------

E|--------------------------------------------------------------------------------------------------
B|-------------5-----------------------5-----------------------2-----------------------2------------
G|------2----------2-----2------2----------2-----2------2----------2-----2------2----------2-----2--
D|--0------0----------0-----0------0----------0-----4------4----------4-----2------2----------2-----
A|--------------------------------------------------------------------------------------------------
E|--------------------------------------------------------------------------------------------------
```


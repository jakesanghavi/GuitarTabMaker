class TranscriptionLine:
    """
    Represents a single line of a guitar tab with six strings (E, B, G, D, A, E).
    Each string starts with '--' as a base for Acousterr compatibilityand is updated with notes as they are added.
    """
    def __init__(self, seq):
        """
        Initializes the tab with the default '--' values
        
        :param seq: Boolean flag indicating if this line follows another in sequence (not used for now)
        """
        self.e_notes = 'E|' + '--'
        self.B_notes = 'B|' + '--'
        self.G_notes = 'G|' + '--'
        self.D_notes = 'D|' + '--'
        self.A_notes = 'A|' + '--'
        self.E_notes = 'E|' + '--'

    @property
    def notes(self):
        """
        Returns a list containing the current state of all six strings.
        
        :return: List of string representations of guitar notes.
        """
        return [self.e_notes, self.B_notes, self.G_notes, self.D_notes, self.A_notes, self.E_notes]
    
    def add_notes(self, notes):
        """
        Adds notes to the transcription line based on input notation.
        Support for more complicated types of notes is coming soon.
        
        :param notes: List of strings, each specifying notes to be added in the format "StringLetterNumber".
        """
        note_map = {
            'e': 'e_notes',
            'B': 'B_notes',
            'G': 'G_notes',
            'D': 'D_notes',
            'A': 'A_notes',
            'E': 'E_notes'
        }

        for note in notes:
            # Track what strings of the guitar have been updated
            updated_strings = set()
            
            # Currently process 2 chars at once but later we will have to widen this net
            for i in range(0, len(note) - 1, 2):
                # Which string we are on
                string_id = note[i]
                
                # Note value (fret number or other)
                value = note[i + 1]

                # Update the string/s which have gotten new notes
                if string_id in note_map:
                    setattr(self, note_map[string_id], getattr(self, note_map[string_id]) + value + '--')
                    updated_strings.add(string_id)
            
            # z is our special character to represent a rest
            if note[0] == 'z':
                for key, attr in note_map.items():
                    if key not in updated_strings:
                        # Add a number of rest dashes equal to the value after z
                        setattr(self, attr, getattr(self, attr) + '-' * int(note[1]))
            # If no rest, update the other strings with a full beat rest
            else:
                for key, attr in note_map.items():
                    if key not in updated_strings:
                        setattr(self, attr, getattr(self, attr) + '---')


class TabMaker:
    """
    Creates a guitar tab for a song, allowing notes to be added and the output file to be saved to .txt
    """
    def __init__(self, bpm=100, capo=None, info=None):
        """
        Initialize self with BPM, capo, and additional song info as needed
        
        :param bpm: Beats per minute for the song.
        :param capo: Capo position, if applicable.
        :param info: Additional info about the tab
        """
        self.bpm = bpm
        self.capo = capo
        self.info = info
        self.spiel = f"""(/) Slide Up  (\) Slide Down  (h) Hammer On  (p) Pull Off  (b) Bend (r) Release (v) Vibrato (x) Muted
Tabs for Song :
BPM : {self.bpm}
{'Capo : ' + self.capo if self.capo else ''}
^This number isn't perfect, but it's close. Play along with the song to get a better feel.
{'Notes : ' + self.info if self.info else ''}\n"""
        
        self.lines = []
        
    def add_line(self, line):
        """
        Adds a new line to the tab full of notes already
        
        :param line: List of notes to be added to the new line.
        """
        seq = len(self.lines) > 0
        t_line = TranscriptionLine(seq)
        t_line.add_notes(line)
        self.lines.append(t_line)
        
    @property
    def output(self):
        """
        Generate the tab output for printing or file saving
        
        :return: String representation of the guitar tab
        """
        return self.spiel + "\n\n".join(["\n".join(line.notes) for line in self.lines])
    
    def save_tab(self, filename=None):
        """
        Save the tab to txt files
        
        :param filename: Name of the file (without extension) to save the tab
        :raises Exception: If no filename is provided.
        """
        if not filename or len(filename) < 1:
            raise Exception("Please provide the song name/file name!")
        with open(f"{filename}.txt", "w") as text_file:
            text_file.write(self.output)

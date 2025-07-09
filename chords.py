import intervals
import sound
import utils

# if bass_note specified is not in any perfect octave apart from list_of_notes, it will not terminate
def inversion_by_name(list_of_notes, bass_note):
    return utils.inversion_by_name(list_of_notes, bass_note)

def inversion_by_number(list_of_notes, position):
    return utils.inversion_by_number(list_of_notes, position)

def major_triad(root):
    return utils.intervals_to_notes(root, ['P1', 'M3', 'P5'])

def major_seventh(root):
    return utils.intervals_to_notes(root, ['P1', 'M3', 'P5', 'M7'])

def major_ninth(root):
    return utils.intervals_to_notes(root, ['P1', 'M3', 'P5', 'M7', 'M9'])

def minor_triad(root):
    return utils.intervals_to_notes(root, ['P1', 'm3', 'P5'])

def minor_seventh(root):
    return utils.intervals_to_notes(root, ['P1', 'm3', 'P5', 'm7'])

def minor_ninth(root):
    return utils.intervals_to_notes(root, ['P1', 'm3', 'P5', 'm7', 'M9'])
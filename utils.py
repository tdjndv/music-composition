import intervals

def intervals_to_notes(root, steps):
    l = []
    for i in steps:
        l.append(intervals.get_node(root, i))
    return l

def raise_note(note, step):
    return intervals.get_node(note, step)

def inversion_by_name(l, bass_note):
    pointer = 0
    while l[pointer] != bass_note:
        l.append(raise_note(l[pointer], 'P8'))
        pointer += 1

    return l[pointer:]

def inversion_by_number(l, position):
    for i in range(0, position):
        l.append(raise_note(l[i], 'P8'))
    
    return l[position:]
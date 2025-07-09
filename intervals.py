import math

chromatic_scale = "C C# D D# E F F# G G# A A# B".split(' ')

intervals = {
    "P1" : 0,
    "m2" : 1,
    "M2" : 2,
    "m3" : 3,
    "M3" : 4,
    "P4" : 5,
    "A4" : 6,
    "d5" : 6,
    "P5" : 7,
    "m6" : 8,
    "M6" : 9,
    "m7" : 10,
    "M7" : 11,
    "P8" : 12,
    "m9" : 13,
    "M9" : 14,
    "P11" : 17,
    "m13" : 20,
    "M13" : 21
}

def find_index(note):
    for i in range(0, len(chromatic_scale)):
        if chromatic_scale[i] == note:
            return i
    return -1

def get_node(root, interval_name):
    note = find_index(root[:-1])
    current_octave = int(root[len(root) - 1])
    s = note + intervals[interval_name]
    raised_octave = math.floor(s / len(chromatic_scale))
    index = s % len(chromatic_scale)
    return chromatic_scale[index] + str(current_octave + raised_octave)
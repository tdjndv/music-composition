import chords
import sound

chord = chords.minor_ninth('F3')
print(chord)
sound.play_list_of_notes(chord)
sound.play_chord(chord)
inversion = chords.inversion_by_number(chord, 2)
print(inversion)
sound.play_list_of_notes(inversion)
sound.play_chord(inversion)



while True:
    break
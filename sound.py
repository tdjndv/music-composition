import numpy as np
import sounddevice as sd

from frequencies import note_freqs

def play_list_of_notes(l):
    for n in l:
        play_note(n)

def play_note(note_name, duration=1.0, fs=44100):
    print(note_name)
    frequency = note_freqs.get(note_name)
    if frequency is None:
        print(f"Note {note_name} not found!")
        return

    t = np.linspace(0, duration, int(fs * duration), endpoint=False)

    # Add harmonics for richer tone
    waveform = (
        0.6 * np.sin(2 * np.pi * frequency * t) +
        0.3 * np.sin(2 * np.pi * 2 * frequency * t) +
        0.1 * np.sin(2 * np.pi * 3 * frequency * t)
    )

    # Exponential decay envelope
    envelope = np.exp(-3 * t)
    waveform *= envelope

    # Normalize
    waveform /= np.max(np.abs(waveform))

    sd.play(waveform, fs)
    sd.wait()

def generate_tone(frequency, duration=1.0, fs=44100):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    waveform = (
        0.6 * np.sin(2 * np.pi * frequency * t) +
        0.3 * np.sin(2 * np.pi * 2 * frequency * t) +
        0.1 * np.sin(2 * np.pi * 3 * frequency * t)
    )
    envelope = np.exp(-3 * t)
    waveform *= envelope
    return waveform

def play_chord(note_names, duration=1.0, fs=44100):
    waveforms = []
    for note in note_names:
        freq = note_freqs.get(note)
        if freq is None:
            print(f"Note {note} not found!")
            continue
        waveforms.append(generate_tone(freq, duration, fs))
    
    if not waveforms:
        print("No valid notes to play!")
        return
    
    # Sum the waveforms to play simultaneously
    chord_waveform = np.sum(waveforms, axis=0)
    
    # Normalize to avoid clipping
    chord_waveform /= np.max(np.abs(chord_waveform))
    
    sd.play(chord_waveform, fs)
    sd.wait()
import sounddevice as sd
from scipy.io.wavfile import write
from pydub import AudioSegment
import json
import numpy as np
import os

def create_audio_recording(seconds = 3, fs = 44100):
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('mic_input.ogg', fs, myrecording)  # Save as WAV file

def get_peaks():
    time = []
    frequency = []
    magnitude = []

    f = open("../examples/data/songdata.json")
    data = json.load(f)
    for freq_ranges in data["frequency_band_to_peaks"].items():
        print(freq_ranges)
        for peaks in freq_ranges[1]:
            frequency.append(peaks["_frequency_hz"])
            magnitude.append(peaks["peak_magnitude"])
            time.append(peaks["_seconds"])
    return np.array(frequency), np.array(time), np.array(magnitude)



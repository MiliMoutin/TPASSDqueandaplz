import sounddevice as sd
from scipy.io.wavfile import write
from pydub import AudioSegment
import json
import numpy as np
import contextlib
import os

def create_audio_recording(seconds = 3, fs = 44100):
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished

    filename='mic_input.ogg'
    with contextlib.suppress(FileNotFoundError):
        os.remove(filename)

    write(filename, fs, myrecording)  # Save as WAV file

    return filename


def get_peaks():
    time = []
    frequency = []
    magnitude = []

    current_path = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(current_path, "extra_files", "songdata.json")
    f = open(filename)
    data = json.load(f)
    for freq_ranges in data["frequency_band_to_peaks"].items():
        print(freq_ranges)
        for peaks in freq_ranges[1]:
            frequency.append(peaks["_frequency_hz"])
            magnitude.append(peaks["peak_magnitude"])
            time.append(peaks["_seconds"])
    f.close()
    return np.array(frequency), np.array(time), np.array(magnitude)



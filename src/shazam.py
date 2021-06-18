import sounddevice as sd
from scipy.io.wavfile import write
from pydub import AudioSegment

def create_audio_recording(seconds = 3, fs = 44100):
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('mic_input.ogg', fs, myrecording)  # Save as WAV file

import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

# Audio settings
duration = 5
sample_rate = 44100

print("Recording will start in 2 seconds...")
sd.sleep(2000)

print("Recording started! Speak now...")

# Record audio
audio = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1,
    dtype="int16"
)

sd.wait()

# Save audio
write("recorded_audio.wav", sample_rate, audio)

# Extract audio signal features
audio_signal = audio.flatten()

amplitude = np.max(np.abs(audio_signal))
average_amplitude = np.mean(np.abs(audio_signal))

print("\nAudio recording completed!")
print("Audio saved as recorded_audio.wav")
print("Total samples:", len(audio_signal))
print("Maximum amplitude:", amplitude)
print("Average amplitude:", round(average_amplitude, 2))
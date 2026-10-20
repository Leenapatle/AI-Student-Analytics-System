import sounddevice as sd
import numpy as np
from scipy.io.wavfile import read

# Load recorded audio
sample_rate, audio = read("recorded_audio.wav")

# Convert audio to mono if needed
if len(audio.shape) > 1:
    audio = audio.mean(axis=1)

# Divide audio into small segments
segment_duration = 0.5
segment_size = int(sample_rate * segment_duration)

print("Audio Analysis Started\n")

for start in range(0, len(audio), segment_size):
    segment = audio[start:start + segment_size]

    if len(segment) == 0:
        continue

    # Calculate audio energy
    rms = np.sqrt(np.mean(segment.astype(float) ** 2))

    # Detect speech activity
    if rms > 500:
        print(f"{start / sample_rate:.1f}s - Speech/Audio detected")
    else:
        print(f"{start / sample_rate:.1f}s - Silence/Low audio detected")

print("\nAudio analysis completed!")
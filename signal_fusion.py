import cv2
import numpy as np
from scipy.io.wavfile import read
import os

print("=" * 40)
print("   MULTIMODAL SIGNAL FUSION")
print("=" * 40)

# 1. Check Face Model
face_score = 0

if os.path.exists("face_model.yml"):
    face_score = 1
    print("Face Signal: Available")
else:
    print("Face Signal: Not Available")

# 2. Analyze Audio Signal
audio_score = 0

if os.path.exists("recorded_audio.wav"):
    sample_rate, audio = read("recorded_audio.wav")

    audio = audio.astype(float)
    rms = np.sqrt(np.mean(audio ** 2))

    if rms > 500:
        audio_score = 1
        print("Audio Signal: Sound Detected")
    else:
        print("Audio Signal: Low Sound")

else:
    print("Audio Signal: Not Available")

# 3. Fuse Both Signals
print("\nCombining Face and Audio Signals...")

if face_score == 1 and audio_score == 1:
    fusion_result = "Face Model Available + Audio Detected"
elif face_score == 1:
    fusion_result = "Face Model Available Only"
elif audio_score == 1:
    fusion_result = "Audio Detected Only"
else:
    fusion_result = "No Signals Available"

print("Fusion Result:", fusion_result)
print("\nMultimodal Signal Fusion Completed!")
print("=" * 40)
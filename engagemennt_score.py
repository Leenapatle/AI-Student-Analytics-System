import cv2
import numpy as np
from scipy.io.wavfile import read
import os

print("=" * 40)
print("    ENGAGEMENT SCORING SYSTEM")
print("=" * 40)

# 1. Check face model availability
face_score = 0

if os.path.exists("face_model.yml"):
    face_score = 50
    print("Face Signal: Available")
else:
    print("Face Signal: Not Available")

# 2. Analyze audio
audio_score = 0

if os.path.exists("recorded_audio.wav"):
    sample_rate, audio = read("recorded_audio.wav")
    audio = audio.astype(float)

    if len(audio) > 0:
        rms = np.sqrt(np.mean(audio ** 2))

        if rms > 500:
            audio_score = 50
            print("Audio Signal: Sound Detected")
        else:
            print("Audio Signal: Low Sound")
else:
    print("Audio Signal: Not Available")

# 3. Calculate engagement score
engagement_score = face_score + audio_score

print("\nEngagement Score:", engagement_score, "/ 100")

if engagement_score >= 100:
    print("Status: Both signals available")
elif engagement_score >= 50:
    print("Status: One signal available")
else:
    print("Status: No signals available")

print("\nEngagement Scoring Completed!")
print("=" * 40)
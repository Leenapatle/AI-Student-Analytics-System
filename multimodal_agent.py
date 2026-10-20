import cv2
import numpy as np
from scipy.io.wavfile import read
import os

print("=" * 40)
print("   MULTIMODAL AI AGENT")
print("=" * 40)

# -------- FACE MODULE STATUS --------
print("\n1. FACE MODULE")

if os.path.exists("face_model.yml"):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("face_model.yml")
    print("Face recognition model loaded successfully!")
else:
    print("Face model not found!")

# -------- AUDIO MODULE STATUS --------
print("\n2. AUDIO MODULE")

if os.path.exists("recorded_audio.wav"):
    sample_rate, audio = read("recorded_audio.wav")

    audio_signal = audio.astype(float)
    rms = np.sqrt(np.mean(audio_signal ** 2))

    print("Audio file loaded successfully!")
    print("Audio RMS:", round(rms, 2))

    if rms > 500:
        print("Audio Status: Sound detected")
    else:
        print("Audio Status: Low sound or silence")
else:
    print("Audio file not found! Run audio_extraction.py first.")

# -------- AGENT SUMMARY --------
print("\n3. AGENT SUMMARY")
print("Face Module: Checked")
print("Audio Module: Checked")
print("Multimodal Agent execution completed!")

print("=" * 40)
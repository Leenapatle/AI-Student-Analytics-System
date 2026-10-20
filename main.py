import os
import subprocess
import sys

print("=" * 45)
print("   AI-POWERED STUDENT ANALYTICS SYSTEM")
print("=" * 45)

modules = [
    ("Face Attendance", "face_attendance.py"),
    ("Audio Extraction", "audio_extraction.py"),
    ("Audio Analysis", "audio_analysis.py"),
    ("Multimodal Agent", "multimodal_agent.py"),
    ("Signal Fusion", "signal_fusion.py"),
    ("Engagement Scoring", "engagement_score.py"),
    ("Teaching Suggestions", "teaching_suggestions.py"),
    ("Session Analytics", "session_analytics.py")
]

print("\nAvailable Modules:")

for index, (name, filename) in enumerate(modules, start=1):
    status = "Available" if os.path.exists(filename) else "File Missing"
    print(f"{index}. {name} - {status}")

print("\nCore application setup check completed!")

print("\nChoose a module to run:")
for index, (name, filename) in enumerate(modules, start=1):
    print(f"{index}. {name}")

choice = input("\nEnter module number (1-8): ")

if choice.isdigit() and 1 <= int(choice) <= len(modules):
    name, filename = modules[int(choice) - 1]

    if os.path.exists(filename):
        print(f"\nStarting {name}...\n")
        subprocess.run([sys.executable, filename])
    else:
        print("Selected module file not found!")
else:
    print("Invalid choice. Please enter a number from 1 to 8.")

print("\nCore application finished!")
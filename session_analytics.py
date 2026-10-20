import os
import csv
from datetime import datetime

print("=" * 45)
print("     STUDENT SESSION ANALYTICS")
print("=" * 45)

# Session information
session_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Check attendance record
attendance_status = "Attendance file not found"

if os.path.exists("attendance.csv"):
    with open("attendance.csv", "r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

        if len(rows) > 1:
            attendance_status = "Attendance record available"
        else:
            attendance_status = "No attendance records"

# Check audio recording
audio_status = "Audio file not found"

if os.path.exists("recorded_audio.wav"):
    audio_status = "Audio recording available"

# Get engagement score
while True:
    try:
        score = int(input("Enter engagement score (0-100): "))

        if 0 <= score <= 100:
            break

        print("Please enter a score between 0 and 100.")

    except ValueError:
        print("Please enter a valid number.")

# Generate report
if score >= 80:
    suggestion = "Continue current teaching method."
elif score >= 50:
    suggestion = "Use interactive teaching methods."
else:
    suggestion = "Try simple explanations and interactive activities."

report = [
    ["Student Session Analytics Report"],
    ["Session Date and Time", session_time],
    ["Attendance Status", attendance_status],
    ["Audio Status", audio_status],
    ["Engagement Score", score],
    ["Teaching Suggestion", suggestion]
]

# Save report to CSV
with open("session_analytics.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(report)

print("\n--- SESSION ANALYTICS ---")
print("Session Time:", session_time)
print("Attendance:", attendance_status)
print("Audio:", audio_status)
print("Engagement Score:", score)
print("Teaching Suggestion:", suggestion)

print("\nReport saved as session_analytics.csv")
print("Student Session Analytics Completed!")
print("=" * 45)
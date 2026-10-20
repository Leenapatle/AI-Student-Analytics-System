print("=" * 45)
print("      AI TEACHING SUGGESTION SYSTEM")
print("=" * 45)

# Get engagement score from user
score = int(input("Enter student engagement score (0-100): "))

print("\n--- Teaching Suggestions ---")

if score >= 80:
    print("Student Engagement: High")
    print("Suggestion: Continue with the current teaching method.")
    print("Activity: Give advanced questions to the student.")

elif score >= 50:
    print("Student Engagement: Moderate")
    print("Suggestion: Use interactive teaching methods.")
    print("Activity: Ask questions and provide examples.")

elif score >= 0:
    print("Student Engagement: Low")
    print("Suggestion: Explain the topic again using simple examples.")
    print("Activity: Include short breaks and interactive activities.")

else:
    print("Invalid score! Enter a number between 0 and 100.")

if score > 100:
    print("Invalid score! Enter a number between 0 and 100.")

print("\nTeaching Suggestion Generation Completed!")
print("=" * 45)
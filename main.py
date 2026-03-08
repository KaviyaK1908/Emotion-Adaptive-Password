from password_analyzer import check_password_strength
from typing_behavior import measure_typing_speed
from context_checker import check_context_similarity
from emotion_detection import detect_emotion

print("Emotion-Adaptive Password Strength Analyzer\n")

username = input("Enter username: ")

print("Type your password:")
password, typing_time = measure_typing_speed()

complexity_score = check_password_strength(password)
context_score = check_context_similarity(username, password)
emotion_score = detect_emotion(typing_time)

final_score = complexity_score + context_score + emotion_score

print("\nSecurity Analysis Result")
print("-----------------------")
print("Password Score:", final_score, "/100")

if final_score < 50:
    print("Weak password detected.")
elif final_score < 75:
    print("Moderate password.")
else:
    print("Strong password.")

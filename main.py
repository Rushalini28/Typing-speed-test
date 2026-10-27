
import time
import random

sentences = [
    "Python is a powerful and easy to learn programming language.",
    "Practice makes a person better at solving difficult problems.",
    "Technology helps people communicate and learn new things.",
    "Programming improves logical thinking and problem solving.",
    "Consistent practice helps improve typing speed and accuracy."
]

print("=" * 50)
print("           TYPING SPEED TEST")
print("=" * 50)

print("\nInstructions:")
print("1. Type the sentence displayed below.")
print("2. Press Enter when you finish.")
print("3. Your speed and accuracy will be calculated.")

input("\nPress Enter when you are ready to start...")

sentence = random.choice(sentences)

print("\nType this sentence:")
print("-" * 50)
print(sentence)
print("-" * 50)

start_time = time.time()
typed_text = input("\nYour typing: ")
end_time = time.time()

time_taken = end_time - start_time
time_taken_minutes = time_taken / 60

words_typed = len(typed_text.split())

if time_taken_minutes > 0:
    wpm = words_typed / time_taken_minutes
else:
    wpm = 0

correct_characters = 0

for i in range(min(len(sentence), len(typed_text))):
    if sentence[i] == typed_text[i]:
        correct_characters += 1

if len(typed_text) > 0:
    accuracy = (correct_characters / len(typed_text)) * 100
else:
    accuracy = 0

print("\n" + "=" * 50)
print("                YOUR RESULTS")
print("=" * 50)

print(f"Time taken: {time_taken:.2f} seconds")
print(f"Typing speed: {wpm:.2f} WPM")
print(f"Accuracy: {accuracy:.2f}%")
print(f"Words typed: {words_typed}")

if wpm >= 60 and accuracy >= 90:
    print("Performance: Excellent!")
elif wpm >= 40 and accuracy >= 80:
    print("Performance: Good job!")
else:
    print("Performance: Keep practising!")

print("=" * 50)

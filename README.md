# ⌨️ Typing Speed Test Using Python

## 📌 About the Project

The Typing Speed Test is a beginner-friendly Python application that measures how quickly and accurately a user can type a given sentence.

The program displays a random sentence, records the time taken to type it, calculates typing speed in Words Per Minute (WPM), measures character accuracy, and provides feedback based on the results.

## ✨ Features

- Displays a random sentence for typing practice.
- Measures typing time in seconds.
- Calculates typing speed in Words Per Minute (WPM).
- Calculates character-level typing accuracy.
- Counts the words typed by the user.
- Provides performance feedback.
- Handles empty input without crashing.
- Uses Python's built-in modules.

## 🛠️ Technologies Used

- **Programming Language:** Python 3
- **Modules:** `time`, `random`
- **Code Editor:** Visual Studio Code

## 📂 Project Structure

```text
Typing Speed Test/
│
└── main.py
```

## ⚙️ Requirements

- Python 3.x installed on your computer.
- Visual Studio Code or another Python editor.

No additional libraries are required.

## 🚀 How to Run the Project

### Step 1: Install Python

Download Python from https://www.python.org/downloads/ if it is not already installed.

### Step 2: Download or Clone the Repository

Download the repository to your computer and open the project folder in VS Code.

### Step 3: Open the Terminal

In VS Code, select **Terminal → New Terminal**.

### Step 4: Run the Program

Execute the following command:

```bash
python main.py
```

### Step 5: Start Typing

1. Press Enter to start the test.
2. Read the displayed sentence.
3. Type the sentence as quickly and accurately as possible.
4. Press Enter to submit your answer.
5. View your typing speed, accuracy, time, and performance feedback.

## 💻 Sample Output

```text
==================================================
           TYPING SPEED TEST
==================================================

Instructions:
1. Type the sentence displayed below.
2. Press Enter when you finish.
3. Your speed and accuracy will be calculated.

Type this sentence:
--------------------------------------------------
Python is a powerful and easy to learn programming language.
--------------------------------------------------

Your typing: Python is a powerful and easy to learn programming language.

==================================================
                YOUR RESULTS
==================================================
Time taken: 12.50 seconds
Typing speed: 57.60 WPM
Accuracy: 100.00%
Words typed: 11
Performance: Good job!
==================================================
```

*Note: The output above is illustrative. Actual results depend on the sentence, typing speed, and accuracy.*

## 🧮 How It Works

### 1. Random Sentence Selection
The `random` module selects a sentence from a predefined list.

### 2. Time Measurement
The `time` module records the start and end times to calculate the time taken.

### 3. Typing Speed Calculation
Typing speed is calculated using:

**WPM = Number of words typed ÷ Time taken in minutes**

### 4. Accuracy Calculation
The program compares the typed text with the original sentence character by character and calculates the percentage of matching characters.

### 5. Performance Feedback
The program displays feedback based on typing speed and accuracy.

## 📚 Python Concepts Learned

- Variables and data types
- Lists and random selection
- User input and output
- Conditional statements
- Loops
- String manipulation
- Time measurement
- Mathematical calculations
- Functions of Python's built-in modules

## 🔮 Future Improvements

- Add a graphical user interface using Tkinter.
- Include a countdown timer.
- Display a live typing-speed indicator.
- Save previous test results.
- Add difficulty levels.
- Track the user's best typing speed.
- Show detailed typing errors.

## 👨‍💻 Author

Created as a beginner-friendly Python project to practise programming fundamentals, string processing, and time measurement.

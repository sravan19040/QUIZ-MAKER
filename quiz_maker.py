# -*- coding: utf-8 -*-
"""QUIZ MAKER

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HZ9_LtK96CGTE679FNOVtBxl73ZxRBdh
"""

# Quiz Game in Python

# List of questions and answers
questions = [
    {"question": "What is the capital of France?", "options": ["A) Berlin", "B) London", "C) Paris", "D) Madrid"], "answer": "C"},
    {"question": "Which planet is known as the Red Planet?", "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"], "answer": "B"},
    {"question": "Who wrote 'To Kill a Mockingbird'?", "options": ["A) Harper Lee", "B) Mark Twain", "C) Ernest Hemingway", "D) F. Scott Fitzgerald"], "answer": "A"},
    {"question": "What is the smallest prime number?", "options": ["A) 1", "B) 2", "C) 3", "D) 5"], "answer": "B"},
    {"question": "Which element has the chemical symbol 'O'?", "options": ["A) Oxygen", "B) Gold", "C) Silver", "D) Iron"], "answer": "A"},
    {"question": "What is the hardest natural substance on Earth?", "options": ["A) Gold", "B) Iron", "C) Diamond", "D) Platinum"], "answer": "C"},
    {"question": "Which year did World War II end?", "options": ["A) 1940", "B) 1942", "C) 1945", "D) 1950"], "answer": "C"},
    {"question": "Who is known as the father of computers?", "options": ["A) Albert Einstein", "B) Charles Babbage", "C) Isaac Newton", "D) Nikola Tesla"], "answer": "B"},
    {"question": "Which gas do plants absorb from the atmosphere?", "options": ["A) Oxygen", "B) Nitrogen", "C) Carbon Dioxide", "D) Hydrogen"], "answer": "C"},
    {"question": "What is the longest river in the world?", "options": ["A) Amazon", "B) Nile", "C) Yangtze", "D) Mississippi"], "answer": "B"}
]

# Function to start the quiz
def start_quiz():
    score = 0
    for i, q in enumerate(questions):
        print(f"\nQuestion {i+1}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").strip().upper()

        if answer == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}")

    print(f"\nQuiz Completed! Your final score is: {score}/{len(questions)}")

# Start the quiz
start_quiz()
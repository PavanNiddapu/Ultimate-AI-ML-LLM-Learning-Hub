"""
Simple Quiz Example for Assessments and Checkpoints
"""

QUESTIONS = [
    {
        "question": "What is the output of 2 + 2?",
        "options": ["3", "4", "5"],
        "answer": "4"
    },
    {
        "question": "Which library is used for machine learning in Python?",
        "options": ["numpy", "scikit-learn", "matplotlib"],
        "answer": "scikit-learn"
    }
]

def run_quiz():
    score = 0
    for idx, q in enumerate(QUESTIONS):
        print(f"Q{idx+1}: {q['question']}")
        for i, opt in enumerate(q['options']):
            print(f"  {i+1}. {opt}")
        ans = input("Your answer (number): ")
        if q['options'][int(ans)-1] == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. Correct answer: {q['answer']}\n")
    print(f"Quiz complete! Your score: {score}/{len(QUESTIONS)}")

if __name__ == "__main__":
    run_quiz()

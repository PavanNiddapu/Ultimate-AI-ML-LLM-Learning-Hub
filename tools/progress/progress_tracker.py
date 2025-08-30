"""
Progress Tracker and Badge Awarding System
"""
import json
import os

PROGRESS_FILE = "user_progress.json"
BADGES = {
    "first_module": "Completed First Module",
    "quiz_master": "Passed All Quizzes",
    "challenge_champion": "Completed a Community Challenge"
}

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r") as f:
            return json.load(f)
    return {"completed_modules": [], "badges": []}

def save_progress(progress):
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)

def complete_module(module_name):
    progress = load_progress()
    if module_name not in progress["completed_modules"]:
        progress["completed_modules"].append(module_name)
        if len(progress["completed_modules"]) == 1:
            award_badge("first_module", progress)
        save_progress(progress)
        print(f"Module '{module_name}' marked as completed.")
    else:
        print(f"Module '{module_name}' already completed.")

def award_badge(badge_key, progress=None):
    if progress is None:
        progress = load_progress()
    badge = BADGES.get(badge_key)
    if badge and badge not in progress["badges"]:
        progress["badges"].append(badge)
        save_progress(progress)
        print(f"Badge awarded: {badge}")
    else:
        print(f"Badge already awarded or invalid badge key.")

def show_progress():
    progress = load_progress()
    print("Completed Modules:", progress["completed_modules"])
    print("Badges:", progress["badges"])

if __name__ == "__main__":
    # Example usage
    show_progress()
    complete_module("linear_regression_scratch")
    award_badge("quiz_master")
    show_progress()

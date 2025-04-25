# learning_path_generator.py

def ask_questions():
    print("\n🔍 Answer the following questions to determine your learning style:\n")
    questions = [
        {
            "question": "1. When trying to remember a phone number, what do you do?",
            "options": {
                "a": "Visualize the number in your head",
                "b": "Say the number aloud or in your head"
            }
        },
        {
            "question": "2. What helps you learn new material best?",
            "options": {
                "a": "Watching videos or looking at diagrams",
                "b": "Listening to podcasts or lectures"
            }
        },
        {
            "question": "3. How do you prefer to study?",
            "options": {
                "a": "Using highlighters and charts",
                "b": "Repeating things out loud or recording notes"
            }
        }
    ]

    visual_score = 0
    auditory_score = 0

    for q in questions:
        print(q["question"])
        for key, option in q["options"].items():
            print(f"  {key}) {option}")
        answer = input("Your answer (a/b): ").strip().lower()
        if answer == 'a':
            visual_score += 1
        elif answer == 'b':
            auditory_score += 1
        else:
            print("Invalid input, skipping question.")

        print()

    if visual_score > auditory_score:
        return "visual"
    elif auditory_score > visual_score:
        return "auditory"
    else:
        return "balanced"


def show_learning_path(style):
    print("\n🎓 Your Personalized Learning Path:\n")

    paths = {
        "visual": [
            ("Mastering Concepts Visually", "Use diagrams and infographics to grasp fundamentals."),
            ("Video-Powered Learning", "Watch expert tutorials with visual aids."),
            ("Visual Note-Taking", "Summarize information using mind maps and charts.")
        ],
        "auditory": [
            ("Audio Lessons", "Start with narrated guides or lectures."),
            ("Interactive Listening", "Participate in audio-based discussions."),
            ("Voice Note Practice", "Practice summarizing lessons by speaking them aloud.")
        ],
        "balanced": [
            ("Mixed Mode Learning", "Combine video and audio content to maximize retention."),
            ("Blended Study Tools", "Use both diagrams and voice recordings."),
            ("Self-Test Toolkit", "Alternate between flashcards and verbal repetition.")
        ]
    }

    for i, (title, desc) in enumerate(paths[style], 1):
        print(f"📘 Module {i}: {title}")
        print(f"   📝 {desc}\n")


if __name__ == "__main__":
    print("📚 Welcome to the Learning Style Quiz & Path Generator!")
    style = ask_questions()
    print(f"👉 You are a **{style.capitalize()} Learner**.")
    show_learning_path(style)

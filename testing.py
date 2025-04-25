import streamlit as st

# --- Page Config ---
st.set_page_config(
    page_title="Smart Learning Path",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- Title and Footer Hiding ---
st.title("📚 Smart Learning Path Generator")
st.markdown("#### Learn smarter with your personal AI guide 🚀")

# Hide Streamlit footer and menu
hide_footer = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_footer, unsafe_allow_html=True)

# --- Quiz Title ---
st.title("🎓 Personalized Learning Path Generator")
st.markdown("Take a short quiz to discover your learning style and get a custom learning path!")

# --- Quiz Questions ---
questions = [
    {
        "question": "When trying to remember a phone number, what do you do?",
        "options": ["Visualize the number in your head", "Say the number aloud or in your head"]
    },
    {
        "question": "What helps you learn new material best?",
        "options": ["Watching videos or looking at diagrams", "Listening to podcasts or lectures"]
    },
    {
        "question": "How do you prefer to study?",
        "options": ["Using highlighters and charts", "Repeating things out loud or recording notes"]
    }
]

# Initialize scores
visual_score = 0
auditory_score = 0
answers = []

# --- Quiz Form ---
with st.form("quiz_form"):
    for idx, q in enumerate(questions):
        answer = st.radio(f"**{q['question']}**", q["options"], key=idx)
        answers.append(answer)
    
    submitted = st.form_submit_button("Submit Quiz")

# --- Quiz Results ---
def new_func(style):
    plan_text = generate_learning_plan_text(style)
    return plan_text

if submitted:
    for ans in answers:
        if "Visual" in ans or "diagrams" in ans or "charts" in ans:
            visual_score += 1
        else:
            auditory_score += 1

    if visual_score > auditory_score:
        style = "visual"
        st.success("🧠 You are a **Visual Learner**")
    elif auditory_score > visual_score:
        style = "auditory"
        st.success("🎧 You are an **Auditory Learner**")
    else:
        style = "balanced"
        st.success("🌀 You are a **Balanced Learner**")

    # --- Show Learning Path ---
    def show_learning_path(style):
        st.markdown("---")
        st.header("📘 Your Personalized Learning Path")
      
        paths = {
            "visual": [
                ("Mastering Concepts Visually", "Use diagrams and infographics to grasp fundamentals.",
                 "https://www.youtube.com/watch?v=ZFDHcZZnBK4"),
                ("Video-Powered Learning", "Watch expert tutorials with visual aids.",
                 "https://www.youtube.com/watch?v=IN-_S_jj3gE"),
                ("Visual Note-Taking", "Summarize information using mind maps and charts.",
                 "https://www.youtube.com/watch?v=RVDfWfXJFxg")
            ],
            "auditory": [
                ("Audio Lessons", "Start with narrated guides or lectures.",
                 "https://www.youtube.com/watch?v=wBqeZLgv2Cg"),
                ("Interactive Listening", "Participate in audio-based discussions.",
                 "https://www.youtube.com/watch?v=6zFvIwcGkO4"),
                ("Voice Note Practice", "Practice summarizing lessons by speaking them aloud.",
                 "https://www.youtube.com/watch?v=LMX2pTUS1m8")
            ],
            "balanced": [
                ("Mixed Mode Learning", "Combine video and audio content to maximize retention.",
                 "https://www.youtube.com/watch?v=spUNpyF58BY"),
                ("Blended Study Tools", "Use both diagrams and voice recordings.",
                 "https://www.youtube.com/watch?v=ECcjHthLN2I"),
                ("Self-Test Toolkit", "Alternate between flashcards and verbal repetition.",
                 "https://www.youtube.com/watch?v=F1y0RS5Uv_M")
            ]
        }

        for i, (title, desc, video_url) in enumerate(paths[style], 1):
            st.subheader(f"📘 Module {i}: {title}")
            st.write(f"📝 {desc}")
            st.video(video_url)

            # Progress checkbox with session state handling
            key = f"module_{i}_done"

            # Initialize session state for each module if not already done
            if key not in st.session_state:
                st.session_state[key] = False

            # Display and track the checkbox state
            checkbox_state = st.checkbox(f"✅ Mark Module {i} as Done", value=st.session_state[key], key=key)
            
            # Update the session state with the new checkbox state after user interaction
            st.session_state[key] = checkbox_state
            st.markdown("---")

    # Call function to show the learning path
    show_learning_path(style)

    # --- Download Plan ---
    st.markdown("### 🧾 Download Your Plan")
    plan_text = new_func(style)
    st.download_button("📥 Download Plan (TXT)", plan_text, file_name="learning_plan.txt")

# --- Generate Learning Plan Text ---
def generate_learning_plan_text(style):
    plans = {
        "visual": [
            "1. Mastering Concepts Visually - Use diagrams and infographics.",
            "2. Video-Powered Learning - Watch tutorials with visual aids.",
            "3. Visual Note-Taking - Create mind maps and flowcharts."
        ],
        "auditory": [
            "1. Audio Lessons - Start with narrated guides.",
            "2. Interactive Listening - Join audio-based discussions.",
            "3. Voice Note Practice - Summarize lessons by speaking aloud."
        ],
        "balanced": [
            "1. Mixed Mode Learning - Combine video and audio formats.",
            "2. Blended Study Tools - Use diagrams & voice recordings.",
            "3. Self-Test Toolkit - Alternate flashcards & verbal recaps."
        ]
    }

    plan_lines = [
        f"Personalized Learning Plan ({style.title()} Learner)\n",
        "----------------------------------------\n"
    ] + plans[style]

    return "\n".join(plan_lines)

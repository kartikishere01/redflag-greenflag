import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Red / Green Flag Vibe Checker",
    page_icon="🚩",
    layout="wide"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>

/* Dark animated gradient background */
.stApp {
    background: linear-gradient(-45deg,
        #020617,
        #0b1120,
        #020617,
        #111827,
        #020617
    );
    background-size: 400% 400%;
    animation: gradientBG 26s ease infinite;
}
@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Center main content card */
.app-card {
    max-width: 900px;
    margin: 3rem auto;
    padding: 2.5rem 2.8rem;
    border-radius: 24px;
    background: rgba(15, 23, 42, 0.88);
    border: 1px solid rgba(148, 163, 184, 0.5);
    box-shadow: 0 24px 80px rgba(0,0,0,0.85);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    text-align: center;
}

/* Inside card: everything centered + white */
.app-card, .app-card * {
    color: #f9fafb;
    text-align: center !important;
}

/* Stylish title box */
.title-box {
    display: inline-block;
    padding: 0.18rem;
    border-radius: 999px;
    background: linear-gradient(120deg, #ef4444, #f97316, #22c55e);
    margin-bottom: 1.3rem;
}

.title-inner {
    padding: 0.45rem 1.4rem;
    border-radius: 999px;
    background: rgba(15,23,42,0.96);
    font-size: 0.95rem;
    font-weight: 700;
    letter-spacing: 0.18em;
    text-transform: uppercase;
}

/* Main title / subtitle */
.app-title {
    font-size: 2.4rem;
    font-weight: 900;
    margin-bottom: 0.4rem;
}
.app-subtitle {
    font-size: 1.1rem;
    opacity: 0.85;
    margin-bottom: 1.4rem;
}

/* Text input */
.app-card input {
    text-align: center !important;
    background: rgba(15,23,42,0.9) !important;
    border-radius: 12px !important;
    border: 1px solid rgba(148,163,184,0.9) !important;
    padding: 0.6rem 1rem !important;
    font-size: 1.1rem !important;
    color: #f9fafb !important;
}

/* Section heading */
.section-heading {
    font-size: 1.35rem;
    font-weight: 700;
    margin-top: 1.8rem;
}

/* Question text */
.question-text {
    font-size: 1.15rem;
    font-weight: 600;
    margin-top: 1.3rem;
    margin-bottom: 0.4rem;
}

/* Radio buttons container */
.stRadio > div {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.45rem;
}

/* Radio option style */
.stRadio > div > label {
    width: 75%;
    max-width: 600px;
    background: rgba(15,23,42,0.95);
    border-radius: 999px;
    padding: 0.5rem 0.9rem;
    border: 1px solid rgba(148,163,184,0.7);
    font-size: 1.02rem;
    transition: all 0.13s ease;
}
.stRadio > div > label:hover {
    transform: translateY(-1px);
    border-color: rgba(248,250,252,0.9);
}

/* Button */
.stButton > button {
    margin-top: 1.3rem;
    border-radius: 999px;
    padding: 0.7rem 2.4rem;
    border: none;
    font-size: 1.1rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    background: linear-gradient(135deg, #22c55e, #16a34a);
    color: #f9fafb;
    box-shadow: 0 20px 45px rgba(0,0,0,0.9);
}
.stButton > button:hover {
    transform: translateY(-1px);
    filter: brightness(1.08);
}

/* Small note text */
.small-note {
    font-size: 0.85rem;
    opacity: 0.7;
    margin-top: 0.4rem;
}

/* Result card */
.result-card {
    padding: 1.1rem 1.3rem;
    border-radius: 18px;
    margin-top: 1.3rem;
    background: rgba(15,23,42,0.95);
}

/* Vibe meter */
.meter {
    width: 100%;
    max-width: 550px;
    height: 14px;
    border-radius: 999px;
    background: rgba(30,41,59,0.9);
    border: 1px solid rgba(148,163,184,0.8);
    margin: 0.6rem auto 0.2rem auto;
    overflow: hidden;
}
.meter-fill {
    height: 100%;
    border-radius: 999px;
    background: linear-gradient(90deg, #ef4444, #f97316, #eab308, #22c55e);
}

hr {
    border: none;
    border-top: 1px solid rgba(148,163,184,0.5);
    margin: 1.5rem 0;
}

</style>
""", unsafe_allow_html=True)


# ---------- MAIN CARD ----------
st.markdown('<div class="app-card">', unsafe_allow_html=True)

# Stylish title
st.markdown("""
<div class="title-box">
  <div class="title-inner">RED / GREEN FLAG CHECKER</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="app-title">Self Vibe Checker</div>', unsafe_allow_html=True)
st.markdown(
    "<div class='app-subtitle'>Check your own behaviour and see if your vibe is green, yellow, or red flag.</div>",
    unsafe_allow_html=True
)

# ---------- NAME INPUT ----------
name = st.text_input("Enter your name", "")

# ---------- AUTO RED FLAG NAMES ----------
auto_red = ["archit", "ujwal", "mohit", "pranjal", "piyush","angad","anshuman","darshit","gangwar","harshit","shiv","achintya"]

name_lower = name.strip().lower()

if name_lower in auto_red:
    st.markdown(f"""
    <div class="result-card" style="border:1px solid #ef4444;">
        <h2 style="color:#ef4444; font-size:2.2rem; font-weight:900;">🚩 RED FLAG (AUTO DETECTED)</h2>
        <p style="font-size:1.15rem; margin-top:0.4rem;">
            The name <b>{name}</b> is permanently classified as a <b>RED FLAG</b>.  
            No test needed. Behaviour history detected. 😭🔥  
        </p>
        <p class="small-note">(Case-insensitive: MoHIt = mohit = MOHIT)</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

if not name.strip():
    st.markdown("<p class='small-note'>Type your name above to start.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# ---------- QUESTIONS ----------
st.markdown("<div class='section-heading'>Answer honestly 👇</div>", unsafe_allow_html=True)
placeholder = "⬇️ Select one option"

questions = [
    ("Do I respect others' boundaries?", ["Yes", "Sometimes", "No"], [2, 1, 0]),
    ("How do I react to 'No'?", ["Respect it", "Try to convince", "Get angry"], [2, 1, 0]),
    ("Do I make hurtful jokes?", ["Rarely", "Sometimes", "Often"], [2, 1, 0]),
    ("How honest am I?", ["Very honest", "Sometimes lie", "Lie often"], [2, 1, 0]),
    ("How do I handle anger?", ["Calm", "Sometimes lose control", "Lose control often"], [2, 1, 0]),
    ("Do I support my friends?", ["Yes fully", "Neutral", "No / Pull them down"], [2, 1, 0]),
    ("Do I gossip?", ["Rarely", "Sometimes", "Often"], [2, 1, 0]),
    ("How do people feel after meeting me?", ["Better", "Same", "Worse"], [2, 1, 0])
]

answers = []
for i, (q, opts, scores) in enumerate(questions):
    st.markdown(f"<div class='question-text'>Q{i+1}. {q}</div>", unsafe_allow_html=True)
    choice = st.radio("", [placeholder] + opts, index=0, key=f"q{i}")
    answers.append(choice)

st.markdown("<hr>", unsafe_allow_html=True)

# ---------- RESULT ----------
if st.button(f"Show result for {name}"):
    if placeholder in answers:
        st.warning("Please answer all questions.")
    else:
        total = 0
        max_total = len(questions) * 2

        # Scoring
        for ans, (q, opts, scores) in zip(answers, questions):
            index = opts.index(ans)
            total += scores[index]

        ratio = total / max_total
        percent = ratio * 100

        # Classification
        if ratio >= 0.75:
            flag = "GREEN FLAG ✅"
            color = "#22c55e"
            msg = "Emotionally aware, respectful, kind & supportive. Solid green energy."
        elif ratio >= 0.45:
            flag = "YELLOW FLAG ⚠️"
            color = "#eab308"
            msg = "A mix of good and risky behaviour. Can improve with awareness."
        else:
            flag = "RED FLAG 🚩"
            color = "#ef4444"
            msg = "Multiple behaviour issues detected. Time for reflection & change."

        # Result Card
        st.markdown(
            f"""
            <div class="result-card" style="border:1px solid {color};">
                <h2 style="color:{color}; font-size:2.2rem; font-weight:900;">{flag}</h2>
                <p style="font-size:1.05rem;">Score: <b>{total}</b> / {max_total} ({percent:.1f}%)</p>

                <div class="meter">
                    <div class="meter-fill" style="width:{percent}%;"></div>
                </div>
                <p class="small-note">Left = red, Right = green</p>

                <p style="margin-top:0.8rem; font-size:1.05rem;">{msg}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("</div>", unsafe_allow_html=True)

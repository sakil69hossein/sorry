import streamlit as st
import time
import os

# 1. Page Configuration
st.set_page_config(
    page_title="For My Bratati 💖",
    page_icon="🥺",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. State Management
if "stage" not in st.session_state:
    st.session_state.stage = 1

# 3. MAGIC FIX: This function destroys all hidden spaces so Streamlit CANNOT show raw code
def render_html(raw_html):
    # This removes all indentation and forces it into a single line of HTML
    clean_html = "".join([line.strip() for line in raw_html.split("\n")])
    st.markdown(clean_html, unsafe_allow_html=True)

# 4. CSS for Pink Theme & Dark Mode Override
css = """
<style>
/* Force Background Pink even in Dark Mode */
[data-testid="stAppViewContainer"], .stApp {
    background: linear-gradient(135deg, #ffeef5 0%, #ffd6e7 50%, #fff0f5 100%) !important;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

[data-testid="stHeader"] {
    background: transparent !important;
}

@keyframes floatUp {
    0% { transform: translateY(100vh) scale(0.5); opacity: 0; }
    50% { opacity: 0.8; }
    100% { transform: translateY(-10vh) scale(1.2); opacity: 0; }
}

.heart-particle {
    position: fixed;
    color: #ff6b95;
    font-size: 24px;
    z-index: 0;
    pointer-events: none;
    animation: floatUp 7s linear infinite;
}

.pink-card {
    background: rgba(255, 255, 255, 0.9) !important;
    backdrop-filter: blur(10px);
    border: 2px solid #ffccd9;
    border-radius: 24px;
    padding: 30px 24px;
    box-shadow: 0 15px 35px rgba(255, 107, 149, 0.18);
    text-align: center;
    margin-bottom: 25px;
}

.title-text {
    color: #d81b60 !important;
    font-weight: 800;
    font-size: 2.2rem;
    margin-bottom: 10px;
}

.subtitle-text {
    color: #6a1b9a !important;
    font-size: 1.15rem;
    line-height: 1.6;
}

.bengali-text {
    background: linear-gradient(135deg, #c2185b 0%, #880e4f 100%) !important;
    color: #ffffff !important;
    font-size: 1.5rem;
    font-weight: 700;
    line-height: 1.6;
    margin: 20px 0;
    padding: 22px 24px;
    border-radius: 20px;
    box-shadow: 0 10px 25px rgba(136, 14, 79, 0.35);
    border: 1.5px solid rgba(255, 255, 255, 0.25);
}

div.stButton > button {
    background: linear-gradient(135deg, #ff4081, #f50057) !important;
    color: white !important;
    border-radius: 50px;
    font-weight: 700;
    font-size: 1.1rem;
    padding: 12px 28px;
    border: none;
    width: 100%;
    transition: 0.3s;
}

.no-btn div.stButton > button {
    background: #f8bbd0 !important;
    color: #880e4f !important;
    box-shadow: none !important;
}
</style>

<div class="heart-particle" style="left: 10%; animation-delay: 0s;">💖</div>
<div class="heart-particle" style="left: 25%; animation-delay: 2.5s;">🌸</div>
<div class="heart-particle" style="left: 50%; animation-delay: 1.2s;">💕</div>
<div class="heart-particle" style="left: 75%; animation-delay: 3.8s;">💗</div>
<div class="heart-particle" style="left: 90%; animation-delay: 5s;">✨</div>
"""
render_html(css)


# =========================================================
# STAGE 1: Photo Screen
# =========================================================
if st.session_state.stage == 1:
    render_html("""
        <div class="pink-card">
            <div class="title-text">Hey Beautiful... 🌸</div>
            <p class="subtitle-text">There is something from the bottom of my heart for you.<br><b>Tap the button below</b> to see 🥺</p>
        </div>
    """)

    photo_path = "our_photo.jpg"
    if os.path.exists(photo_path):
        st.image(photo_path, use_container_width=True, caption="Our Special Memory 💖")
    else:
        st.info("💡 Place your picture as `our_photo.jpg` in this folder to display it here!")
        render_html('<div style="font-size: 80px; text-align: center; margin: 20px 0;">📸 👩‍❤️‍👨 🌸</div>')

    st.write("")
    if st.button("👉 Tap Here to Open My Message 💌"):
        st.session_state.stage = 2
        st.rerun()


# =========================================================
# STAGE 2: Apology Page
# =========================================================
elif st.session_state.stage == 2:
    render_html("""
        <div class="pink-card">
            <div style="font-size: 70px;">🥺💔</div>
            <div class="title-text">I'm Really Sorry, Bratati...</div>
            <p class="subtitle-text" style="font-size: 1.25rem; font-weight: 600; color: #c2185b !important;">
                "I know I made a mistake, and hurting you is the absolute last thing I ever want to do in this world."
            </p>
            <div style="margin: 20px 0; font-size: 35px;">😭 🥀 🕊️ 💗</div>
            <p class="subtitle-text">
                Every second you are upset with me feels completely empty. You mean everything to me, and my smile only exists when you are smiling with me.
            </p>
            <hr style="border: 1px dashed #f48fb1; margin: 20px 0;">
            <p style="font-size: 1.4rem; color: #e91e63 !important; font-weight: 800;">
                I Love You So Much, Bratati. Always and Forever. 💖💍
            </p>
        </div>
    """)

    if st.button("Continue... 🥺👉"):
        st.session_state.stage = 3
        st.rerun()


# =========================================================
# STAGE 3: Bengali Apology
# =========================================================
elif st.session_state.stage == 3:
    render_html("""
        <div class="pink-card">
            <div style="font-size: 75px;">🥺🙏</div>
            
            <div class="bengali-text">
                "তোমাকে রাগানোর জন্য আমি সত্যিই খুব দুঃখিত... প্লিজ আর রাগ করে থেকো না।" 💔
            </div>
            
            <p class="subtitle-text" style="margin-top: 15px;">
                আমার ভুল হয়ে গেছে সোনা... তোমার এই রাগি মুখটা আর দেখতে পারছি না 😭
            </p>
            
            <h3 style="color: #ad1457 !important; margin-top: 25px; font-weight: 800;">
                Will you please forgive me? 🥺
            </h3>
        </div>
    """)

    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button("Yes, I forgive you! 💕"):
            st.session_state.stage = 4
            st.rerun()

    with col2:
        render_html('<div class="no-btn">')
        if st.button("No 😤"):
            st.toast("Nope! 'No' is not an option... Going back until you forgive me! 🥺😭", icon="❌")
            time.sleep(1.2)
            st.session_state.stage = 2
            st.rerun()
        render_html('</div>')


# =========================================================
# STAGE 4: Final Celebration
# =========================================================
elif st.session_state.stage == 4:
    st.balloons()
    st.snow()

    render_html("""
        <div class="pink-card">
            <div style="font-size: 80px;">🥰🎉</div>
            <div class="title-text" style="color: #c2185b !important;">
                Thank you Bratati! Love you so much 😘💖
            </div>
            
            <div class="bengali-text">
                "থ্যাঙ্ক ইউ আমার মিষ্টি বউটা! এবার তো একটু মিষ্টি করে হাসো? 🥰✨"
            </div>
            
            <div style="font-size: 40px; margin: 20px 0;">💐 🍫 🧸 🍧 💋</div>
            <p class="subtitle-text" style="font-weight: 600;">
                I promise to take extra care of your heart from now on. Now send me a cute selfie with a smile! 📸✨
            </p>
        </div>
    """)

    if st.button("Restart from Beginning 🔁"):
        st.session_state.stage = 1
        st.rerun()
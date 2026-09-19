import streamlit as st
from google import genai

# =========================================================
# 1. PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="আদর্শ প্রাইভেট কেয়ার",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# 2. CUSTOM CSS (প্রিমিয়াম কালার কম্বিনেশন ও ব্যাকগ্রাউন্ড)
# =========================================================
st.markdown(
    """
    <style>
    /* Main application background */
    .stApp {
        background: linear-gradient(135deg, #f5f9ff 0%, #eef5ff 100%);
    }

    /* Sidebar background */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #101d4f 0%, #182b72 100%);
    }

    section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] h2, 
    section[data-testid="stSidebar"] h3, 
    section[data-testid="stSidebar"] p, 
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] label {
        color: white !important;
    }

    /* Hero section */
    .hero {
        background: linear-gradient(135deg, #172b72, #3155b8);
        padding: 35px;
        border-radius: 22px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
    }

    .hero h1 {
        color: white !important;
        font-size: 40px;
        font-weight: 800;
        margin-bottom: 10px;
    }

    .hero p {
        color: #e8eeff !important;
        font-size: 18px;
        line-height: 1.7;
    }

    /* Cards design */
    .card {
        background: white;
        padding: 25px;
        border-radius: 18px;
        margin-bottom: 20px;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.07);
        border: 1px solid #e5eaf5;
    }

    .card h3 {
        color: #172b72;
        margin-top: 0;
    }

    .card p {
        color: #4a5568;
        line-height: 1.7;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 10px;
        font-weight: 600;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #68748a;
        padding: 30px 10px;
        margin-top: 30px;
    }

    @media (max-width: 768px) {
        .hero { padding: 25px; }
        .hero h1 { font-size: 30px; }
        .hero p { font-size: 16px; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# 3. GEMINI API CONFIGURATION
# =========================================================
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
except Exception:
    API_KEY = ""

client = None
if API_KEY:
    try:
        client = genai.Client(api_key=API_KEY)
    except Exception:
        client = None

# =========================================================
# 4. SIDEBAR (লোগো, ঠিকানা ও সোশ্যাল মিডিয়া লিঙ্ক)
# =========================================================
with st.sidebar:
    # -----------------------------------------------------
    # LOGO
    # -----------------------------------------------------
    try:
        st.image("logo.png", use_container_width=True)
    except Exception:
        st.markdown(
            """
            <div style="text-align:center; font-size:60px; padding:20px;">
                🎓
            </div>
            """,
            unsafe_allow_html=True
        )

    # -----------------------------------------------------
    # NAME & SLOGAN
    # -----------------------------------------------------
    st.markdown(
        """
        <div style="text-align:center; padding:5px;">
            <h2 style="margin-bottom:5px;">আদর্শ প্রাইভেট কেয়ার</h2>
            <p style="color:#dce5ff; margin-top:5px;">গুণগত শিক্ষা, উজ্জ্বল ভবিষ্যৎ</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # -----------------------------------------------------
    # CONTACT INFO
    # -----------------------------------------------------
    st.subheader("📞 যোগাযোগ")
    st.markdown(
        """
        📍 **স্থান:** ঢাকা, বাংলাদেশ  
        📱 **মোবাইল:** 01XXXXXXXXX  
        ✉️ **Email:** example@gmail.com
        """
    )

    st.divider()

    # -----------------------------------------------------
    # SOCIAL MEDIA LINKS
    # -----------------------------------------------------
    st.subheader("🌐 সোশ্যাল মিডিয়া")

    # YouTube Channel
    st.markdown(
        """
        <a href="https://www.youtube.com/channel/UC0_gzD3mlN1O1FhjTu2Qkzg" target="_blank" style="display:block; background:#ff0000; color:white; padding:12px; margin:8px 0; border-radius:10px; text-align:center; text-decoration:none; font-weight:bold;">
            🎥 YouTube Channel
        </a>
        """,
        unsafe_allow_html=True
    )

    # Facebook Profile
    st.markdown(
        """
        <a href="https://www.facebook.com/share/1DHesGeakU/" target="_blank" style="display:block; background:#1877f2; color:white; padding:12px; margin:8px 0; border-radius:10px; text-align:center; text-decoration:none; font-weight:bold;">
            👤 Facebook Profile
        </a>
        """,
        unsafe_allow_html=True
    )

    st.divider()
    st.caption("© 2026 আদর্শ প্রাইভেট কেয়ার")

# =========================================================
# 5. HERO SECTION
# =========================================================
st.markdown(
    """
    <div class="hero">
        <h1>🎓 আদর্শ প্রাইভেট কেয়ার</h1>
        <p>আধুনিক প্রযুক্তি ও মানসম্মত শিক্ষার সমন্বয়ে শিক্ষার্থীদের জন্য একটি সুন্দর ডিজিটাল শিক্ষা প্ল্যাটফর্ম।</p>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# 6. MAIN TABS
# =========================================================
tab1, tab2, tab3 = st.tabs(
    [
        "🏠 হোম",
        "🤖 AI স্টাডি অ্যাসিস্ট্যান্ট",
        "📚 আমাদের সম্পর্কে"
    ]
)

# =========================================================
# 7. HOME TAB
# =========================================================
with tab1:
    st.header("স্বাগতম! 👋")
    st.write("আপনার পড়াশোনাকে আরও সহজ, সুন্দর ও কার্যকর করার জন্য আদর্শ প্রাইভেট কেয়ারের অনলাইন লার্নিং পোর্টালে আপনাকে স্বাগতম।")
    
    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="card">
                <h3>📚 কোর্সসমূহ</h3>
                <p>পঞ্চম থেকে দশম শ্রেণির শিক্ষার্থীদের জন্য বিভিন্ন বিষয়ের কোর্স।</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="card">
                <h3>🧮 গণিত</h3>
                <p>কঠিন গণিত সহজভাবে শেখার জন্য নিয়মিত অনুশীলন ও সহায়তা।</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="card">
                <h3>📖 ইংরেজি</h3>
                <p>Grammar, Writing, Reading এবং Vocabulary শেখার সুযোগ।</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.subheader("📢 বিশেষ ঘোষণা")
    st.info("🎉 নতুন ব্যাচে ভর্তি চলছে! ভর্তি ও বিস্তারিত তথ্যের জন্য আমাদের সাথে যোগাযোগ করুন।")

    st.subheader("⭐ আমাদের সুবিধা")
    feature1, feature2 = st.columns(2)

    with feature1:
        st.success("✅ অভিজ্ঞ শিক্ষক")
        st.success("✅ নিয়মিত পরীক্ষা")
        st.success("✅ সহজ ভাষায় পাঠদান")

    with feature2:
        st.success("✅ ডিজিটাল শিক্ষা")
        st.success("✅ AI Study Assistant")
        st.success("✅ শিক্ষার্থীবান্ধব পরিবেশ")

# =========================================================
# 8. AI STUDY ASSISTANT TAB (GEMINI AI CHATBOT)
# =========================================================
with tab2:
    st.header("🤖 আপনার AI Tutor")
    st.write("গণিত, ইংরেজি, বিজ্ঞান অথবা যেকোনো পড়াশোনার প্রশ্ন করুন। AI আপনাকে সহজভাবে বুঝিয়ে দেবে।")

    clear_col1, clear_col2 = st.columns([5, 1])
    with clear_col2:
        if st.button("🗑️ চ্যাট মুছুন", use_container_width=True):
            st.session_state.messages = []
            st.rerun()

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if len(st.session_state.messages) == 0:
        st.markdown(
            """
            <div class="card">
                <h3>👋 আসসালামু আলাইকুম!</h3>
                <p>আমি আদর্শ প্রাইভেট কেয়ারের AI Study Tutor।</p>
                <p>আপনি আমাকে গণিত, ইংরেজি, বিজ্ঞান, সাধারণ জ্ঞান অথবা যেকোনো পড়াশোনার প্রশ্ন করতে পারেন।</p>
                <p><b>উদাহরণ:</b></p>
                <ul>
                    <li>ভগ্নাংশ কীভাবে বুঝব?</li>
                    <li>Present Perfect Tense বুঝিয়ে দাও।</li>
                    <li>Photosynthesis কী?</li>
                    <li>2x + 5 = 15 সমাধান করো।</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("📚 আপনার পড়াশোনার প্রশ্ন এখানে লিখুন...")

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        if not API_KEY:
            answer = "⚠️ Gemini API Key পাওয়া যায়নি। Streamlit Secrets-এ GEMINI_API_KEY যোগ করুন।"
            with st.chat_message("assistant"):
                st.warning(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})

        elif client is None:
            answer = "⚠️ Gemini Client তৈরি করা যায়নি। আপনার API Key পরীক্ষা করুন।"
            with st.chat_message("assistant"):
                st.error(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})

        else:
            try:
                system_instruction = (
                    "আপনি আদর্শ প্রাইভেট কেয়ারের একজন সহায়ক AI Tutor।\n"
                    "শিক্ষার্থীদের সহজ ও সুন্দর বাংলায় পড়াবেন।\n"
                    "নিয়ম:\n"
                    "১. কঠিন বিষয় সহজ ভাষায় ব্যাখ্যা করবেন।\n"
                    "২. গণিত হলে ধাপে ধাপে সমাধান দেখাবেন।\n"
                    "৩. ইংরেজি হলে বাংলা ব্যাখ্যা ও উদাহরণ দেবেন।\n"
                    "৪. শুধু উত্তর না দিয়ে বিষয়টি বুঝিয়ে শেখাবেন।\n"
                    "৫. শিক্ষার্থীর বয়স উপযোগী ভাষা ব্যবহার করবেন।"
                )

                # চ্যাট হিস্ট্রি গুছিয়ে তৈরি করা
                contents = []
                for msg in st.session_state.messages:
                    role = "user" if msg["role"] == "user" else "model"
                    contents.append({
                        "role": role,
                        "parts": [{"text": msg["content"]}]
                    })

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=contents,
                    config={"system_instruction": system_instruction}
                )

                answer = response.text

                with st.chat_message("assistant"):
                    st.markdown(answer)

                st.session_state.messages.append({"role": "assistant", "content": answer})

            except Exception as e:
                error_message = f"❌ AI থেকে উত্তর পাওয়া যায়নি। Error: {str(e)}"
                with st.chat_message("assistant"):
                    st.error(error_message)
                st.session_state.messages.append({"role": "assistant", "content": error_message})

# =========================================================
# 9. ABOUT TAB
# =========================================================
with tab3:
    st.header("📚 আমাদের সম্পর্কে")
    st.markdown(
        """
        <div class="card">
            <h3>🎓 আদর্শ প্রাইভেট কেয়ার</h3>
            <p>আদর্শ প্রাইভেট কেয়ার শিক্ষার্থীদের মানসম্মত শিক্ষা, নিয়মিত অনুশীলন এবং আধুনিক প্রযুক্তিনির্ভর শিক্ষা প্রদানের লক্ষ্যে কাজ করে।</p>
            <p>আমাদের লক্ষ্য হলো শিক্ষার্থীদের পড়াশোনাকে আরও সহজ, আনন্দদায়ক এবং কার্যকর করে তোলা।</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("🎯 আমাদের লক্ষ্য")
    about_col1, about_col2 = st.columns(2)
    with about_col1:
        st.success("📖 মানসম্মত শিক্ষা")
        st.success("👨‍🏫 দক্ষ শিক্ষক")
        st.success("📝 নিয়মিত পরীক্ষা")
    with about_col2:
        st.success("💻 ডিজিটাল শিক্ষা")
        st.success("🤖 AI সহায়তা")
        st.success("🌱 শিক্ষার্থীর উন্নয়ন")

# =========================================================
# 10. FOOTER
# =========================================================
st.markdown(
    """
    <div class="footer">
        <hr>
        🎓 <b>আদর্শ প্রাইভেট কেয়ার</b><br><br>
        গুণগত শিক্ষা, উজ্জ্বল ভবিষ্যৎ 🌱<br><br>
        © 2026 আদর্শ প্রাইভেট কেয়ার | All Rights Reserved
    </div>
    """,
    unsafe_allow_html=True
)

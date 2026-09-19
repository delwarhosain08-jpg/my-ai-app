import streamlit as st
from google import genai

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="আদর্শ প্রাইভেট কেয়ার",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #f5f9ff 0%, #eef5ff 100%);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #101d4f 0%, #182b72 100%);
}

section[data-testid="stSidebar"] * {
    color: white;
}

/* Hero */
.hero {
    background: linear-gradient(135deg, #172b72, #3155b8);
    padding: 35px;
    border-radius: 22px;
    color: white;
    margin-bottom: 25px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.15);
}

.hero h1 {
    color: white;
    font-size: 38px;
    font-weight: 800;
}

.hero p {
    color: #e8eeff;
    font-size: 18px;
}

/* Cards */
.card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    margin-bottom: 20px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.07);
    border: 1px solid #e5eaf5;
}

.card h3 {
    color: #172b72;
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
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# GEMINI API KEY
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
# SIDEBAR
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
            <div style="
                text-align:center;
                font-size:60px;
                padding:20px;
            ">
                🎓
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div style="text-align:center; padding:5px;">
            <h2 style="margin-bottom:5px;">
                আদর্শ প্রাইভেট কেয়ার
            </h2>

            <p style="color:#dce5ff;">
                গুণগত শিক্ষা, উজ্জ্বল ভবিষ্যৎ
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # -----------------------------------------------------
    # CONTACT
    # -----------------------------------------------------

    st.subheader("📞 যোগাযোগ")

    st.markdown("""
    📍 **স্থান:** ঢাকা, বাংলাদেশ

    📱 **মোবাইল:** 01XXXXXXXXX

    ✉️ **Email:** example@gmail.com
    """)

    st.divider()

    # -----------------------------------------------------
    # SOCIAL MEDIA
    # -----------------------------------------------------

    st.subheader("🌐 সোশ্যাল মিডিয়া")

    st.markdown(
        """
        <a href="https://www.youtube.com/channel/UC0_gzD3mlN1O1FhjTu2Qkzg"
        target="_blank"
        style="
        display:block;
        background:#ff0000;
        color:white;
        padding:12px;
        margin:8px 0;
        border-radius:10px;
        text-align:center;
        text-decoration:none;
        font-weight:bold;
        ">
        🎥 YouTube Channel
        </a>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <a href="https://www.facebook.com/share/1DHesGeakU/"
        target="_blank"
        style="
        display:block;
        background:#1877f2;
        color:white;
        padding:12px;
        margin:8px 0;
        border-radius:10px;
        text-align:center;
        text-decoration:none;
        font-weight:bold;
        ">
        👤 Facebook Profile
        </a>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.caption("© 2026 আদর্শ প্রাইভেট কেয়ার")


# =========================================================
# HERO SECTION
# =========================================================

st.markdown(
    """
    <div class="hero">

        <h1>🎓 আদর্শ প্রাইভেট কেয়ার</h1>

        <p>
        আধুনিক প্রযুক্তি ও মানসম্মত শিক্ষার সমন্বয়ে
        শিক্ষার্থীদের জন্য একটি সুন্দর ডিজিটাল শিক্ষা প্ল্যাটফর্ম।
        </p>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# TABS
# =========================================================

tab1, tab2, tab3 = st.tabs([
    "🏠 হোম",
    "🤖 AI স্টাডি অ্যাসিস্ট্যান্ট",
    "📚 আমাদের সম্পর্কে"
])


# =========================================================
# HOME
# =========================================================

with tab1:

    st.header("স্বাগতম! 👋")

    st.write(
        "আপনার পড়াশোনাকে আরও সহজ, সুন্দর ও কার্যকর করার জন্য "
        "আদর্শ প্রাইভেট কেয়ারের অনলাইন লার্নিং পোর্টালে আপনাকে স্বাগতম।"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="card">
                <h3>📚 কোর্সসমূহ</h3>
                <p>
                পঞ্চম থেকে দশম শ্রেণির শিক্ষার্থীদের
                জন্য বিভিন্ন বিষয়ের কোর্স।
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="card">
                <h3>🧮 গণিত</h3>
                <p>
                কঠিন গণিত সহজভাবে শেখার
                ব্যবস্থা।
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="card">
                <h3>📖 ইংরেজি</h3>
                <p>
                Grammar, Writing, Reading এবং
                Vocabulary শেখার সুযোগ।
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.subheader("📢 বিশেষ ঘোষণা")

    st.info(
        "🎉 নতুন ব্যাচে ভর্তি চলছে! "
        "ভর্তি ও বিস্তারিত তথ্যের জন্য আমাদের সাথে যোগাযোগ করুন।"
    )

    st.subheader("⭐ আমাদের সুবিধা")

    c1, c2 = st.columns(2)

    with c1:
        st.success("✅ অভিজ্ঞ শিক্ষক")
        st.success("✅ নিয়মিত পরীক্ষা")
        st.success("✅ সহজ ভাষায় পাঠদান")

    with c2:
        st.success("✅ ডিজিটাল শিক্ষা")
        st.success("✅ AI Study Assistant")
        st.success("✅ শিক্ষার্থীবান্ধব পরিবেশ")


# =========================================================
# AI STUDY ASSISTANT
# =========================================================

with tab2:

    st.header("🤖 আপনার AI Tutor")

    st.write(
        "গণিত, ইংরেজি, বিজ্ঞান অথবা যেকোনো পড়াশোনার "
        "প্রশ্ন করুন। AI আপনাকে সহজভাবে বুঝিয়ে দেবে।"
    )

    # Chat clear button
    if st.button("🗑️ চ্যাট মুছে ফেলুন"):

        st.session_state.messages = []

        st.rerun()

    # Chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Old messages
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

    # Chat input
    prompt = st.chat_input(
        "📚 আপনার প্রশ্ন এখানে লিখুন..."
    )

    if prompt:

        # User message
        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })

        with st.chat_message("user"):
            st.markdown(prompt)

        # Check API
        if not API_KEY:

            answer = """
⚠️ Gemini API Key পাওয়া যায়নি।

Streamlit Cloud-এ:

**Manage app → Settings → Secrets**

এ গিয়ে নিচেরটি যোগ করুন:

```toml
GEMINI_API_KEY = "আপনার_API_KEY"

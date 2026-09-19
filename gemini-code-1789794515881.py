import streamlit as st

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
# 2. CUSTOM CSS
# =========================================================
st.markdown(
    """
    <style>
    /* Main application background */
    .stApp {
        background: linear-gradient(135deg, #f5f9ff 0%, #eef5ff 100%);
    }

    /* Sidebar background (পরিবর্তিত কালার শেড) */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1f4068 0%, #162447 100%);
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

    /* Cards */
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
# 3. SIDEBAR (লোগো, ঠিকানা ও সোশ্যাল মিডিয়া)
# =========================================================
with st.sidebar:
    try:
        st.image("1000038219.png", use_container_width=True)
    except Exception:
        st.markdown(
            """
            <div style="text-align:center; font-size:60px; padding:20px;">
                🎓
            </div>
            """,
            unsafe_allow_html=True
        )

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

    st.subheader("📞 যোগাযোগ")
    st.markdown(
        """
        📍 **স্থান:** ঢাকা, বাংলাদেশ  
        📱 **মোবাইল:** 01734165721, 01563148910  
        ✉️ **Email:** delwarhosain08@gmail.com
        """
    )

    st.divider()

    st.subheader("🌐 সোশ্যাল মিডিয়া")

    st.markdown(
        """
        <a href="https://www.youtube.com/channel/UC0_gzD3mlN1O1FhjTu2Qkzg" target="_blank" style="display:block; background:#ff0000; color:white; padding:12px; margin:8px 0; border-radius:10px; text-align:center; text-decoration:none; font-weight:bold;">
            🎥 YouTube Channel
        </a>
        <a href="https://www.facebook.com/share/1DHesGeakU/" target="_blank" style="display:block; background:#1877f2; color:white; padding:12px; margin:8px 0; border-radius:10px; text-align:center; text-decoration:none; font-weight:bold;">
            👤 Facebook Profile
        </a>
        """,
        unsafe_allow_html=True
    )

    st.divider()
    st.caption("© 2026 আদর্শ প্রাইভেট কেয়ার")

# =========================================================
# 4. HERO SECTION
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
# 5. MAIN TABS (AI বাদ দিয়ে স্টুডেন্ট চ্যাট রুম যোগ করা হয়েছে)
# =========================================================
tab1, tab2, tab3 = st.tabs(
    [
        "🏠 হোম",
        "💬 শিক্ষার্থী চ্যাট রুম",
        "📚 আমাদের সম্পর্কে"
    ]
)

# =========================================================
# 6. HOME TAB
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
        st.success("✅ শিক্ষার্থীবান্ধব পরিবেশ")
        st.success("✅ নিয়মিত গাইডলাইন")

# =========================================================
# 7. STUDENT CHAT ROOM TAB (শিক্ষার্থীদের নিজেদের মধ্যে আলোচনার জন্য)
# =========================================================
with tab2:
    st.header("💬 শিক্ষার্থী আলোচনা ও চ্যাট রুম")
    st.write("এখানে শিক্ষার্থীরা তাদের পড়াশোনা সংক্রান্ত বিষয় নিয়ে নিজেদের মধ্যে আলোচনা ও বার্তা আদান-প্রদান করতে পারবে।")

    # চ্যাট হিস্ট্রি স্টোরেজ ইনিশিয়ালাইজেশন
    if "student_messages" not in st.session_state:
        st.session_state.student_messages = [
            {"name": "শিক্ষক মহোদয়", "text": "সবাইকে আদর্শ প্রাইভেট কেয়ার চ্যাট রুমে স্বাগতম! পড়ালেখার বিষয়ে এখানে আলোচনা করতে পারো।"}
        ]

    # মেসেজ ইনপুট ফর্ম
    with st.form("chat_form", clear_on_submit=True):
        col_name, col_msg = st.columns([1, 2])
        with col_name:
            student_name = st.text_input("আপনার নাম ও শ্রেণী:", placeholder="যেমন: রাহিম (নবম শ্রেণি)")
        with col_msg:
            student_text = st.text_input("আপনার বার্তা বা প্রশ্ন:", placeholder="এখানে কিছু লিখুন...")
        
        submit_btn = st.form_submit_button("📤 বার্তা পাঠান")

        if submit_btn:
            if student_name.strip() and student_text.strip():
                st.session_state.student_messages.append({
                    "name": student_name,
                    "text": student_text
                })
                st.success("আপনার বার্তাটি সফলভাবে যুক্ত হয়েছে!")
            else:
                st.warning("দয়া করে নাম এবং বার্তা উভয়ই পূরণ করুন।")

    st.divider()
    st.subheader("📜 সাম্প্রতিক আলোচনা:")

    # মেসেজগুলো নিচ থেকে উপরে বা উপর থেকে নিচে দেখানোর জন্য
    for msg in reversed(st.session_state.student_messages):
        st.markdown(
            f"""
            <div style="background: white; padding: 15px; border-radius: 12px; margin-bottom: 10px; border-left: 5px solid #172b72; box-shadow: 0 2px 5px rgba(0,0,0,0.05);">
                <b>👤 {msg['name']}</b><br>
                <p style="margin: 5px 0 0 0; color: #333;">{msg['text']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================================================
# 8. ABOUT TAB
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
        st.success("🌱 শিক্ষার্থীর উন্নয়ন")

# =========================================================
# 9. FOOTER
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

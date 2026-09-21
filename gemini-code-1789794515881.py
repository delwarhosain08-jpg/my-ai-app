import streamlit as st
from supabase import create_client, Client

# =========================================================
# 1. SUPABASE CONNECTION (অনলাইন ডাটাবেজ কানেকশন)
# =========================================================
SUPABASE_URL = "mbmgebvnxwnvbiwjipbk"
SUPABASE_KEY = "sb_publishable_qb0mb9W7_9jfIsbkaDz_EQ_xLqegm5s"

try:
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
except Exception:
    supabase = None

# =========================================================
# 2. PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="আদর্শ প্রাইভেট কেয়ার",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# 3. CUSTOM CSS (স্টাইল ও ডিজাইন)
# =========================================================
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #f5f9ff 0%, #eef5ff 100%);
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1f4068 0%, #162447 100%);
    }

    section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] h2, 
    section[data-testid="stSidebar"] h3, 
    section[data-testid="stSidebar"] p, 
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] a {
        color: white !important;
    }

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

    .card {
        background: white;
        padding: 25px;
        border-radius: 18px;
        margin-bottom: 20px;
        box-shadow: 0 5px 20px rgba(0, 0, 0,0.07);
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

    .footer {
        text-align: center;
        color: #68748a;
        padding: 30px 10px;
        margin-top: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# 4. SIDEBAR (লোগো, যোগাযোগ ও সোশ্যাল মিডিয়া লিংক)
# =========================================================
with st.sidebar:
    try:
        st.image("logo.png", use_container_width=True)
    except Exception:
        st.markdown("<div style='text-align:center; font-size:60px;'>🎓</div>", unsafe_allow_html=True)

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
    st.markdown("📍 **স্থান:** ঢাকা, বাংলাদেশ\n📱 **মোবাইল:** 01734165721\n✉️ **Email:** info@adarshaprivatecare.com")
    
    st.divider()
    st.subheader("🌐 সোশ্যাল মিডিয়া ও ইউটিউব")
    # এখানে আপনার ফেসবুক পেজ বা গ্রুপ এবং ইউটিউব চ্যানেলের আসল লিংক বসিয়ে দেবেন
    st.markdown(
        """
        st.markdown(
    """
    - 📘 **[আমাদের ফেসবুক পেজ]("https://www.facebook.com/share/1J55ZjGBqT/" target="_blank" style="display:block; background:#1877f2; color:white; padding:12px; margin:8px 0; border-radius:10px; text-align:center; text-decoration:none; font-weight:bold;">
            👤 Facebook Profile
)**
    - 🔴 **[আমাদের ইউটিউব চ্যানেল]("https://www.youtube.com/channel/UC0_gzD3mlN1O1FhjTu2Qkzg" target="_blank" style="display:block; background:#ff0000; color:white; padding:12px; margin:8px 0; border-radius:10px; text-align:center; text-decoration:none; font-weight:bold;">
            🎥 YouTube Channel
)**
    """,
    unsafe_allow_html=True
)
)
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
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "🏠 হোম ও নোটিশ",
        "📚 কোর্স ও সাজেশন",
        "💬 শিক্ষার্থী চ্যাট রুম",
        "⚙️ শিক্ষক/এডমিন প্যানেল",
        "📖 আমাদের সম্পর্কে"
    ]
)

# =========================================================
# 7. HOME & NOTICE TAB (হোম ও নোটিশ বোর্ড)
# =========================================================
with tab1:
    st.header("স্বাগতম! 👋")
    st.write("আপনার পড়াশোনাকে আরও সহজ এবং কার্যকর করতে আদর্শ প্রাইভেট কেয়ারের অনলাইন পোর্টালে স্বাগতম।")
    
    st.divider()
    st.subheader("📢 জরুরি নোটিশ ও আপডেট বোর্ড")
    
    if supabase:
        try:
            response = supabase.table("notices").select("*").order("id", desc=True).execute()
            notices = response.data
            if notices:
                for notice in notices:
                    st.markdown(
                        f"""
                        <div class="card">
                            <h3>{notice.get('title')}</h3>
                            <p>{notice.get('description')}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
            else:
                st.info("বর্তমানে কোনো নতুন নোটিশ নেই।")
        except Exception:
            st.info("নোটিশ লোড করতে সমস্যা হচ্ছে।")
    else:
        st.warning("ডাটাবেজ কানেকশন কনফিগার করা হয়নি।")

# =========================================================
# 8. COURSES & SUGGESTIONS TAB
# =========================================================
with tab2:
    st.header("📚 আমাদের কোর্সসমূহ ও সাজেশন")
    selected_class = st.selectbox(
        "শ্রেণি নির্বাচন করুন:",
        ["ষষ্ঠ শ্রেণি", "সপ্তম শ্রেণি", "অষ্টম শ্রেণি", "নবম-দশম শ্রেণি"]
    )
    st.divider()
    if selected_class == "নবম-দশম শ্রেণি":
        st.subheader("🔥 নবম-দশম শ্রেণির কোর্স ও সাজেশন")
        with st.expander("📐 গণিত কোর্স ও সাজেশন"):
            st.markdown("- **অধ্যায় ৩:** বীজগণিতীয় রাশি")
            st.markdown("- **অধ্যায় ৯:** ত্রিকোণমিতি")
    else:
        st.subheader(f"📖 {selected_class} এর পঠ্যসূচি")
        st.write("খুব শীঘ্রই আপডেট করা হবে।")

# =========================================================
# 9. STUDENT CHAT ROOM TAB (রিয়েল-টাইম চ্যাট)
# =========================================================
with tab3:
    st.header("💬 শিক্ষার্থী আলোচনা ও চ্যাট রুম")
    st.write("এখানে শিক্ষার্থীরা নিজেদের মধ্যে পড়ালেখা নিয়ে রিয়েল-টাইমে চ্যাট করতে পারবে।")
    
    with st.form("chat_form", clear_on_submit=True):
        col_name, col_msg = st.columns([1, 2])
        with col_name:
            student_name = st.text_input("আপনার নাম ও শ্রেণী:", placeholder="যেমন: রাহিম (নবম)")
        with col_msg:
            student_text = st.text_input("আপনার বার্তা বা প্রশ্ন:", placeholder="এখানে লিখুন...")
        
        submit_btn = st.form_submit_button("📤 বার্তা পাঠান")

        if submit_btn:
            if student_name.strip() and student_text.strip() and supabase:
                try:
                    supabase.table("messages").insert({
                        "name": student_name,
                        "message": student_text
                    }).execute()
                    st.success("বার্তা পাঠানো হয়েছে!")
                    st.rerun()
                except Exception:
                    st.error("বার্তা পাঠাতে সমস্যা হয়েছে।")
            else:
                st.warning("নাম এবং বার্তা উভয়ই লিখুন অথবা ডাটাবেজ চেক করুন।")

    st.divider()
    
    if supabase:
        try:
            chat_res = supabase.table("messages").select("*").order("id", desc=True).limit(20).execute()
            messages = chat_res.data
            if messages:
                for msg in messages:
                    st.markdown(
                        f"""
                        <div style="background: white; padding: 12px; border-radius: 10px; margin-bottom: 8px; border-left: 4px solid #172b72;">
                            <b>👤 {msg.get('name')}</b><br>
                            <p style="margin: 4px 0 0 0; color: #333;">{msg.get('message')}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
            else:
                st.info("এখনো কোনো চ্যাট নেই। প্রথম বার্তাটি আপনি পাঠান!")
        except Exception:
            st.warning("চ্যাট লোড করা যাচ্ছে না।")

# =========================================================
# 10. ADMIN PANEL (এডমিন প্যানেল)
# =========================================================
with tab4:
    st.header("⚙️ শিক্ষক/এডমিন প্যানেল")
    st.warning("🔒 এই সেকশনটি শুধু আপনার (শিক্ষক) ব্যবহারের জন্য। এখান থেকে নোটিশ প্রকাশ করলে তা সব শিক্ষার্থীর ডিভাইসে সাথে সাথে দেখা যাবে।")

    with st.form("admin_form", clear_on_submit=True):
        notice_title = st.text_input("নোটিশের শিরোনাম:", placeholder="যেমন: আগামীকালের কোচিং বন্ধ সংক্রান্ত")
        notice_desc = st.text_area("বিস্তারিত বিবরণ:", placeholder="এখানে বিস্তারিত লিখুন...")
        admin_submit = st.form_submit_button("📢 নোটিশ প্রকাশ করুন")

        if admin_submit:
            if notice_title.strip() and notice_desc.strip() and supabase:
                try:
                    supabase.table("notices").insert({
                        "title": notice_title,
                        "description": notice_desc
                    }).execute()
                    st.success("সফলভাবে নোটিশ প্রকাশ করা হয়েছে!")
                    st.rerun()
                except Exception:
                    st.error("নোটিশ প্রকাশ করতে সমস্যা হয়েছে।")
            else:
                st.error("সবগুলো ঘর পূরণ করুন।")

# =========================================================
# 11. ABOUT TAB
# =========================================================
with tab5:
    st.header("📚 আমাদের সম্পর্কে")
    st.markdown(
        """
        <div class="card">
            <h3>🎓 আদর্শ প্রাইভেট কেয়ার</h3>
            <p>শিক্ষার্থীদের মানসম্মত শিক্ষা ও ডিজিটাল সেবা প্রদানের জন্য আমরা প্রতিশ্রুতিবদ্ধ।</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# 12. FOOTER
# =========================================================
st.markdown(
    """
    <div class="footer">
        <hr>
        🎓 <b>আদর্শ প্রাইভেট কেয়ার</b><br>
        গুণগত শিক্ষা, উজ্জ্বল ভবিষ্যৎ 🌱<br>
        © 2026 All Rights Reserved
    </div>
    """,
    unsafe_allow_html=True
)

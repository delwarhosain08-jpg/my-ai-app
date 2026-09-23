import streamlit as __st
import datetime as __dt
from supabase import create_client as __cc, Client as __cl

# Page Configuration
__st.set_page_config(
    page_title="আর্দশ প্রাইভেট কেয়ার",
    page_icon="📚",
    layout="wide"
)

# Custom Styling for Text Visibility & Branding
__st.markdown("""
<style>
    /* Global Text and Background Contrast Fix */
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    h1, h2, h3, h4, h5, h6, p, span, label {
        color: #ffffff !important;
    }
    .stTextInput input, .stTextArea textarea, .stSelectbox select {
        color: #000000 !important;
        background-color: #ffffff !important;
    }
    /* Notice Board Box Styling */
    .notice-card {
        background-color: #1e293b;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #3b82f6;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# Supabase Configuration
# (আপনার সুপাবেস প্রজেক্টের ইউআরএল এবং কি এখানে বসাতে হবে)
SUPABASE_URL = "YOUR_SUPABASE_URL"
SUPABASE_KEY = "YOUR_SUPABASE_KEY"

@__st.cache_resource
def init_supabase() -> __cl:
    return __cc(SUPABASE_URL, SUPABASE_KEY)

try:
    supabase = init_supabase()
except Exception as e:
    __st.error(f"Database connection error: {e}")

# Header Section
__st.title("📚 আর্দশ প্রাইভেট কেয়ার")
__st.subheader("শিক্ষার্থী এবং অভিভাবকদের অফিশিয়াল পোর্টাল")
__st.markdown("---")

# Sidebar Navigation
menu = __st.sidebar.selectbox("মেনু নির্বাচন করুন", ["হোম / নোটিশ বোর্ড", "ছাত্র-ছাত্রী চ্যাট রুম", "অ্যাডমিন প্যানেল"])

# 1. Notice Board Section
if menu == "হোম / নোটিশ বোর্ড":
    __st.header("📢 জরুরি নোটিশ ও ঘোষণা")
    
    try:
        response = supabase.table("notices").select("*").order("created_at", desc=True).execute()
        notices = response.data
        
        if notices:
            for notice in notices:
                __st.markdown(f"""
                <div class="notice-card">
                    <h3>{notice.get('title', 'নোটিশ')}</h3>
                    <p>{notice.get('content', '')}</p>
                    <small style="color: #94a3b8 !important;">প্রকাশের সময়: {notice.get('created_at', '')}</small>
                </div>
                """, unsafe_allow_html=True)
        else:
            __st.info("এই মুহূর্তে কোনো নতুন নোটিশ নেই।")
    except Exception as e:
        __st.warning("নোটিশ লোড করতে সুপাবেস ডাটাবেস টেবিল কানেকশন চেক করুন।")

# 2. Student Chat Room Section
elif menu == "ছাত্র-ছাত্রী চ্যাট রুম":
    __st.header("💬 শিক্ষার্থী আলোচনা ও চ্যাট রুম")
    
    student_name = __st.text_input("আপনার নাম লিখুন:")
    
    if student_name:
        message_text = __st.text_area("আপনার বার্তা বা প্রশ্ন লিখুন:")
        if __st.button("বার্তা পাঠান"):
            if message_text.strip():
                try:
                    supabase.table("messages").insert({"name": student_name, "message": message_text}).execute()
                    __st.success("বার্তা সফলভাবে পাঠানো হয়েছে!")
                    __st.rerun()
                except Exception as e:
                    __st.error(f"বার্তা পাঠাতে সমস্যা হয়েছে: {e}")
            else:
                __st.warning("দয়া করে কিছু লিখে তারপর পাঠান।")
                
        __st.markdown("---")
        __st.subheader("সাম্প্রতিক আলোচনা:")
        try:
            msg_response = supabase.table("messages").select("*").order("created_at", desc=True).limit(20).execute()
            messages = msg_response.data
            if messages:
                for msg in messages:
                    __st.markdown(f"**{msg.get('name', 'Anonymous')}**: {msg.get('message', '')}")
            else:
                __st.info("এখনো কোনো বার্তা নেই। প্রথম বার্তাটি আপনিই পাঠান!")
        except Exception as e:
        __st.warning("চ্যাটের ডেটা লোড করা যাচ্ছে না।")
    else:
        __st.info("চ্যাটে অংশগ্রহণের জন্য ওপরে আপনার নাম লিখুন।")

# 3. Admin Panel Section
elif menu == "অ্যাডমিন প্যানেল":
    __st.header("⚙️ অ্যাডমিন কন্ট্রোল প্যানেল")
    admin_pass = __st.text_input("অ্যাডমিন পাসওয়ার্ড দিন:", type="password")
    
    # সাধারণ নিরাপত্তার জন্য ডিফল্ট পাসওয়ার্ড 'admin123' রাখা হলো
    if admin_pass == "admin123":
        __st.success("সফলভাবে লগইন হয়েছে!")
        
        tab1, tab2 = __st.tabs(["নতুন নোটিশ প্রকাশ করুন", "নোটিশ মুছুন বা ম্যানেজ করুন"])
        
        with tab1:
            n_title = __st.text_input("নোটিশের শিরোনাম")
            n_content = __st.text_area("নোটিশের বিস্তারিত বর্ণনা")
            if __st.button("নোটিশ প্রকাশ করুন"):
                if n_title and n_content:
                    try:
                        supabase.table("notices").insert({"title": n_title, "content": n_content}).execute()
                        __st.success("নোটিশ সফলভাবে প্রকাশিত হয়েছে!")
                    except Exception as e:
                        __st.error(f"ত্রুটি: {e}")
                else:
                    __st.warning("শিরোনাম এবং বিবরণ উভয়ই পূরণ করুন।")
                    
        with tab2:
            __st.info("নোটিশ ম্যানেজমেন্ট অপশন সক্রিয় আছে।")
    elif admin_pass:
        __st.error("ভুল পাসওয়ার্ড! সঠিক পাসওয়ার্ড দিয়ে প্রবেশ করুন।")

import streamlit as st
import google.generativeai as genai

# ১. পেজ কনফিগারেশন
st.set_page_config(
    page_title="আদর্শ প্রাইভেট কেয়ার",
    page_icon="🎓",
    layout="wide"
)

# ==========================================
# 🔑 আপনার আসল API Key টি নিচের কোটেশনের ভেতরে বসান:
# ==========================================
MY_API_KEY = "এখানে_আপনার_API_KEY_বসাবেন"

# ব্যাকএন্ডে API Key কনফিগার করা
if MY_API_KEY and MY_API_KEY != "এখানে_আপনার_API_KEY_বসাবেন":
    genai.configure(api_key=MY_API_KEY)

# সাইডবার: সোশ্যাল মিডিয়া লিংক ও পরিচিতি
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3429/3429149.png", width=90)
    st.title("আদর্শ প্রাইভেট কেয়ার")
    st.caption("গুণগত শিক্ষা, উজ্জ্বল ভবিষ্যৎ")
    st.divider()
    
    st.subheader("🔗 আমাদের সোশ্যাল মিডিয়া")
    st.markdown("[🎥 ইউটিউব চ্যানেল](https://youtube.com)")
    st.markdown("[👤 হোসেনের ফেসবুক প্রোফাইল](https://facebook.com)")

# মূল পেজ নেভিগেশন (ট্যাব)
tab1, tab2, tab3, tab4 = st.tabs(["🏠 পরিচিতি ও কোর্সসমূহ", "🌟 বিশেষ বৈশিষ্ট্য", "📚 এআই শিক্ষক", "📞 যোগাযোগ ও ঠিকানা"])

# ট্যাব ১: পরিচিতি ও কোর্সসমূহ
with tab1:
    st.header("স্বাগতম 'আদর্শ প্রাইভেট কেয়ার'-এ")
    st.subheader("আপনার সন্তানের ভবিষ্যৎ কি সঠিক পথে এগোচ্ছে? ভর্তির জন্য আপনার সন্তানকে আদর্শ প্রাইভেট কেয়ার-এ নিয়ে আসুন।")
    st.info("🏆 **আদর্শ প্রাইভেট কেয়ার - আপনার সন্তানের সাফল্যের সাথী!**")
    
    st.divider()
    st.subheader("📚 আমাদের পাঠদান ব্যবস্থা")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("### 🏫 পঞ্চম থেকে অষ্টম শ্রেণি")
        st.write("👉 **সকল বিষয় যত্নসহকারে পড়ানো হয়।**")
        
    with col2:
        st.warning("### 🎓 নবম ও দশম শ্রেণি")
        st.write("👉 **সকল বিভাগের গণিত ও ইংরেজি**")
        st.write("👉 **বাণিজ্য বিভাগের সকল বিষয়**")

# ট্যাব ২: আমাদের বিশেষ বৈশিষ্ট্য
with tab2:
    st.header("🌟 আমাদের বিশেষ বৈশিষ্ট্যসমূহ")
    
    st.markdown("""
    * 🎯 **গণিতের বেসিক তৈরি:** দুর্বল শিক্ষার্থীদের গণিতের ভিত্তি মজবুত করা হয়।
    * 📖 **ইংরেজি গ্রামার ও সিলেবাস:** সহজ নিয়মে গ্রামার এবং সম্পূর্ণ সিলেবাস শেষ করা হয়।
    * 📝 **সাপ্তাহিক মডেল টেস্ট:** নিয়মিত পরীক্ষার মাধ্যমে মেধা যাচাই ও প্র্যাকটিস।
    * 👨‍🏫 **বিশেষ কেয়ার:** দুর্বল ছাত্র-ছাত্রীদের আলাদাভাবে যত্ন ও গাইডলাইন দেওয়া হয়।
    """)
    
    st.divider()
    st.subheader("📊 আমাদের সাফল্য")
    col_a, col_b, col_c = st.columns(3)
    col_a.metric("পঞ্চম-অষ্টম সাফল্য", "১০০%")
    col_b.metric("এসএসসি পাশের হার", "৯৮%")
    col_c.metric("মডেল টেস্ট সুবিধা", "সাপ্তাহিক")

# ট্যাব ৩: এআই টিউটর (কোনো Key ইনপুট ছাড়া সরাসরি চ্যাট)
with tab3:
    st.header("🤖 আপনার এআই স্টাডি অ্যাসিস্ট্যান্ট")
    st.write("গণিত, ইংরেজি বা অন্য যেকোনো বিষয়ের পড়া বুঝতে এআই শিক্ষকের সাহায্য নিন।")
    
    if MY_API_KEY and MY_API_KEY != "এখানে_আপনার_API_KEY_বসাবেন":
        try:
            model = genai.GenerativeModel('gemini-2.5-flash')
            
            if "messages" not in st.session_state:
                st.session_state.messages = []

            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

            if prompt := st.chat_input("পড়াশোনা সম্পর্কিত আপনার প্রশ্নটি লিখুন..."):
                st.session_state.messages.append({"role": "user", "content": prompt})
                with st.chat_message("user"):
                    st.markdown(prompt)

                with st.chat_message("assistant"):
                    response = model.generate_content(prompt)
                    st.markdown(response.text)
                    st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"একটি ত্রুটি ঘটেছে: {e}")
    else:
        st.warning("⚠️ কোডের ভেতরে API Key বসানো হয়নি। দয়া করে কোডের ১৬ নম্বর লাইনে আপনার API Key টি বসান।")

# ট্যাব ৪: যোগাযোগ
with tab4:
    st.header("📞 আমাদের সাথে যোগাযোগ করুন")
    
    col_loc, col_call = st.columns(2)
    
    with col_loc:
        st.subheader("📍 ঠিকানা")
        st.write("দক্ষিণগাঁও এক নম্বর রোড,")
        st.write("ইবনে সিনা স্কুলের পাশে, ঢাকা।")
        st.caption("📍 *গুগল ম্যাপে লোকেশন প্রদান করা আছে।*")
        
    with col_call:
        st.subheader("📱 ফোন নম্বর")
        st.write("📞 **০১৭২৩১৬৫৭২১**")
        st.write("📞 **০১৫৬৩১৪৮৯১০**")

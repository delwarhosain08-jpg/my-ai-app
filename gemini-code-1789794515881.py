import google.generativeai as genai
import streamlit as st

# ১. ওয়েবসাইটের শিরোনাম ও পেজ কনফিগারেশন
st.set_page_config(page_title="Custom AI Assistant", page_icon="🤖")
st.title("🤖 কাস্টম এআই অ্যাসিস্ট্যান্ট")
st.caption("আপনার ব্যবসার জন্য একটি স্মার্ট এআই সমাধান")

# ২. সাইডবার (API Key এবং কনফিগারেশনের জন্য)
with st.sidebar:
    st.header("⚙️ সিস্টেম সেটআপ")
    api_key = st.text_input("আপনার Gemini API Key দিন:", type="password")
    system_role = st.text_area(
        "এআই-এর ভূমিকা (System Prompt):",
        value="তুমি একজন পেশাদার কাস্টমার সাপোর্ট এজেন্ট। নম্র ও সহজ ভাষায় সংক্ষিপ্ত উত্তর দাও।",
    )

# ৩. চ্যাট হিস্ট্রি ধরে রাখার মেমোরি
if "messages" not in st.session_state:
    st.session_state.messages = []

# ৪. পূর্বের মেসেজগুলো স্ক্রিনে দেখানো
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# ৫. ইউজার ইনপুট ও এআই রেসপন্স
user_input = st.chat_input("আপনার প্রশ্ন লিখুন...")

if user_input:
    if not api_key:
        st.error("দয়া করে সাইডবারে আপনার Gemini API Key প্রদান করুন!")
    else:
        # ইউজারের প্রশ্ন স্ক্রিনে যোগ করা
        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )
        with st.chat_message("user"):
            st.write(user_input)

        # Gemini API কানেক্ট ও প্রসেসিং
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-3.6-flash")

            full_prompt = f"System Role: {system_role}\nUser Question: {user_input}"

            with st.chat_message("assistant"):
                with st.spinner("চিন্তা করছে..."):
                    response = model.generate_content(full_prompt)
                    st.write(response.text)

            # এআই-এর উত্তর মেমোরিতে সেভ করা
            st.session_state.messages.append(
                {"role": "assistant", "content": response.text}
            )

        except Exception as e:
            st.error(f"একটি ত্রুটি ঘটেছে: {e}")

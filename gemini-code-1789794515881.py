# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    # Logo
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
        <div style="
            text-align:center;
            padding:5px 0 15px 0;
        ">
            <h2 style="
                margin:0;
                font-size:22px;
                color:white;
            ">
                আদর্শ প্রাইভেট কেয়ার
            </h2>

            <p style="
                margin-top:5px;
                color:#dceeff;
                font-size:14px;
            ">
                গুণগত শিক্ষা, উজ্জ্বল ভবিষ্যৎ
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # যোগাযোগ
    st.markdown(
        """
        <h3 style="color:white;">
            📞 যোগাযোগ
        </h3>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="
            background:rgba(255,255,255,0.10);
            padding:12px;
            border-radius:12px;
            line-height:1.8;
        ">
            📍 <b>ঠিকানা:</b> ঢাকা, বাংলাদেশ<br>
            📱 <b>মোবাইল:</b> 01XXXXXXXXX<br>
            ✉️ <b>Email:</b> example@gmail.com
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # Social Media
    st.markdown(
        """
        <h3 style="color:white;">
            🌐 সোশ্যাল মিডিয়া
        </h3>
        """,
        unsafe_allow_html=True
    )

    # YouTube
    st.markdown(
        """
        <a href="https://www.youtube.com/channel/UC0_gzD3mlN1O1FhjTu2Qkzg"
           target="_blank"
           style="
                display:block;
                text-decoration:none;
                background:#ff0000;
                color:white;
                padding:11px;
                margin:8px 0;
                border-radius:10px;
                text-align:center;
                font-weight:bold;
           ">
           🎥 YouTube Channel
        </a>
        """,
        unsafe_allow_html=True
    )

    # Facebook
    st.markdown(
        """
        <a href="https://www.facebook.com/share/1DHesGeakU/"
           target="_blank"
           style="
                display:block;
                text-decoration:none;
                background:#1877f2;
                color:white;
                padding:11px;
                margin:8px 0;
                border-radius:10px;
                text-align:center;
                font-weight:bold;
           ">
           👤 Facebook Profile
        </a>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown(
        """
        <div style="
            text-align:center;
            color:#dceeff;
            font-size:12px;
            padding:10px;
        ">
            🎓 আদর্শ প্রাইভেট কেয়ার<br>
            <span>© 2026 All Rights Reserved</span>
        </div>
        """,
        unsafe_allow_html=True
    )

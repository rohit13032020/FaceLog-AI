import streamlit as st

from src.ui.base_layout import style_background_dashboard, style_base_layout


def header_home():
    st.markdown(
        """
        <div class="stitch-head">
            <div class="stitch-strip">🛡️ Campus Liveness Engine • <b>Active v2.4</b></div>
            <div class="stitch-brand">
                <div class="stitch-logo">🎓</div>
                <div class="stitch-word">
                    <div class="stitch-word-main">SNAP<span>CLASS</span></div>
                    <div class="stitch-word-sub">Campus Workspace Portal</div>
                </div>
            </div>
            <p class="stitch-tag">Automated neural biometric attendance &amp; classroom intelligence platform</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def header_dashboard():


    st.markdown(
        """
        <div class="tp-nav">
            <div class="tp-nav-brand">
                <div class="tp-nav-logo">🎓</div>
                <div>
                    <div class="tp-nav-name">SNAP<span>CLASS</span></div>
                    <div class="tp-nav-sub">Faculty Portal</div>
                </div>
            </div>
            <div class="tp-live"><span class="tp-live-dot"></span>Live Sync</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def teacher_auth_shell(title, subtitle, back_key="gobackbtn_teacher_auth"):
    """Stitch UI_teacher_portal: mesh wash + top nav + centered white auth card shell."""
    style_background_dashboard()
    style_base_layout()
    header_dashboard()
    if st.button("← Back to Home", type="tertiary", key=back_key):
        st.session_state["login_type"] = None
        st.rerun()
    st.markdown('<p class="tp-back"><span>Enter your credentials to manage classrooms</span></p>', unsafe_allow_html=True)
    _l, center, _r = st.columns([1, 6, 1])
    with center:
        st.markdown('<div class="tp-auth-card-marker"></div>', unsafe_allow_html=True)
        st.markdown(f'<p class="tp-auth-title">{title}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="tp-auth-sub">{subtitle}</p>', unsafe_allow_html=True)
        mode = st.segmented_control(
            "mode",
            options=["Registration", "Sign In"],
            default="Registration" if st.session_state.get("teacher_login_type", "register") == "register" else "Sign In",
            key="tp_auth_mode",
            label_visibility="collapsed",
        )
        want = "register" if mode == "Registration" else "login"
        if want != st.session_state.get("teacher_login_type", "register"):
            st.session_state.teacher_login_type = want
            st.rerun()
        st.markdown(
            '<p class="tp-switch-note">Use your institutional email to secure your faculty workspace</p>',
            unsafe_allow_html=True,
        )
    return center

import streamlit as st

from src.components.brand import emblem_html, hero_logo_html

DEPARTMENTS = [
    "Computer Science & AI",
    "Data Structures & Algorithms",
    "Applied Mathematics",
    "Applied Physics & Electronics",
    "Full Stack Web Engineering",
]


def _portal_nav():
    st.markdown(
        "<div class='tp-nav-wrap'>"
        "<div class='tp-brand'>"
        + emblem_html()
        + "<div style='line-height:1;'>"
        "<p class='tp-brand-name'>SNAP<span class='tp-brand-name-blue'>CLASS</span></p>"
        "<p class='tp-brand-sub'>Teacher Portal</p>"
        "</div></div></div>",
        unsafe_allow_html=True,
    )
    if st.button("← Back to Home", key="tp_back_home", type="secondary"):
        st.session_state.pop("login_type", None)
        st.session_state.pop("tp_mode", None)
        st.rerun()


def _portal_header(mode: str):
    title = "Register your teacher profile" if mode == "register" else "Welcome back, teacher"
    sub = (
        "Set up your faculty credentials to manage automated attendance and classroom rosters."
        if mode == "register"
        else "Sign in with your faculty credentials to continue to live attendance."
    )
    st.markdown(
        "<div class='snap-hero' style='padding-top:0.4rem;'>"
        "<span class='lumina-live-badge'>"
        "<span class='lumina-live-dot'></span>"
        "AI Facial Recognition v2.4 Active</span>"
        + hero_logo_html(size=56)
        + "<p class='lumina-brand-title' style='font-size:1.9rem;'>Snap Class</p>"
        "<p class='lumina-tagline'>Smart automatic attendance, powered by "
        "real-time neural vision. One snap at a time.</p>"
        "<span class='lumina-live-badge tp-badge'>Faculty Access Portal</span>"
        f"<p class='tp-title'>{title}</p>"
        f"<p class='tp-sub'>{sub}</p></div>",
        unsafe_allow_html=True,
    )

def _portal_switcher(mode: str) -> str:
    picked = st.segmented_control(
        "Account mode",
        options=["Registration", "Sign In"],
        default="Registration" if mode == "register" else "Sign In",
        selection_mode="single",
        key="tp_mode_switch",
        label_visibility="collapsed",
    )
    return "register" if picked == "Registration" else "login"


def _register_form() -> None:
    with st.form("tp_register_form", clear_on_submit=False, border=False):
        username = st.text_input("Enter username *", value="abhishek")
        st.caption("Unique teacher handle across institution")
        full_name = st.text_input("Enter full name *", value="Abhishek Sharma")
        department = st.selectbox("Department & Subject *", options=DEPARTMENTS, index=0)
        password = st.text_input("Enter password *", type="password", value="SecureProfPass2026!")
        st.markdown("<span class='tp-strong-pill'>Strong</span>", unsafe_allow_html=True)
        confirm = st.text_input("Confirm password *", type="password")
        agree = st.checkbox("I agree to the Faculty Privacy Protocol and terms.", value=True)
        reg = st.form_submit_button("Register Now", type="primary", use_container_width=True)
        if reg:
            if not username.strip() or not full_name.strip() or not password:
                st.error("Please fill username, full name and password.")
            elif confirm and confirm != password:
                st.error("Passwords do not match.")
            elif not agree:
                st.warning("Please accept the Faculty Privacy Protocol.")
            else:
                st.session_state["teacher_profile"] = {
                    "username": username.strip(),
                    "full_name": full_name.strip(),
                    "department": department,
                    "registered": True,
                }
                st.success(f"Welcome, {full_name.strip()}! Registered for {department}.")


def _login_form() -> None:
    with st.form("tp_login_form", clear_on_submit=False, border=False):
        username = st.text_input("Username *")
        password = st.text_input("Password *", type="password")
        go = st.form_submit_button("Login", type="primary", use_container_width=True)
        if go:
            profile = st.session_state.get("teacher_profile", {})
            if profile and profile.get("username") == username.strip():
                st.success(f"Welcome back, {profile.get('full_name', username)}!")
            elif username.strip():
                st.session_state["teacher_profile"] = {"username": username.strip(), "registered": True}
                st.success(f"Signed in as {username.strip()}.")
            else:
                st.error("Enter your username to sign in.")
    if st.button("Need an account? Go to Registration", key="tp_goto_register", type="tertiary"):
        st.session_state["tp_mode"] = "register"
        st.rerun()

def teacher_screen():
    from src.UI.base_layout import style_background_home, style_base_layout
    style_base_layout()
    style_background_home()
    st.markdown(
        "<style>"
        ".tp-badge { background: rgba(77,97,255,0.10) !important; border-color: rgba(77,97,255,0.25) !important; color:#4D61FF !important; margin-top:0.8rem; }"
        ".tp-title { font-size:1.6rem; font-weight:800; color:#0F172A !important; margin:0.6rem 0 0.2rem 0 !important; letter-spacing:-0.02em; }"
        ".tp-sub { font-size:0.85rem; color:#475569 !important; margin:0 auto !important; max-width:26rem; line-height:1.5; }"
        ".tp-strong-pill { font-size:0.65rem; font-weight:700; color:#047857 !important; background:#ECFDF5; border:1px solid #A7F3D0; border-radius:9999px; padding:0.15rem 0.6rem; }"
        ".stForm { background: rgba(255,255,255,0.95) !important; border:1px solid #E2E8F0 !important; border-radius:1.5rem !important; padding:1.4rem !important; box-shadow: 0 20px 45px -12px rgba(91,92,229,0.12) !important; }"
        "label[data-testid='stWidgetLabel'] p { color:#0F172A !important; font-weight:700 !important; font-size:0.75rem !important; }"
        ".stTextInput input, .stSelectbox div[data-baseweb='select'] { border-radius:1rem !important; background:#F8FAFC !important; }"
        "div[data-testid='stSegmentedControl'] { justify-content:center; }"
        "</style>",
        unsafe_allow_html=True,
    )
    _portal_nav()
    mode = st.session_state.get("tp_mode", "register")
    mode = _portal_switcher(mode)
    st.session_state["tp_mode"] = mode
    _portal_header(mode)
    if mode == "register":
        _register_form()
    else:
        _login_form()
    st.markdown(
        "<div class='lumina-footer'>"
        "<span class='lumina-pill'>&#128737; Anti-Spoofing Protected</span> "
        "<span class='lumina-pill'>&#128272; End-to-End Encrypted</span> "
        "<span class='lumina-pill'>&#9889; &lt; 0.2s Detection</span><br><br>"
        "<small>Snap Class Attendance System &bull; Intelligent Campus Platform &bull; Need Help?</small></div>",
        unsafe_allow_html=True,
    )


import streamlit as st

from src.UI.base_layout import (
    style_background_home,
    style_base_layout,
    style_portal_cards,
)
from src.components.header_home import header_home


TEACHER_FEATS = ["Instant camera batch scan", "Auto-generated attendance logs & CSV", "Classroom roster & proxy alerts"]
STUDENT_FEATS = ["One-tap mobile biometric verification", "Personal absence & presence log", "Timetable & period notification alerts"]


def _feats(items):
    rows = "".join(f"<li><span class='lumina-check'>&#10003;</span><span>{t}</span></li>" for t in items)
    return f"<ul class='lumina-feats'>{rows}</ul>"


def home_screen():
    style_base_layout()
    style_background_home()
    style_portal_cards()
    header_home()
    col_teacher, col_student = st.columns(2, gap="medium")
    with col_teacher:
        st.markdown("<div class='teacher-card-marker'></div>", unsafe_allow_html=True)
        st.markdown(
            "<div class='lumina-card-top'><div class='lumina-icon-box lumina-icon-indigo'>&#127891;</div>"
            "<span class='lumina-role-tag lumina-role-faculty'>Faculty</span></div>"
            "<p class='lumina-card-title'>Teacher Portal</p>"
            "<p class='lumina-card-desc'>Initiate automated live roll calls, take instant classroom snaps, oversee roster registers, and export analytics.</p>"
            + _feats(TEACHER_FEATS),
            unsafe_allow_html=True,
        )
        if st.button("Enter as Teacher  >", key="home_teacher_btn", type="primary", width="stretch"):
            st.session_state["login_type"] = "teacher"
            st.rerun()
    with col_student:
        st.markdown("<div class='student-card-marker'></div>", unsafe_allow_html=True)
        st.markdown(
            "<div class='lumina-card-top'><div class='lumina-icon-box lumina-icon-sky'>&#129489;</div>"
            "<span class='lumina-role-tag lumina-role-scholar'>Scholar</span></div>"
            "<p class='lumina-card-title'>Student Portal</p>"
            "<p class='lumina-card-desc'>Verify personal face check-ins, verify your course attendance rate, review leave status, and view daily timetables.</p>"
            + _feats(STUDENT_FEATS),
            unsafe_allow_html=True,
        )
        if st.button("Enter as Student  >", key="home_student_btn", type="secondary", width="stretch"):
            st.session_state["login_type"] = "student"
            st.rerun()
    st.markdown(
        "<div class='lumina-footer'><span class='lumina-pill'>&#128737; Anti-Spoofing Protected</span> "
        "<span class='lumina-pill'>&#128272; End-to-End Encrypted</span> "
        "<span class='lumina-pill'>&#9889; &lt; 0.2s Detection</span><br><br>"
        "<small>Snap Class Attendance System &bull; Intelligent Campus Platform &bull; Need Help?</small></div>",
        unsafe_allow_html=True,
    )

import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home
def home_screen():


    header_home()
    style_background_home()
    style_base_layout()

    col_teacher, col_student = st.columns(2, gap="medium")

    with col_teacher:
        st.markdown('<div class="teacher-card-marker"></div>', unsafe_allow_html=True)
        st.markdown('<div class="lumina-card-top"><div class="lumina-icon-box lumina-icon-indigo">👨‍🏫</div><span class="lumina-role-tag lumina-role-faculty">Faculty</span></div>', unsafe_allow_html=True)
        st.markdown('<p class="lumina-card-title">Teacher Portal</p>', unsafe_allow_html=True)
        st.markdown('<p class="lumina-card-desc">Initiate live class roll calls, capture instant batch camera snaps, oversee rosters, and export verified attendance records.</p>', unsafe_allow_html=True)
        st.markdown('<ul class="lumina-feats"><li><span class="lumina-check">✓</span>Instant AI batch facial scan &amp; match</li><li><span class="lumina-check">✓</span>Auto-generated attendance logs &amp; CSV export</li><li><span class="lumina-check">✓</span>Proxy detection &amp; live classroom roster alerts</li></ul>', unsafe_allow_html=True)
        if st.button('Enter as Teacher →', type='primary', key='enter_teacher'):
            st.session_state['login_type']='teacher'
            st.rerun()

    with col_student:
        st.markdown('<div class="student-card-marker"></div>', unsafe_allow_html=True)
        st.markdown('<div class="lumina-card-top"><div class="lumina-icon-box lumina-icon-sky">🎓</div><span class="lumina-role-tag lumina-role-scholar">Student</span></div>', unsafe_allow_html=True)
        st.markdown('<p class="lumina-card-title">Student Portal</p>', unsafe_allow_html=True)
        st.markdown('<p class="lumina-card-desc">Verify personal face check-ins, view individual course attendance percentage, monitor leave permissions, and inspect lecture timetables.</p>', unsafe_allow_html=True)
        st.markdown('<ul class="lumina-feats"><li><span class="lumina-check">✓</span>One-tap personal biometric check-in log</li><li><span class="lumina-check">✓</span>Live subject presence &amp; shortfall alerts</li><li><span class="lumina-check">✓</span>Campus schedule &amp; timetable sync</li></ul>', unsafe_allow_html=True)
        if st.button('Enter as Student →', type='secondary', key='enter_student'):
            st.session_state['login_type']='student'
            st.rerun()

    footer_home()
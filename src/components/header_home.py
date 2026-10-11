import streamlit as st

from src.components.brand import hero_logo_html


def header_home():
    st.markdown(
        "<div class='snap-hero'>"
        "<span class='lumina-live-badge'>"
        "<span class='lumina-live-dot'></span>"
        "AI Facial Recognition v2.4 Active</span>"
        + hero_logo_html(size=56)
        + "<p class='lumina-brand-title'>Snap Class</p>"
        "<p class='lumina-tagline'>Smart automatic attendance, powered by "
        "real-time neural vision. One snap at a time.</p></div>",
        unsafe_allow_html=True,
    )

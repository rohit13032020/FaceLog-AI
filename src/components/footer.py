import streamlit as st

from src.components.brand import get_logo_data_uri


def footer_home():
    st.markdown(
        """
        <div class="stitch-trust"><span>🔒 End-to-End Encrypted</span><span style="color:#cbd5e1;">•</span><span>✨ AI Camera Sync Ready</span></div>
        <div class="stitch-credit">Created with  by <b>ROHIT <span>JANA</span></b></div>
        <div class="stitch-meta">Snap Class Intelligent Campus Platform • <a href="#help">Need Help?</a></div>
        """,
        unsafe_allow_html=True,
    )


def footer_dashboard():
    logo_url = get_logo_data_uri(max_size=128) or ""
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
         <p style="font-weight:bold; color:black;"> Created with by </p>  
         <img src='{logo_url}' style='max-height:25px' />
        </div>
                
                """, unsafe_allow_html=True)

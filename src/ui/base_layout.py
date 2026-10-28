import streamlit as st


# FaceLog-AI Lumina 


_LUMINA_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

/* Background color and gradient */


.stApp, .stAppViewContainer, .stMain, .stMainBlockContainer, section.stMain > div {
    background-color: #faf8ff !important;
    background-image: radial-gradient(
    circle at 50% 0%,
    #e0e7ff 0%,
    #f8fafc 40%,
    #f1f5f9 100%) !important;
    background-attachment: fixed !important;
    font-family: 'Plus Jakarta Sans', -apple-system, 'Segoe UI', Roboto, sans-serif !important;
}

/* Text colors and content width */

.stApp { 
    color: #0F172A !important;
 }
.block-container { 
    padding-top: 0.5rem !important;
    padding-bottom: 1rem !important; 
    max-width: 64rem !important; 
 }

 
/* Hiding Streamlit's default menu and footer */
#MainMenu, 
footer { 
        visibility: hidden;
    }
header[data-testid="stHeader"] { 
    background: transparent !important; 
 }
div[data-testid="stToolbar"], 
div[data-testid="stDecoration"] { 
    visibility: hidden;
 }

/*Heading and paragraph styling*/
h1 { 
    font-family: 'Plus Jakarta Sans', sans-serif !important; 
    font-weight: 800 !important; 
    letter-spacing: -0.025em !important; 
    color: #0F172A !important; 
 }
h2, h3, h4 { 
    font-family: 'Plus Jakarta Sans', sans-serif !important; 
    font-weight: 700 !important; 
    color: #0F172A !important; 
 }

p, label, div, span:not([translate="no"]) { font-family: 'Plus Jakarta Sans', sans-serif !important; }
/* Material icon spans (button/label icons) must keep Streamlit's icon font,
   otherwise ligature names like "ar_on_you" render as raw text. */
span[translate="no"] { 
    font-family: "Material Symbols Rounded", sans-serif !important; 
    font-weight: 400 !important; 
    font-style: normal; 
    line-height: 1 !important; 
    letter-spacing: normal !important; 
    text-transform: none !important; 
    display: inline-block; 
    white-space: nowrap; 
    word-wrap: normal; 
    direction: ltr; 
    font-feature-settings: "liga"; -webkit-font-feature-settings: "liga"; -webkit-font-smoothing: antialiased; 
    user-select: none; 
    vertical-align: bottom; 
    }
[data-testid="stMarkdownContainer"] p { color: #0F172A !important; }
.lumina-live-badge { 
    display: inline-flex; 
    align-items: center; 
    gap: 0.5rem; 
    padding: 0.25rem 0.9rem; 
    border-radius: 9999px; 
    font-size: 0.75rem; 
    font-weight: 600; 
    background: rgba(255,255,255,0.8); 
    border: 1px solid #e0e7ff; 
    color: #4338ca !important; 
    box-shadow: 0 2px 10px -1px rgba(99,102,241,0.15); 
}
.lumina-live-dot { 
    width: 0.5rem; 
    height: 0.5rem; 
    border-radius: 9999px; 
    background: #10b981; 
    animation: lumina-pulse 1.6s ease-in-out infinite; 
}
/*How the logo is styled*/
@keyframes lumina-pulse { 0%,100% { opacity: 1; } 50% { opacity: 0.45; } }
.lumina-logo { 
    width: 3rem; 
    height: 3rem; 
    border-radius: 1rem; 
    background: linear-gradient(135deg, #4f46e5 0%, #6366f1 50%, #8b5cf6 100%); 
    display: flex; 
    align-items: center; 
    justify-content: center; 
    box-shadow: 0 8px 20px -4px rgba(99,102,241,0.45); 
    font-size: 1.5rem; 
}
.lumina-brand-title { 
    font-size: 2.25rem; 
    font-weight: 800; 
    letter-spacing: -0.03em; 
    color: #0F172A !important; margin: 0 !important; 
    line-height: 1.1 !important;
}
.lumina-tagline { 
    color: #0F172A !important; 
    font-size: 1rem !important; 
    margin-top: 0.35rem !important;
}

/*Remove the default card styling*/

[data-testid="stColumn"] > div { 
    background: transparent !important;
    border: none !important; 
    box-shadow: none !important; 
    backdrop-filter: none !important; 
    padding: 0.25rem !important;
 }
/* Add styling to the Teacher and Student cards */

[data-testid="stColumn"]:has(.teacher-card-marker) > div, 
[data-testid="stColumn"]:has(.student-card-marker) > div { 
    background: rgba(255,255,255,0.92) !important; 
    border: 1px solid #e2e8f0 !important; 
    border-radius: 1.5rem !important; 
    backdrop-filter: blur(16px) !important; 
    -webkit-backdrop-filter: blur(16px) !important; 
    box-shadow: 0 10px 25px -5px rgba(99,102,241,0.08), 
                0 8px 10px -6px rgba(0,0,0,0.04) !important; 
                padding: 1.6rem 1.5rem 1.5rem 1.5rem !important; 
                position: relative !important; 
                overflow: hidden !important; 
 }
/* Top accent strips */
[data-testid="stColumn"]:has(.teacher-card-marker) > div::before,
[data-testid="stColumn"]:has(.student-card-marker) > div::before { 
      content: ""; 
      position: absolute; 
      top: 0; 
      left: 0; 
      right: 0; 
      height: 6px;
 }
[data-testid="stColumn"]:has(.teacher-card-marker) > div::before { 
     background: linear-gradient(to right, #fbbf24, #4f46e5, #9333ea);
    }
[data-testid="stColumn"]:has(.student-card-marker) > div::before {
    background: linear-gradient(to right, #2563eb, #4f46e5, #9333ea);
 }

 /*Hide the marker elements*/

.teacher-card-marker, 
.student-card-marker { 
    display: none !important; 
    height: 0 !important; 
 }

 /*Change paragraph and list text colours*/

[data-testid="stColumn"]:has(.teacher-card-marker) > div p,
[data-testid="stColumn"]:has(.teacher-card-marker) > div li,
[data-testid="stColumn"]:has(.student-card-marker) > div p, 
[data-testid="stColumn"]:has(.student-card-marker) > div li {
     color: #0F172A !important;
 }

 /*Card hover effect*/
[data-testid="stColumn"]:has(.teacher-card-marker) > div:hover,
[data-testid="stColumn"]:has(.student-card-marker) > div:hover {
    border-color: rgba(99,102,241,0.35) !important; 
    box-shadow: 0 20px 35px -8px rgba(99,102,241,0.16) !important;
 }
[data-testid="stColumn"] h2 { 
    font-size: 1.5rem !important; 
    color: #0F172A !important;
    margin-bottom: 0.25rem !important;
 }

.lumina-card-top { 
    display: flex; 
    align-items: center; 
    justify-content: space-between; 
    margin-bottom: 1.1rem; 
    margin-top: 0.35rem; 
 }
.lumina-icon-box { 
    width: 3rem; 
    height: 3rem; 
    border-radius: 1rem; 
    display: flex; 
    align-items: center; 
    justify-content: center; 
    font-size: 1.45rem; 
    box-shadow: 0 1px 2px rgba(15,23,42,0.06); 
}
.lumina-icon-indigo {
    background: #eef2ff; 
    border: 1px solid #e0e7ff; 
 }
.lumina-icon-sky { 
    background: #eff6ff; 
    border: 1px solid #dbeafe; 
 }
.lumina-role-tag { 
    font-size: 0.68rem; 
    font-weight: 800; 
    letter-spacing: 0.08em; 
    text-transform: uppercase; 
    padding: 0.3rem 0.75rem; 
    border-radius: 9999px; 
    border: 1px solid; 
    box-shadow: 0 1px 2px rgba(15,23,42,0.05); 
 }
.lumina-role-faculty { 
    color: #4338ca !important; 
    background: #eef2ff; 
    border-color: #c7d2fe; 
 }
.lumina-role-scholar { 
    color: #1d4ed8 !important; 
    background: #eff6ff; 
    border-color: #bfdbfe; 
 }
.lumina-card-title { 
    font-size: 1.4rem !important; 
    font-weight: 800 !important; 
    letter-spacing: -0.02em !important; 
    color: #0F172A !important; 
    margin: 0 0 0.4rem 0 !important;
 }
.lumina-card-desc { 
    font-size: 0.875rem !important; 
    color: #475569 !important; 
    margin-bottom: 1.1rem !important; 
    line-height: 1.6 !important; 
 }
.lumina-feats { 
    list-style: none !important; 
    padding: 0 !important; 
    margin: 0 0 1.4rem 0 !important;
 }
.lumina-feats li { 
    display: flex; 
    align-items: center; gap: 0.55rem; 
    font-size: 0.76rem !important; 
    color: #334155 !important; 
    font-weight: 500; 
    margin-bottom: 0.6rem !important;
 }
.lumina-check { 
    width: 1.25rem; 
    height: 1.25rem; 
    border-radius: 9999px; 
    background: #ecfdf5; 
    border: 1px solid #a7f3d0; 
    color: #059669 !important; 
    font-weight: 800; 
    font-size: 0.7rem; 
    display: inline-flex; 
    align-items: center; 
    justify-content: center; 
    flex-shrink: 0; 
 }

/*Basic button styling*/

div.stButton > button { 
    width: 100%; 
    border-radius: 0.75rem !important; 
    font-weight: 600 !important; 
    font-size: 0.875rem !important; 
    padding: 0.75rem 1rem !important; 
 }

 /*Primary button*/

div.stButton > button[kind="primary"] { 
    background: linear-gradient(
        to right, 
        #4f46e5, 
        #4f46e5, 
        #9333ea
    ) !important; 
    color: #fff !important; 
    border: none !important; 
    box-shadow: 
        0 4px 12px rgba(99,102,241,0.25), 
        0 10px 15px -3px rgba(99,102,241,0.25) !important; 
 }

 /*Primary button hover effect*/
div.stButton > button[kind="primary"]:hover { 
    filter: brightness(1.08) !important; 
    color: #fff !important; 
 }

 /*Primary button text*/

div.stButton > button[kind="primary"] p { 
    color: #FFFFFF !important;
 }

/*Secondary button*/
div.stButton > button[kind="secondary"] { 
    background: rgba(238,242,255,0.8) !important; 
    color: #4338ca !important; 
    border: 1px solid #c7d2fe !important; 
    box-shadow: 0 1px 2px rgba(15,23,42,0.05) !important; 
 }

/*Secondary button hover*/
div.stButton > button[kind="secondary"]:hover { 
    background: #e0e7ff !important; 
    border-color: #c7d2fe !important; 
    color: #4338ca !important; 
 }

div.stButton > button[kind="secondary"] p { 
    color: inherit !important; 
 }

/*Tertiary button*/
div.stButton > button[kind="tertiary"] { 
    background: transparent !important; 
    color: #0F172A !important; 
 }

 /*Metric cards and sidebar*/
[data-testid="stMetric"] { 
    background: rgba(255,255,255,0.92) !important; 
    border: 1px solid #e2e8f0 !important; 
    border-radius: 1rem !important; 
    padding: 1rem 1.2rem !important; 
 }
section[data-testid="stSidebar"] {
    background: rgba(255,255,255,0.85) !important; 
    border-right: 1px solid #e2e8f0 !important; 
 }
.lumina-pill { 
    display: inline-flex; 
    align-items: center; 
    gap: 0.35rem; 
    padding: 0.2rem 0.7rem; 
    border-radius: 9999px; 
    font-size: 0.72rem; 
    font-weight: 600; 
    border: 1px solid #e2e8f0; 
    background: rgba(255,255,255,0.9); 
    color: #475569 !important; 
 }
/* ---- Stitch landing header/footer ---- */
.stitch-head { 
    text-align: center; 
    padding: 1.2rem 0 0.2rem 0; 
 }
.stitch-strip { 
    display: inline-flex; 
    align-items: center; 
    gap: 0.4rem; 
    padding: 0.28rem 0.85rem; 
    border-radius: 9999px; 
    background: #eff6ff; 
    border: 1px solid #dbeafe; 
    color: #1d4ed8 !important; 
    font-size: 0.72rem; 
    font-weight: 700; 
    box-shadow: 0 1px 2px rgba(15,23,42,0.06); 
 }
.stitch-strip b { 
    color: #4f46e5 !important; 
    font-weight: 800; 
 }
.stitch-brand { 
    display: flex; 
    align-items: center; 
    justify-content: center; 
    gap: 0.7rem; 
    margin: 1rem 0 0.3rem 0; 
 }
.stitch-logo { 
    width: 2.9rem; 
    height: 2.9rem; 
    background: #fbbf24; 
    border: 2px solid #0f172a; 
    border-radius: 1rem; 
    display: inline-flex; 
    align-items: center; 
    justify-content: center; 
    box-shadow: 3px 3px 0px #0f172a; 
    transform: rotate(-4deg); 
    font-size: 1.35rem; 
 }
.stitch-word { 
    text-align: left; 
    line-height: 1; 
 }
.stitch-word-main { 
    font-weight: 900; 
    font-size: 1.5rem; 
    letter-spacing: -0.03em; 
    color: #0F172A !important; 
 }
.stitch-word-main span { 
    color: #2563eb !important; 
    margin-left: 0.15rem; 
 }
.stitch-word-sub { 
    font-size: 0.56rem; 
    font-weight: 800; 
    letter-spacing: 0.18em; 
    text-transform: uppercase; 
    color: #64748b !important; 
    margin-top: 0.22rem;
 }
.stitch-tag { 
    text-align: center; 
    color: #475569 !important; 
    font-size: 0.88rem !important; 
    max-width: 26rem; 
    margin: 0.55rem auto 0 auto !important; 
    line-height: 1.55 !important; 
 }
.stitch-trust { 
    display: flex; 
    align-items: center; 
    justify-content: center; 
    gap: 0.6rem; 
    font-size: 0.7rem; 
    font-weight: 600; 
    color: #64748b !important;
    margin: 1.4rem 0 0.55rem 0; 
    flex-wrap: wrap; 
 }
.stitch-credit { 
    text-align: center; 
    font-size: 0.75rem; 
    color: #475569 !important; 
    margin-bottom: 0.2rem; 
 }
.stitch-credit b { 
    color: #0F172A !important; 
    font-weight: 900; 
    letter-spacing: 0.04em;
 }
.stitch-credit b span { 
    color: #d97706 !important;
 }
.stitch-meta { 
    text-align: center; 
    font-size: 0.68rem; 
    color: #64748b !important; 
 }

 
 /*Teacher authentication card*/
.tp-auth-card-marker { 
    display: none !important; 
    height: 0 !important; 
 }

 
/*Style the teacher authentication card*/
[data-testid="stColumn"]:has(.tp-auth-card-marker) > div {
    background: #ffffff !important; 
    border: 1px solid #f1f5f9 !important; 
    border-radius: 1.5rem !important; 
    box-shadow:
         0 20px 45px -12px rgba(91,92,229,0.12), 
         0 4px 16px -2px rgba(15,23,42,0.04) !important; 
    padding: 1.6rem 1.5rem 1.5rem 1.5rem !important; 
    position: relative !important; 
    overflow: hidden !important; 
 }
[data-testid="stColumn"]:has(.tp-auth-card-marker) > div::before { 
    content: ""; 
    position: absolute; 
    top: 0; 
    left: 0; 
    right: 0; 
    height: 5px; 
    background: linear-gradient(
        to right, 
        #FFDF00, 
        #4D61FF, 
        #F43F8E
    ); 
 }
[data-testid="stColumn"]:has(.tp-auth-card-marker) > div:hover { 
    border-color: #f1f5f9 !important;
    box-shadow: 
        0 20px 45px -12px rgba(91,92,229,0.12), 
        0 4px 16px -2px rgba(15,23,42,0.04) !important; 
 }

.tp-auth-title { 
    font-size: 1.5rem !important; 
    font-weight: 800 !important; 
    letter-spacing: -0.025em !important; 
    color: #0f172a !important; 
    text-align: center; 
    margin: 0.4rem 0 0.25rem 0 !important;
 }
.tp-auth-sub { 
    font-size: 0.8rem !important; 
    color: #64748b !important; 
    text-align: center; 
    margin-bottom: 1rem !important;
 }
/* Mesh-style background */
.stApp:has(.tp-auth-card-marker) { 
    background-color: #EBF0FD !important; 
    background-image: 
        radial-gradient(at 0% 0%, 
        rgba(99,102,241,0.12) 0px, 
        transparent 50%), 
        radial-gradient(
            at 100% 0%,
            rgba(244,63,142,0.10) 0px,
            transparent 50%
        ), 
        radial-gradient(
            at 50% 100%,
            rgba(255,223,0,0.15) 0px,
            transparent 60%
            ) 
        !important;
 }
/* Switcher segmented pill */
[data-testid="stColumn"]:has(.tp-auth-card-marker) div[data-testid="stSegmentedControl"] { background: #f1f5f9 !important; border-radius: 9999px !important; padding: 4px !important; }
.tp-switch-note { text-align: center; font-size: 0.72rem; color: #64748b !important; margin-top: 0.5rem; }
/* Icon inputs inside teacher auth card */
[data-testid="stColumn"]:has(.tp-auth-card-marker) div[data-testid="stTextInput"] input { background: #f8fafc !important; border: 1px solid #e2e8f0 !important; border-radius: 0.9rem !important; font-size: 0.875rem !important; color: #0f172a !important; }
[data-testid="stColumn"]:has(.tp-auth-card-marker) div[data-testid="stTextInput"] input::placeholder { color: #94a3b8 !important; }
[data-testid="stColumn"]:has(.tp-auth-card-marker) div[data-testid="stTextInput"] input:focus { border-color: #6366f1 !important; box-shadow: 0 0 0 3px rgba(99,102,241,0.15) !important; background: #ffffff !important; }
[data-testid="stColumn"]:has(.tp-auth-card-marker) div[data-testid="stTextInput"] label p { font-size: 0.72rem !important; font-weight: 800 !important; letter-spacing: 0.08em !important; text-transform: uppercase !important; color: #334155 !important; }
/* Teacher auth buttons: primary blue glow, secondary pink glow (Stitch) */
[data-testid="stColumn"]:has(.tp-auth-card-marker) div.stButton > button[kind="primary"] { background: linear-gradient(to right, #4D61FF, #5B5CE5) !important; border-radius: 1rem !important; font-weight: 700 !important; box-shadow: 0 8px 24px -4px rgba(77,97,255,0.35) !important; }
[data-testid="stColumn"]:has(.tp-auth-card-marker) div.stButton > button[kind="secondary"] { background: #F43F8E !important; color: #ffffff !important; border: none !important; border-radius: 1rem !important; font-weight: 700 !important; box-shadow: 0 8px 24px -4px rgba(244,63,142,0.35) !important; }
[data-testid="stColumn"]:has(.tp-auth-card-marker) div.stButton > button[kind="secondary"]:hover { background: #E83E8C !important; color: #ffffff !important; }
[data-testid="stColumn"]:has(.tp-auth-card-marker) div.stButton > button[kind="secondary"] p { color: #ffffff !important; }
[data-testid="stColumn"]:has(.tp-auth-card-marker) input[type="checkbox"] { accent-color: #4D61FF !important; width: 1rem; height: 1rem; }
.tp-trust { display: flex; align-items: center; justify-content: center; gap: 0.6rem; font-size: 0.68rem; font-weight: 600; color: #64748b !important; margin-top: 1rem; flex-wrap: wrap; }
/* Teacher portal top nav (Stitch TopNavigation) */
.tp-nav { display: flex; align-items: center; justify-content: space-between; gap: 0.75rem; padding: 0.4rem 0.1rem 0.1rem 0.1rem; }
.tp-nav-brand { display: flex; align-items: center; gap: 0.65rem; }
.tp-nav-logo { width: 2.75rem; height: 2.75rem; background: #FFDF00; border: 2px solid #0f172a; border-radius: 1rem; display: inline-flex; align-items: center; justify-content: center; box-shadow: 3px 3px 0px #0f172a; transform: rotate(-4deg); font-size: 1.35rem; }
/* Real Logo.png variants: drop the emoji chip chrome, show the emblem itself */
.stitch-logo--img, .tp-nav-logo--img { width: auto !important; height: auto !important; background: transparent !important; border: none !important; box-shadow: none !important; transform: none !important; font-size: 0 !important; }
.stitch-logo--img img { display: block; height: 3.1rem; width: auto; }
.tp-nav-logo--img img { display: block; height: 2.9rem; width: auto; }
.tp-nav-name { font-weight: 900; font-size: 1.2rem; letter-spacing: -0.02em; color: #0f172a !important; line-height: 1; }
.tp-nav-name span { color: #4D61FF !important; }
.tp-nav-sub { font-size: 0.6rem; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: #64748b !important; margin-top: 0.2rem; }
.tp-live { display: inline-flex; align-items: center; gap: 0.45rem; background: rgba(255,255,255,0.9); border: 1px solid #e2e8f0; border-radius: 9999px; padding: 0.35rem 0.8rem; font-size: 0.7rem; font-weight: 700; color: #0f172a !important; box-shadow: 0 1px 2px rgba(15,23,42,0.06); }
.tp-live-dot { width: 0.5rem; height: 0.5rem; border-radius: 9999px; background: #10b981; animation: lumina-pulse 1.6s ease-in-out infinite; }
.tp-back { text-align: center; margin: 0.35rem 0 0.8rem 0; }
.tp-back span { font-size: 0.75rem; font-weight: 600; color: #475569 !important; text-decoration: underline; text-underline-offset: 3px; }
.lumina-footer { text-align: center; padding: 1.2rem 1rem 0.3rem 1rem; }
.lumina-footer small { color: #94a3b8 !important; font-size: 0.75rem; }
a { color: #4f46e5 !important; }
@media (max-width: 640px) {
  .block-container { padding-left: 1rem !important; padding-right: 1rem !important; }
  .lumina-brand-title { font-size: 1.7rem !important; }
}
</style>
"""


def style_base_layout():
    st.markdown(_LUMINA_CSS, unsafe_allow_html=True)


def style_background_home():
    # Canvas driven by _LUMINA_CSS (#faf8ff + indigo radial per Stitch code.html body).
    st.markdown("<style>.stApp{background-color:#faf8ff !important;}</style>", unsafe_allow_html=True)


def style_background_dashboard():
    style_background_home()


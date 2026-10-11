
import streamlit as st

st.set_page_config(page_title="Snap Class - AI Attendance", layout="centered")

from src.screen.home_screen import home_screen
from src.screen.student_screen import student_screen
from src.screen.teacher_screen import teacher_screen

def main():
    if "login_type" not in st.session_state:
        home_screen()
    else:
        match st.session_state['login_type']:
            case "teacher":
                teacher_screen()
            case "student":
                student_screen()
            case None | _:
                home_screen()

if __name__ == "__main__":
    main()


import streamlit as st

from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen

from src.components.dialog_auto_enroll import auto_enroll_dialog

def main():
    st.set_page_config(
        page_title='SnapClass - Making Attendance faster using AI',
        page_icon= "https://i.ibb.co/YTYGn5qV/logo.png"
    )
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()

        case 'student':
            student_screen()
        
        case None:
            home_screen()


    join_code = st.query_params.get('join-code')
    if join_code:
        if st.session_state.login_type != 'student':
            st.session_state.login_type = 'student'
            st.rerun()
        if st.session_state.get('is_logged_in') and st.session_state.get('user_role') == 'student':
            auto_enroll_dialog(join_code)
main()


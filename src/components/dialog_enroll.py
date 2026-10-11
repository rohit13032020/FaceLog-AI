import streamlit as st
from src.database.db import (
    enroll_student_to_subject,
    lookup_subject_by_code,
    check_enrollment,
)

import time


@st.dialog("Enroll in Subject")
def enroll_dialog():
    st.write('Enter the subject code provided by your teacher to enroll')
    join_code = st.text_input('Subject Code', placeholder='Eg. CS101')

    if st.button('Enroll now', type='primary', width='stretch'):
        if join_code:
            res, _ = lookup_subject_by_code(join_code, 'subject_id, name, subject_code')
            if res.data:
                subject = res.data[0]
                student_id = st.session_state.student_data['student_id']

                check = check_enrollment(subject['subject_id'], student_id)
                if check.data:
                    st.warning('You are already enrolled in this program')
                else:
                    enroll_student_to_subject(student_id, subject['subject_id'])
                    st.success('Succesfully enrolled!')
                    time.sleep(1)
                    st.rerun()
        else:
            st.warning('Please enter a subject code')
import streamlit as st
import time

from src.database.db import (
    enroll_student_to_subject,
    lookup_subject_by_code,
    check_enrollment,
)


@st.dialog("Quick Enrollment")
def enroll_dialog():

    student_id = st.session_state.student_data["student_id"]

    # Step 1: Enter the subject code
    with st.form("subject_enrollment_form"):

        subject_code = st.text_input(
            "Enter Subject Code",
            placeholder="e.g. CS101",
        ).strip()

        find_subject = st.form_submit_button(
            "Find Subject",
            type="primary",
            width="stretch",
        )

    # Step 2: Find the subject in the database
    if find_subject:

        if not subject_code:
            st.warning("Please enter a subject code.")

        else:
            try:
                res, _ = lookup_subject_by_code(
                    subject_code,
                    "subject_id, name",
                )

                if not res or not res.data:
                    st.error("Subject code not found. Please check the code.")

                    st.session_state.pop(
                        "enroll_subject_to_confirm", None
                    )

                else:
                    subject = res.data[0]

                    check = check_enrollment(
                        subject["subject_id"],
                        student_id,
                    )

                    if check and check.data:
                        st.info("You are already enrolled in this subject.")

                        st.session_state.pop(
                            "enroll_subject_to_confirm", None
                        )

                    else:
                        st.session_state[
                            "enroll_subject_to_confirm"
                        ] = subject

            except Exception as e:
                st.error(f"Unable to find the subject: {e}")

    # Step 3: Show the subject and ask for confirmation
    subject = st.session_state.get("enroll_subject_to_confirm")

    if subject:

        st.divider()

        st.subheader("Subject Found")

        st.write(f"**Subject Name:** {subject['name']}")

        st.write("Would you like to enroll in this subject?")

        col1, col2 = st.columns(2)

        # Cancel enrollment
        with col1:
            if st.button(
                "Cancel",
                width="stretch",
            ):
                st.session_state.pop(
                    "enroll_subject_to_confirm", None
                )
                st.session_state.pop("enroll_subject_code", None)
                st.session_state["show_enroll_dialog"] = False
                st.rerun()

        # Confirm enrollment
        with col2:
            if st.button(
                "Yes, enroll now!",
                type="primary",
                width="stretch",
            ):
                try:
                    enroll_student_to_subject(
                        student_id,
                        subject["subject_id"],
                    )

                    st.session_state.pop(
                        "enroll_subject_to_confirm", None
                    )
                    st.session_state.pop("enroll_subject_code", None)
                    st.session_state["show_enroll_dialog"] = False

                    st.toast("Successfully enrolled in the subject!")

                    time.sleep(1)
                    st.rerun()

                except Exception as e:
                    st.error(f"Enrollment failed: {e}")


auto_enroll_dialog = enroll_dialog

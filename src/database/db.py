from src.database.config import supabase
import bcrypt
import streamlit as st


def _handle_db_error(e, op: str):
    raw = e.args[0] if e.args and isinstance(e.args[0], dict) else {}
    if isinstance(raw, dict):
        msg = raw.get("message") or str(e)
        code = raw.get("code") or getattr(e, "code", None)
        details = raw.get("details") or raw.get("hint") or ""
    else:
        msg = str(e)
        code = getattr(e, "code", None)
        details = getattr(e, "message", None) or getattr(e, "details", None) or ""
        if details == msg:
            details = ""
    # postgrest APIError often carries .message / .details / .code
    hint = ""
    blob = f"{msg} {details} {code or ''}"
    if (code == "42P01" or "does not exist" in blob
            or "Could not find the table" in blob):
        hint = f" A table required by '{op}' was not found — check Supabase Dashboard > Table Editor."
    elif ("Invalid API key" in blob or "API key" in blob
          or "401" in blob or "403" in blob or "PGRST" in blob
          or "JWT" in blob or "expired" in blob.lower()):
        hint = (" Supabase rejected the API key. In Dashboard > Project Settings > API, copy the"
                " `anon public` JWT (starts with `eyJ`) into SUPABASE_KEY, then `pip install -U supabase`."
                " `sb_secret_*` keys need a recent supabase-py.")
    elif "RLS" in blob or "row-level security" in blob or "permission" in blob.lower():
        hint = (" Row-Level Security blocked the request — in Dashboard > Authentication > Policies,"
                " add a SELECT (+INSERT for registration) policy on the app tables, or use a service_role key server-side.")
    full = f"Database error during {op} [{code or 'no-code'}]: {msg}"
    if details:
        full += f" | details: {details}"
    full += f".{hint}"
    st.error(full)
    # Raise (don't return []) so @st.cache_resource does NOT cache this
    # failure as a valid empty result — next run will retry the DB.
    raise RuntimeError(full) from e



def _warn_db_error(e, op: str) -> list:
    """Show the DB error as a non-fatal message and return [] so the page survives."""
    try:
        _handle_db_error(e, op)
    except RuntimeError:
        pass
    return []


def hash_pass(pwd):
    return bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()


def check_pass(pwd, hashed):
    return bcrypt.checkpw(pwd.encode(), hashed.encode())


# ---- Canonical table names (confirmed against the live Supabase schema) ----
T_TEACHER = "teacher"
T_STUDENT = "student"
T_SUBJECT = "subject"
T_SUBJECT_STUDENT = "subject_student"
T_ATTENDANCE = "attendance_logs"

# Fallback candidates in case some tables are still plural in Supabase.
# _exec_first_available() tries each until one is found (ignores PGRST205).
_TABLE_FALLBACKS = {
    T_TEACHER: [T_TEACHER, "teachers"],
    T_STUDENT: [T_STUDENT, "students"],
    T_SUBJECT: [T_SUBJECT, "subjects"],
    T_SUBJECT_STUDENT: [T_SUBJECT_STUDENT, "subject_students"],
    T_ATTENDANCE: [T_ATTENDANCE, "attendance_log"],
}


def _is_missing_table_error(e) -> bool:
    """True if the exception is a PGRST205 missing-table error."""
    raw = e.args[0] if e.args and isinstance(e.args[0], dict) else {}
    if not isinstance(raw, dict):
        raw = {}
    code = raw.get("code") or getattr(e, "code", "") or ""
    msg = raw.get("message") or getattr(e, "message", "") or ""
    hint = raw.get("hint") or getattr(e, "hint", "") or ""
    blob = f"{code} {msg} {hint} {e}"
    return "PGRST205" in blob or "Could not find the table" in blob


def _exec_first_available(build_fn, candidates):
    """build_fn(table_name) -> request-builder. Tries candidates on PGRST205."""
    last = None
    for t in candidates:
        try:
            return build_fn(t).execute(), t
        except Exception as e:
            if _is_missing_table_error(e) and t != candidates[-1]:
                last = e
                continue
            raise
    raise last


def _resolve_tables(link_key, single_key):
    """Return (link_table, single_table) that exist, trying singular then plural."""
    plural = {"subject_student": "subject_students",
              "subject": "subjects", "student": "students"}
    for link_t, single_t in [(link_key, single_key),
                             (plural.get(link_key, link_key),
                              plural.get(single_key, single_key))]:
        try:
            supabase.table(link_t).select("*").limit(0).execute()
            return link_t, single_t
        except Exception as e:
            if _is_missing_table_error(e):
                continue
            raise
    return link_key, single_key


def fetch_enrolled_students(subject_id):
    """subject_student rows joined with student, singular/plural safe. Join key normalised to 'student'."""
    link_t, single_t = _resolve_tables(T_SUBJECT_STUDENT, T_STUDENT)
    for lt, st in [(link_t, single_t), ("subject_students", "students")]:
        try:
            res = supabase.table(lt).select(f"*, {st}(*)").eq("subject_id", subject_id).execute()
            rows = res.data or []
            for r in rows:
                if "students" in r and "student" not in r:
                    r["student"] = r.pop("students")
                elif st not in ("student", "students") and st in r and "student" not in r:
                    r["student"] = r.pop(st)
            return rows
        except Exception as e:
            if _is_missing_table_error(e) and lt != "subject_students":
                continue
            raise
    return []


def lookup_subject_by_code(subject_code, columns="subject_id, name"):
    for subj_t in [T_SUBJECT, "subjects"]:
        try:
            return supabase.table(subj_t).select(columns).eq("subject_code", subject_code).execute(), subj_t
        except Exception as e:
            if _is_missing_table_error(e) and subj_t != "subjects":
                continue
            raise


def check_enrollment(subject_id, student_id):
    link_t, _ = _resolve_tables(T_SUBJECT_STUDENT, T_STUDENT)
    for lt in [link_t, "subject_students"]:
        try:
            return supabase.table(lt).select("*").eq("subject_id", subject_id).eq("student_id", student_id).execute()
        except Exception as e:
            if _is_missing_table_error(e) and lt != "subject_students":
                continue
            raise


def check_teacher_exists(username):
    # Check for unique username, returns false when username is already taken
    response, _ = _exec_first_available(
        lambda t: supabase.table(t).select("username").eq("username", username),
        _TABLE_FALLBACKS[T_TEACHER])
    return len(response.data) > 0 



def create_teacher(username, password, name):

    data = { "username" : username, "password": hash_pass(password), "name": name}
    response, _ = _exec_first_available(
        lambda t: supabase.table(t).insert(data),
        _TABLE_FALLBACKS[T_TEACHER])
    return response.data


def teacher_login(username, password):
    response, _ = _exec_first_available(
        lambda t: supabase.table(t).select("*").eq("username", username),
        _TABLE_FALLBACKS[T_TEACHER])
    if response.data:
        teacher = response.data[0]
        if check_pass(password, teacher['password']):
            return teacher
    return None


def get_all_students():
    try:
        response, _ = _exec_first_available(
            lambda t: supabase.table(t).select("*"),
            _TABLE_FALLBACKS[T_STUDENT])
        return response.data
    except Exception as e:
        return _handle_db_error(e, "get_all_students")

def create_student(new_name, face_embedding=None, voice_embedding=None):
    data = {'name': new_name, 'face_embedding':face_embedding, "voice_embedding": voice_embedding}
    response, _ = _exec_first_available(
        lambda t: supabase.table(t).insert(data),
        _TABLE_FALLBACKS[T_STUDENT])
    return response.data


def create_subject(subject_code, name, section, teacher_id):
    data = {"subject_code": subject_code, "name": name, "section": section, "teacher_id": teacher_id}
    response, _ = _exec_first_available(
        lambda t: supabase.table(t).insert(data),
        _TABLE_FALLBACKS[T_SUBJECT])
    return response.data

def get_teacher_subjects(teacher_id):
    combos = [(T_SUBJECT, T_SUBJECT_STUDENT, T_ATTENDANCE)]
    for subj_t, link_t, log_t in combos:
        try:
            response = supabase.table(subj_t).select(f"*, {link_t}(count), {log_t}(timestamp)").eq("teacher_id", teacher_id).execute()
            subjects = response.data


            for sub in subjects:
                sub['total_students'] = sub.get(link_t, [{}])[0].get('count', 0) if sub.get(link_t) else 0
                attendance = sub.get(log_t, [])
                unique_sessions = len(set(log['timestamp'] for log in attendance))
                sub['total_classes'] = unique_sessions


                sub.pop(link_t, None)
                sub.pop(log_t, None)

            return subjects
        except Exception as e:
            if _is_missing_table_error(e):
                continue
            _handle_db_error(e, "get_teacher_subjects")
    return []


def  enroll_student_to_subject(student_id, subject_id):
    data = {'student_id': student_id, "subject_id": subject_id}
    response, _ = _exec_first_available(
        lambda t: supabase.table(t).insert(data),
        _TABLE_FALLBACKS[T_SUBJECT_STUDENT])
    return response.data


def  unenroll_student_to_subject(student_id, subject_id):
    response, _ = _exec_first_available(
        lambda t: supabase.table(t).delete().eq('student_id', student_id).eq('subject_id', subject_id),
        _TABLE_FALLBACKS[T_SUBJECT_STUDENT])
    return response.data



def get_student_subjects(student_id):
    try:
        response = (supabase.table(T_SUBJECT_STUDENT)
                    .select(f'*, {T_SUBJECT}(*)')
                    .eq('student_id', student_id)
                    .execute())
        return [_norm_join(r, "subject") for r in (response.data or [])]
    except Exception as e:
        # Non-fatal: dashboard must still render if this read fails.
        return _warn_db_error(e, "get_student_subjects")


def _norm_join(row, singular: str):
    """Ensure both singular and plural join keys exist for caller-proof access."""
    plural = singular + "s"
    if singular in row and plural not in row:
        row[plural] = row[singular]
    elif plural in row and singular not in row:
        row[singular] = row[plural]
    return row


def get_student_attendance(student_id):
    try:
        response = (supabase.table(T_ATTENDANCE)
                    .select(f'*, {T_SUBJECT}(*)')
                    .eq('student_id', student_id)
                    .execute())
        return [_norm_join(r, "subject") for r in (response.data or [])]
    except Exception as e:
        # Non-fatal: student dashboard renders with zero attendance instead of crashing.
        return _warn_db_error(e, "get_student_attendance")



def create_attendance(logs):
    response, _ = _exec_first_available(
        lambda t: supabase.table(t).insert(logs),
        _TABLE_FALLBACKS[T_ATTENDANCE])
    return response.data

def get_attendance_for_teacher(teacher_id):
    try:
        response = (supabase.table(T_ATTENDANCE)
                    .select(f"*, {T_SUBJECT}!inner(*)")
                    .eq(f'{T_SUBJECT}.teacher_id', teacher_id)
                    .execute())
        return [_norm_join(r, "subject") for r in (response.data or [])]
    except Exception as e:
        # Non-fatal: records tab shows an error box instead of killing the app.
        return _warn_db_error(e, "get_attendance_for_teacher")


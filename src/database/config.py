import os

import streamlit as st
from supabase import create_client, Client


def _get_secret(name: str, *fallbacks: str):
    try:
        val = st.secrets.get(name)
        if val:
            return str(val).strip()
    except Exception:
        pass
    env_val = os.getenv(name)
    if env_val:
        return env_val.strip()
    for alt in fallbacks:
        try:
            val = st.secrets.get(alt)
            if val:
                return str(val).strip()
        except Exception:
            pass
        env_val = os.getenv(alt)
        if env_val:
            return env_val.strip()
    return None


SUPABASE_URL = _get_secret("SUPABASE_URL")
SUPABASE_KEY = _get_secret("SUPABASE_KEY", "SUPABASE_ANON_KEY", "SUPABASE_PUBLISHABLE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    st.error(
        "Missing Supabase credentials. Add to `.streamlit/secrets.toml`:\n\n"
        'SUPABASE_URL = "https://your-project.supabase.co"\n'
        'SUPABASE_KEY = "your-anon-or-publishable-key"'
    )
    st.stop()

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
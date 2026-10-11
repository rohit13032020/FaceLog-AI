"""Shared brand assets — single source for Logo.png used on Home + Teacher."""
from __future__ import annotations

import base64
import io
from pathlib import Path

import streamlit as st

_ASSETS = Path(__file__).parent.parent / "UI" / "assets"
LOGO_PATH = _ASSETS / "Logo.png"

_FALLBACK_EMOJI = "&#128248;"


@st.cache_data(show_spinner=False)
def get_logo_data_uri(max_size: int = 256) -> str | None:
    """Return a resized data-URI for Logo.png, or None if missing.

    Resized with Pillow so we don't inject the full 3.4MB file on every rerun.
    """
    try:
        if not LOGO_PATH.exists():
            return None
        from PIL import Image

        with Image.open(LOGO_PATH) as img:
            img = img.convert("RGBA")
            img.thumbnail((max_size, max_size), Image.LANCZOS)
            buf = io.BytesIO()
            img.save(buf, format="PNG")
        b64 = base64.b64encode(buf.getvalue()).decode("ascii")
        return f"data:image/png;base64,{b64}"
    except Exception:
        return None


def hero_logo_html(size: int = 56) -> str:
    """Centered hero logo HTML — same on Home and Teacher pages."""
    uri = get_logo_data_uri()
    if uri:
        return (
            f"<div><div class='snap-hero-logo'>"
            f"<img src='{uri}' alt='Snap Class logo' "
            f"height='{size}' /></div></div>"
        )
    return f"<div><div class='snap-hero-logo'>{_FALLBACK_EMOJI}</div></div>"


def emblem_html() -> str:
    """Small nav emblem HTML — same asset, smaller resize."""
    uri = get_logo_data_uri(max_size=256)
    if uri:
        return (
            f"<div class='tp-emblem'>"
            f"<img src='{uri}' alt='Snap Class logo' height='36' /></div>"
        )
    return f"<div class='tp-emblem'>{_FALLBACK_EMOJI}</div>"

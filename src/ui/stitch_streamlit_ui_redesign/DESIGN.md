---
name: Snap Class Lumina
colors:
  surface: '#faf8ff'
  surface-dim: '#d2d9f4'
  surface-bright: '#faf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f3ff'
  surface-container: '#eaedff'
  surface-container-high: '#e2e7ff'
  surface-container-highest: '#dae2fd'
  on-surface: '#131b2e'
  on-surface-variant: '#464554'
  inverse-surface: '#283044'
  inverse-on-surface: '#eef0ff'
  outline: '#767586'
  outline-variant: '#c7c4d7'
  surface-tint: '#494bd6'
  primary: '#4648d4'
  on-primary: '#ffffff'
  primary-container: '#6063ee'
  on-primary-container: '#fffbff'
  inverse-primary: '#c0c1ff'
  secondary: '#6b38d4'
  on-secondary: '#ffffff'
  secondary-container: '#8455ef'
  on-secondary-container: '#fffbff'
  tertiary: '#006c49'
  on-tertiary: '#ffffff'
  tertiary-container: '#00885d'
  on-tertiary-container: '#000703'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e1e0ff'
  primary-fixed-dim: '#c0c1ff'
  on-primary-fixed: '#07006c'
  on-primary-fixed-variant: '#2f2ebe'
  secondary-fixed: '#e9ddff'
  secondary-fixed-dim: '#d0bcff'
  on-secondary-fixed: '#23005c'
  on-secondary-fixed-variant: '#5516be'
  tertiary-fixed: '#6ffbbe'
  tertiary-fixed-dim: '#4edea3'
  on-tertiary-fixed: '#002113'
  on-tertiary-fixed-variant: '#005236'
  background: '#faf8ff'
  on-background: '#131b2e'
  surface-variant: '#dae2fd'
typography:
  headline-xl:
    fontFamily: Plus Jakarta Sans
    fontSize: 3rem
    fontWeight: '800'
    lineHeight: 3.5rem
    letterSpacing: -0.03em
  headline-xl-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 2rem
    fontWeight: '800'
    lineHeight: 2.5rem
    letterSpacing: -0.025em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 2.25rem
    fontWeight: '700'
    lineHeight: 2.75rem
    letterSpacing: -0.025em
  headline-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 1.625rem
    fontWeight: '700'
    lineHeight: 2.125rem
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 1.5rem
    fontWeight: '600'
    lineHeight: 2rem
    letterSpacing: -0.02em
  headline-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 1.25rem
    fontWeight: '600'
    lineHeight: 1.75rem
    letterSpacing: -0.015em
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 1.125rem
    fontWeight: '400'
    lineHeight: 1.75rem
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 1rem
    fontWeight: '400'
    lineHeight: 1.5rem
  body-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 0.875rem
    fontWeight: '400'
    lineHeight: 1.25rem
  label-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 0.875rem
    fontWeight: '600'
    lineHeight: 1.25rem
    letterSpacing: 0.01em
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 0.75rem
    fontWeight: '600'
    lineHeight: 1rem
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 0.6875rem
    fontWeight: '700'
    lineHeight: 0.875rem
    letterSpacing: 0.04em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1.5rem
  gutter-sm: 1rem
  margin: 2rem
  margin-sm: 1rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
---

## Brand & Style
The design system embodies the efficiency, clarity, and precision of modern automated attendance tracking. It pairs an approachable, institutional reliability with the progressive energy of artificial intelligence. Designed for educators, administrators, and students, the interface prioritizes effortless visual scanning, rapid status comprehension, and reduced cognitive load during high-tempo classroom transitions.

The design movement combines **Modern SaaS Minimalism** with **Refined Frosted Glassmorphism**. Clean, elevated structural hierarchy meets luminous, semi-translucent card components over airy, tinted canvases. Rather than heavy novelty glass, the system utilizes subtle diffusion, micro-borders, and disciplined gradient energy to highlight primary calls-to-action, scan confirmations, and critical operational metrics.

## Colors
The color palette establishes an authoritative, high-contrast visual architecture grounded in cool slate neutrals, punctuated by energetic digital accents.

- **Primary & Secondary (`#6366f1` Indigo to `#8b5cf6` Violet):** Drives primary user action, active scanning states, recognition pulses, and forward navigation. Used independently or merged into a directional 135-degree gradient (`linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)`).
- **Tertiary (`#10b981` Emerald):** Serves as the primary indicator for confirmed presence, positive face matches, and active sync states. Paired with an electric sky blue (`#0284c7`) for secondary info tags.
- **Neutrals & Surfaces:**
  - Base canvas: `#f8fafc` grading dynamically into `#f1f5f9`.
  - Frosted surface layers: `rgba(255, 255, 255, 0.85)` with fallback solid `#ffffff`.
  - Borders and structure lines: Subtle slate `#e2e8f0` with focused accents at `#cbd5e1`.
  - Typography: Deep slate navy `#0f172a` for display headings and high-priority figures, `#334155` for standard text and metadata, and `#64748b` for subtle timestamps, hints, and placeholder text.

## Typography
Plus Jakarta Sans is utilized across all levels to balance geometric clarity with human warmth. Its generous x-height and clear letterforms remain legible on quick-glance tablet wall mounts, mobile inspection views, and complex desktop rosters.

- **Headlines:** Use heavy weights (`700` and `800`) with tight letter spacing for numerical statistics, recognition ratios, and class titles.
- **Data & Tables:** Body sizes (`body-md` and `body-sm`) retain strict numeric tabular alignment where appropriate to preserve column consistency in attendance matrices.
- **Labels & Micro-indicators:** Rendered in semi-bold and bold weights with slightly expanded tracking to provide clarity across miniature face-tag chips and attendance badges.

## Layout & Spacing
The layout follows a fluid-grid structure configured around a 12-column system for wide-screen dashboards, collapsing into an 8-column layout for tablets, and a 4-column stack for mobile scanning views.

- **Breakpoints:**
  - **Desktop (>= 1280px):** 12-column layout, `margin: 2.5rem`, `gutter: 1.5rem`. Max container width spans 1440px.
  - **Tablet / Smart Display (768px – 1279px):** 8-column layout, `margin: 1.5rem`, `gutter: 1rem`. Focus on dynamic split-screens (real-time camera viewfinder on left, participant roster on right).
  - **Mobile (< 768px):** 4-column layout, `margin: 1rem`, `gutter: 0.75rem`. Full-width card stacking with bottom-sheet modals for student drill-downs.

All structural element offsets, component internal paddings, and card gaps adhere to an 8-point base spatial rhythm (`0.25rem`, `0.5rem`, `1rem`, `1.5rem`, `2.5rem`).

## Elevation & Depth
Depth in the system is created through a synergy of frosted glass transparency, subtle edge illumination, and multi-layered, low-opacity ambient shadows.

- **Surface Translucency:** Card containers apply `background: rgba(255, 255, 255, 0.85)` over the `#f8fafc` canvas, backed by `backdrop-filter: blur(12px)`.
- **Micro-borders:** Every surface layer is framed by a 1px solid border of `#e2e8f0` (or `rgba(226, 232, 240, 0.8)`), establishing defined geometric edges against light-tinted backgrounds.
- **Ambient Shadow Tiers:**
  - **Tier 1 (Resting Cards, Metrics):** `0 1px 3px 0 rgba(15, 23, 42, 0.04), 0 4px 12px -2px rgba(15, 23, 42, 0.03)`.
  - **Tier 2 (Interactive Cards, Hover States):** `0 4px 6px -1px rgba(99, 102, 241, 0.06), 0 12px 24px -4px rgba(15, 23, 42, 0.06)`.
  - **Tier 3 (Floating Overlays, Detection Viewers, Modals):** `0 20px 35px -5px rgba(15, 23, 42, 0.08), 0 10px 15px -5px rgba(15, 23, 42, 0.04)`.
- **Active Detection Layer:** When an AI facial detection box or verified state triggers, the element casts a localized glow: `0 0 0 2px #6366f1, 0 8px 20px -2px rgba(99, 102, 241, 0.25)`.

## Shapes
The visual identity relies on level-2 (`Rounded`) geometry, presenting friendly, approachable curves that prevent clinical sterility while preserving crisp technical alignment.

- **Base Radius (0.5rem / 8px):** Standard inputs, status badges, buttons, tooltips, and table row groupings.
- **Large Radius (1rem / 16px):** Metric panels, video feed wrappers, live attendee cards, and modal dialogs.
- **Extra-Large Radius (1.5rem / 24px):** Primary app navigation sidebars, high-level summary cards, and ambient glass sheets.
- **Pill (Full Rounding):** Student status pills, filter toggles, live state counters, and avatar indicators.

## Components

### Buttons
- **Primary:** High-impact gradient background (`linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)`), white label text (`#ffffff`), `box-shadow: 0 4px 12px rgba(99, 102, 241, 0.25)`. On hover, slight brightness uplift and y-axis translation of -1px.
- **Secondary:** Surface white (`#ffffff`), border 1px solid `#e2e8f0`, text `#334155`. Hover shifts border to `#cbd5e1` with subtle background tint `#f8fafc`.
- **Ghost:** Transparent background, slate navy text `#334155`, soft background hover state (`rgba(226, 232, 240, 0.4)`).

### Chips & Status Badges
- **Present / Verified:** Emerald background (`#ecfdf5`), border 1px solid (`#a7f3d0`), emerald text (`#065f46`), dot indicator (`#10b981`).
- **Processing / AI Scan:** Indigo background (`#eef2ff`), border 1px solid (`#c7d2fe`), indigo text (`#3730a3`), optional pulsing indicator.
- **Absent / Flagged:** Rose background (`#fff1f2`), border 1px solid (`#fecdd3`), rose text (`#9f1239`).
- **Late / Review:** Amber background (`#fffbeb`), border 1px solid (`#fde68a`), amber text (`#92400e`).

### Cards & Glass Surfaces
- Built on `rgba(255, 255, 255, 0.85)` with `backdrop-filter: blur(12px)` and 1px border `#e2e8f0`.
- Padding transitions cleanly from `space-md` on mobile to `space-lg` on wide screens.

### Inputs & Form Fields
- Crisp `#ffffff` base, 1px solid `#e2e8f0` border, `rounded-md` (8px). Placeholder text `#64748b`.
- Active focus state: border shifts to `#6366f1` with an outer focus ring `box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.15)`.

### Checkboxes & Radio Buttons
- Custom square/circle controls with `#ffffff` fill and 1.5px border in `#cbd5e1`.
- Checked state fills with `#6366f1` displaying a sharp white SVG check or inner circle.

### Lists & Attendee Rosters
- Dividers use ultra-faint borders (`rgba(226, 232, 240, 0.6)`).
- Alternate row highlights or hover states shift to `rgba(241, 245, 249, 0.6)`. Rows feature avatar frames with subtle 1.5px rings signaling verification status.

### Camera HUD & AI Scan Bounding Boxes
- Video viewport encapsulated with `rounded-xl`, overlaid with semi-transparent scan frames.
- Identified faces utilize a rounded target box bounded by `#6366f1` with attached pill metadata displaying student name and confidence score (`#0f172a` text on frosted white pill).
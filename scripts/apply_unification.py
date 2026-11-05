import re
import os

BASE_DIR = "/Users/radha/.gemini/antigravity/scratch/shiksha-sopan-redesign"

# Dictionary of active keys per page
PAGES = {
    'index.html': 'home',
    'executive-committee.html': 'ec',
    'activity.html': 'activity',
    'contribution.html': 'contribution',
    'achievements.html': 'achievements',
    'experiments.html': 'experiments',
    'about-us.html': 'about',
    'contact-us.html': 'contact'
}

UNIFIED_HEADER_CSS = """
    /* Main Brand Header Banner (Uniform Blueprint Grid Theme Matching Home Page) */
    .header-banner-wrapper {
      background: #F0F8FF;
      background-image: 
        radial-gradient(circle at 15% 50%, rgba(2, 132, 199, 0.09) 0%, transparent 60%),
        radial-gradient(circle at 85% 50%, rgba(0, 229, 255, 0.07) 0%, transparent 50%),
        linear-gradient(to right, rgba(2, 132, 199, 0.08) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(2, 132, 199, 0.08) 1px, transparent 1px);
      background-size: 100% 100%, 100% 100%, 32px 32px, 32px 32px;
      border-bottom: 1.5px solid var(--border-subtle, #E2E8F0);
      padding: 0.95rem 0;
      box-shadow: 0 2px 6px rgba(2, 132, 199, 0.04);
      position: relative;
      overflow: hidden;
    }

    .header-watermark-formula {
      position: absolute;
      top: 18px;
      right: 18%;
      transform: rotate(8deg);
      font-family: 'Outfit', monospace;
      font-size: 0.85rem;
      font-weight: 700;
      color: rgba(2, 132, 199, 0.22);
      pointer-events: none;
      user-select: none;
      z-index: 0;
    }

    .header-branding-flex {
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: relative;
      z-index: 1;
    }

    .brand-logo-combo {
      display: flex;
      align-items: center;
      gap: 1.25rem;
      text-decoration: none;
      color: inherit;
    }

    .brand-emblem-svg {
      width: 56px;
      height: 56px;
      flex-shrink: 0;
      transition: transform var(--transition-fast, 0.15s ease);
    }
    .brand-logo-combo:hover .brand-emblem-svg {
      transform: rotate(5deg) scale(1.04);
    }

    .brand-title-box {
      display: flex;
      flex-direction: column;
    }

    .brand-main-title {
      font-size: 1.55rem;
      font-weight: 850;
      color: var(--sopan-iitk-navy, #0B192C);
      letter-spacing: -0.02em;
      line-height: 1.15;
    }

    .brand-main-title span.hindi {
      font-family: 'Mukta', sans-serif;
      color: var(--sopan-orange, #EA580C);
      font-size: 1.45rem;
      font-weight: 800;
      margin-left: 0.35rem;
    }

    .brand-tagline-sub {
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--sopan-blue-dark, #0369A1);
      margin-top: 0.2rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .brand-tagline-sub::before {
      content: '⚡';
      font-size: 0.75rem;
    }

    .header-actions-group {
      display: flex;
      align-items: center;
      gap: 1rem;
    }

    .lang-toggle-box {
      display: flex;
      align-items: center;
      background: rgba(255, 255, 255, 0.9);
      border: 1px solid var(--border-subtle, #E2E8F0);
      border-radius: var(--radius-full, 9999px);
      padding: 3px;
      box-shadow: 0 1px 4px rgba(15, 23, 42, 0.04);
    }

    .lang-btn {
      border: none;
      background: transparent;
      padding: 0.35rem 0.85rem;
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--text-secondary, #475569);
      border-radius: var(--radius-full, 9999px);
      cursor: pointer;
      transition: all var(--transition-fast, 0.15s ease);
    }

    .lang-btn.active {
      background: #0284C7;
      color: #FFFFFF;
      box-shadow: 0 1px 4px rgba(2, 132, 199, 0.25);
    }

    /* ==========================================================================
       3. NAVIGATION BAR (STICKY, UNIFORM PILL ACTIVE INDICATOR)
       ========================================================================== */
    .navbar-sticky {
      position: sticky;
      top: 0;
      z-index: 50;
      background: rgba(255, 255, 255, 0.96);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border-bottom: 2px solid var(--border-subtle, #E2E8F0);
      box-shadow: 0 2px 10px rgba(15, 39, 74, 0.05);
    }

    .nav-inner-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      height: 54px;
    }

    .nav-links-menu {
      display: flex;
      align-items: center;
      gap: 0.35rem;
      list-style: none;
      overflow-x: auto;
      scrollbar-width: none;
    }
    .nav-links-menu::-webkit-scrollbar { display: none; }

    .nav-link-btn {
      font-size: 0.825rem;
      font-weight: 700;
      letter-spacing: 0.03em;
      text-transform: uppercase;
      color: var(--text-secondary, #475569);
      text-decoration: none;
      padding: 0.5rem 0.85rem;
      border-radius: var(--radius-sm, 8px);
      transition: all var(--transition-fast, 0.15s ease);
      white-space: nowrap;
      display: inline-block;
    }

    .nav-link-btn:hover {
      color: var(--sopan-blue-dark, #0369A1);
      background: rgba(2, 132, 199, 0.08);
    }

    .nav-link-btn.active {
      color: #0369A1 !important;
      background: #E0F2FE !important;
      font-weight: 800 !important;
    }

    .btn-join-us {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      background: var(--sopan-orange, #EA580C);
      color: #FFFFFF;
      font-size: 0.825rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      padding: 0.55rem 1.35rem;
      border-radius: var(--radius-full, 9999px);
      box-shadow: 0 4px 12px rgba(234, 88, 12, 0.28);
      transition: all var(--transition-standard, 0.2s ease);
      flex-shrink: 0;
      text-decoration: none;
    }

    .btn-join-us:hover {
      background: var(--sopan-orange-hover, #C2410C);
      transform: translateY(-1px);
      color: #FFFFFF;
    }
"""

def make_header_markup(active_page):
    active_flags = {
        'home': 'active' if active_page == 'home' else '',
        'ec': 'active' if active_page == 'ec' else '',
        'activity': 'active' if active_page == 'activity' else '',
        'contribution': 'active' if active_page == 'contribution' else '',
        'achievements': 'active' if active_page == 'achievements' else '',
        'experiments': 'active' if active_page == 'experiments' else '',
        'about': 'active' if active_page == 'about' else '',
        'contact': 'active' if active_page == 'contact' else ''
    }

    return f"""<aside class="top-motto-bar" aria-label="Motto Bar">
    <div class="container motto-content" data-i18n="mottoText">
      <img src="https://www.shiksha-sopan.org/Images/Icons/lamp.png" alt="Deep Lamp" class="lamp-icon-img" onerror="this.src='data:image/svg+xml,<svg xmlns=\\'http://www.w3.org/2000/svg\\' viewBox=\\'0 0 24 24\\' fill=\\'%23EA580C\\'><path d=\\'M12 2c1.5 2 3 4.5 3 7a3 3 0 0 1-6 0c0-2.5 1.5-5 3-7zm-7 13c0 3 3 5 7 5s7-2 7-5H5z\\'/></svg>'" />
      <span>अंधकार को क्यों धिक्कारें, अच्छा हैं एक दीप जलायें</span>
      <img src="https://www.shiksha-sopan.org/Images/Icons/lamp.png" alt="Deep Lamp" class="lamp-icon-img" onerror="this.src='data:image/svg+xml,<svg xmlns=\\'http://www.w3.org/2000/svg\\' viewBox=\\'0 0 24 24\\' fill=\\'%23EA580C\\'><path d=\\'M12 2c1.5 2 3 4.5 3 7a3 3 0 0 1-6 0c0-2.5 1.5-5 3-7zm-7 13c0 3 3 5 7 5s7-2 7-5H5z\\'/></svg>'" />
    </div>
  </aside>

  <!-- =======================================================================
       2. HEADER BRANDING & LANGUAGE SWITCHER (BLUEPRINT GRAPH & WATERMARK)
       ======================================================================= -->
  <header class="header-banner-wrapper">
    <div class="header-watermark-formula" aria-hidden="true">∇ × E = -∂B/∂t</div>
    <div class="container header-branding-flex">
      <a href="index.html" class="brand-logo-combo" aria-label="Shiksha Sopan Home">
        <svg class="brand-emblem-svg" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
          <circle cx="50" cy="50" r="46" fill="#F0F8FF" stroke="#BAE6FD" stroke-width="1.5"/>
          <ellipse cx="50" cy="52" rx="36" ry="14" stroke="#0284C7" stroke-width="2.2" stroke-dasharray="5 3" transform="rotate(-28 50 52)"/>
          <circle cx="20" cy="38" r="3.5" fill="#0EA5E9"/>
          <ellipse cx="50" cy="52" rx="36" ry="14" stroke="#EA580C" stroke-width="2.2" stroke-dasharray="5 3" transform="rotate(28 50 52)"/>
          <circle cx="80" cy="38" r="3.5" fill="#EA580C"/>
          <path d="M26 66 C 36 78, 64 78, 74 66 C 70 79, 58 84, 50 84 C 42 84, 30 79, 26 66 Z" fill="#EA580C"/>
          <path d="M24 64 C 36 70, 64 70, 76 64 C 74 67, 60 72, 50 72 C 40 72, 26 67, 24 64 Z" fill="#C2410C"/>
          <path d="M50 24 C 58 38, 62 52, 50 64 C 38 52, 42 38, 50 24 Z" fill="url(#flameGradH)"/>
          <path d="M50 36 C 54 44, 56 52, 50 60 C 44 52, 46 44, 50 36 Z" fill="#FEF08A"/>
          <defs>
            <linearGradient id="flameGradH" x1="50" y1="24" x2="50" y2="64" gradientUnits="userSpaceOnUse">
              <stop stop-color="#F59E0B"/>
              <stop offset="0.6" stop-color="#EA580C"/>
              <stop offset="1" stop-color="#DC2626"/>
            </linearGradient>
          </defs>
        </svg>

        <div class="brand-title-box">
          <div class="brand-main-title">
            SHIKSHA SOPAN <span class="hindi">शिक्षा सोपान</span>
          </div>
          <div class="brand-tagline-sub" data-i18n="headerSub">
            AN EDUCATIONAL & SOCIAL INITIATIVE BY IIT KANPUR COMMUNITY
          </div>
        </div>
      </a>

      <div class="header-actions-group">
        <div class="lang-toggle-box" role="radiogroup" aria-label="Language Selector">
          <button type="button" class="lang-btn active" id="btnLangEn" data-lang="en" onclick="setLanguage('en')">English</button>
          <button type="button" class="lang-btn" id="btnLangHi" data-lang="hi" onclick="setLanguage('hi')">हिन्दी</button>
        </div>
      </div>
    </div>
  </header>

  <!-- =======================================================================
       3. NAVIGATION BAR (EXACT UNIFIED LAYOUT & ACTIVE INDICATOR)
       ======================================================================= -->
  <nav class="navbar-sticky" aria-label="Main Navigation">
    <div class="container nav-inner-row">
      <ul class="nav-links-menu">
        <li><a href="index.html" class="nav-link-btn {active_flags['home']}" data-i18n="navHome">Home</a></li>
        <li><a href="executive-committee.html" class="nav-link-btn {active_flags['ec']}" data-i18n="navEC">Executive Committee</a></li>
        <li><a href="activity.html" class="nav-link-btn {active_flags['activity']}" data-i18n="navActivity">Activity</a></li>
        <li><a href="contribution.html" class="nav-link-btn {active_flags['contribution']}" data-i18n="navContribution">Contribution</a></li>
        <li><a href="achievements.html" class="nav-link-btn {active_flags['achievements']}" data-i18n="navAchievements">Achivements</a></li>
        <li><a href="experiments.html" class="nav-link-btn {active_flags['experiments']}" data-i18n="navExperiments">Experiments</a></li>
        <li><a href="about-us.html" class="nav-link-btn {active_flags['about']}" data-i18n="navAbout">About Us</a></li>
        <li><a href="contact-us.html" class="nav-link-btn {active_flags['contact']}" data-i18n="navContact">Contact Us</a></li>
      </ul>

      <a href="https://www.shiksha-sopan.org/join" class="btn-join-us" target="_blank" rel="noopener noreferrer" data-i18n="joinBtn">
        Join Us →
      </a>
    </div>
  </nav>"""

for fname, pkey in PAGES.items():
    fpath = os.path.join(BASE_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Replace the header and nav block
    header_pattern = r'(<(?:aside|div)\s+class=[\"\']top-motto-bar[\"\'].*?</nav>)'
    new_header = make_header_markup(pkey)
    if re.search(header_pattern, content, re.DOTALL):
        content = re.sub(header_pattern, new_header, content, count=1, flags=re.DOTALL)
    else:
        print(f"Warning: header pattern not matched in {fname}")

    # 2. Inject or ensure uniform header & nav CSS
    # Add UNIFIED_HEADER_CSS right before </style>
    if "/* Main Brand Header Banner (Uniform Blueprint Grid Theme" not in content:
        content = content.replace("</style>", UNIFIED_HEADER_CSS + "\n  </style>")

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Applied unified header & navbar to {fname}")


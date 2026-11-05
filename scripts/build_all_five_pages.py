import os
import sys

BASE_DIR = "/Users/radha/.gemini/antigravity/scratch/shiksha-sopan-redesign"

def get_head(title, description, active_page):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
  <meta http-equiv="x-ua-compatible" content="ie=edge" />
  <title>{title} — Shiksha Sopan | शिक्षा सोपान</title>
  <meta name="description" content="{description}" />
  <link rel="icon" type="image/png" href="https://www.shiksha-sopan.org/Images/Icons/favicon.ico" />

  <!-- Typography: Plus Jakarta Sans, Playfair Display, and Mukta -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Mukta:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;0,800;1,600&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&display=swap" rel="stylesheet" />
"""

def get_shared_css():
    return """  <style>
    /* ==========================================================================
       1. ROOT DESIGN SYSTEM & CSS VARIABLES
       ========================================================================== */
    :root {
      --sopan-iitk-navy: #0B192C;
      --sopan-navy-card: #0F274A;
      --sopan-navy-light: #1E3A8A;
      --sopan-blue: #0284C7;
      --sopan-blue-light: #E0F2FE;
      --sopan-blue-hover: #0369A1;
      --sopan-blue-dark: #0369A1;
      --sopan-sky: #0EA5E9;
      --sopan-sky-subtle: #F0F9FF;
      --sopan-orange: #EA580C;
      --sopan-orange-hover: #C2410C;
      --sopan-gold: #D97706;
      --sopan-gold-light: #FEF3C7;
      --sopan-gold-border: #FDE68A;

      --bg-page: #FDFEFE;
      --bg-card: #FFFFFF;
      --bg-subtle: #F8FAFC;
      --border-subtle: #E2E8F0;
      --border-light: #CBD5E1;
      --border-focus: #38BDF8;

      --text-primary: #0F172A;
      --text-secondary: #334155;
      --text-muted: #64748B;
      --text-light: #F8FAFC;

      --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.05);
      --shadow-md: 0 4px 14px -1px rgba(11, 25, 44, 0.07);
      --shadow-lg: 0 10px 25px -3px rgba(11, 25, 44, 0.09);
      --shadow-card: 0 8px 24px -4px rgba(2, 132, 199, 0.08);
      --radius-sm: 6px;
      --radius-md: 10px;
      --radius-lg: 16px;
      --radius-xl: 22px;
      --radius-full: 9999px;

      --transition-fast: 0.15s ease;
      --transition-standard: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }

    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background-color: var(--bg-page);
      color: var(--text-primary);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      overflow-x: hidden;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }

    a {
      color: inherit;
      text-decoration: none;
      transition: var(--transition-standard);
    }

    img {
      max-width: 100%;
      height: auto;
      display: block;
    }

    .container {
      width: 100%;
      max-width: 1240px;
      margin-left: auto;
      margin-right: auto;
      padding-left: 1.25rem;
      padding-right: 1.25rem;
    }

    /* ==========================================================================
       2. TOP MOTTO TICKER & BRAND HEADER (IDENTICAL ACROSS ALL PAGES)
       ========================================================================== */
    .top-motto-bar {
      background: linear-gradient(90deg, #F0F8FF 0%, #FFFFFF 50%, #F0F8FF 100%);
      border-bottom: 1px solid var(--border-subtle);
      padding: 0.45rem 1rem;
      font-size: 0.9rem;
      color: var(--text-secondary);
      display: flex;
      justify-content: center;
      align-items: center;
      position: relative;
      z-index: 51;
    }

    .motto-content {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      font-weight: 700;
      color: var(--sopan-iitk-navy);
      font-family: 'Mukta', sans-serif;
      font-size: 1.1rem;
    }

    .lamp-icon-img {
      width: 22px;
      height: 22px;
      object-fit: contain;
      filter: drop-shadow(0 0 6px rgba(234, 88, 12, 0.5));
    }

    /* Main Brand Header Banner */
    .header-banner-wrapper {
      background: #FFFFFF;
      border-bottom: 1.5px solid var(--border-subtle);
      padding: 0.95rem 0;
      box-shadow: 0 2px 6px rgba(2, 132, 199, 0.04);
    }

    .header-branding-flex {
      display: flex;
      align-items: center;
      justify-content: space-between;
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
      transition: transform var(--transition-fast);
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
      color: var(--sopan-iitk-navy);
      letter-spacing: -0.02em;
      line-height: 1.15;
    }

    .brand-main-title span.hindi {
      font-family: 'Mukta', sans-serif;
      color: var(--sopan-orange);
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
      background: var(--bg-secondary, #F8FAFC);
      border: 1px solid var(--border-subtle, #E2E8F0);
      border-radius: var(--radius-full, 9999px);
      padding: 3px;
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
      transition: all var(--transition-fast);
    }

    .lang-btn.active {
      background: #FFFFFF;
      color: var(--sopan-blue-dark, #0369A1);
      box-shadow: 0 1px 3px rgba(2, 132, 199, 0.15);
    }

    /* ==========================================================================
       3. NAVIGATION BAR (STICKY, ALL 8 LINKS PRESERVED)
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
      transition: all var(--transition-fast);
      white-space: nowrap;
      display: inline-block;
    }

    .nav-link-btn:hover, .nav-link-btn.active {
      color: var(--sopan-blue-dark, #0369A1);
      background: var(--sopan-blue-light, #E0F2FE);
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
      letter-spacing: 0.05em;
      padding: 0.55rem 1.35rem;
      border-radius: var(--radius-full);
      box-shadow: 0 4px 12px rgba(234, 88, 12, 0.28);
      transition: all var(--transition-standard);
      flex-shrink: 0;
    }

    .btn-join-us:hover {
      background: var(--sopan-orange-hover, #C2410C);
      transform: translateY(-1px);
      color: #FFFFFF;
    }

    /* ==========================================================================
       4. HERO SECTION: CONTAINED LIGHT BLUEPRINT CARD (EXACT UNIFIED STYLE)
       ========================================================================== */
    .ec-hero-section {
      position: relative;
      max-width: 980px;
      width: calc(100% - 2.5rem);
      margin: 2rem auto 1.75rem;
      background: linear-gradient(145deg, #F0F9FF 0%, #E0F2FE 45%, #F8FAFC 100%);
      color: #0F172A;
      padding: 3rem 2rem 2.5rem;
      border-radius: 22px;
      overflow: hidden;
      border: 1px solid #BAE6FD;
      border-bottom: 3.5px solid #0EA5E9;
      box-shadow: 0 12px 32px -10px rgba(2, 132, 199, 0.10), 0 4px 12px rgba(15, 23, 42, 0.03);
    }

    .ec-hero-section::before {
      content: '';
      position: absolute;
      inset: 0;
      background-image: 
        radial-gradient(circle at 12% 20%, rgba(56, 189, 248, 0.14) 0%, transparent 45%),
        radial-gradient(circle at 88% 85%, rgba(245, 158, 11, 0.08) 0%, transparent 40%),
        linear-gradient(to right, rgba(2, 132, 199, 0.05) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(2, 132, 199, 0.05) 1px, transparent 1px);
      background-size: 100% 100%, 100% 100%, 36px 36px, 36px 36px;
      pointer-events: none;
    }

    .ec-hero-content {
      position: relative;
      z-index: 2;
      max-width: 780px;
      margin: 0 auto;
      text-align: center;
    }

    .hero-eyebrow-pill {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.4rem 1.25rem;
      background: #FFFFFF;
      border: 1px solid #BAE6FD;
      border-radius: var(--radius-full);
      font-size: 0.78rem;
      font-weight: 800;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: #0284C7;
      margin-bottom: 1.25rem;
      box-shadow: 0 2px 8px rgba(2, 132, 199, 0.08);
    }

    .ec-hero-title {
      font-family: 'Playfair Display', Georgia, serif;
      font-size: clamp(2.2rem, 4.5vw, 3.4rem);
      font-weight: 800;
      letter-spacing: -0.02em;
      line-height: 1.15;
      color: #0B192C;
      margin-bottom: 0.75rem;
    }

    .ec-hero-title .hindi-sub {
      display: block;
      font-family: 'Mukta', sans-serif;
      font-size: clamp(1.25rem, 2.5vw, 1.75rem);
      font-weight: 700;
      color: #B45309;
      margin-top: 0.25rem;
      letter-spacing: 0;
    }

    .ec-hero-lead {
      font-size: clamp(0.98rem, 1.4vw, 1.1rem);
      color: #334155;
      max-width: 660px;
      margin: 0 auto 1.75rem;
      line-height: 1.7;
      font-weight: 450;
    }

    .ornamental-divider {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 1rem;
      max-width: 360px;
      margin: 0 auto;
    }

    .ornamental-line {
      flex: 1;
      height: 1px;
      background: linear-gradient(90deg, transparent, rgba(2, 132, 199, 0.35), transparent);
    }

    .ornamental-emblem {
      width: 24px;
      height: 24px;
      object-fit: contain;
      filter: drop-shadow(0 2px 4px rgba(217, 119, 6, 0.25));
    }

    /* ==========================================================================
       SITE FOOTER (UNIFIED WITH OFFICIAL MAP & BIGTECH EMBED)
       ========================================================================== */
    .site-footer {
      background: var(--sopan-iitk-navy);
      color: #94A3B8;
      padding: 4rem 0 2rem;
      margin-top: auto;
      border-top: 4px solid var(--sopan-orange);
    }

    .footer-pre-grid {
      display: grid;
      grid-template-columns: 1.3fr 1fr 1.3fr;
      gap: 2.5rem;
      padding-bottom: 3rem;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }

    @media (max-width: 900px) {
      .footer-pre-grid {
        grid-template-columns: 1fr;
        gap: 2rem;
      }
    }

    .footer-brand-title {
      font-family: 'Mukta', sans-serif;
      font-size: 1.3rem;
      font-weight: 800;
      color: #FFFFFF;
      margin-bottom: 0.75rem;
      letter-spacing: 0.02em;
    }

    .footer-brand-desc {
      font-size: 0.92rem;
      line-height: 1.65;
      color: #94A3B8;
      margin-bottom: 1rem;
    }

    .footer-bigtech-img {
      max-width: 175px;
      background: #FFFFFF;
      padding: 6px 12px;
      border-radius: 6px;
      display: inline-block;
    }

    .footer-col-title {
      font-size: 1.05rem;
      font-weight: 700;
      color: #FFFFFF;
      margin-bottom: 1.25rem;
      position: relative;
      padding-bottom: 0.5rem;
    }

    .footer-col-title::after {
      content: '';
      position: absolute;
      left: 0;
      bottom: 0;
      width: 36px;
      height: 2px;
      background: var(--sopan-orange);
    }

    .important-links-list {
      list-style: none;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.65rem 1rem;
    }

    .imp-link-anchor {
      font-size: 0.88rem;
      color: #CBD5E1;
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      transition: color var(--transition-fast);
    }

    .imp-link-anchor:hover {
      color: #38BDF8;
      transform: translateX(3px);
    }

    .map-frame-box {
      border-radius: 12px;
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.15);
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.25);
    }

    .footer-bottom-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 1rem;
      padding-top: 1.75rem;
      font-size: 0.85rem;
      color: #64748B;
    }
  </style>
"""

def get_header_and_nav(active_page):
    # active_page in ['home', 'ec', 'activity', 'contribution', 'achievements', 'experiments', 'about', 'contact']
    active_cls = {p: "active" if p == active_page else "" for p in ['home', 'ec', 'activity', 'contribution', 'achievements', 'experiments', 'about', 'contact']}
    
    return f"""  <!-- =======================================================================
       TOP MOTTO BAR & HEADER BRANDING
       ======================================================================= -->
  <div class="top-motto-bar">
    <div class="container motto-content" data-i18n="mottoText">
      <img src="https://www.shiksha-sopan.org/Images/Icons/lamp.png" alt="Lamp" class="lamp-icon-img" />
      <span>अंधकार को क्यों धिक्कारें, अच्छा हैं एक दीप जलायें</span>
      <img src="https://www.shiksha-sopan.org/Images/Icons/lamp.png" alt="Lamp" class="lamp-icon-img" />
    </div>
  </div>

  <header class="header-banner-wrapper">
    <div class="container header-branding-flex">
      <a href="index.html" class="brand-logo-combo" aria-label="Shiksha Sopan Home">
        <svg class="brand-emblem-svg" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
          <circle cx="32" cy="32" r="30" fill="url(#atomDiyaGrad)" stroke="#38BDF8" stroke-width="1.5" stroke-dasharray="3 2" />
          <defs>
            <linearGradient id="atomDiyaGrad" x1="8" y1="8" x2="56" y2="56" gradientUnits="userSpaceOnUse">
              <stop stop-color="#F0F9FF" />
              <stop offset="1" stop-color="#E0F2FE" />
            </linearGradient>
            <linearGradient id="diyaGrad" x1="20" y1="36" x2="44" y2="48" gradientUnits="userSpaceOnUse">
              <stop stop-color="#EA580C" />
              <stop offset="1" stop-color="#C2410C" />
            </linearGradient>
            <linearGradient id="flameGrad" x1="32" y1="18" x2="32" y2="34" gradientUnits="userSpaceOnUse">
              <stop stop-color="#FDE047" />
              <stop offset="0.5" stop-color="#F97316" />
              <stop offset="1" stop-color="#DC2626" />
            </linearGradient>
          </defs>
          <ellipse cx="32" cy="32" rx="25" ry="9" stroke="#0284C7" stroke-width="1.5" transform="rotate(-30 32 32)" stroke-dasharray="2 3" opacity="0.85" />
          <ellipse cx="32" cy="32" rx="25" ry="9" stroke="#0284C7" stroke-width="1.5" transform="rotate(30 32 32)" stroke-dasharray="2 3" opacity="0.85" />
          <ellipse cx="32" cy="32" rx="25" ry="9" stroke="#0EA5E9" stroke-width="1.5" transform="rotate(90 32 32)" stroke-dasharray="2 3" opacity="0.7" />
          <path d="M19 37 Q32 47 45 37 C42 45 22 45 19 37Z" fill="url(#diyaGrad)" stroke="#9A3412" stroke-width="1" />
          <path d="M32 20 C35 24 37 28 35 32 C33 34 31 34 29 32 C27 28 29 24 32 20Z" fill="url(#flameGrad)" />
          <circle cx="32" cy="29" r="2.2" fill="#FEF08A" />
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
        <div class="lang-toggle-box" role="group" aria-label="Language Selector">
          <button class="lang-btn active" id="btnLangEn" onclick="setLanguage('en')">English</button>
          <button class="lang-btn" id="btnLangHi" onclick="setLanguage('hi')">हिन्दी</button>
        </div>
      </div>
    </div>
  </header>

  <!-- =======================================================================
       STICKY NAVBAR (ALL 8 LINKS PRESERVED)
       ======================================================================= -->
  <nav class="navbar-sticky" aria-label="Main Navigation">
    <div class="container nav-inner-row">
      <ul class="nav-links-menu">
        <li><a href="index.html" class="nav-link-btn {active_cls['home']}" data-i18n="navHome">Home</a></li>
        <li><a href="executive-committee.html" class="nav-link-btn {active_cls['ec']}" data-i18n="navEC">Executive Committee</a></li>
        <li><a href="activity.html" class="nav-link-btn {active_cls['activity']}" data-i18n="navActivity">Activity</a></li>
        <li><a href="contribution.html" class="nav-link-btn {active_cls['contribution']}" data-i18n="navContribution">Contribution</a></li>
        <li><a href="achievements.html" class="nav-link-btn {active_cls['achievements']}" data-i18n="navAchievements">Achivements</a></li>
        <li><a href="experiments.html" class="nav-link-btn {active_cls['experiments']}" data-i18n="navExperiments">Experiments</a></li>
        <li><a href="about-us.html" class="nav-link-btn {active_cls['about']}" data-i18n="navAbout">About Us</a></li>
        <li><a href="contact-us.html" class="nav-link-btn {active_cls['contact']}" data-i18n="navContact">Contact Us</a></li>
      </ul>

      <a href="https://www.shiksha-sopan.org/join" class="btn-join-us" target="_blank" rel="noopener noreferrer" data-i18n="joinBtn">
        Join Us →
      </a>
    </div>
  </nav>
"""

def get_hero_card(pill_emoji, pill_text, title_en, title_hi, lead_text):
    return f"""  <main id="mainContent">
    <!-- =======================================================================
         HERO SECTION: CONTAINED LIGHT BLUEPRINT CARD
         ======================================================================= -->
    <section class="ec-hero-section" aria-labelledby="pageHeroHeading">
      <div class="container ec-hero-content">
        <div class="hero-eyebrow-pill">
          <span>{pill_emoji}</span>
          <span data-i18n="heroPill">{pill_text}</span>
        </div>

        <h1 class="ec-hero-title" id="pageHeroHeading">
          <span data-i18n="heroTitle">{title_en}</span>
          <span class="hindi-sub" data-i18n="heroTitleHi">{title_hi}</span>
        </h1>

        <p class="ec-hero-lead" data-i18n="heroLead">
          {lead_text}
        </p>

        <div class="ornamental-divider" aria-hidden="true">
          <span class="ornamental-line"></span>
          <img src="https://www.shiksha-sopan.org/Images/Icons/lamp.png" alt="Lamp" class="ornamental-emblem" />
          <span class="ornamental-line"></span>
        </div>
      </div>
    </section>
"""

def get_footer(current_active_link):
    # Returns standardized footer
    return f"""  <!-- =======================================================================
       SITE FOOTER (UNIFIED WITH OFFICIAL MAP & BIGTECH EMBED)
       ======================================================================= -->
  <footer class="site-footer" role="contentinfo">
    <div class="container">
      <div class="footer-pre-grid">
        <!-- Col 1: BigTech Partner & Info -->
        <div>
          <div class="footer-brand-title">शिक्षा सोपान | SHIKSHA SOPAN</div>
          <p class="footer-brand-desc">
            An Educational & Social Initiative by IIT Kanpur Community imparting value-based education since 2001.
          </p>
          <div style="margin-top: 1rem;">
            <img src="https://www.shiksha-sopan.org/Images/bigTech.png" alt="BigTech Partner Support" class="footer-bigtech-img" onerror="this.style.display='none'" />
          </div>
        </div>

        <!-- Col 2: Important Links (EXACT Links) -->
        <div>
          <h4 class="footer-col-title" data-i18n="impLinksHead">Important Links</h4>
          <ul class="important-links-list">
            <li><a href="index.html" class="imp-link-anchor">▸ Home</a></li>
            <li><a href="executive-committee.html" class="imp-link-anchor">▸ Executive Committee</a></li>
            <li><a href="activity.html" class="imp-link-anchor">▸ Activity</a></li>
            <li><a href="contribution.html" class="imp-link-anchor" {"style='font-weight:700; color:var(--sopan-sky);'" if current_active_link == 'contribution' else ""}>▸ Contribution</a></li>
            <li><a href="achievements.html" class="imp-link-anchor" {"style='font-weight:700; color:var(--sopan-sky);'" if current_active_link == 'achievements' else ""}>▸ Achivements</a></li>
            <li><a href="experiments.html" class="imp-link-anchor" {"style='font-weight:700; color:var(--sopan-sky);'" if current_active_link == 'experiments' else ""}>▸ Experiments</a></li>
            <li><a href="about-us.html" class="imp-link-anchor" {"style='font-weight:700; color:var(--sopan-sky);'" if current_active_link == 'about' else ""}>▸ About Us</a></li>
            <li><a href="contact-us.html" class="imp-link-anchor" {"style='font-weight:700; color:var(--sopan-sky);'" if current_active_link == 'contact' else ""}>▸ Contact Us</a></li>
            <li><a href="https://www.shiksha-sopan.org/Internship" class="imp-link-anchor" target="_blank" rel="noopener noreferrer">▸ Internship</a></li>
          </ul>
        </div>

        <!-- Col 3: Google Maps Embed (Exact from Shiksha Sopan Ashram) -->
        <div class="map-frame-box">
          <iframe 
            src="https://www.google.com/maps/embed/v1/place?key=AIzaSyA0Dx_boXQiwvdz8sJHoYeZNVTdoWONYkU&amp;q=place_id:ChIJH3A1ceM2nDkRS9JBtXLgq6A" 
            width="100%" 
            height="200" 
            style="border:0; display:block;" 
            allowfullscreen="" 
            loading="lazy" 
            title="Shiksha Sopan Location Map">
          </iframe>
        </div>
      </div>

      <div class="footer-bottom-bar">
        <div>
          <span>Copyright© 2024 shiksha-sopan.org</span>
        </div>
        <div>
          Official Portal: <a href="https://www.shiksha-sopan.org/" target="_blank" rel="noopener noreferrer" style="color:var(--sopan-sky);">shiksha-sopan.org</a>
        </div>
      </div>
    </div>
  </footer>
"""

print("Common components module ready.")

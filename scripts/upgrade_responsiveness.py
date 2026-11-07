import os
import re

BASE_DIR = "/Users/radha/.gemini/antigravity/scratch/shiksha-sopan-redesign"

FILES = [
    'index.html',
    'executive-committee.html',
    'activity.html',
    'contribution.html',
    'achievements.html',
    'experiments.html',
    'about-us.html',
    'contact-us.html',
    'functions.html',
    'finance-management.html',
    'sopan-anaupcharik-shikshan-kendra.html',
    'evening-learning-centers.html',
    'sopan-science-cell.html',
    'v-n-kulkarni-merit-scholarship.html',
    'higher-education-cell.html',
    'sushree-shashikala-joshi-memorial-sopan-library.html'
]

COMMON_RESPONSIVE_CSS = """
    /* ==========================================================================
       RESPONSIVE DESIGN SYSTEM & MOBILE NAVIGATION (ALL SCREENS & DEVICES)
       ========================================================================== */
    html, body {
      overflow-x: hidden !important;
      max-width: 100vw !important;
      width: 100% !important;
    }

    img, picture, video, canvas, svg {
      max-width: 100%;
      height: auto;
    }

    /* Mobile Hamburger Menu Toggle Button */
    .mobile-menu-toggle {
      display: none;
      background: transparent;
      border: 1px solid var(--border-subtle, #CBD5E1);
      cursor: pointer;
      padding: 0.5rem;
      flex-direction: column;
      justify-content: center;
      gap: 5px;
      width: 42px;
      height: 42px;
      border-radius: var(--radius-sm, 6px);
      transition: all var(--transition-fast, 0.15s ease);
      z-index: 101;
    }
    .mobile-menu-toggle:hover {
      background: rgba(2, 132, 199, 0.08);
      border-color: #0284C7;
    }
    .hamburger-bar {
      display: block;
      width: 22px;
      height: 2px;
      background-color: #0F172A;
      border-radius: 2px;
      transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .mobile-menu-toggle.is-open .hamburger-bar:nth-child(1) {
      transform: translateY(7px) rotate(45deg);
    }
    .mobile-menu-toggle.is-open .hamburger-bar:nth-child(2) {
      opacity: 0;
      transform: translateX(-8px);
    }
    .mobile-menu-toggle.is-open .hamburger-bar:nth-child(3) {
      transform: translateY(-7px) rotate(-45deg);
    }
    .mobile-join-item {
      display: none;
    }
    .desktop-join-btn {
      display: inline-flex;
    }

    /* TABLET & MOBILE NAVIGATION BREAKPOINT (<= 992px) */
    @media (max-width: 992px) {
      .mobile-menu-toggle {
        display: flex;
      }
      .desktop-join-btn {
        display: none !important;
      }
      .mobile-join-item {
        display: block;
        margin-top: 0.5rem;
        padding-top: 0.75rem;
        border-top: 1px solid var(--border-subtle, #E2E8F0);
      }
      .mobile-btn-join {
        width: 100% !important;
        justify-content: center !important;
        padding: 0.75rem 1rem !important;
        font-size: 0.9375rem !important;
      }
      .nav-inner-row {
        position: relative;
        justify-content: space-between;
        height: 54px;
      }
      .nav-links-menu {
        display: none;
        position: absolute;
        top: 100%;
        left: 0;
        right: 0;
        width: 100%;
        background: #FFFFFF;
        border-bottom: 2px solid #BAE6FD;
        box-shadow: 0 14px 28px -4px rgba(15, 23, 42, 0.16);
        flex-direction: column;
        align-items: stretch;
        gap: 0.35rem;
        padding: 0.85rem 1.25rem 1.25rem;
        max-height: 80vh;
        overflow-y: auto;
        z-index: 1000;
      }
      .nav-links-menu.is-active {
        display: flex;
        animation: navSlideDown 0.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      }
      .nav-link-btn {
        padding: 0.75rem 1rem !important;
        font-size: 0.9375rem !important;
        width: 100% !important;
        border-radius: var(--radius-sm, 6px);
      }
      @keyframes navSlideDown {
        from { opacity: 0; transform: translateY(-8px); }
        to { opacity: 1; transform: translateY(0); }
      }

      /* Grid & Bento Adaptations */
      .card-grid-2, .card-grid-3, .bento-grid-2, .bento-grid-3 {
        grid-template-columns: 1fr !important;
      }
      .footer-pre-grid {
        grid-template-columns: 1fr !important;
        gap: 2rem !important;
      }
      .metrics-bar-grid {
        grid-template-columns: repeat(2, 1fr) !important;
      }
    }

    /* GENERAL MOBILE DEVICES (<= 768px) */
    @media (max-width: 768px) {
      .top-motto-bar {
        font-size: 0.75rem !important;
        padding: 0.35rem 0.75rem !important;
        line-height: 1.4 !important;
      }
      .header-banner-wrapper {
        padding: 0.85rem 0 !important;
      }
      .header-branding-flex {
        flex-direction: column !important;
        gap: 0.75rem !important;
        text-align: center !important;
      }
      .brand-logo-combo {
        flex-direction: row !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 0.75rem !important;
      }
      .brand-emblem-img {
        width: 48px !important;
        height: 48px !important;
      }
      .brand-main-title {
        font-size: 1.15rem !important;
      }
      .brand-main-title .hindi {
        font-size: 1.05rem !important;
      }
      .brand-tagline-sub {
        font-size: 0.625rem !important;
        letter-spacing: 0.04em !important;
      }
      .header-watermark-formula {
        display: none !important;
      }
      .header-actions-group {
        justify-content: center !important;
      }
      .lang-btn {
        padding: 0.3rem 0.75rem !important;
        font-size: 0.72rem !important;
      }

      /* Event Cards (Functions & Subpages) */
      .event-card {
        grid-template-columns: 1fr !important;
        gap: 1rem !important;
        padding: 1.25rem !important;
      }
      .event-date-col {
        padding: 0.85rem !important;
      }

      /* Bank Box Responsive */
      .bank-box {
        padding: 1.5rem !important;
      }
      .bank-box::after {
        position: static !important;
        display: inline-block !important;
        margin-bottom: 0.75rem !important;
      }
      .bank-details-grid {
        grid-template-columns: 1fr !important;
        gap: 1rem !important;
        padding: 1rem !important;
      }
      .bank-detail-item .val {
        font-size: 1rem !important;
        word-break: break-all !important;
      }

      /* Breadcrumbs */
      .subpage-breadcrumb-bar {
        padding: 0.6rem 0 !important;
      }
      .breadcrumb-inner {
        flex-direction: column !important;
        align-items: flex-start !important;
        gap: 0.5rem !important;
      }

      /* Subpage Hero */
      .subpage-hero {
        padding: 2rem 0 1.5rem !important;
      }
      .subpage-title {
        font-size: 1.75rem !important;
      }
      .subpage-title .hindi-title {
        font-size: 1.35rem !important;
      }
      .subpage-lead {
        font-size: 1rem !important;
      }
    }

    /* SMALL MOBILE PHONES (<= 480px) */
    @media (max-width: 480px) {
      .container {
        padding: 0 0.875rem !important;
      }
      .brand-logo-combo {
        gap: 0.5rem !important;
      }
      .brand-emblem-img {
        width: 40px !important;
        height: 40px !important;
      }
      .brand-main-title {
        font-size: 1rem !important;
      }
      .brand-main-title .hindi {
        font-size: 0.95rem !important;
      }
      .brand-tagline-sub {
        font-size: 0.56rem !important;
        letter-spacing: 0.02em !important;
      }
      .top-motto-bar {
        font-size: 0.7rem !important;
        padding: 0.3rem 0.5rem !important;
      }
      .metrics-bar-grid {
        grid-template-columns: 1fr !important;
      }
      .activity-dir-grid {
        grid-template-columns: 1fr !important;
      }
    }
"""

JS_MOBILE_TOGGLE = """
    /* Responsive Mobile Navigation Toggle Handler */
    function toggleMobileNav() {
      const toggle = document.getElementById('mobileMenuToggle');
      const menu = document.getElementById('navLinksMenu');
      if (!toggle || !menu) return;
      const isOpen = toggle.classList.toggle('is-open');
      menu.classList.toggle('is-active', isOpen);
      toggle.setAttribute('aria-expanded', isOpen);
    }

    document.addEventListener('click', (e) => {
      const nav = document.querySelector('.navbar-sticky');
      const toggle = document.getElementById('mobileMenuToggle');
      const menu = document.getElementById('navLinksMenu');
      if (nav && toggle && menu && !nav.contains(e.target) && menu.classList.contains('is-active')) {
        toggle.classList.remove('is-open');
        menu.classList.remove('is-active');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
"""

def update_page_responsiveness(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update Viewport tag
    html = re.sub(
        r'<meta name=[\"\']viewport[\"\'][^>]*>',
        '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no, viewport-fit=cover" />',
        html
    )

    # 2. Update Navbar HTML
    def repl_nav(m):
        full_nav = m.group(0)
        ul_m = re.search(r'<ul class=[\"\']nav-links-menu[\"\']>(.*?)</ul>', full_nav, re.DOTALL)
        if not ul_m:
            return full_nav
        ul_content = ul_m.group(1).rstrip()
        
        # Check if already has mobile-join-item
        if 'mobile-join-item' not in ul_content:
            ul_content += '''
        <li class="mobile-join-item">
          <a href="https://www.shiksha-sopan.org/join" class="btn-join-us mobile-btn-join" target="_blank" rel="noopener noreferrer" data-i18n="joinBtn">
            Join Us →
          </a>
        </li>'''
        
        new_nav = f'''<nav class="navbar-sticky" aria-label="Main Navigation">
    <div class="container nav-inner-row">
      <button type="button" class="mobile-menu-toggle" id="mobileMenuToggle" aria-label="Toggle navigation menu" aria-expanded="false" onclick="toggleMobileNav()">
        <span class="hamburger-bar"></span>
        <span class="hamburger-bar"></span>
        <span class="hamburger-bar"></span>
      </button>

      <ul class="nav-links-menu" id="navLinksMenu">{ul_content}
      </ul>

      <a href="https://www.shiksha-sopan.org/join" class="btn-join-us desktop-join-btn" target="_blank" rel="noopener noreferrer" data-i18n="joinBtn">
        Join Us →
      </a>
    </div>
  </nav>'''
        return new_nav

    html = re.sub(r'<nav class=[\"\']navbar-sticky[\"\'].*?</nav>', repl_nav, html, flags=re.DOTALL)

    # 3. Add COMMON_RESPONSIVE_CSS to </style>
    if 'RESPONSIVE MOBILE NAVIGATION & HAMBURGER SYSTEM' not in html:
        html = html.replace('</style>', f"{COMMON_RESPONSIVE_CSS}\n  </style>")

    # 4. Add JS_MOBILE_TOGGLE to <script>
    if 'function toggleMobileNav()' not in html:
        # insert right before closing </script>
        html = html.replace('</script>', f"{JS_MOBILE_TOGGLE}\n  </script>")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Upgraded responsiveness for: {os.path.basename(filepath)}")

for fname in FILES:
    path = os.path.join(BASE_DIR, fname)
    if os.path.exists(path):
        update_page_responsiveness(path)

print("All 16 pages successfully upgraded with responsive mobile nav, hamburger toggle, and CSS media queries.")

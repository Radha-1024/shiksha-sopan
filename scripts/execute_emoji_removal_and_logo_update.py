import re
import os

BASE_DIR = "/Users/radha/.gemini/antigravity/scratch/shiksha-sopan-redesign"

FILES = [
    'index.html',
    'executive-committee.html',
    'activity.html',
    'contribution.html',
    'achievements.html',
    'experiments.html',
    'about-us.html',
    'contact-us.html'
]

# SVG replacement regex
svg_logo_pattern = re.compile(
    r'<svg class=[\"\']brand-emblem-svg[\"\'].*?</svg>',
    re.DOTALL
)

new_logo_tag = '<img src="images/shiksha-sopan-logo.jpg" alt="Shiksha Sopan Emblem" class="brand-emblem-img" />'

# CSS to ensure brand-emblem-img is beautifully rounded and styled
LOGO_CSS = """
    .brand-emblem-img {
      width: 56px;
      height: 56px;
      border-radius: 50%;
      object-fit: cover;
      box-shadow: 0 2px 8px rgba(11, 25, 44, 0.12);
      border: 1.5px solid rgba(234, 88, 12, 0.35);
      transition: transform var(--transition-fast, 0.15s ease);
      flex-shrink: 0;
    }
    .brand-logo-combo:hover .brand-emblem-img {
      transform: scale(1.05);
    }
    .ornamental-dot {
      color: #0284C7;
      font-size: 1.25rem;
      line-height: 1;
    }
"""

for fname in FILES:
    fpath = os.path.join(BASE_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as fp:
        c = fp.read()

    # 1. Replace SVG logo with the uploaded logo image
    if svg_logo_pattern.search(c):
        c = svg_logo_pattern.sub(new_logo_tag, c)
        print(f"[{fname}] Replaced SVG logo with images/shiksha-sopan-logo.jpg")

    # 2. Update favicon in <head>
    c = re.sub(
        r'<link rel=[\"\']icon[\"\'][^>]*>',
        '<link rel="icon" type="image/jpeg" href="images/shiksha-sopan-logo.jpg" />',
        c
    )

    # 3. Add brand-emblem-img CSS if not present
    if ".brand-emblem-img" not in c:
        c = c.replace("</style>", LOGO_CSS + "\n  </style>")

    # 4. Remove Deep Lamp images and emojis from Top Motto Bar
    # Replace the top motto container content
    motto_clean = '<aside class="top-motto-bar" aria-label="Motto Bar">\n    <div class="container motto-content" data-i18n="mottoText">\n      <span>अंधकार को क्यों धिक्कारें, अच्छा हैं एक दीप जलायें</span>\n    </div>\n  </aside>'
    c = re.sub(
        r'<(?:aside|div)\s+class=[\"\']top-motto-bar[\"\'].*?</(?:aside|div)>',
        motto_clean,
        c,
        flags=re.DOTALL
    )

    # Remove lamp icons from JS mottoText definitions
    c = re.sub(
        r'mottoText:\s*[\'\"].*?अंधकार को क्यों धिक्कारें.*?[\'\"]',
        'mottoText: "अंधकार को क्यों धिक्कारें, अच्छा हैं एक दीप जलायें"',
        c
    )

    # 5. Remove lightning emoji ⚡ from tagline
    c = c.replace("content: '⚡';", "content: none;")
    c = c.replace("content: '⚡'", "content: ''")
    c = c.replace("⚡ ", "")
    c = c.replace("⚡", "")

    # 6. Remove ornamental lamp stickers / emojis
    c = re.sub(
        r'<img [^>]*class=[\"\']ornamental-emblem[\"\'][^>]*>',
        '<span class="ornamental-dot">•</span>',
        c
    )
    c = re.sub(
        r'<span class=[\"\']ornamental-emblem[\"\']>🪔</span>',
        '<span class="ornamental-dot">•</span>',
        c
    )
    c = re.sub(
        r'<span class=[\"\']ornamental-emblem[\"\']>[^<]*</span>',
        '<span class="ornamental-dot">•</span>',
        c
    )

    # 7. Remove emojis from hero eyebrow pills
    c = re.sub(
        r'<div class=[\"\']hero-eyebrow-pill[\"\']>\s*<span>[^<]*</span>\s*',
        '<div class="hero-eyebrow-pill">',
        c
    )

    # 8. Clean specific emoji instances per page
    # Common emojis across pages
    replacements = [
        ('🪔', ''),
        ('<span>🏛️</span>', ''),
        ('🏛️ ', ''),
        ('🏛️', ''),
        ('<span>🌟</span>', ''),
        ('🌟 ', ''),
        ('🌟', ''),
        ('<span>📖</span>', ''),
        ('📖 ', ''),
        ('📖', ''),
        ('<span>📍</span>', ''),
        ('📍 ', ''),
        ('📍', ''),
        ('<span>🔬</span>', ''),
        ('🔬 ', ''),
        ('🔬', ''),
        ('<span>⚛️</span>', ''),
        ('⚛️ ', ''),
        ('⚛️', ''),
        ('<span>🏆</span>', ''),
        ('🏆 ', ''),
        ('🏆', ''),
        ('<span>🤝</span>', ''),
        ('🤝 ', ''),
        ('🤝', ''),
        ('<span>🌊</span>', ''),
        ('<span>🌈</span>', ''),
        ('<span>📝</span>', ''),
        ('<span>📰</span>', ''),
        ('<span>✉️</span>', '<strong>Email:</strong>'),
        ('<span>📱</span>', '<strong>Tel:</strong>'),
        ('📋 Copy Address', 'Copy Address'),
        ('📋 Copy A/c No', 'Copy A/c No'),
        ('📋 Copy IFSC', 'Copy IFSC'),
        ('📋 Copy Phone Number', 'Copy Phone Number'),
        ('📋 Copy Phone', 'Copy Phone'),
        ('📋 Copy Email', 'Copy Email'),
        ('📋 Copy Postal Address', 'Copy Postal Address'),
        ('✉️ Send Email', 'Send Email'),
        ('✓ Copied!', 'Copied!'),
        ('✓ 100% Tax Deductible', '100% Tax Deductible'),
        ('🌱 2001-02 Inception:', '2001-02 Inception:'),
        ('📈 2013-14 Outreach:', '2013-14 Outreach:'),
        ('✨ Office Maintenance Expense:', 'Office Maintenance Expense:'),
        ('<div class="open-donation-icon">💡</div>', ''),
        ('<div class="channel-icon-circle">\n              📮\n            </div>', '<div class="channel-icon-circle" style="font-size:1.1rem; font-weight:800; color:#0284C7;">01</div>'),
        ('<div class="channel-icon-circle">\n              🇮🇳\n            </div>', '<div class="channel-icon-circle" style="font-size:1.1rem; font-weight:800; color:#0284C7;">02</div>'),
        ('<div class="channel-icon-circle">\n              🌐\n            </div>', '<div class="channel-icon-circle" style="font-size:1.1rem; font-weight:800; color:#0284C7;">03</div>'),
        ('<div class="tax-shield-icon">🛡️</div>', '<div class="tax-shield-icon" style="font-size:1rem; font-weight:800; color:#059669;">80/G</div>'),
        ('💻 <span data-i18n="hgRole">', '<span data-i18n="hgRole">'),
        ('⚓ <span data-i18n="ritRole">', '<span data-i18n="ritRole">'),
        ('🛠️ <span data-i18n="dkRole">', '<span data-i18n="dkRole">'),
        ('🧪 <span data-i18n="shubRole">', '<span data-i18n="shubRole">'),
        ('<span class="search-icon-inside">🔍</span>', '<span class="search-icon-inside" style="font-size:0.75rem; font-weight:700; color:#64748B;">FIND</span>'),
        ('📁 <span data-i18n="playlistTitle">', '<span data-i18n="playlistTitle">'),
        ('▶ Watch on YouTube ↗', 'Watch on YouTube ↗'),
        ('<div class="mission-quote-title">🎯 <span', '<div class="mission-quote-title"><span'),
        ('<div class="pillar-icon-box">\n              📚\n            </div>', '<div class="pillar-icon-box" style="font-size:1.3rem; font-weight:800; color:#0284C7; font-family:Georgia,serif;">I</div>'),
        ('<div class="pillar-icon-box" style="background:#FFFBEB; border-color:#FDE68A; color:#D97706;">\n              🪔\n            </div>', '<div class="pillar-icon-box" style="background:#FFFBEB; border-color:#FDE68A; color:#D97706; font-size:1.3rem; font-weight:800; font-family:Georgia,serif;">II</div>'),
        ('<div class="pillar-icon-box" style="background:#ECFDF5; border-color:#A7F3D0; color:#059669;">\n              ⚙️\n            </div>', '<div class="pillar-icon-box" style="background:#ECFDF5; border-color:#A7F3D0; color:#059669; font-size:1.3rem; font-weight:800; font-family:Georgia,serif;">III</div>'),
        ('<div class="pane-icon-badge">📬</div>', '<div class="pane-icon-badge" style="font-size:0.85rem; font-weight:800;">POST</div>'),
        ('<div class="pane-icon-badge" style="background:#FFFBEB; border-color:#FDE68A; color:#D97706;">📞</div>', '<div class="pane-icon-badge" style="background:#FFFBEB; border-color:#FDE68A; color:#D97706; font-size:0.85rem; font-weight:800;">CALL</div>'),
        ('↺ Reset', 'Reset'),
        ('📊 NAEST-2025 Official Report (PDF)', 'NAEST-2025 Official Report (PDF)'),
        ('📄 Download 2025 Report (PDF)', 'Download 2025 Report (PDF)'),
        ('<div class="ph-icon">📸</div>', '<div class="ph-icon" style="font-size:0.85rem; font-weight:700;">VIEW</div>'),
        ('<div style="font-size: 2.5rem;">🏡🔬</div>', ''),
        ('<div style="font-size: 2.5rem;">🚌✨</div>', ''),
        ('🎯 Explore All 8 Activities & Centers →', 'Explore All 8 Activities & Centers →'),
        ('<div class="pillar-icon-badge badge-shiksha">📚</div>', '<div class="pillar-icon-badge badge-shiksha" style="font-weight:800;">I</div>'),
        ('<div class="pillar-icon-badge badge-sanskar">🙏</div>', '<div class="pillar-icon-badge badge-sanskar" style="font-weight:800;">II</div>'),
        ('<div class="pillar-icon-badge badge-swavalamban">🌱</div>', '<div class="pillar-icon-badge badge-swavalamban" style="font-weight:800;">III</div>')
    ]

    for old, new in replacements:
        c = c.replace(old, new)

    with open(fpath, "w", encoding="utf-8") as fp:
        fp.write(c)

    print(f"[{fname}] Successfully cleaned and saved.")


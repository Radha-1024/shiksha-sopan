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

for fname in FILES:
    fpath = os.path.join(BASE_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as fp:
        c = fp.read()

    # Clean any malformed mottoText in JS
    c = re.sub(
        r'mottoText:\s*["\'].*?अंधकार.*?["\'](?:[^,\n]*),?',
        'mottoText: "अंधकार को क्यों धिक्कारें, अच्छा हैं एक दीप जलायें",',
        c
    )

    # Clean 🔍 in gallery overlays and card zoom indicators
    c = c.replace('<div class="card-zoom-indicator">🔍</div>', '<div class="card-zoom-indicator">+</div>')
    c = re.sub(r'<span class=[\"\']zoom-icon[\"\']>🔍</span>', '<span class="zoom-icon">+</span>', c)
    c = c.replace('🔍', '+')

    # Clean 🏡
    c = c.replace('🏡', '')

    # Clean ✓ in thank you message
    c = c.replace('✓ Thank you!', 'Thank you!')

    # Remove unused CSS for lamp-icon-img
    c = re.sub(r'\.lamp-icon-img\s*\{[^}]*\}', '', c)

    with open(fpath, "w", encoding="utf-8") as fp:
        fp.write(c)

    print(f"Cleaned {fname}")


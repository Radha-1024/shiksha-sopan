import re
import os

BASE_DIR = "/Users/radha/.gemini/antigravity/scratch/shiksha-sopan-redesign"

replacements = [
    ('href="https://www.shiksha-sopan.org/Contribution"', 'href="contribution.html"'),
    ('href="https://www.shiksha-sopan.org/Achivements"', 'href="achievements.html"'),
    ('href="https://www.shiksha-sopan.org/Experiments"', 'href="experiments.html"'),
    ('href="https://www.shiksha-sopan.org/About-Us"', 'href="about-us.html"'),
    ('href="https://www.shiksha-sopan.org/Contact-Us"', 'href="contact-us.html"'),
    ('href="https://www.shiksha-sopan.org/" class="brand-logo-combo"', 'href="index.html" class="brand-logo-combo"')
]

# Update index.html
index_path = os.path.join(BASE_DIR, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    c = f.read()

for old, new in replacements:
    c = c.replace(old, new)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(c)
print("Updated index.html")

# Update executive-committee.html
ec_path = os.path.join(BASE_DIR, "executive-committee.html")
with open(ec_path, "r", encoding="utf-8") as f:
    c = f.read()

for old, new in replacements:
    c = c.replace(old, new)

with open(ec_path, "w", encoding="utf-8") as f:
    f.write(c)
print("Updated executive-committee.html")

# Update activity.html
act_path = os.path.join(BASE_DIR, "activity.html")
with open(act_path, "r", encoding="utf-8") as f:
    c = f.read()

for old, new in replacements:
    c = c.replace(old, new)

with open(act_path, "w", encoding="utf-8") as f:
    f.write(c)
print("Updated activity.html")


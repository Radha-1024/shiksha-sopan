# Shiksha Sopan (शिक्षा सोपान) — Modern Website Redesign

A modern, responsive, and accessible redesign of the **Shiksha Sopan** web platform (originally at [shiksha-sopan.org](https://www.shiksha-sopan.org)).

Shiksha Sopan is a non-governmental organization founded and guided by **Prof. H.C. Verma** and members of the **IIT Kanpur** community, imparting value-based education (*Shiksha, Sanskar, Swavalamban*) and experiential hands-on science learning to children from economically disadvantaged rural communities.

---

## ✨ Features & Design Highlights

- **Light STEM Aesthetic**: Bright, airy layout with clean typography (`Plus Jakarta Sans`, `Playfair Display`, `Mukta`), subtle blueprint gridlines, and mathematical watermarks (`∇ × E = -∂B/∂t`).
- **Official Branding**: Features the official circular emblem with rising sun, children climbing steps, and wheat stalk across all pages and favicons.
- **Bilingual Interface**: Built-in real-time English and Hindi switcher.
- **100% Authentic Content**: Accurately preserves all historical facts, member biographies, program details, and banking information from the official site.
- **Responsive Layout**: Designed for desktops, laptops, tablets, and smartphones.

---

## 📂 Project Architecture

```
shiksha-sopan-redesign/
├── index.html                                        # Home Page & Hero Showcase
├── executive-committee.html                          # Executive Committee & Leadership
├── activity.html                                     # Key Activities Directory
├── contribution.html                                 # Donation, Schemes & 80G Tax Exemption
├── achievements.html                                 # Milestones, NAEST & Student Honors
├── experiments.html                                  # Hands-on Physics Demonstrations & Anti-Gravity Hub
├── about-us.html                                     # Mission, History & IIT Kanpur Association
├── contact-us.html                                   # Sopan Ashram Location, Map & Contact Form
│
├── functions.html                                    # (G) Annual Function, 15th Aug & 2nd Oct Celebrations
├── finance-management.html                           # (H) Financial Transparency, Audits & Bank Details
├── sopan-anaupcharik-shikshan-kendra.html            # (A) SASK Informal Morning Primary School
├── evening-learning-centers.html                     # (B) Evening Remedial Centers (Old SAC & Barasirohi)
├── sopan-science-cell.html                           # (C) Low-Cost Physics Experiments & School Shows
├── v-n-kulkarni-merit-scholarship.html               # (D) Dr. V.N. Kulkarni Merit Scholarship (Grades 5, 8, 10)
├── higher-education-cell.html                        # (E) SGPV College & Professional Degree Grants
├── sushree-shashikala-joshi-memorial-sopan-library.html # (F) Campus Community Library
│
├── images/                                           # Official logo & photography gallery
│   ├── shiksha-sopan-logo.jpg
│   └── gallery/
├── styles.css                                        # Core design system CSS
├── app.js                                            # Bilingual translation & UI interaction engine
└── scripts/                                          # Maintenance & page generation utilities
```

---

## 🚀 Running Locally

You can serve this static website with any local HTTP server:

```bash
# Navigate to the project root
cd /path/to/shiksha-sopan-redesign

# Start a local web server (Python 3)
python3 -m http.server 8000
```

Open your browser and navigate to:
**`http://localhost:8000/index.html`**

---

## 📤 Pushing to a GitHub Repository

To push this codebase to your own GitHub repository:

1. Create a new repository on [GitHub](https://github.com/new) (e.g. `shiksha-sopan-redesign`).
2. Run the following commands in your terminal:

```bash
cd /Users/radha/.gemini/antigravity/scratch/shiksha-sopan-redesign

# Initialize Git (if not already initialized)
git init
git add .
git commit -m "feat: complete modern redesign of Shiksha Sopan platform"

# Set main branch and link your remote GitHub repository
git branch -M main
git remote add origin https://github.com/<YOUR-USERNAME>/<YOUR-REPO-NAME>.git

# Push the code
git push -u origin main
```

---

## 📜 License & Acknowledgments

- **Organization**: [Shiksha Sopan](https://www.shiksha-sopan.org)
- **Guidance**: Prof. H.C. Verma & the IIT Kanpur Community.
- Built for educational, social, and non-profit community outreach.

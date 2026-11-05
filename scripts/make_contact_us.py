import os
import build_all_five_pages as b

html_content = b.get_head("Contact Us", "Get in touch with Shiksha Sopan — email, telephone contacts, postal addresses at IIT Kanpur & Sopan Ashram, and location map.", "contact")

html_content += b.get_shared_css()

# Additional page specific CSS
html_content += """
  <style>
    /* Page Specific: Contact Us */
    .contact-content-section {
      padding: 2.5rem 0 5rem;
      background: #FFFFFF;
    }

    .section-eyebrow-center {
      text-align: center;
      margin-bottom: 2.75rem;
    }

    .section-eyebrow-tag {
      display: inline-block;
      font-size: 0.78rem;
      font-weight: 800;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--sopan-sky);
      margin-bottom: 0.5rem;
    }

    .section-main-heading {
      font-family: 'Playfair Display', Georgia, serif;
      font-size: clamp(1.8rem, 3.2vw, 2.5rem);
      font-weight: 800;
      color: var(--sopan-iitk-navy);
      line-height: 1.2;
    }

    /* Email Featured Box */
    .email-featured-card {
      background: linear-gradient(135deg, #F0F9FF 0%, #E0F2FE 100%);
      border: 1.5px solid #BAE6FD;
      border-radius: var(--radius-xl);
      padding: 2.25rem 2rem;
      text-align: center;
      box-shadow: 0 4px 18px rgba(2, 132, 199, 0.08);
      max-width: 820px;
      margin: 0 auto 3.5rem;
    }

    .email-card-title {
      font-family: 'Playfair Display', Georgia, serif;
      font-size: 1.45rem;
      font-weight: 800;
      color: var(--sopan-iitk-navy);
      margin-bottom: 0.75rem;
    }

    .email-link-main {
      font-size: clamp(1.2rem, 2.8vw, 1.65rem);
      font-weight: 800;
      color: var(--sopan-orange);
      text-decoration: none;
      display: inline-block;
      margin-bottom: 1rem;
      transition: all var(--transition-fast);
    }
    .email-link-main:hover {
      color: var(--sopan-orange-hover);
      transform: scale(1.02);
    }

    .email-actions-row {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.75rem;
    }

    .copy-pill-btn {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      background: #FFFFFF;
      border: 1px solid #CBD5E1;
      padding: 0.45rem 1.15rem;
      border-radius: var(--radius-full);
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--sopan-iitk-navy);
      cursor: pointer;
      transition: all var(--transition-fast);
    }
    .copy-pill-btn:hover {
      background: var(--sopan-blue-light);
      border-color: #BAE6FD;
      color: var(--sopan-blue-dark);
    }

    /* 2 Columns: Postal vs Telephonic */
    .contact-cols-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2.25rem;
      margin-bottom: 3.5rem;
    }

    @media (max-width: 860px) {
      .contact-cols-grid {
        grid-template-columns: 1fr;
      }
    }

    .contact-pane-card {
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-xl);
      padding: 2.25rem 2rem;
      box-shadow: 0 6px 20px rgba(15, 23, 42, 0.05);
      display: flex;
      flex-direction: column;
    }

    .pane-header-row {
      display: flex;
      align-items: center;
      gap: 1rem;
      padding-bottom: 1.25rem;
      border-bottom: 1px solid #F1F5F9;
      margin-bottom: 1.75rem;
    }

    .pane-icon-badge {
      width: 48px;
      height: 48px;
      border-radius: 14px;
      background: #F0F9FF;
      border: 1px solid #BAE6FD;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.4rem;
      color: var(--sopan-blue);
      flex-shrink: 0;
    }

    .pane-title {
      font-family: 'Playfair Display', Georgia, serif;
      font-size: 1.35rem;
      font-weight: 800;
      color: var(--sopan-iitk-navy);
    }

    .contact-item-box {
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      border-radius: var(--radius-lg);
      padding: 1.4rem 1.5rem;
      margin-bottom: 1.25rem;
      transition: all var(--transition-fast);
    }
    .contact-item-box:last-child {
      margin-bottom: 0;
    }
    .contact-item-box:hover {
      background: #FFFFFF;
      border-color: #BAE6FD;
      box-shadow: 0 4px 14px rgba(2, 132, 199, 0.08);
    }

    .contact-person-name {
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--sopan-iitk-navy);
      margin-bottom: 0.35rem;
    }

    .contact-designation {
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--sopan-orange);
      margin-bottom: 0.5rem;
    }

    .contact-details-p {
      font-size: 0.92rem;
      color: #334155;
      line-height: 1.65;
    }

    .contact-link-row {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      margin-top: 0.5rem;
      font-size: 0.9rem;
      font-weight: 700;
      color: var(--sopan-blue-dark);
    }
    .contact-link-row a:hover {
      text-decoration: underline;
    }

    /* Map Showcase Container */
    .map-showcase-card {
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-xl);
      overflow: hidden;
      box-shadow: 0 8px 24px rgba(15, 23, 42, 0.06);
    }

    .map-header-bar {
      padding: 1.25rem 1.75rem;
      background: #F8FAFC;
      border-bottom: 1px solid #E2E8F0;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 1rem;
    }

    .map-title {
      font-size: 1rem;
      font-weight: 800;
      color: var(--sopan-iitk-navy);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .map-directions-btn {
      font-size: 0.82rem;
      font-weight: 800;
      color: #FFFFFF;
      background: var(--sopan-blue-dark);
      padding: 0.45rem 1.1rem;
      border-radius: var(--radius-full);
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
    }
    .map-directions-btn:hover {
      background: var(--sopan-blue);
      color: #FFFFFF;
    }
  </style>
</head>
<body>
"""

html_content += b.get_header_and_nav("contact")

html_content += b.get_hero_card(
  "📍",
  "REACH OUT • SHIKSHA SOPAN",
  "Contact Us",
  "संपर्क करें",
  "We welcome questions, suggestions, volunteers, and visitors. Connect with our coordinators at IIT Kanpur and Sopan Ashram."
)

# Page Body Content
html_content += """
    <!-- =======================================================================
         CONTACT DIRECTORY (EXACT CONTACT DETAILS WITH EDITORIAL UI)
         ======================================================================= -->
    <section class="contact-content-section" aria-labelledby="contactListHeading">
      <div class="container">
        
        <!-- 1. Email Us @ -->
        <div class="email-featured-card">
          <h2 class="email-card-title" data-i18n="emailHead">Email Us @</h2>
          <div>
            <a href="mailto:info@shiksha-sopan.org" class="email-link-main" data-i18n="emailAddress">info@shiksha-sopan.org</a>
          </div>
          <div class="email-actions-row">
            <button class="copy-pill-btn" onclick="copyToClipboard('info@shiksha-sopan.org', this)">
              📋 Copy Email
            </button>
            <a href="mailto:info@shiksha-sopan.org" class="copy-pill-btn" style="background:var(--sopan-orange); color:#FFFFFF; border-color:var(--sopan-orange);">
              ✉️ Send Email
            </a>
          </div>
        </div>

        <!-- 2. Address for Postal Contact & Telephonic Contact (2 Columns) -->
        <div class="contact-cols-grid">
          
          <!-- Column 1: Address for Postal Contact -->
          <div class="contact-pane-card">
            <div class="pane-header-row">
              <div class="pane-icon-badge">📬</div>
              <h3 class="pane-title" data-i18n="postalHead">Address for Postal Contact</h3>
            </div>

            <!-- Postal 1: Prof. H. C. Verma -->
            <div class="contact-item-box">
              <div class="contact-person-name" data-i18n="p1Name">Prof. H. C. Verma</div>
              <p class="contact-details-p" data-i18n="p1Addr">
                12/1-3 Sopan Ashram, Chakratanpur, Nankari<br />
                IIT Kanpur, Uttar Pradesh - 208016
              </p>
              <div class="contact-link-row">
                <span>✉️</span>
                <a href="mailto:hcverma@iitk.ac.in">hcverma@iitk.ac.in</a>
              </div>
              <button class="copy-pill-btn" style="margin-top:0.6rem; font-size:0.75rem; padding:0.3rem 0.75rem;" onclick="copyToClipboard('Prof. H. C. Verma, 12/1-3 Sopan Ashram, Chakratanpur, Nankari, IIT Kanpur, Uttar Pradesh - 208016', this)">
                📋 Copy Postal Address
              </button>
            </div>

            <!-- Postal 2: Prof. Anurag Tripathi -->
            <div class="contact-item-box">
              <div class="contact-person-name" data-i18n="p2Name">Prof. Anurag Tripathi</div>
              <p class="contact-details-p" data-i18n="p2Addr">
                Department of Chemical Engineering<br />
                IIT Kanpur, Uttar Pradesh - 208016
              </p>
              <div class="contact-link-row">
                <span>✉️</span>
                <a href="mailto:anuragt@iitk.ac.in">anuragt@iitk.ac.in</a>
              </div>
              <button class="copy-pill-btn" style="margin-top:0.6rem; font-size:0.75rem; padding:0.3rem 0.75rem;" onclick="copyToClipboard('Prof. Anurag Tripathi, Department of Chemical Engineering, IIT Kanpur, Uttar Pradesh - 208016', this)">
                📋 Copy Postal Address
              </button>
            </div>
          </div>

          <!-- Column 2: For Telephonic Contact -->
          <div class="contact-pane-card">
            <div class="pane-header-row">
              <div class="pane-icon-badge" style="background:#FFFBEB; border-color:#FDE68A; color:#D97706;">📞</div>
              <h3 class="pane-title" data-i18n="phoneHead">For Telephonic Contact</h3>
            </div>

            <!-- Phone 1: Shri Ranjan Upadhyay -->
            <div class="contact-item-box">
              <div class="contact-person-name" data-i18n="t1Name">Shri Ranjan Upadhyay</div>
              <div class="contact-link-row" style="margin-top:0.65rem;">
                <span>📱</span>
                <a href="tel:+919235905046" style="color:var(--sopan-iitk-navy); font-size:1.05rem;">+91- 92359 05046</a>
              </div>
              <button class="copy-pill-btn" style="margin-top:0.6rem; font-size:0.75rem; padding:0.3rem 0.75rem;" onclick="copyToClipboard('+919235905046', this)">
                📋 Copy Phone Number
              </button>
            </div>

            <!-- Phone 2: Shri Amit Kumar Bajpai -->
            <div class="contact-item-box">
              <div class="contact-person-name" data-i18n="t2Name">Shri Amit Kumar Bajpai</div>
              <div class="contact-designation" data-i18n="t2Role">
                Chief Coordinator Public Relations - Shiksha Sopan
              </div>
              <div class="contact-link-row">
                <span>📱</span>
                <a href="tel:+919506611484" style="color:var(--sopan-iitk-navy); font-size:1.05rem;">+91-9506611484</a>
              </div>
              <div class="contact-link-row" style="margin-top:0.35rem;">
                <span>✉️</span>
                <a href="mailto:amit@shiksha-sopan.org">amit@shiksha-sopan.org</a>
              </div>
              <div style="display:flex; gap:0.5rem; flex-wrap:wrap; margin-top:0.6rem;">
                <button class="copy-pill-btn" style="font-size:0.75rem; padding:0.3rem 0.75rem;" onclick="copyToClipboard('+919506611484', this)">
                  📋 Copy Phone
                </button>
                <button class="copy-pill-btn" style="font-size:0.75rem; padding:0.3rem 0.75rem;" onclick="copyToClipboard('amit@shiksha-sopan.org', this)">
                  📋 Copy Email
                </button>
              </div>
            </div>

          </div>

        </div>

        <!-- 3. Interactive Location Map -->
        <div class="map-showcase-card">
          <div class="map-header-bar">
            <div class="map-title" data-i18n="mapTitle">
              <span>🏛️</span>
              <span>Sopan Ashram Location • Nankari, IIT Kanpur</span>
            </div>
            <a href="https://maps.google.com/?cid=12023593025268478547" target="_blank" rel="noopener noreferrer" class="map-directions-btn" data-i18n="getDirBtn">
              Get Directions ↗
            </a>
          </div>
          <iframe 
            src="https://www.google.com/maps/embed/v1/place?key=AIzaSyA0Dx_boXQiwvdz8sJHoYeZNVTdoWONYkU&amp;q=place_id:ChIJH3A1ceM2nDkRS9JBtXLgq6A" 
            width="100%" 
            height="380" 
            style="border:0; display:block;" 
            allowfullscreen="" 
            loading="lazy" 
            title="Shiksha Sopan Ashram Google Maps">
          </iframe>
        </div>

      </div>
    </section>
  </main>
"""

html_content += b.get_footer("contact")

# Bilingual JS
html_content += """
  <!-- =======================================================================
       JAVASCRIPT: BILINGUAL ENGINE & CLIPBOARD HELPER
       ======================================================================= -->
  <script>
    const contactLangDict = {
      en: {
        mottoText: '<img src="https://www.shiksha-sopan.org/Images/Icons/lamp.png" alt="Lamp" class="lamp-icon-img" /> <span>अंधकार को क्यों धिक्कारें, अच्छा हैं एक दीप जलायें</span> <img src="https://www.shiksha-sopan.org/Images/Icons/lamp.png" alt="Lamp" class="lamp-icon-img" />',
        headerSub: "AN EDUCATIONAL & SOCIAL INITIATIVE BY IIT KANPUR COMMUNITY",
        navHome: "Home",
        navEC: "Executive Committee",
        navActivity: "Activity",
        navContribution: "Contribution",
        navAchievements: "Achivements",
        navExperiments: "Experiments",
        navAbout: "About Us",
        navContact: "Contact Us",
        joinBtn: "Join Us →",
        heroPill: "REACH OUT • SHIKSHA SOPAN",
        heroTitle: "Contact Us",
        heroTitleHi: "संपर्क करें",
        heroLead: "We welcome questions, suggestions, volunteers, and visitors. Connect with our coordinators at IIT Kanpur and Sopan Ashram.",
        emailHead: "Email Us @",
        emailAddress: "info@shiksha-sopan.org",
        postalHead: "Address for Postal Contact",
        p1Name: "Prof. H. C. Verma",
        p1Addr: "12/1-3 Sopan Ashram, Chakratanpur, Nankari<br />IIT Kanpur, Uttar Pradesh - 208016",
        p2Name: "Prof. Anurag Tripathi",
        p2Addr: "Department of Chemical Engineering<br />IIT Kanpur, Uttar Pradesh - 208016",
        phoneHead: "For Telephonic Contact",
        t1Name: "Shri Ranjan Upadhyay",
        t2Name: "Shri Amit Kumar Bajpai",
        t2Role: "Chief Coordinator Public Relations - Shiksha Sopan",
        mapTitle: "Sopan Ashram Location • Nankari, IIT Kanpur",
        getDirBtn: "Get Directions ↗",
        impLinksHead: "Important Links"
      },
      hi: {
        mottoText: '<img src="https://www.shiksha-sopan.org/Images/Icons/lamp.png" alt="Lamp" class="lamp-icon-img" /> <span>अंधकार को क्यों धिक्कारें, अच्छा हैं एक दीप जलायें</span> <img src="https://www.shiksha-sopan.org/Images/Icons/lamp.png" alt="Lamp" class="lamp-icon-img" />',
        headerSub: "आईआईटी कानपुर समुदाय द्वारा संचालित शैक्षिक व सामाजिक पहल",
        navHome: "होम",
        navEC: "कार्यकारिणी समिति",
        navActivity: "गतिविधियां",
        navContribution: "सहयोग",
        navAchievements: "उपलब्धियां",
        navExperiments: "प्रयोग",
        navAbout: "हमारे बारे में",
        navContact: "संपर्क करें",
        joinBtn: "जुड़ें →",
        heroPill: "संपर्क सूत्र • शिक्षा सोपान",
        heroTitle: "संपर्क करें",
        heroTitleHi: "Contact Us",
        heroLead: "प्रश्नों, सुझावों, स्वयंसेवा एवं आश्रम भ्रमण हेतु संपर्क करें — आईआईटी कानपुर एवं सोपान आश्रम के हमारे समन्वयक सदैव उपलब्ध हैं।",
        emailHead: "ईमेल द्वारा संपर्क करें @",
        emailAddress: "info@shiksha-sopan.org",
        postalHead: "डाक द्वारा पत्राचार का पता",
        p1Name: "प्रो. एच. सी. वर्मा",
        p1Addr: "12/1-3 सोपान आश्रम, चक्रतनपुर, ननकारी<br />आईआईटी कानपुर, उत्तर प्रदेश - 208016",
        p2Name: "प्रो. अनुराग त्रिपाठी",
        p2Addr: "रासायनिक अभियांत्रिकी विभाग<br />आईआईटी कानपुर, उत्तर प्रदेश - 208016",
        phoneHead: "दूरभाष (फोन) द्वारा संपर्क",
        t1Name: "श्री रंजन उपाध्याय",
        t2Name: "श्री अमित कुमार बाजपेई",
        t2Role: "मुख्य समन्वयक जनसंपर्क - शिक्षा सोपान",
        mapTitle: "सोपान आश्रम स्थिति • ननकारी, आईआईटी कानपुर",
        getDirBtn: "दिशा-निर्देश प्राप्त करें ↗",
        impLinksHead: "महत्वपूर्ण लिंक"
      }
    };

    let currentLang = 'en';

    function setLanguage(lang) {
      currentLang = lang;
      document.getElementById('btnLangEn').classList.toggle('active', lang === 'en');
      document.getElementById('btnLangHi').classList.toggle('active', lang === 'hi');

      const dict = contactLangDict[lang];
      document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (dict[key]) {
          el.innerHTML = dict[key];
        }
      });
    }

    function copyToClipboard(text, btnElement) {
      navigator.clipboard.writeText(text).then(() => {
        const originalText = btnElement.innerHTML;
        btnElement.innerHTML = '✓ Copied!';
        btnElement.style.color = '#059669';
        btnElement.style.borderColor = '#10B981';
        setTimeout(() => {
          btnElement.innerHTML = originalText;
          btnElement.style.color = '';
          btnElement.style.borderColor = '';
        }, 2000);
      }).catch(err => {
        console.error('Copy failed', err);
      });
    }
  </script>
</body>
</html>
"""

output_path = os.path.join(b.BASE_DIR, "contact-us.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully generated {output_path} ({len(html_content)} bytes)")

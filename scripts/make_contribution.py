import os
import build_all_five_pages as b

html_content = b.get_head("Contribution", "Support Shiksha Sopan — voluntary individual contributions, endowment schemes, child sponsorships, and tax-exempt giving under Section 80/G.", "contribution")

html_content += b.get_shared_css()

# Additional page specific CSS
html_content += """
  <style>
    /* Page Specific: Contribution */
    .contribution-content-section {
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

    /* Narrative Callout Box */
    .narrative-card {
      background: linear-gradient(135deg, #F8FAFC 0%, #F0F9FF 100%);
      border: 1px solid #BAE6FD;
      border-left: 5px solid var(--sopan-blue);
      border-radius: var(--radius-lg);
      padding: 1.75rem 2rem;
      margin-bottom: 2.5rem;
      box-shadow: 0 4px 16px rgba(2, 132, 199, 0.06);
    }

    .narrative-text {
      font-size: 1.05rem;
      line-height: 1.75;
      color: #334155;
    }

    .expenditure-badge-row {
      display: flex;
      flex-wrap: wrap;
      gap: 1.25rem;
      margin-top: 1.25rem;
      padding-top: 1.25rem;
      border-top: 1px solid rgba(186, 230, 253, 0.6);
    }

    .exp-stat-pill {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: #FFFFFF;
      border: 1px solid #CBD5E1;
      padding: 0.45rem 1rem;
      border-radius: var(--radius-full);
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--sopan-iitk-navy);
    }
    .exp-stat-pill strong {
      color: var(--sopan-orange);
    }

    /* Table Design */
    .schemes-table-card {
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-xl);
      overflow: hidden;
      box-shadow: 0 8px 24px rgba(15, 23, 42, 0.05);
      margin-bottom: 2.5rem;
    }

    .table-responsive-wrapper {
      width: 100%;
      overflow-x: auto;
    }

    .schemes-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
    }

    .schemes-table thead {
      background: #F1F5F9;
      border-bottom: 2px solid #CBD5E1;
    }

    .schemes-table th {
      padding: 1.1rem 1.5rem;
      font-size: 0.85rem;
      font-weight: 800;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      color: var(--sopan-iitk-navy);
    }

    .schemes-table td {
      padding: 1.2rem 1.5rem;
      font-size: 0.96rem;
      color: #334155;
      border-bottom: 1px solid #F1F5F9;
      line-height: 1.6;
    }

    .schemes-table tbody tr:last-child td {
      border-bottom: none;
    }

    .schemes-table tbody tr:hover {
      background: #F8FAFC;
    }

    .scheme-name {
      font-weight: 750;
      color: var(--sopan-iitk-navy);
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }

    .scheme-bullet {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--sopan-sky);
      flex-shrink: 0;
    }

    .scheme-tag {
      display: inline-block;
      font-size: 0.72rem;
      font-weight: 800;
      text-transform: uppercase;
      padding: 0.2rem 0.55rem;
      border-radius: var(--radius-full);
      background: #E0F2FE;
      color: #0369A1;
      margin-left: 0.5rem;
    }

    .open-donation-banner {
      background: #FFFBEB;
      border: 1px solid #FDE68A;
      border-radius: var(--radius-lg);
      padding: 1.35rem 1.75rem;
      display: flex;
      align-items: flex-start;
      gap: 1rem;
      margin-bottom: 3.5rem;
    }

    .open-donation-icon {
      font-size: 1.5rem;
      flex-shrink: 0;
      margin-top: 0.1rem;
    }

    .open-donation-text {
      font-size: 0.98rem;
      color: #92400E;
      line-height: 1.65;
    }

    /* How to Donate 3 Cards */
    .donate-modes-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.75rem;
      margin-bottom: 3rem;
    }

    @media (max-width: 992px) {
      .donate-modes-grid {
        grid-template-columns: 1fr;
      }
    }

    .donate-channel-card {
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-xl);
      padding: 2.25rem 1.75rem 2rem;
      display: flex;
      flex-direction: column;
      box-shadow: 0 4px 18px rgba(15, 23, 42, 0.05);
      transition: all var(--transition-standard);
      position: relative;
    }

    .donate-channel-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 14px 30px rgba(2, 132, 199, 0.12);
      border-color: #BAE6FD;
    }

    .channel-icon-circle {
      width: 64px;
      height: 64px;
      border-radius: 18px;
      background: #F0F9FF;
      border: 1px solid #BAE6FD;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 1.5rem;
      color: var(--sopan-blue);
      font-size: 1.8rem;
    }

    .channel-title {
      font-family: 'Playfair Display', Georgia, serif;
      font-size: 1.35rem;
      font-weight: 750;
      color: var(--sopan-iitk-navy);
      margin-bottom: 1rem;
    }

    .channel-desc {
      font-size: 0.92rem;
      color: #475569;
      line-height: 1.7;
      flex-grow: 1;
      margin-bottom: 1.25rem;
    }

    .channel-data-box {
      background: #F8FAFC;
      border: 1px dashed #CBD5E1;
      border-radius: var(--radius-md);
      padding: 1rem;
      font-size: 0.88rem;
      color: var(--sopan-iitk-navy);
      line-height: 1.6;
    }

    .channel-data-box strong {
      color: var(--sopan-orange);
    }

    .copy-btn-action {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      margin-top: 0.65rem;
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--sopan-sky);
      background: #FFFFFF;
      border: 1px solid #BAE6FD;
      padding: 0.35rem 0.75rem;
      border-radius: var(--radius-full);
      cursor: pointer;
      transition: all var(--transition-fast);
    }
    .copy-btn-action:hover {
      background: var(--sopan-blue-light);
      color: var(--sopan-blue-dark);
    }

    /* Tax Exemption Stamp Banner */
    .tax-exemption-card {
      background: linear-gradient(135deg, #ECFDF5 0%, #D1FAE5 100%);
      border: 1.5px solid #A7F3D0;
      border-radius: var(--radius-xl);
      padding: 1.75rem 2rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 1.5rem;
      box-shadow: 0 4px 14px rgba(16, 185, 129, 0.08);
    }

    .tax-left-info {
      display: flex;
      align-items: center;
      gap: 1.25rem;
    }

    .tax-shield-icon {
      width: 52px;
      height: 52px;
      border-radius: 14px;
      background: #FFFFFF;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.6rem;
      color: #059669;
      box-shadow: 0 2px 8px rgba(5, 150, 105, 0.15);
      flex-shrink: 0;
    }

    .tax-title {
      font-size: 1.15rem;
      font-weight: 800;
      color: #065F46;
      margin-bottom: 0.25rem;
    }

    .tax-subtitle {
      font-size: 0.92rem;
      color: #047857;
      line-height: 1.5;
    }
  </style>
</head>
<body>
"""

html_content += b.get_header_and_nav("contribution")

html_content += b.get_hero_card(
  "🏛️",
  "VOLUNTARY SUPPORT • SHIKSHA SOPAN",
  "Contribution",
  "सहयोग",
  "The money needed to run Shiksha Sopan activities comes only through individual donations from its members and well wishers. So far, we have not accepted any grants from any funding agencies. All donations are Tax Free under Section 80/G."
)

# Page Body Content
html_content += """
    <!-- =======================================================================
         1. MODE OF FINANCIAL CONTRIBUTION & ENDOWMENT SCHEMES
         ======================================================================= -->
    <section class="contribution-content-section" aria-labelledby="modeContribHeading">
      <div class="container">
        
        <div class="section-eyebrow-center">
          <span class="section-eyebrow-tag" data-i18n="secTag1">FINANCIAL PHILOSOPHY & TRANSPARENCY</span>
          <h2 class="section-main-heading" id="modeContribHeading" data-i18n="modeHeading">
            Mode of Financial Contribution
          </h2>
        </div>

        <!-- Narrative & Expenditure Journey -->
        <div class="narrative-card">
          <p class="narrative-text" data-i18n="narrativeP">
            The money needed to run Shiksha Sopan activities comes only through individual donations from its members and well wishers. So far, we have not accepted any grants from any funding agencies. With ever expanding activities and expectations of the society, we need to develop certain endowment funds. Starting from a modest expenditure of Rs 22,086 in the first year, that is 2001-02, the expense in 2013-14 was about Rs 15 lacs. We look forward for donations in the following schemes.
          </p>
          <div class="expenditure-badge-row">
            <span class="exp-stat-pill">🌱 2001-02 Inception: <strong>Rs 22,086</strong></span>
            <span class="exp-stat-pill">📈 2013-14 Outreach: <strong>~Rs 15 Lacs</strong></span>
            <span class="exp-stat-pill">✨ Office Maintenance Expense: <strong>Almost Zero</strong></span>
          </div>
        </div>

        <!-- Schemes Table -->
        <div class="schemes-table-card">
          <div class="table-responsive-wrapper">
            <table class="schemes-table" aria-label="Endowment Schemes and Sponsorships">
              <thead>
                <tr>
                  <th scope="col" style="width: 45%;" data-i18n="thScheme">Scheme</th>
                  <th scope="col" style="width: 55%;" data-i18n="thTarget">Endowment Target & Details</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>
                    <div class="scheme-name">
                      <span class="scheme-bullet"></span>
                      <span data-i18n="scheme1Name">Community Library</span>
                      <span class="scheme-tag" data-i18n="tagEndowment">Endowment</span>
                    </div>
                  </td>
                  <td data-i18n="scheme1Desc">
                    Endowment fund being created, target Rs 5 lacs ($8000), presently 1 lac
                  </td>
                </tr>
                <tr>
                  <td>
                    <div class="scheme-name">
                      <span class="scheme-bullet"></span>
                      <span data-i18n="scheme2Name">Higher Education Cell</span>
                      <span class="scheme-tag" data-i18n="tagEndowment">Endowment</span>
                    </div>
                  </td>
                  <td data-i18n="scheme2Desc">
                    Endowment fund being created, target Rs10 lacs ($16,000), presently 5 lac
                  </td>
                </tr>
                <tr>
                  <td>
                    <div class="scheme-name">
                      <span class="scheme-bullet"></span>
                      <span data-i18n="scheme3Name">VNK Merit Scholarship</span>
                      <span class="scheme-tag" data-i18n="tagEndowment">Endowment</span>
                    </div>
                  </td>
                  <td data-i18n="scheme3Desc">
                    Endowment fund being created, target Rs 15 lacs ($24,000), presently 9 lacs
                  </td>
                </tr>
                <tr>
                  <td>
                    <div class="scheme-name">
                      <span class="scheme-bullet"></span>
                      <span data-i18n="scheme4Name">Creating e-Resource</span>
                      <span class="scheme-tag" style="background:#FEF3C7; color:#92400E;" data-i18n="tagAnnual">Annual</span>
                    </div>
                  </td>
                  <td data-i18n="scheme4Desc">
                    Rs 300,000 ($5000) per year
                  </td>
                </tr>
                <tr>
                  <td>
                    <div class="scheme-name">
                      <span class="scheme-bullet"></span>
                      <span data-i18n="scheme5Name">Pratibha Poshan yojana Senior</span>
                      <span class="scheme-tag" style="background:#FEF3C7; color:#92400E;" data-i18n="tagChild">Child Sponsor</span>
                    </div>
                  </td>
                  <td data-i18n="scheme5Desc">
                    Rs 8,000 ($125) Per year/per child
                  </td>
                </tr>
                <tr>
                  <td>
                    <div class="scheme-name">
                      <span class="scheme-bullet"></span>
                      <span data-i18n="scheme6Name">Shiksha Sopan Anaupacharik Shikshan Kendra</span>
                      <span class="scheme-tag" style="background:#FEF3C7; color:#92400E;" data-i18n="tagChild">Child Sponsor</span>
                    </div>
                  </td>
                  <td data-i18n="scheme6Desc">
                    Rs 4,000 ($60)Per year/per child
                  </td>
                </tr>
                <tr>
                  <td>
                    <div class="scheme-name">
                      <span class="scheme-bullet"></span>
                      <span data-i18n="scheme7Name">Evening Learning Centers</span>
                      <span class="scheme-tag" style="background:#FEF3C7; color:#92400E;" data-i18n="tagChild">Child Sponsor</span>
                    </div>
                  </td>
                  <td data-i18n="scheme7Desc">
                    Rs 2,000 ($30) Per year/per child
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- Open Donation Note Banner -->
        <div class="open-donation-banner">
          <div class="open-donation-icon">💡</div>
          <div class="open-donation-text" data-i18n="openDonationP">
            Apart from the above schemes, any open donation of any amount is gratefully accepted. These are used for cultural functions, special training classes, audit fee etc. Our office maintenance expense is almost zero.
          </div>
        </div>

        <!-- ===================================================================
             2. HOW TO DONATE (3 CHANNELS)
             =================================================================== -->
        <div class="section-eyebrow-center">
          <span class="section-eyebrow-tag" data-i18n="secTag2">PAYMENT CHANNELS & DETAILS</span>
          <h2 class="section-main-heading" data-i18n="howToDonateHeading">
            How to donate
          </h2>
        </div>

        <div class="donate-modes-grid">
          
          <!-- Channel 1: Cheques / Draft -->
          <div class="donate-channel-card">
            <div class="channel-icon-circle">
              📮
            </div>
            <h3 class="channel-title" data-i18n="chan1Title">Cheques / Draft</h3>
            <p class="channel-desc" data-i18n="chan1Desc">
              You can write Cheques/Draft for donations in the name of <strong>"Shiksha Sopan"</strong> payble at Kanpur and send to the address:
            </p>
            <div class="channel-data-box">
              <strong>Prof. H.C. Verma</strong><br />
              12/1-3 Sopan Ashram, Chakratanpur, Nankari<br />
              IIT Kanpur, Uttar Pradesh, India - 208016
              <button class="copy-btn-action" onclick="copyToClipboard('Prof. H.C. Verma, 12/1-3 Sopan Ashram, Chakratanpur, Nankari, IIT Kanpur, Uttar Pradesh, India - 208016', this)">
                📋 Copy Address
              </button>
            </div>
          </div>

          <!-- Channel 2: Indian Passport -->
          <div class="donate-channel-card">
            <div class="channel-icon-circle">
              🇮🇳
            </div>
            <h3 class="channel-title" data-i18n="chan2Title">Indian Passport</h3>
            <p class="channel-desc" data-i18n="chan2Desc">
              Online transfer for Indian Passport holders can be made in State Bank of India, IIT Kanpur branch.
            </p>
            <div class="channel-data-box">
              Account No : <strong>10426002488</strong><br />
              Account Name : <strong>Shiksha Sopan</strong><br />
              IFSC code : <strong>SBIN0001161</strong>
              <div style="display:flex; gap:0.5rem; flex-wrap:wrap; margin-top:0.5rem;">
                <button class="copy-btn-action" onclick="copyToClipboard('10426002488', this)">
                  📋 Copy A/c No
                </button>
                <button class="copy-btn-action" onclick="copyToClipboard('SBIN0001161', this)">
                  📋 Copy IFSC
                </button>
              </div>
            </div>
          </div>

          <!-- Channel 3: Non-Indian Passport -->
          <div class="donate-channel-card">
            <div class="channel-icon-circle">
              🌐
            </div>
            <h3 class="channel-title" data-i18n="chan3Title">Non-Indian Passport</h3>
            <p class="channel-desc" data-i18n="chan3Desc">
              Please do not make any transaction in the FCRA account.
            </p>
            <div class="channel-data-box" style="background:#FEF2F2; border-color:#FECACA; color:#991B1B;">
              <strong>Advisory Notice:</strong><br />
              Foreign / FCRA contributions are currently on hold as per regulatory guidelines. Please contact <a href="mailto:info@shiksha-sopan.org" style="text-decoration:underline;">info@shiksha-sopan.org</a> for prior inquiry.
            </div>
          </div>

        </div>

        <!-- 80/G Tax Exemption Card -->
        <div class="tax-exemption-card">
          <div class="tax-left-info">
            <div class="tax-shield-icon">🛡️</div>
            <div>
              <div class="tax-title" data-i18n="taxTitle">Tax Exemption under Section 80/G</div>
              <div class="tax-subtitle" data-i18n="taxSub">
                Please note that you may give any open donation, besides sponsoring a child. All donations are Tax Free under Section 80/G.
              </div>
            </div>
          </div>
          <div>
            <span style="display:inline-block; font-size:0.85rem; font-weight:800; background:#059669; color:#FFFFFF; padding:0.5rem 1.25rem; border-radius:9999px;">
              ✓ 100% Tax Deductible
            </span>
          </div>
        </div>

      </div>
    </section>
  </main>
"""

html_content += b.get_footer("contribution")

# Bilingual JS
html_content += """
  <!-- =======================================================================
       JAVASCRIPT: BILINGUAL ENGINE & CLIPBOARD HELPER
       ======================================================================= -->
  <script>
    const contLangDict = {
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
        heroPill: "VOLUNTARY SUPPORT • SHIKSHA SOPAN",
        heroTitle: "Contribution",
        heroTitleHi: "सहयोग",
        heroLead: "The money needed to run Shiksha Sopan activities comes only through individual donations from its members and well wishers. So far, we have not accepted any grants from any funding agencies. All donations are Tax Free under Section 80/G.",
        secTag1: "FINANCIAL PHILOSOPHY & TRANSPARENCY",
        modeHeading: "Mode of Financial Contribution",
        narrativeP: "The money needed to run Shiksha Sopan activities comes only through individual donations from its members and well wishers. So far, we have not accepted any grants from any funding agencies. With ever expanding activities and expectations of the society, we need to develop certain endowment funds. Starting from a modest expenditure of Rs 22,086 in the first year, that is 2001-02, the expense in 2013-14 was about Rs 15 lacs. We look forward for donations in the following schemes.",
        thScheme: "Scheme",
        thTarget: "Endowment Target & Details",
        scheme1Name: "Community Library",
        scheme1Desc: "Endowment fund being created, target Rs 5 lacs ($8000), presently 1 lac",
        scheme2Name: "Higher Education Cell",
        scheme2Desc: "Endowment fund being created, target Rs10 lacs ($16,000), presently 5 lac",
        scheme3Name: "VNK Merit Scholarship",
        scheme3Desc: "Endowment fund being created, target Rs 15 lacs ($24,000), presently 9 lacs",
        scheme4Name: "Creating e-Resource",
        scheme4Desc: "Rs 300,000 ($5000) per year",
        scheme5Name: "Pratibha Poshan yojana Senior",
        scheme5Desc: "Rs 8,000 ($125) Per year/per child",
        scheme6Name: "Shiksha Sopan Anaupacharik Shikshan Kendra",
        scheme6Desc: "Rs 4,000 ($60)Per year/per child",
        scheme7Name: "Evening Learning Centers",
        scheme7Desc: "Rs 2,000 ($30) Per year/per child",
        openDonationP: "Apart from the above schemes, any open donation of any amount is gratefully accepted. These are used for cultural functions, special training classes, audit fee etc. Our office maintenance expense is almost zero.",
        secTag2: "PAYMENT CHANNELS & DETAILS",
        howToDonateHeading: "How to donate",
        chan1Title: "Cheques / Draft",
        chan1Desc: "You can write Cheques/Draft for donations in the name of <strong>\"Shiksha Sopan\"</strong> payble at Kanpur and send to the address:",
        chan2Title: "Indian Passport",
        chan2Desc: "Online transfer for Indian Passport holders can be made in State Bank of India, IIT Kanpur branch.",
        chan3Title: "Non-Indian Passport",
        chan3Desc: "Please do not make any transaction in the FCRA account.",
        taxTitle: "Tax Exemption under Section 80/G",
        taxSub: "Please note that you may give any open donation, besides sponsoring a child. All donations are Tax Free under Section 80/G.",
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
        heroPill: "स्वैच्छिक सहयोग • शिक्षा सोपान",
        heroTitle: "सहयोग",
        heroTitleHi: "Contribution",
        heroLead: "शिक्षा सोपान की गतिविधियों के संचालन हेतु आवश्यक धनराशि केवल इसके सदस्यों एवं शुभचिंतकों के व्यक्तिगत सहयोग से प्राप्त होती है। अभी तक हमने किसी भी वित्तपोषक संस्था से अनुदान नहीं लिया है। धारा 80/G के तहत सभी दान कर-मुक्त हैं।",
        secTag1: "वित्तीय व्यवस्था एवं पारदर्शिता",
        modeHeading: "वित्तीय योगदान के माध्यम",
        narrativeP: "शिक्षा सोपान की गतिविधियों के संचालन हेतु आवश्यक धनराशि केवल इसके सदस्यों एवं शुभचिंतकों के व्यक्तिगत सहयोग से प्राप्त होती है। अब तक हमने किसी भी वित्तपोषक संस्था से कोई अनुदान स्वीकार नहीं किया है। निरंतर बढ़ती गतिविधियों और समाज की अपेक्षाओं के साथ हमें कुछ स्थायी कोष विकसित करने की आवश्यकता है। पहले वर्ष २००१-०२ में मात्र ₹२२,०८६ के व्यय से प्रारंभ होकर, २०१३-१४ में यह व्यय लगभग ₹१५ लाख था। हम निम्नलिखित योजनाओं में सहयोग का स्वागत करते हैं।",
        thScheme: "योजना",
        thTarget: "स्थायी कोष लक्ष्य एवं विवरण",
        scheme1Name: "सामुदायिक पुस्तकालय",
        scheme1Desc: "स्थायी कोष निर्माण प्रगति पर, लक्ष्य ₹५ लाख ($8000), वर्तमान में १ लाख",
        scheme2Name: "उच्च शिक्षा प्रकोष्ठ",
        scheme2Desc: "स्थायी कोष निर्माण प्रगति पर, लक्ष्य ₹१० लाख ($16,000), वर्तमान में ५ लाख",
        scheme3Name: "वी.एन. कुलकर्णी मेधा छात्रवृत्ति",
        scheme3Desc: "स्थायी कोष निर्माण प्रगति पर, लक्ष्य ₹१५ लाख ($24,000), वर्तमान में ९ लाख",
        scheme4Name: "ई-संसाधन निर्माण",
        scheme4Desc: "₹३,००,००० ($5000) प्रति वर्ष",
        scheme5Name: "प्रतिभा पोषण योजना (वरिष्ठ)",
        scheme5Desc: "₹८,००० ($125) प्रति वर्ष / प्रति छात्र",
        scheme6Name: "सोपान अनौपचारिक शिक्षण केंद्र",
        scheme6Desc: "₹४,००० ($60) प्रति वर्ष / प्रति छात्र",
        scheme7Name: "सांध्यकालीन शिक्षण केंद्र",
        scheme7Desc: "₹२,००० ($30) प्रति वर्ष / प्रति छात्र",
        openDonationP: "उपर्युक्त योजनाओं के अतिरिक्त, किसी भी धनराशि का खुला दान कृतज्ञतापूर्वक स्वीकार किया जाता है। इसका उपयोग सांस्कृतिक आयोजनों, विशेष प्रशिक्षण कक्षाओं, ऑडिट शुल्क आदि में होता है। हमारा कार्यालय रखरखाव व्यय लगभग शून्य है।",
        secTag2: "भुगतान माध्यम एवं बैंक विवरण",
        howToDonateHeading: "दान कैसे करें",
        chan1Title: "चेक / डिमांड ड्राफ्ट",
        chan1Desc: "आप चेक/ड्राफ्ट \"शिक्षा सोपान\" (Shiksha Sopan) के नाम पर कानपुर में देय बनाकर निम्नलिखित पते पर भेज सकते हैं:",
        chan2Title: "भारतीय पासपोर्ट धारक",
        chan2Desc: "भारतीय पासपोर्ट धारकों के लिए ऑनलाइन अंतरण भारतीय स्टेट बैंक (SBI), आईआईटी कानपुर शाखा में किया जा सकता है।",
        chan3Title: "गैर-भारतीय पासपोर्ट धारक",
        chan3Desc: "कृपया एफसीआरए (FCRA) खाते में कोई लेन-देन न करें।",
        taxTitle: "आयकर धारा 80/G के तहत कर छूट",
        taxSub: "कृपया ध्यान दें कि किसी बच्चे को प्रायोजित करने के अतिरिक्त आप कोई भी खुला दान दे सकते हैं। धारा 80/G के तहत सभी दान कर-मुक्त हैं।",
        impLinksHead: "महत्वपूर्ण लिंक"
      }
    };

    let currentLang = 'en';

    function setLanguage(lang) {
      currentLang = lang;
      document.getElementById('btnLangEn').classList.toggle('active', lang === 'en');
      document.getElementById('btnLangHi').classList.toggle('active', lang === 'hi');

      const dict = contLangDict[lang];
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

output_path = os.path.join(b.BASE_DIR, "contribution.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully generated {output_path} ({len(html_content)} bytes)")

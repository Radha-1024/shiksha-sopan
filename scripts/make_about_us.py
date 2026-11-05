import os
import build_all_five_pages as b

html_content = b.get_head("About Us", "About Shiksha Sopan — our motivation, genesis in 2001 at IIT Kanpur, and the three guiding pillars: Shiksha (Education), Sanskar (Values), and Swavalamban (Self-Reliance).", "about")

html_content += b.get_shared_css()

# Additional page specific CSS
html_content += """
  <style>
    /* Page Specific: About Us */
    .about-content-section {
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

    /* Motivation Split Editorial Grid */
    .motivation-grid {
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 2.5rem;
      align-items: center;
      background: linear-gradient(135deg, #F8FAFC 0%, #F0F9FF 100%);
      border: 1px solid #BAE6FD;
      border-radius: var(--radius-xl);
      padding: 2.5rem;
      box-shadow: 0 4px 20px rgba(2, 132, 199, 0.06);
      margin-bottom: 4rem;
    }

    @media (max-width: 900px) {
      .motivation-grid {
        grid-template-columns: 1fr;
        padding: 1.75rem;
      }
    }

    .motivation-narrative {
      font-size: 1.02rem;
      line-height: 1.8;
      color: #334155;
      text-align: justify;
    }

    .mission-highlight-card {
      background: #FFFFFF;
      border: 1.5px solid var(--border-subtle);
      border-left: 5px solid var(--sopan-orange);
      border-radius: var(--radius-lg);
      padding: 1.75rem;
      box-shadow: 0 8px 24px rgba(15, 23, 42, 0.05);
    }

    .mission-quote-title {
      font-size: 0.82rem;
      font-weight: 800;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--sopan-orange);
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .mission-quote-text {
      font-family: 'Playfair Display', Georgia, serif;
      font-size: 1.15rem;
      font-weight: 600;
      line-height: 1.6;
      color: var(--sopan-iitk-navy);
      font-style: italic;
    }

    /* The Three Pillars Section */
    .pillars-intro-box {
      max-width: 760px;
      margin: 0 auto 3rem;
      text-align: center;
    }

    .pillars-intro-text {
      font-size: 1.1rem;
      line-height: 1.75;
      color: #475569;
    }

    .pillars-cards-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 2rem;
    }

    @media (max-width: 992px) {
      .pillars-cards-grid {
        grid-template-columns: 1fr;
      }
    }

    .pillar-card {
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-xl);
      padding: 2.5rem 1.75rem 2rem;
      display: flex;
      flex-direction: column;
      box-shadow: 0 6px 20px rgba(15, 23, 42, 0.04);
      transition: all var(--transition-standard);
      position: relative;
    }

    .pillar-card:hover {
      transform: translateY(-5px);
      box-shadow: 0 16px 36px rgba(2, 132, 199, 0.12);
      border-color: #BAE6FD;
    }

    .pillar-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 10%;
      right: 10%;
      height: 3px;
      background: var(--sopan-blue);
      border-radius: var(--radius-full);
      opacity: 0.8;
    }

    .pillar-icon-box {
      width: 72px;
      height: 72px;
      border-radius: 20px;
      background: #F0F9FF;
      border: 1.5px solid #BAE6FD;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 1.5rem;
      font-size: 2rem;
      color: var(--sopan-blue);
      box-shadow: 0 4px 12px rgba(2, 132, 199, 0.08);
    }

    .pillar-title {
      font-family: 'Playfair Display', Georgia, serif;
      font-size: 1.6rem;
      font-weight: 800;
      color: var(--sopan-iitk-navy);
      margin-bottom: 0.25rem;
    }

    .pillar-hindi-title {
      font-family: 'Mukta', sans-serif;
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--sopan-orange);
      margin-bottom: 1.25rem;
      display: block;
    }

    .pillar-desc {
      font-size: 0.95rem;
      color: #334155;
      line-height: 1.75;
      text-align: justify;
      flex-grow: 1;
    }
  </style>
</head>
<body>
"""

html_content += b.get_header_and_nav("about")

html_content += b.get_hero_card(
  "📖",
  "GENESIS & PHILOSOPHY • SHIKSHA SOPAN",
  "About Us",
  "हमारे बारे में",
  "Education to be used as a ladder — bridging academic excellence with rural reality since 2001 through values, practical learning, and self-reliance."
)

# Page Body Content
html_content += """
    <!-- =======================================================================
         1. MOTIVATION & FOUNDING IMPULSE (2001)
         ======================================================================= -->
    <section class="about-content-section" aria-labelledby="motivationHeading">
      <div class="container">
        
        <div class="section-eyebrow-center">
          <span class="section-eyebrow-tag" data-i18n="secTag1">FOUNDATIONAL VISION & GENESIS</span>
          <h2 class="section-main-heading" id="motivationHeading" data-i18n="motHeading">
            Motivation
          </h2>
        </div>

        <div class="motivation-grid">
          <div class="motivation-narrative">
            <p data-i18n="motP1">
              It has long been felt that the present education system in our country lacks the basic elements of practical knowledge, ethical and virtuous value system. This kind of educational system is neither of much use in the life of a common villager nor does it help making him/her self-sustained or self department. Inspired by such rational thoughts, a group of IIT Kanpur students together with some socially active persons from the locality decided to overcome this bottleneck by setting up a system that would go beyond the narrow bookish education and link the education to the everyday life of students. These concepts led to the establishment of <strong style="color:var(--sopan-orange);">"Shiksha Sopan"</strong>, literally meaning 'Education to be used as a ladder' in the year 2001. To put in one sentence.
            </p>
          </div>

          <div class="mission-highlight-card">
            <div class="mission-quote-title">🎯 <span data-i18n="aimTitle">Our Core Purpose</span></div>
            <p class="mission-quote-text" data-i18n="motP2">
              “Shiksha Sopan aims to evolve educational module, in direct collaboration with the villages close to IITK campus, that will build knowledgeable, self-department, confident, socially conscious being who would be responsible and sensitive to society.”
            </p>
          </div>
        </div>

        <!-- ===================================================================
             2. THE THREE PILLARS (SHIKSHA, SANSKAR, SWAVALAMBAN)
             =================================================================== -->
        <div class="section-eyebrow-center" style="margin-top: 1rem;">
          <span class="section-eyebrow-tag" data-i18n="secTag2">CORE GUIDING PRINCIPLES</span>
          <h2 class="section-main-heading" data-i18n="pillarsHeading">
            The Three Pillars of Shiksha Sopan
          </h2>
        </div>

        <div class="pillars-intro-box">
          <p class="pillars-intro-text" data-i18n="pillarsIntro">
            The three keywords which provide the guidelines to Shiksha Sopan are <strong style="color:var(--sopan-blue);">Shiksha</strong>, <strong style="color:var(--sopan-orange);">Sanskar</strong> and <strong style="color:var(--sopan-blue-dark);">Swavalamban</strong>. Thus we work to develop models where education is not just to earn bread, but which inculcates human values and makes on self confident.
          </p>
        </div>

        <div class="pillars-cards-grid">
          
          <!-- Pillar 1: Shiksha -->
          <article class="pillar-card" aria-labelledby="pillarShikshaTitle">
            <div class="pillar-icon-box">
              📚
            </div>
            <h3 class="pillar-title" id="pillarShikshaTitle" data-i18n="pil1Title">Shiksha</h3>
            <span class="pillar-hindi-title" data-i18n="pil1Sub">शिक्षा • Balanced Practical Learning</span>
            <p class="pillar-desc" data-i18n="pil1Desc">
              Shiksha means education, not only to make machines out of people, but to produce socially sensitive, cultured and responsible citizen who will assets and not liabilities for society. Leaving aside the most commonly followed scheme of education through chalk and talk alone, a balanced delivery of knowledge through games, educational visits, audio and visual aids, demonstrations etc. is the theme on which we are trying to run our system.
            </p>
          </article>

          <!-- Pillar 2: Sanskar -->
          <article class="pillar-card" aria-labelledby="pillarSanskarTitle">
            <div class="pillar-icon-box" style="background:#FFFBEB; border-color:#FDE68A; color:#D97706;">
              🪔
            </div>
            <h3 class="pillar-title" id="pillarSanskarTitle" data-i18n="pil2Title">Sanskar</h3>
            <span class="pillar-hindi-title" style="color:#D97706;" data-i18n="pil2Sub">संस्कार • Character & Moral Values</span>
            <p class="pillar-desc" data-i18n="pil2Desc">
              Character building and inculcation of moral values to develop sense of altruism, feeling of patriotism and respect for humanity among its disciples and beneficiaries through regular practices is one of our main objectives.
            </p>
          </article>

          <!-- Pillar 3: Swavalamban -->
          <article class="pillar-card" aria-labelledby="pillarSwavalambanTitle">
            <div class="pillar-icon-box" style="background:#ECFDF5; border-color:#A7F3D0; color:#059669;">
              ⚙️
            </div>
            <h3 class="pillar-title" id="pillarSwavalambanTitle" data-i18n="pil3Title">Swavalamban</h3>
            <span class="pillar-hindi-title" style="color:#059669;" data-i18n="pil3Sub">स्वावलंबन • Dignity of Labour & Skills</span>
            <p class="pillar-desc" data-i18n="pil3Desc">
              Unemployment is one of the most serious problems of mankind. And the solution lies in developing respect for human labour. During the school education we are trying to train the students in various labour-oriented skills that will help them creating employment for themselves. These include tailoring, handicrafts and production of consumable items such as candles, notebooks, etc. Such exercise will build self confidence and respect for labour and help the student in acquiring enough expertise in at least one profession to earn live hood for himself/herself.
            </p>
          </article>

        </div>

      </div>
    </section>
  </main>
"""

html_content += b.get_footer("about")

# Bilingual JS
html_content += """
  <!-- =======================================================================
       JAVASCRIPT: BILINGUAL ENGINE
       ======================================================================= -->
  <script>
    const aboutLangDict = {
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
        heroPill: "GENESIS & PHILOSOPHY • SHIKSHA SOPAN",
        heroTitle: "About Us",
        heroTitleHi: "हमारे बारे में",
        heroLead: "Education to be used as a ladder — bridging academic excellence with rural reality since 2001 through values, practical learning, and self-reliance.",
        secTag1: "FOUNDATIONAL VISION & GENESIS",
        motHeading: "Motivation",
        motP1: "It has long been felt that the present education system in our country lacks the basic elements of practical knowledge, ethical and virtuous value system. This kind of educational system is neither of much use in the life of a common villager nor does it help making him/her self-sustained or self department. Inspired by such rational thoughts, a group of IIT Kanpur students together with some socially active persons from the locality decided to overcome this bottleneck by setting up a system that would go beyond the narrow bookish education and link the education to the everyday life of students. These concepts led to the establishment of <strong style=\"color:var(--sopan-orange);\">\"Shiksha Sopan\"</strong>, literally meaning 'Education to be used as a ladder' in the year 2001. To put in one sentence.",
        aimTitle: "Our Core Purpose",
        motP2: "“Shiksha Sopan aims to evolve educational module, in direct collaboration with the villages close to IITK campus, that will build knowledgeable, self-department, confident, socially conscious being who would be responsible and sensitive to society.”",
        secTag2: "CORE GUIDING PRINCIPLES",
        pillarsHeading: "The Three Pillars of Shiksha Sopan",
        pillarsIntro: "The three keywords which provide the guidelines to Shiksha Sopan are <strong style=\"color:var(--sopan-blue);\">Shiksha</strong>, <strong style=\"color:var(--sopan-orange);\">Sanskar</strong> and <strong style=\"color:var(--sopan-blue-dark);\">Swavalamban</strong>. Thus we work to develop models where education is not just to earn bread, but which inculcates human values and makes on self confident.",
        pil1Title: "Shiksha",
        pil1Sub: "शिक्षा • Balanced Practical Learning",
        pil1Desc: "Shiksha means education, not only to make machines out of people, but to produce socially sensitive, cultured and responsible citizen who will assets and not liabilities for society. Leaving aside the most commonly followed scheme of education through chalk and talk alone, a balanced delivery of knowledge through games, educational visits, audio and visual aids, demonstrations etc. is the theme on which we are trying to run our system.",
        pil2Title: "Sanskar",
        pil2Sub: "संस्कार • Character & Moral Values",
        pil2Desc: "Character building and inculcation of moral values to develop sense of altruism, feeling of patriotism and respect for humanity among its disciples and beneficiaries through regular practices is one of our main objectives.",
        pil3Title: "Swavalamban",
        pil3Sub: "स्वावलंबन • Dignity of Labour & Skills",
        pil3Desc: "Unemployment is one of the most serious problems of mankind. And the solution lies in developing respect for human labour. During the school education we are trying to train the students in various labour-oriented skills that will help them creating employment for themselves. These include tailoring, handicrafts and production of consumable items such as candles, notebooks, etc. Such exercise will build self confidence and respect for labour and help the student in acquiring enough expertise in at least one profession to earn live hood for himself/herself.",
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
        heroPill: "प्रेरणा एवं मूल दर्शन • शिक्षा सोपान",
        heroTitle: "हमारे बारे में",
        heroTitleHi: "About Us",
        heroLead: "शिक्षा रूपी सीढ़ी — २००१ से आईआईटी कानपुर के प्राध्यापकों व छात्रों द्वारा ग्रामीण परिवेश में व्यावहारिक ज्ञान, मानवीय संस्कार और स्वावलंबन को जोड़ने का संकल्प।",
        secTag1: "स्थापना प्रेरणा एवं उद्देश्य",
        motHeading: "प्रेरणा (Motivation)",
        motP1: "यह लंबे समय से अनुभव किया जा रहा था कि हमारे देश की वर्तमान शिक्षा प्रणाली में व्यावहारिक ज्ञान तथा नैतिक एवं मानवीय मूल्यों का अभाव है। ऐसी शिक्षा न तो किसी सामान्य ग्रामीण के जीवन में उपयोगी सिद्ध होती है और न ही उसे स्वावलंबी बनाती है। इन्हीं विचारों से प्रेरित होकर आईआईटी कानपुर के कुछ विद्यार्थियों एवं स्थानीय प्रबुद्ध नागरिकों ने इस संकीर्ण किताबी शिक्षा से आगे बढ़कर शिक्षा को जीवन से जोड़ने का निर्णय लिया। इसी विचार से वर्ष २००१ में <strong style=\"color:var(--sopan-orange);\">\"शिक्षा सोपान\"</strong> (अर्थात 'शिक्षा को सीढ़ी के रूप में उपयोग करना') की स्थापना हुई। संक्षेप में कहें तो:",
        aimTitle: "हमारा मुख्य उद्देश्य",
        motP2: "“शिक्षा सोपान का उद्देश्य आईआईटी कानपुर परिसर के निकटवर्ती गांवों के सीधे सहयोग से ऐसे शैक्षिक मॉड्यूल विकसित करना है, जिससे ज्ञानी, स्वावलंबी, आत्मविश्वासी व सामाजिक रूप से संवेदनशील नागरिक बन सकें।”",
        secTag2: "मार्गदर्शक सिद्धांत",
        pillarsHeading: "शिक्षा सोपान के तीन आधार स्तंभ",
        pillarsIntro: "शिक्षा सोपान का मार्गदर्शन करने वाले तीन मूल शब्द हैं: <strong style=\"color:var(--sopan-blue);\">शिक्षा</strong>, <strong style=\"color:var(--sopan-orange);\">संस्कार</strong> और <strong style=\"color:var(--sopan-blue-dark);\">स्वावलंबन</strong>। अतः हम ऐसे मॉडल विकसित करने के लिए कार्य करते हैं जहां शिक्षा केवल आजीविका का साधन न होकर मानवीय मूल्यों का संवर्धन करे।",
        pil1Title: "शिक्षा",
        pil1Sub: "Shiksha • सर्वांगीण व्यावहारिक ज्ञान",
        pil1Desc: "शिक्षा का अर्थ केवल मानव को मशीन बनाना नहीं, अपितु संवेदनशील, सुसंस्कृत एवं जिम्मेदार नागरिक तैयार करना है जो समाज के लिए संबल बनें। केवल चाक-और-टॉक की पारंपरिक पद्धति से परे खेल, शैक्षणिक भ्रमण, ऑडियो-विजुअल माध्यमों तथा प्रयोगों द्वारा संतुलित ज्ञान प्रदान करना हमारी कार्यपद्धति का आधार है।",
        pil2Title: "संस्कार",
        pil2Sub: "Sanskar • चरित्र निर्माण एवं राष्ट्रप्रेम",
        pil2Desc: "नियमित अभ्यासों के माध्यम से विद्यार्थियों में परोपकार की भावना, देशभक्ति तथा मानवता के प्रति आदर भाव विकसित करना और नैतिक मूल्यों से चरित्र निर्माण करना हमारा प्रमुख ध्येय है।",
        pil3Title: "स्वावलंबन",
        pil3Sub: "Swavalamban • श्रम की प्रतिष्ठा एवं आत्मनिर्भरता",
        pil3Desc: "बेरोजगारी मानव समाज की एक गंभीर समस्या है, जिसका समाधान श्रम के प्रति आदर भाव में निहित है। स्कूली शिक्षा के दौरान ही हम छात्रों को श्रम-उन्मुख कौशलों जैसे सिलाई, हस्तशिल्प तथा मोमबत्ती, नोटबुक आदि उपयोगी वस्तुओं के निर्माण का प्रशिक्षण देते हैं जिससे उनमें स्वावलंबन और कम से कम एक व्यवसाय में आत्मनिर्भरता आए।",
        impLinksHead: "महत्वपूर्ण लिंक"
      }
    };

    let currentLang = 'en';

    function setLanguage(lang) {
      currentLang = lang;
      document.getElementById('btnLangEn').classList.toggle('active', lang === 'en');
      document.getElementById('btnLangHi').classList.toggle('active', lang === 'hi');

      const dict = aboutLangDict[lang];
      document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (dict[key]) {
          el.innerHTML = dict[key];
        }
      });
    }
  </script>
</body>
</html>
"""

output_path = os.path.join(b.BASE_DIR, "about-us.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully generated {output_path} ({len(html_content)} bytes)")

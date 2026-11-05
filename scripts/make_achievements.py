import os
import build_all_five_pages as b

html_content = b.get_head("Some personal Achievements", "Inspiring personal achievements of students nurtured by Shiksha Sopan — stories of perseverance, science education, national service, and graduation.", "achievements")

html_content += b.get_shared_css()

# Additional page specific CSS
html_content += """
  <style>
    /* Page Specific: Achievements */
    .achieve-content-section {
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

    .achieve-cards-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 2rem;
    }

    @media (max-width: 860px) {
      .achieve-cards-grid {
        grid-template-columns: 1fr;
      }
    }

    .achieve-card {
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-xl);
      padding: 2.25rem 2rem;
      box-shadow: 0 4px 18px rgba(15, 23, 42, 0.05);
      transition: all var(--transition-standard);
      display: flex;
      flex-direction: column;
      position: relative;
      overflow: hidden;
    }

    .achieve-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4px;
      background: linear-gradient(90deg, var(--sopan-sky), var(--sopan-orange));
      opacity: 0.9;
    }

    .achieve-card:hover {
      transform: translateY(-5px);
      box-shadow: 0 16px 32px rgba(2, 132, 199, 0.12);
      border-color: #BAE6FD;
    }

    .card-header-flex {
      display: flex;
      align-items: center;
      gap: 1.25rem;
      margin-bottom: 1.5rem;
    }

    .avatar-initials-badge {
      width: 58px;
      height: 58px;
      border-radius: 16px;
      background: linear-gradient(135deg, #F0F9FF 0%, #E0F2FE 100%);
      border: 1.5px solid #BAE6FD;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: 'Playfair Display', Georgia, serif;
      font-size: 1.4rem;
      font-weight: 800;
      color: var(--sopan-blue-dark);
      flex-shrink: 0;
      box-shadow: 0 2px 8px rgba(2, 132, 199, 0.1);
    }

    .header-name-box {
      display: flex;
      flex-direction: column;
    }

    .student-name {
      font-family: 'Playfair Display', Georgia, serif;
      font-size: 1.45rem;
      font-weight: 800;
      color: var(--sopan-iitk-navy);
      line-height: 1.2;
    }

    .milestone-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      font-size: 0.78rem;
      font-weight: 750;
      color: var(--sopan-orange);
      margin-top: 0.25rem;
      letter-spacing: 0.02em;
    }

    .story-blockquote {
      background: #F8FAFC;
      border-left: 3px solid #38BDF8;
      border-radius: 0 var(--radius-md) var(--radius-md) 0;
      padding: 1.25rem 1.4rem;
      margin: 0 0 1.5rem;
      flex-grow: 1;
    }

    .story-text {
      font-size: 0.98rem;
      color: #334155;
      line-height: 1.75;
      text-align: justify;
    }

    .tags-footer-row {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      padding-top: 1rem;
      border-top: 1px solid #F1F5F9;
    }

    .story-pill-tag {
      font-size: 0.75rem;
      font-weight: 700;
      padding: 0.25rem 0.75rem;
      border-radius: var(--radius-full);
      background: #F1F5F9;
      color: #475569;
    }

    .pill-highlight {
      background: #E0F2FE;
      color: #0369A1;
    }
  </style>
</head>
<body>
"""

html_content += b.get_header_and_nav("achievements")

html_content += b.get_hero_card(
  "🌟",
  "STUDENT IMPACT • SHIKSHA SOPAN",
  "Some personal Achievements",
  "व्यक्तिगत उपलब्धियां",
  "Inspiring journeys of determination, mentorship, and transformative impact — how young minds nurtured by Shiksha Sopan volunteers overcame hardship to excel in science communication, national naval defense, education, and professional careers."
)

# Page Body Content
html_content += """
    <!-- =======================================================================
         STORIES DIRECTORY (EXACT ORIGINAL STORIES WITH EDITORIAL UI)
         ======================================================================= -->
    <section class="achieve-content-section" aria-labelledby="achieveListHeading">
      <div class="container">
        
        <div class="section-eyebrow-center">
          <span class="section-eyebrow-tag" data-i18n="secTag">NURTURING POTENTIAL INTO EXCELLENCE</span>
          <h2 class="section-main-heading" id="achieveListHeading" data-i18n="secHeading">
            Some personal Achievements
          </h2>
        </div>

        <div class="achieve-cards-grid">
          
          <!-- Story 1: Hanuman Gupta -->
          <article class="achieve-card" aria-labelledby="story1Title">
            <div class="card-header-flex">
              <div class="avatar-initials-badge">HG</div>
              <div class="header-name-box">
                <h3 class="student-name" id="story1Title" data-i18n="hgName">Hanuman Gupta</h3>
                <span class="milestone-badge">💻 <span data-i18n="hgRole">Computer Professional • Science Communicator</span></span>
              </div>
            </div>
            <blockquote class="story-blockquote">
              <p class="story-text" data-i18n="hgStory">
                Hanuman, a boy from a very poor family, was able to continue his studies only because of Shiksha Sopan. After his class 12, he was assisted in various ways to do different computer courses. Presently he is a Computer professional at Dehradun with a web-based education company. Excellent science communicator, he appears in Vigyan Prasar (DST, Govt of India) created Science CD “Fun with Physics” with his video shooted experiments.
              </p>
            </blockquote>
            <div class="tags-footer-row">
              <span class="story-pill-tag pill-highlight" data-i18n="tagDST">Vigyan Prasar (DST) Contributor</span>
              <span class="story-pill-tag">Fun with Physics CD</span>
              <span class="story-pill-tag">Dehradun Web Education</span>
            </div>
          </article>

          <!-- Story 2: Ritosh -->
          <article class="achieve-card" aria-labelledby="story2Title">
            <div class="card-header-flex">
              <div class="avatar-initials-badge" style="background:linear-gradient(135deg, #FEF3C7 0%, #FDE68A 100%); border-color:#FCD34D; color:#92400E;">R</div>
              <div class="header-name-box">
                <h3 class="student-name" id="story2Title" data-i18n="ritName">Ritosh</h3>
                <span class="milestone-badge" style="color:#B45309;">⚓ <span data-i18n="ritRole">Indian Naval Force (SSR) • Goa</span></span>
              </div>
            </div>
            <blockquote class="story-blockquote">
              <p class="story-text" data-i18n="ritStory">
                Ritosh started his association with Shiksha Sopan when he was in class 10th and used to come at SAC evening center. His family was not in good condition. He was completed his 12th and joined Sopan science cell and developed some innovative experiments. He is very laborious, and got selected in Indian Naval Force as SSR. Present time He is posted at GOA.
              </p>
            </blockquote>
            <div class="tags-footer-row">
              <span class="story-pill-tag pill-highlight" data-i18n="tagNavy">Indian Naval Force SSR</span>
              <span class="story-pill-tag">SAC Evening Center</span>
              <span class="story-pill-tag">Sopan Science Cell</span>
            </div>
          </article>

          <!-- Story 3: Deepu Kumar -->
          <article class="achieve-card" aria-labelledby="story3Title">
            <div class="card-header-flex">
              <div class="avatar-initials-badge">DK</div>
              <div class="header-name-box">
                <h3 class="student-name" id="story3Title" data-i18n="dkName">Deepu Kumar</h3>
                <span class="milestone-badge">🛠️ <span data-i18n="dkRole">Graduate • Technical Business Lead</span></span>
              </div>
            </div>
            <blockquote class="story-blockquote">
              <p class="story-text" data-i18n="dkStory">
                Deepu Kumar is the son of Mr. Kanhaiya lal, carpenter, who lived for a long time in one of our IITK outhouses. As usual with the outhouse children, Deepu was not serious about his studies and used to spend most of his time in playing street games near his house. Then someone brought him to Shiksha Sopan SAC center and was persuaded to come regularly. Gradually he also developed interest in studies given by Shiksha Sopan volunteers, he completed his graduation. Presently he is working with his father and also giving technical touch to their business.
              </p>
            </blockquote>
            <div class="tags-footer-row">
              <span class="story-pill-tag pill-highlight">IITK Outhouse to Graduate</span>
              <span class="story-pill-tag">SAC Mentorship</span>
              <span class="story-pill-tag">Family Business Modernization</span>
            </div>
          </article>

          <!-- Story 4: Shubhangi -->
          <article class="achieve-card" aria-labelledby="story4Title">
            <div class="card-header-flex">
              <div class="avatar-initials-badge" style="background:linear-gradient(135deg, #ECFDF5 0%, #D1FAE5 100%); border-color:#A7F3D0; color:#065F46;">S</div>
              <div class="header-name-box">
                <h3 class="student-name" id="story4Title" data-i18n="shubName">Shubhangi</h3>
                <span class="milestone-badge" style="color:#059669;">🧪 <span data-i18n="shubRole">B.Sc Dayalbag University • M.Sc Chemistry</span></span>
              </div>
            </div>
            <blockquote class="story-blockquote">
              <p class="story-text" data-i18n="shubStory">
                Shubhangi was a regular student of Gahan Adhyan Kendra. She did quite well in class 12th with biology group and was keen to go for Science stream. We advised her to prepare for the Entrance Exam of Dayalbag institution at Agra. The competition was quite tough as there are only 9 seats for open competition in general category. Shubhangi gave a serious try to this and with Sopan assistance she competed in the exam. She completed her Bachelor Degree from Dayal Bag University and pursuing her M.Sc in Chemistry.
              </p>
            </blockquote>
            <div class="tags-footer-row">
              <span class="story-pill-tag pill-highlight" data-i18n="tagDayal">Dayalbag University Entrance (9 Open Seats)</span>
              <span class="story-pill-tag">Gahan Adhyan Kendra</span>
              <span class="story-pill-tag">M.Sc in Chemistry</span>
            </div>
          </article>

        </div>

      </div>
    </section>
  </main>
"""

html_content += b.get_footer("achievements")

# Bilingual JS
html_content += """
  <!-- =======================================================================
       JAVASCRIPT: BILINGUAL ENGINE
       ======================================================================= -->
  <script>
    const achLangDict = {
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
        heroPill: "STUDENT IMPACT • SHIKSHA SOPAN",
        heroTitle: "Some personal Achievements",
        heroTitleHi: "व्यक्तिगत उपलब्धियां",
        heroLead: "Inspiring journeys of determination, mentorship, and transformative impact — how young minds nurtured by Shiksha Sopan volunteers overcame hardship to excel in science communication, national naval defense, education, and professional careers.",
        secTag: "NURTURING POTENTIAL INTO EXCELLENCE",
        secHeading: "Some personal Achievements",
        hgName: "Hanuman Gupta",
        hgRole: "Computer Professional • Science Communicator",
        hgStory: "Hanuman, a boy from a very poor family, was able to continue his studies only because of Shiksha Sopan. After his class 12, he was assisted in various ways to do different computer courses. Presently he is a Computer professional at Dehradun with a web-based education company. Excellent science communicator, he appears in Vigyan Prasar (DST, Govt of India) created Science CD “Fun with Physics” with his video shooted experiments.",
        ritName: "Ritosh",
        ritRole: "Indian Naval Force (SSR) • Goa",
        ritStory: "Ritosh started his association with Shiksha Sopan when he was in class 10th and used to come at SAC evening center. His family was not in good condition. He was completed his 12th and joined Sopan science cell and developed some innovative experiments. He is very laborious, and got selected in Indian Naval Force as SSR. Present time He is posted at GOA.",
        dkName: "Deepu Kumar",
        dkRole: "Graduate • Technical Business Lead",
        dkStory: "Deepu Kumar is the son of Mr. Kanhaiya lal, carpenter, who lived for a long time in one of our IITK outhouses. As usual with the outhouse children, Deepu was not serious about his studies and used to spend most of his time in playing street games near his house. Then someone brought him to Shiksha Sopan SAC center and was persuaded to come regularly. Gradually he also developed interest in studies given by Shiksha Sopan volunteers, he completed his graduation. Presently he is working with his father and also giving technical touch to their business.",
        shubName: "Shubhangi",
        shubRole: "B.Sc Dayalbag University • M.Sc Chemistry",
        shubStory: "Shubhangi was a regular student of Gahan Adhyan Kendra. She did quite well in class 12th with biology group and was keen to go for Science stream. We advised her to prepare for the Entrance Exam of Dayalbag institution at Agra. The competition was quite tough as there are only 9 seats for open competition in general category. Shubhangi gave a serious try to this and with Sopan assistance she competed in the exam. She completed her Bachelor Degree from Dayal Bag University and pursuing her M.Sc in Chemistry.",
        tagDST: "Vigyan Prasar (DST) Contributor",
        tagNavy: "Indian Naval Force SSR",
        tagDayal: "Dayalbag University Entrance (9 Open Seats)",
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
        heroPill: "छात्र उपलब्धियां • शिक्षा सोपान",
        heroTitle: "व्यक्तिगत उपलब्धियां",
        heroTitleHi: "Some personal Achievements",
        heroLead: "दृढ़ संकल्प, मार्गदर्शन और रूपांतरकारी प्रभाव की प्रेरक कहानियां — कैसे शिक्षा सोपान के स्वयंसेवकों के मार्गदर्शन में वंचित पृष्ठभूमि के बच्चों ने कठिनाइयों को पार कर विज्ञान संचार, नौसेना, उच्च शिक्षा और व्यावसायिक क्षेत्र में कीर्तिमान स्थापित किया।",
        secTag: "प्रतिभा को उत्कृष्ट बनाना",
        secHeading: "कुछ व्यक्तिगत उपलब्धियां",
        hgName: "हनुमान गुप्ता",
        hgRole: "कंप्यूटर प्रोफेशनल • विज्ञान संचारक",
        hgStory: "अत्यंत निर्धन परिवार का बालक हनुमान केवल शिक्षा सोपान के सहयोग से अपनी पढ़ाई जारी रख सका। कक्षा 12 के पश्चात उसे विभिन्न कंप्यूटर पाठ्यक्रम करने में सहायता की गई। वर्तमान में वह देहरादून में एक वेब-आधारित शिक्षा कंपनी में कंप्यूटर प्रोफेशनल है। उत्कृष्ट विज्ञान संचारक होने के नाते वह विज्ञान प्रसार (भारत सरकार) द्वारा निर्मित विज्ञान सीडी “फन विद फिजिक्स” में अपने प्रायोगिक वीडियो के साथ सम्मिलित हैं।",
        ritName: "रितोष",
        ritRole: "भारतीय नौसेना (SSR) • गोवा",
        ritStory: "रितोष का शिक्षा सोपान से संबंध कक्षा 10 में प्रारंभ हुआ जब वह एसएसी सांध्य केंद्र में आता था। उसके परिवार की स्थिति ठीक नहीं थी। उसने 12वीं उत्तीर्ण कर सोपान विज्ञान प्रकोष्ठ से जुड़कर कुछ नवाचारी प्रयोग विकसित किए। वह अत्यंत परिश्रमी है तथा भारतीय नौसेना में एसएसआर (SSR) पद पर चयनित हुआ। वर्तमान में वह गोवा में पदस्थापित है।",
        dkName: "दीपू कुमार",
        dkRole: "स्नातक • तकनीकी व्यवसाय मार्गदर्शक",
        dkStory: "दीपू कुमार बढ़ई श्री कन्हैया लाल जी के सुपुत्र हैं, जो लंबे समय तक आईआईटी कानपुर के एक आउटहाउस में रहते थे। आउटहाउस के बच्चों की तरह दीपू भी पढ़ाई के प्रति गंभीर नहीं था और घर के आसपास गलियों में खेलता रहता था। फिर किसी ने उसे शिक्षा सोपान के एसएसी केंद्र पहुंचाया और नियमित आने को प्रेरित किया। धीरे-धीरे सोपान स्वयंसेवकों के सहयोग से उसने पढ़ाई में रुचि विकसित की और स्नातक पूर्ण किया। वर्तमान में वह अपने पिता के व्यवसाय में तकनीकी योगदान दे रहा है।",
        shubName: "शुभांगी",
        shubRole: "बी.एससी दयालबाग वि.वि. • एम.एससी रसायन विज्ञान",
        shubStory: "शुभांगी गहन अध्ययन केंद्र की नियमित छात्रा थी। उसने जीव विज्ञान समूह से कक्षा 12 में बहुत अच्छा प्रदर्शन किया और विज्ञान संकाय में आगे बढ़ना चाहती थी। हमने उसे आगरा स्थित दयालबाग संस्थान की प्रवेश परीक्षा की तैयारी की सलाह दी। सामान्य वर्ग में केवल 9 खुली सीटें होने के कारण यह प्रतियोगिता बहुत कठिन थी। शुभांगी ने गंभीर प्रयास किया और सोपान की सहायता से परीक्षा उत्तीर्ण की। उसने दयालबाग विश्वविद्यालय से स्नातक पूर्ण कर रसायन विज्ञान में एम.एससी की पढ़ाई जारी रखी है।",
        tagDST: "विज्ञान प्रसार (DST) योगदानकर्ता",
        tagNavy: "भारतीय नौसेना एसएसआर",
        tagDayal: "दयालबाग वि.वि. प्रवेश (९ खुली सीटें)",
        impLinksHead: "महत्वपूर्ण लिंक"
      }
    };

    let currentLang = 'en';

    function setLanguage(lang) {
      currentLang = lang;
      document.getElementById('btnLangEn').classList.toggle('active', lang === 'en');
      document.getElementById('btnLangHi').classList.toggle('active', lang === 'hi');

      const dict = achLangDict[lang];
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

output_path = os.path.join(b.BASE_DIR, "achievements.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully generated {output_path} ({len(html_content)} bytes)")

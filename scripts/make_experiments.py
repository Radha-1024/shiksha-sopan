import os
import json
import build_all_five_pages as b

html_content = b.get_head("Experiments", "Hands-on Physics Experiments by Prof. H.C. Verma and Shiksha Sopan — simple, low-cost tabletop demonstrations in mechanics, optics, electromagnetism, and waves.", "experiments")

html_content += b.get_shared_css()

# Additional page specific CSS
html_content += """
  <style>
    /* Page Specific: Experiments */
    .exp-content-section {
      padding: 2.5rem 0 5rem;
      background: #FFFFFF;
    }

    .section-eyebrow-center {
      text-align: center;
      margin-bottom: 2.5rem;
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

    /* Philosophy Card */
    .philosophy-banner-card {
      background: linear-gradient(135deg, #F8FAFC 0%, #F0F9FF 100%);
      border: 1px solid #BAE6FD;
      border-radius: var(--radius-xl);
      padding: 2.25rem 2.5rem;
      margin-bottom: 3rem;
      box-shadow: 0 4px 18px rgba(2, 132, 199, 0.06);
    }

    .phil-title-row {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      margin-bottom: 1rem;
    }

    .phil-badge {
      background: var(--sopan-blue-light);
      color: var(--sopan-blue-dark);
      font-size: 0.8rem;
      font-weight: 800;
      text-transform: uppercase;
      padding: 0.3rem 0.85rem;
      border-radius: var(--radius-full);
      letter-spacing: 0.05em;
    }

    .phil-text {
      font-size: 1.02rem;
      line-height: 1.8;
      color: #334155;
      text-align: justify;
      margin-bottom: 1rem;
    }
    .phil-text:last-child {
      margin-bottom: 0;
    }

    /* Controls Bar: Search & Category Chips */
    .controls-panel {
      margin-bottom: 2rem;
    }

    .search-filter-box {
      display: flex;
      gap: 1rem;
      margin-bottom: 1.25rem;
      flex-wrap: wrap;
    }

    .search-input-wrap {
      flex: 1;
      min-width: 260px;
      position: relative;
    }

    .search-input-field {
      width: 100%;
      padding: 0.75rem 1rem 0.75rem 2.6rem;
      border: 1.5px solid var(--border-subtle);
      border-radius: var(--radius-full);
      font-size: 0.92rem;
      font-family: inherit;
      color: var(--sopan-iitk-navy);
      background: #FFFFFF;
      transition: all var(--transition-fast);
    }
    .search-input-field:focus {
      outline: none;
      border-color: var(--sopan-sky);
      box-shadow: 0 0 0 3px rgba(14, 165, 233, 0.15);
    }

    .search-icon-inside {
      position: absolute;
      left: 1rem;
      top: 50%;
      transform: translateY(-50%);
      color: #94A3B8;
      font-size: 1rem;
    }

    .category-pills-scroll {
      display: flex;
      gap: 0.5rem;
      overflow-x: auto;
      padding-bottom: 0.5rem;
      scrollbar-width: thin;
    }

    .cat-chip-btn {
      border: 1px solid #CBD5E1;
      background: #FFFFFF;
      padding: 0.4rem 1rem;
      border-radius: var(--radius-full);
      font-size: 0.82rem;
      font-weight: 700;
      color: #475569;
      white-space: nowrap;
      cursor: pointer;
      transition: all var(--transition-fast);
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
    }
    .cat-chip-btn:hover {
      background: #F1F5F9;
      color: var(--sopan-iitk-navy);
      border-color: #94A3B8;
    }
    .cat-chip-btn.active {
      background: var(--sopan-blue-dark);
      color: #FFFFFF;
      border-color: var(--sopan-blue-dark);
      box-shadow: 0 2px 8px rgba(3, 105, 161, 0.25);
    }

    .chip-count {
      font-size: 0.72rem;
      padding: 0.1rem 0.45rem;
      border-radius: var(--radius-full);
      background: rgba(0, 0, 0, 0.08);
    }
    .cat-chip-btn.active .chip-count {
      background: rgba(255, 255, 255, 0.25);
    }

    /* Video Lab Layout: 2 Columns (Playlist vs Player) */
    .video-lab-grid {
      display: grid;
      grid-template-columns: 0.9fr 1.35fr;
      gap: 2rem;
      align-items: flex-start;
    }

    @media (max-width: 992px) {
      .video-lab-grid {
        grid-template-columns: 1fr;
      }
    }

    /* Left: Playlist Card */
    .playlist-card {
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-xl);
      overflow: hidden;
      box-shadow: 0 4px 18px rgba(15, 23, 42, 0.05);
      max-height: 720px;
      display: flex;
      flex-direction: column;
    }

    .playlist-header {
      padding: 1.15rem 1.5rem;
      background: #F8FAFC;
      border-bottom: 1px solid #E2E8F0;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .playlist-title {
      font-size: 0.95rem;
      font-weight: 800;
      color: var(--sopan-iitk-navy);
      letter-spacing: 0.02em;
    }

    .playlist-items-scroll {
      overflow-y: auto;
      padding: 0.5rem;
      flex-grow: 1;
    }

    .chapter-group {
      margin-bottom: 0.75rem;
    }

    .chapter-header {
      padding: 0.6rem 0.85rem;
      background: #F1F5F9;
      border-radius: var(--radius-sm);
      font-size: 0.82rem;
      font-weight: 800;
      color: var(--sopan-blue-dark);
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin-bottom: 0.35rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .experiment-btn {
      width: 100%;
      text-align: left;
      padding: 0.65rem 0.85rem;
      border-radius: var(--radius-md);
      background: transparent;
      border: 1px solid transparent;
      font-size: 0.88rem;
      color: #334155;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.65rem;
      transition: all var(--transition-fast);
      margin-bottom: 0.25rem;
      line-height: 1.4;
    }
    .experiment-btn:hover {
      background: #F8FAFC;
      border-color: #E2E8F0;
      color: var(--sopan-iitk-navy);
    }
    .experiment-btn.active {
      background: #E0F2FE;
      border-color: #BAE6FD;
      color: var(--sopan-blue-dark);
      font-weight: 750;
      box-shadow: 0 1px 4px rgba(2, 132, 199, 0.1);
    }

    .exp-play-icon {
      font-size: 0.8rem;
      flex-shrink: 0;
      opacity: 0.6;
    }
    .experiment-btn.active .exp-play-icon {
      opacity: 1;
      color: var(--sopan-orange);
    }

    /* Right: Player Theater */
    .player-theater-card {
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-xl);
      overflow: hidden;
      box-shadow: 0 8px 28px rgba(15, 23, 42, 0.08);
      position: sticky;
      top: 80px;
    }

    .video-aspect-frame {
      position: relative;
      width: 100%;
      padding-top: 56.25%; /* 16:9 Aspect Ratio */
      background: #0B192C;
    }

    .video-aspect-frame iframe {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      border: 0;
    }

    .player-info-footer {
      padding: 1.5rem 1.75rem;
      background: #FFFFFF;
      border-top: 1px solid #E2E8F0;
    }

    .current-chapter-pill {
      display: inline-block;
      font-size: 0.72rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      padding: 0.25rem 0.7rem;
      border-radius: var(--radius-full);
      background: #E0F2FE;
      color: #0369A1;
      margin-bottom: 0.65rem;
    }

    .current-video-title {
      font-family: 'Playfair Display', Georgia, serif;
      font-size: clamp(1.2rem, 2vw, 1.45rem);
      font-weight: 800;
      color: var(--sopan-iitk-navy);
      line-height: 1.35;
      margin-bottom: 1rem;
    }

    .player-controls-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 1rem;
      padding-top: 1rem;
      border-top: 1px solid #F1F5F9;
    }

    .step-btn-group {
      display: flex;
      gap: 0.5rem;
    }

    .nav-step-btn {
      background: #F1F5F9;
      border: 1px solid #CBD5E1;
      padding: 0.45rem 1rem;
      border-radius: var(--radius-full);
      font-size: 0.82rem;
      font-weight: 700;
      color: #334155;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: all var(--transition-fast);
    }
    .nav-step-btn:hover {
      background: #E2E8F0;
      color: var(--sopan-iitk-navy);
    }

    .yt-external-btn {
      font-size: 0.82rem;
      font-weight: 750;
      color: #DC2626;
      background: #FEF2F2;
      border: 1px solid #FECACA;
      padding: 0.45rem 1rem;
      border-radius: var(--radius-full);
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: all var(--transition-fast);
    }
    .yt-external-btn:hover {
      background: #FEE2E2;
    }
  </style>
</head>
<body>
"""

html_content += b.get_header_and_nav("experiments")

html_content += b.get_hero_card(
  "🔬",
  "HANDS-ON SCIENCE • SHIKSHA SOPAN",
  "Experiments",
  "प्रयोग",
  "Experiments in Physics can not only be done in the physics laboratory with big, expensive, and sophisticated instruments, they can also be done outside it with very simple and easily available apparatus like scale, bottles, balances, wires, magnets etc."
)

# Page Body Content
html_content += """
    <!-- =======================================================================
         EXPERIMENTS LABORATORY (EXACT TEXT & 42 VIDEO EXPERIMENTS)
         ======================================================================= -->
    <section class="exp-content-section" aria-labelledby="expHeading">
      <div class="container">
        
        <!-- Philosophy of Physics Experiments -->
        <div class="philosophy-banner-card">
          <div class="phil-title-row">
            <span class="phil-badge" data-i18n="philTag">Philosophy of Hands-on Physics</span>
          </div>
          <p class="phil-text" data-i18n="philP1">
            Experiments in Physics can not only be done in the physics laboratory with big, expensive, and sophisticated instruments, they can also be done outside it with very simple and easily available apparatus like scale, bottles, balances, wires, magnets etc. This is the main motto of the webpage.
          </p>
          <p class="phil-text" data-i18n="philP2">
            Here, in the videos, we show some simple experiments for the Physics teachers and students. Such small experiments can make a Physics class come alive and many important concepts of physics can be understood by their in-depth analysis.
          </p>
          <p class="phil-text" data-i18n="philP3">
            Using the experiment as a teaching tool, I have made an attempt to briefly explain the concepts involved in it, as one would do in a physics class. The teachers and students viewing them should try to do these experiments to get a first-hand experience. Most of the material used in the experiments can be easily procured from your home itself. You may then add to the experiment and explanation. These simple experiments have a great potential of enhancing our analytical powers.
          </p>
          <p class="phil-text" data-i18n="philP4">
            The experiments have mostly been categorized according to the chapters taught in the class and put into various headings here for your ready reference.
          </p>
        </div>

        <!-- Controls: Search & Category Chips -->
        <div class="controls-panel">
          <div class="search-filter-box">
            <div class="search-input-wrap">
              <span class="search-icon-inside">🔍</span>
              <input type="text" id="expSearchInput" class="search-input-field" placeholder="Search experiments by title or concept (e.g. magnet, pressure, scale)..." oninput="handleSearch(this.value)" />
            </div>
          </div>

          <div class="category-pills-scroll" id="catChipsRow" role="tablist" aria-label="Physics Categories">
            <!-- Dynamically generated category filter chips -->
          </div>
        </div>

        <!-- Interactive 2-Column Video Lab -->
        <div class="video-lab-grid">
          
          <!-- Column 1: Playlist / Table of Contents -->
          <div class="playlist-card">
            <div class="playlist-header">
              <div class="playlist-title">📁 <span data-i18n="playlistTitle">Physics Experiments Playlist</span></div>
              <span id="playlistCountBadge" style="font-size:0.75rem; font-weight:800; color:var(--sopan-sky); background:#F0F9FF; padding:0.2rem 0.6rem; border-radius:9999px;">
                42 Experiments
              </span>
            </div>
            <div class="playlist-items-scroll" id="playlistScroll">
              <!-- Dynamically rendered chapters and video items -->
            </div>
          </div>

          <!-- Column 2: Player Theater -->
          <div class="player-theater-card" id="playerContainer">
            <div class="video-aspect-frame">
              <iframe id="videoIframe" src="https://www.youtube.com/embed/UavtVBoVNLs?rel=0&autoplay=0" title="Physics Experiment Video Player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            </div>
            <div class="player-info-footer">
              <span class="current-chapter-pill" id="currentCategoryBadge">Motion</span>
              <h3 class="current-video-title" id="currentVideoTitle">Reaction Time from Scale</h3>
              
              <div class="player-controls-row">
                <div class="step-btn-group">
                  <button class="nav-step-btn" onclick="stepVideo(-1)">
                    ← Previous
                  </button>
                  <button class="nav-step-btn" onclick="stepVideo(1)">
                    Next →
                  </button>
                </div>
                <a id="ytWatchLink" href="https://www.youtube.com/watch?v=UavtVBoVNLs" target="_blank" rel="noopener noreferrer" class="yt-external-btn">
                  ▶ Watch on YouTube ↗
                </a>
              </div>
            </div>
          </div>

        </div>

      </div>
    </section>
  </main>
"""

html_content += b.get_footer("experiments")

# Bilingual JS and Interactive Player Engine
html_content += """
  <!-- =======================================================================
       JAVASCRIPT: 42 PHYSICS EXPERIMENTS DATA & INTERACTIVE PLAYER ENGINE
       ======================================================================= -->
  <script>
    const physicsData = [
      {
        category: "Motion",
        categoryHi: "गति (Motion)",
        videos: [
          { title: "Reaction Time from Scale", id: "UavtVBoVNLs" }
        ]
      },
      {
        category: "Newton's Laws",
        categoryHi: "न्यूटन के गति नियम (Newton's Laws)",
        videos: [
          { title: "Can you push the magnet further down?", id: "Kgyw0AI6Wwc" },
          { title: "Hanging Magnet", id: "jT025vQbxH0" },
          { title: "It is NOT inertia!", id: "r3h9jwT1OLg" },
          { title: "Does the coin go up or down?", id: "wEZ4mTVV5mA" },
          { title: "Free falling box - Part 1", id: "YbLIpV-7Tnw" },
          { title: "Free falling Box- Part 2", id: "G6Nayhx1jjc" }
        ]
      },
      {
        category: "Electromagnetism",
        categoryHi: "विद्युतचुंबकत्व (Electromagnetism)",
        videos: [
          { title: "Does the red tip of a magnetic compass always point North?", id: "by7tIdq6vgw" },
          { title: "Field of a current carrying coil", id: "G8IggvHV1KU" },
          { title: "An electroscope", id: "uO4LDgO9pzM" },
          { title: "Who is moving the straw?", id: "3LNlheUIaX0" },
          { title: "Magical atta", id: "F4j1ufQn04w" },
          { title: "What slowed the magnet?", id: "vaSBvBCb_0Y" },
          { title: "Why didn't the magnet slow down?", id: "wzueFZ7CYcY" },
          { title: "Charged particles in EB fields.", id: "k5CqzKafGms" },
          { title: "Which bulb glows more -100W or 40W?", id: "UyBlV65fTEI" },
          { title: "Why did the bulb glow?", id: "dEE9_Ms9l6E" },
          { title: "Do you actually know the resistance of a 100W bulb?", id: "oXqEvyhvQdU" },
          { title: "Reaching the Curie temperature!", id: "1j30J2MQqQA" },
          { title: "Change the glow!", id: "S8K0K7RswBM" },
          { title: "Can a magnet have more than two poles?", id: "DzB-pUy3F5k" },
          { title: "Cells from kitchen utensils", id: "ZkZcA4RQgtQ" },
          { title: "Which LED glows first?", id: "IHNmFueQr78" }
        ]
      },
      {
        category: "Rotational Mechanics",
        categoryHi: "घूर्णन यांत्रिकी (Rotational Mechanics)",
        videos: [
          { title: "What holds the bottle?", id: "o9C0D-UUHLo" },
          { title: "Rolling Belan", id: "obnogrWfcLw" },
          { title: "Move your fingers on a scale", id: "VfQU8MvLx-o" },
          { title: "Why didn't the water fall down?", id: "tskJQFx7rBw" }
        ]
      },
      {
        category: "Fluid Mechanics",
        categoryHi: "तरल यांत्रिकी (Fluid Mechanics)",
        videos: [
          { title: "Obedient bottle!", id: "JbGyQQDFO7I" },
          { title: "Measure the Air pressure with food packets and syringe!", id: "mmhXC5x9QAA" },
          { title: "Feel the Air pressure!", id: "S0pqHFbwe2Q" },
          { title: "A manometer", id: "8CbgVagELAA" }
        ]
      },
      {
        category: "Vertical Circle",
        categoryHi: "ऊर्ध्वाधर वृत्त (Vertical Circle)",
        videos: [
          { title: "Why didn't the water fall down?", id: "tskJQFx7rBw" }
        ]
      },
      {
        category: "Optics",
        categoryHi: "प्रकाशिकी (Optics)",
        videos: [
          { title: "See the path of light as it refracts and reflects!", id: "U98m5Z4r_1A" },
          { title: "Colourful image of white light", id: "l9iOEaPzQS4" },
          { title: "Image of a candle flame", id: "oxkpbZzymE0" },
          { title: "Changing boundaries", id: "yXFF55XXARM" },
          { title: "Convex or Concave", id: "t--q45xktac" },
          { title: "Eye accommodation", id: "XoaTBs-5yIM" },
          { title: "Zigzag path of light!", id: "fAvlJuCgqiA" },
          { title: "Sunset point", id: "Zf2dPkL0rjo" }
        ]
      },
      {
        category: "Oscillations and Waves",
        categoryHi: "दोलन एवं तरंगें (Oscillations and Waves)",
        videos: [
          { title: "Changing tension of an oscillating pendulum", id: "wKntZNK7yxc" },
          { title: "Pendulum oscillating at the desired frequency!", id: "a6VEhSxulOo" },
          { title: "Blow and listen!", id: "HOHV5GFmQNQ" }
        ]
      }
    ];

    // Flatten for easy stepping
    let flatPlaylist = [];
    physicsData.forEach(cat => {
      cat.videos.forEach(v => {
        flatPlaylist.push({
          category: cat.category,
          categoryHi: cat.categoryHi,
          title: v.title,
          id: v.id
        });
      });
    });

    let currentActiveIndex = 0;
    let selectedCategory = 'All';
    let searchQuery = '';

    const expLangDict = {
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
        heroPill: "HANDS-ON SCIENCE • SHIKSHA SOPAN",
        heroTitle: "Experiments",
        heroTitleHi: "प्रयोग",
        heroLead: "Experiments in Physics can not only be done in the physics laboratory with big, expensive, and sophisticated instruments, they can also be done outside it with very simple and easily available apparatus like scale, bottles, balances, wires, magnets etc.",
        philTag: "Philosophy of Hands-on Physics",
        philP1: "Experiments in Physics can not only be done in the physics laboratory with big, expensive, and sophisticated instruments, they can also be done outside it with very simple and easily available apparatus like scale, bottles, balances, wires, magnets etc. This is the main motto of the webpage.",
        philP2: "Here, in the videos, we show some simple experiments for the Physics teachers and students. Such small experiments can make a Physics class come alive and many important concepts of physics can be understood by their in-depth analysis.",
        philP3: "Using the experiment as a teaching tool, I have made an attempt to briefly explain the concepts involved in it, as one would do in a physics class. The teachers and students viewing them should try to do these experiments to get a first-hand experience. Most of the material used in the experiments can be easily procured from your home itself. You may then add to the experiment and explanation. These simple experiments have a great potential of enhancing our analytical powers.",
        philP4: "The experiments have mostly been categorized according to the chapters taught in the class and put into various headings here for your ready reference.",
        playlistTitle: "Physics Experiments Playlist",
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
        heroPill: "प्रायोगिक विज्ञान • शिक्षा सोपान",
        heroTitle: "प्रयोग",
        heroTitleHi: "Experiments",
        heroLead: "भौतिकी में प्रयोग केवल बड़ी व महंगी प्रयोगशालाओं में ही नहीं, अपितु घर पर उपलब्ध सामान्य वस्तुओं जैसे बोतल, तार, चुंबक, स्केल से भी किए जा सकते हैं।",
        philTag: "प्रायोगिक भौतिकी का मूल दर्शन",
        philP1: "भौतिक विज्ञान के प्रयोग केवल बड़े, महंगे और परिष्कृत उपकरणों वाली प्रयोगशालाओं में ही नहीं किए जाते, बल्कि उन्हें घर पर उपलब्ध साधारण वस्तुओं जैसे स्केल, बोतल, तराजू, तार, चुम्बक आदि से भी किया जा सकता है। यही इस पृष्ठ का मूल उद्देश्य है।",
        philP2: "यहाँ वीडियो के माध्यम से हम भौतिकी शिक्षकों और छात्रों के लिए कुछ सरल प्रयोग प्रस्तुत कर रहे हैं। ऐसे छोटे प्रयोग भौतिकी की कक्षा को जीवंत बना देते हैं और इनके गहन विश्लेषण से कई महत्वपूर्ण अवधारणाओं को आसानी से समझा जा सकता है।",
        philP3: "प्रयोग को शिक्षण उपकरण के रूप में उपयोग करते हुए मैंने इसमें निहित अवधारणाओं को संक्षेप में समझाने का प्रयास किया है। शिक्षकों एवं छात्रों को स्वयं ये प्रयोग करके देखना चाहिए। अधिकांश सामग्री घर में ही उपलब्ध हो जाती है।",
        philP4: "कक्षा में पढ़ाए जाने वाले अध्यायों के अनुसार इन प्रयोगों को वर्गीकृत करके विभिन्न शीर्षकों के अंतर्गत प्रस्तुत किया गया है।",
        playlistTitle: "भौतिकी प्रयोग सूची",
        impLinksHead: "महत्वपूर्ण लिंक"
      }
    };

    let currentLang = 'en';

    function setLanguage(lang) {
      currentLang = lang;
      document.getElementById('btnLangEn').classList.toggle('active', lang === 'en');
      document.getElementById('btnLangHi').classList.toggle('active', lang === 'hi');

      const dict = expLangDict[lang];
      document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (dict[key]) {
          el.innerHTML = dict[key];
        }
      });

      renderCategoryChips();
      renderPlaylist();
      updatePlayerInfo();
    }

    function renderCategoryChips() {
      const container = document.getElementById('catChipsRow');
      let html = `<button class="cat-chip-btn ${selectedCategory === 'All' ? 'active' : ''}" onclick="filterCategory('All')">
        ${currentLang === 'hi' ? 'सभी' : 'All'} <span class="chip-count">${flatPlaylist.length}</span>
      </button>`;

      physicsData.forEach(cat => {
        const catName = currentLang === 'hi' ? cat.categoryHi : cat.category;
        const isActive = selectedCategory === cat.category;
        html += `<button class="cat-chip-btn ${isActive ? 'active' : ''}" onclick="filterCategory('${cat.category}')">
          ${catName} <span class="chip-count">${cat.videos.length}</span>
        </button>`;
      });

      container.innerHTML = html;
    }

    function renderPlaylist() {
      const container = document.getElementById('playlistScroll');
      let html = '';
      let renderedCount = 0;

      physicsData.forEach(group => {
        if (selectedCategory !== 'All' && selectedCategory !== group.category) {
          return;
        }

        const filteredVideos = group.videos.filter(v => {
          if (!searchQuery) return true;
          return v.title.toLowerCase().includes(searchQuery.toLowerCase()) || 
                 group.category.toLowerCase().includes(searchQuery.toLowerCase());
        });

        if (filteredVideos.length === 0) return;

        const groupName = currentLang === 'hi' ? group.categoryHi : group.category;
        html += `<div class="chapter-group">
          <div class="chapter-header">
            <span>${groupName}</span>
            <span>(${filteredVideos.length})</span>
          </div>`;

        filteredVideos.forEach(v => {
          renderedCount++;
          const flatIdx = flatPlaylist.findIndex(item => item.id === v.id && item.category === group.category);
          const isActive = flatIdx === currentActiveIndex;
          html += `<button class="experiment-btn ${isActive ? 'active' : ''}" onclick="selectVideo(${flatIdx})">
            <span class="exp-play-icon">${isActive ? '▶' : '○'}</span>
            <span>${v.title}</span>
          </button>`;
        });

        html += `</div>`;
      });

      if (renderedCount === 0) {
        html = `<div style="padding:2rem 1rem; text-align:center; color:#94A3B8; font-size:0.9rem;">
          No experiments match "${searchQuery}".
        </div>`;
      }

      container.innerHTML = html;
      document.getElementById('playlistCountBadge').innerText = `${renderedCount} Experiments`;
    }

    function selectVideo(index) {
      if (index < 0 || index >= flatPlaylist.length) return;
      currentActiveIndex = index;
      const vid = flatPlaylist[currentActiveIndex];

      document.getElementById('videoIframe').src = `https://www.youtube.com/embed/${vid.id}?rel=0&autoplay=1`;
      updatePlayerInfo();
      renderPlaylist();

      // On mobile view, scroll slightly to player
      if (window.innerWidth < 992) {
        document.getElementById('playerContainer').scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    }

    function updatePlayerInfo() {
      const vid = flatPlaylist[currentActiveIndex];
      const catText = currentLang === 'hi' ? vid.categoryHi : vid.category;
      document.getElementById('currentCategoryBadge').innerText = catText;
      document.getElementById('currentVideoTitle').innerText = vid.title;
      document.getElementById('ytWatchLink').href = `https://www.youtube.com/watch?v=https://www.youtube.com/watch?v=${vid.id}`;
    }

    function stepVideo(direction) {
      let nextIdx = currentActiveIndex + direction;
      if (nextIdx < 0) nextIdx = flatPlaylist.length - 1;
      if (nextIdx >= flatPlaylist.length) nextIdx = 0;
      selectVideo(nextIdx);
    }

    function filterCategory(catName) {
      selectedCategory = catName;
      renderCategoryChips();
      renderPlaylist();
    }

    function handleSearch(val) {
      searchQuery = val.trim();
      renderPlaylist();
    }

    // Initialize
    window.addEventListener('DOMContentLoaded', () => {
      renderCategoryChips();
      renderPlaylist();
      updatePlayerInfo();
    });
  </script>
</body>
</html>
"""

output_path = os.path.join(b.BASE_DIR, "experiments.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully generated {output_path} ({len(html_content)} bytes)")

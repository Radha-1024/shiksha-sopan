/**
 * SHIKSHA SOPAN (शिक्षा सोपान) — Interactive Web Engine & Simulations
 * Features:
 * - Bilingual (English / Hindi) Live Content Switching
 * - Anti-Gravity Levitation Vector Schematic & Harmonic Physics Simulation
 * - Companion Mini-Visualizers: Pendulum Waves, Optics TIR, Eddy Current Braking, Rotational Inertia
 * - Interactive Experiment Modal System & Telemetry HUD
 */

// ==========================================================================
// 1. BILINGUAL TRANSLATION DICTIONARY
// ==========================================================================
const translations = {
  en: {
    mottoTagline: "“Why curse the darkness, better to light a lamp.”",
    mottoAffiliation: "IIT KANPUR COMMUNITY INITIATIVE",
    navHome: "Home",
    navExperiments: "Experiments",
    navPrograms: "Programs",
    navAbout: "About Us",
    navContact: "Contact",
    navJoin: "Support / Join",
    heroBadge: "IIT KANPUR SOCIAL & SCIENTIFIC INITIATIVE • ESTD. 2001",
    heroHeadlinePart1: "SPARKING CURIOSITY | ",
    heroHeadlineSpark: "Hands-On Physics & STEM",
    heroHeadlinePart2: " for Everyone.",
    heroSubheading: "Founded under the guidance of <strong>Padma Shri Prof. H.C. Verma</strong>, Shiksha Sopan connects classroom physics with everyday curiosity through value-based learning across three pillars: <strong>Shiksha</strong>, <strong>Sanskar</strong>, and <strong>Swavalamban</strong>.",
    heroCtaExperiments: "Explore Experiments",
    heroCtaMission: "Our Mission",
    statStudents: "Students Reached",
    statCenters: "Anveshika Centers",
    statFreeStem: "Open Hands-On STEM",
    statMentorship: "H.C. Verma Mentorship",
    hubBadge: "BENTO EXPERIMENT SHOWCASE",
    hubTitle: "Experiments Hub",
    hubSubtitle: "Physics comes alive not inside expensive laboratories, but in simple experiments done with household items and keen observation.",
    antiGravityTag: "FLAGSHIP SCHEMATIC LAB",
    antiGravityTitle: "EXPLORE ANTI-GRAVITY HUB",
    antiGravityDesc: "Interactive electromagnetic levitation chamber schematic demonstrating Earnshaw theorem bypass, diamagnetic stability, and active flux control.",
    badgeLevitation: "LEVITATION MECHANICS",
    badgeShield: "GRAVITY SHIELD ACTIVE",
    badgeTelemetry: "DATA VISUALIZATION",
    telemetryHeight: "Levitation Alt.",
    telemetryFlux: "Field Density",
    telemetryStability: "Stability Index",
    telemetryDamping: "Harmonic Damping",
    labelFieldPower: "Field Power:",
    btnPerturb: "Perturb Core",
    btnReset: "Reset",
    btnTheoryNotes: "Theory & Lab Notes",
    pendulumTitle: "PENDULUM WAVES",
    pendulumDesc: "Harmonically tuned pendulums producing mesmerizing synchronized wave motion and phase interference.",
    opticsTitle: "OPTICS & REFRACTION",
    opticsDesc: "Laser beam refraction, critical angle mechanics, and total internal reflection in water columns.",
    eddyTitle: "EDDY CURRENTS",
    eddyDesc: "Lenz’s law in action: Neodymium magnet slow-motion braking through high-conductivity copper pipes.",
    rotationTitle: "ROTATIONAL INERTIA",
    rotationDesc: "Conservation of angular momentum: how changing mass distribution accelerates rotational spin.",
    btnTryExperiment: "Try This Experiment",
    programsBadge: "NATIONAL IMPACT & PEDAGOGY",
    programsTitle: "Key Educational Programs",
    programsSubtitle: "From rural evening learning centers around IIT Kanpur to nationwide experimental competitions.",
    naestTag: "NATIONAL FLAGSHIP",
    naestTitle: "NAEST (National Anveshika Experimental Skill Test)",
    naestDesc: "India’s unique annual science competition that evaluates students on real observational and experimental skills rather than book memorization.",
    naestMetric1: "Over 50,000+ student participants across 80+ regional Anveshika centers",
    naestMetric2: "Junior (Classes 9-10) and Senior (Classes 11-12 & BSc) divisions",
    naestMetric3: "National Finals hosted at Sopan Ashram / IIT Kanpur campus",
    sgpvTag: "HIGHER EDUCATION",
    sgpvTitle: "SGPV Uchch Shiksha Prakalp",
    sgpvDesc: "Shree Ganesh Prasad Verma program providing direct academic and financial mentorship to bright underprivileged students pursuing engineering and sciences.",
    scholarshipTag: "MERIT SCHOLARSHIP",
    scholarshipTitle: "Dr. V.N. Kulkarni Medha Chhatravritti",
    scholarshipDesc: "Annual merit scholarships instituted in memory of eminent IIT Kanpur physicist Dr. V.N. Kulkarni to support promising rural scholars.",
    ashramTag: "COMMUNITY HUB",
    ashramTitle: "Sopan Ashram & Science on Wheels",
    ashramDesc: "A bustling experimental physics facility in Kanpur offering residential short courses, science tours, and mobile science vans visiting remote villages.",
    philosophyBadge: "FOUNDATIONAL VALUES",
    philosophyTitle: "The Three Pillars of Shiksha Sopan",
    philosophySubtitle: "Real development transcends rote instruction; education must instill noble character and economic self-reliance.",
    pillar1Title: "Education (शिक्षा)",
    pillar1Desc: "Rooted in hands-on observation, questioning nature, and connecting textbook science to daily-life phenomenon.",
    pillar2Title: "Culture & Values (संस्कार)",
    pillar2Desc: "Nurturing empathy, ethical integrity, respect for society, and civic responsibility among young learners.",
    pillar3Title: "Self-Reliance (स्वावलंबन)",
    pillar3Desc: "Empowering students and community youth with practical problem-solving skills to build self-sustaining lives.",
    testimonialsBadge: "COMMUNITY VOICES",
    testimonialsTitle: "Testimonials & Leadership",
    testimonialsSubtitle: "Reflections from academic leaders and alumni whose lives intersect with Shiksha Sopan.",
    footerQuote: "अन्धकार को क्यों धिक्कारें, अच्छा हैं एक दीप जलायें",
    footerQuoteSub: "IIT KANPUR COMMUNITY • ESTD. 2001",
    footerDesc: "Shiksha Sopan is a dedicated non-governmental organization imparting value-based science and social education to the economically weaker sections in and around IIT Kanpur.",
    footerColPrograms: "Programs",
    footerColExperiments: "Experiments",
    footerColConnect: "Connect & Visit",
    footerAddress: "Sopan Ashram, Near IIT Kanpur, Kanpur, Uttar Pradesh 208016",
    footerCopyright: "© 2026 Shiksha Sopan. All rights reserved. Registered Society & 80G Tax Exempt."
  },
  hi: {
    mottoTagline: "“अन्धकार को क्यों धिक्कारें, अच्छा हैं एक दीप जलायें”",
    mottoAffiliation: "आईआईटी कानपुर समुदाय की पहल",
    navHome: "होम",
    navExperiments: "प्रयोग",
    navPrograms: "कार्यक्रम",
    navAbout: "हमारे बारे में",
    navContact: "संपर्क करें",
    navJoin: "सहयोग / जुड़ें",
    heroBadge: "आईआईटी कानपुर सामाजिक व वैज्ञानिक पहल • स्था. २००१",
    heroHeadlinePart1: "जिज्ञासा का दीप | ",
    heroHeadlineSpark: "प्रायोगिक भौतिकी व विज्ञान",
    heroHeadlinePart2: " सबके लिए।",
    heroSubheading: "<strong>पद्मश्री प्रो. एच. सी. वर्मा</strong> के मार्गदर्शन में स्थापित, शिक्षा सोपान पाठ्यपुस्तकों की भौतिकी को दैनिक जीवन की जिज्ञासा से जोड़ता है। तीन स्तंभ: <strong>शिक्षा</strong>, <strong>संस्कार</strong>, और <strong>स्वावलंबन</strong>।",
    heroCtaExperiments: "प्रयोग देखें",
    heroCtaMission: "हमारा उद्देश्य",
    statStudents: "विद्यार्थी लाभान्वित",
    statCenters: "अन्वेषिका केंद्र",
    statFreeStem: "निःशुल्क प्रायोगिक विज्ञान",
    statMentorship: "प्रो. एच.सी. वर्मा का मार्गदर्शन",
    hubBadge: "बेंटो प्रयोग प्रदर्शनी",
    hubTitle: "प्रयोग केंद्र (Experiments Hub)",
    hubSubtitle: "भौतिकी महंगी प्रयोगशालाओं में नहीं, बल्कि घरेलू सामग्री और सजग अवलोकन के साथ किए गए सरल प्रयोगों में जीवंत होती है।",
    antiGravityTag: "प्रमुख प्रायोगिक रेखाचित्र",
    antiGravityTitle: "एंटी-ग्रेविटी व उत्तोलन हब",
    antiGravityDesc: "अर्न्शॉ प्रमेय के बाईपास, प्रति-चुंबकीय स्थिरता और सक्रिय चुंबकीय फ्लक्स का सजीव इंटरेक्टिव तकनीकी रेखाचित्र।",
    badgeLevitation: "उत्तोलन यांत्रिकी (LEVITATION)",
    badgeShield: "गुरुत्व शील्ड सक्रिय",
    badgeTelemetry: "लाइव डेटा विज़ुअलाइज़ेशन",
    telemetryHeight: "उत्तोलन ऊंचाई",
    telemetryFlux: "चुंबकीय घनत्व",
    telemetryStability: "स्थिरता सूचकांक",
    telemetryDamping: "डैम्पिंग गुणांक",
    labelFieldPower: "चुंबकीय शक्ति:",
    btnPerturb: "कोर को विचलित करें",
    btnReset: "रीसेट",
    btnTheoryNotes: "सिद्धांत व विवरण",
    pendulumTitle: "पेंडुलम तरंगें (PENDULUM WAVES)",
    pendulumDesc: "सटीक सामंजस्य से बंधे १२ लोलक, जो एक साथ झूलते हुए सम्मोहक सर्पिल तरंगें व कला-व्यतिकरण उत्पन्न करते हैं।",
    opticsTitle: "प्रकाशिकी व पूर्ण आंतरिक परावर्तन",
    opticsDesc: "लेज़र किरण का अपवर्तन, क्रांतिक कोण यांत्रिकी और जल धारा में प्रकाश का पूर्ण आंतरिक परावर्तन।",
    eddyTitle: "एडी धाराएं व लेन्ज़ का नियम",
    eddyDesc: "तांबे के पाइप में गिरते निओडिमियम चुंबक की मंद गति — विद्युत चुंबकीय प्रेरण का प्रत्यक्ष प्रमाण।",
    rotationTitle: "घूर्णन गति व जड़त्व आघूर्ण",
    rotationDesc: "कोणीय संवेग संरक्षण: द्रव्यमान के वितरण को बदलने से घूर्णन गति में तीव्र त्वरण का प्रदर्शन।",
    btnTryExperiment: "यह प्रयोग स्वयं करें",
    programsBadge: "राष्ट्रीय प्रभाव व शिक्षण पहल",
    programsTitle: "प्रमुख शैक्षिक कार्यक्रम",
    programsSubtitle: "आईआईटी कानपुर के ग्रामीण शिक्षण केंद्रों से लेकर अखिल भारतीय प्रायोगिक प्रतियोगिताओं तक।",
    naestTag: "राष्ट्रीय स्तर",
    naestTitle: "राष्ट्रीय अन्वेषिका प्रायोगिक कौशल परीक्षा (NAEST)",
    naestDesc: "भारत की अनूठी विज्ञान प्रतियोगिता जो रटने के बजाय छात्रों के वास्तविक अवलोकन और प्रायोगिक विश्लेषण क्षमता को परखती है।",
    naestMetric1: "८०+ क्षेत्रीय अन्वेषिका केंद्रों में ५०,०००+ छात्रों की सहभागिता",
    naestMetric2: "कक्षा ९-१० (जूनियर) तथा ११-१२ व बीएससी (सीनियर) वर्ग",
    naestMetric3: "राष्ट्रीय फाइनल सोपान आश्रम व आईआईटी कानपुर में आयोजित",
    sgpvTag: "उच्च शिक्षा",
    sgpvTitle: "श्री गणेश प्रसाद वर्मा उच्च शिक्षा प्रकल्प",
    sgpvDesc: "आर्थिक रूप से वंचित मेधावी ग्रामीण छात्रों को इंजीनियरिंग, मेडिकल व विज्ञान स्नातक के लिए पूर्ण मार्गदर्शन और सहयोग।",
    scholarshipTag: "मेधा छात्रवृत्ति",
    scholarshipTitle: "डॉ. व्ही. एन. कुलकर्णी मेधा छात्रवृत्ति",
    scholarshipDesc: "आईआईटी कानपुर के प्रख्यात भौतिक विज्ञानी डॉ. कुलकर्णी की स्मृति में प्रतिभावान विद्यार्थियों हेतु वार्षिक छात्रवृत्ति।",
    ashramTag: "सामुदायिक केंद्र",
    ashramTitle: "सोपान आश्रम व सचल विज्ञान केंद्र",
    ashramDesc: "कानपुर में आवासीय विज्ञान कार्यशालाएं, स्कूल भ्रमण एवं सुदूर गांवों में प्रायोगिक किट ले जाने वाली विज्ञान वैन।",
    philosophyBadge: "मूल दर्शन",
    philosophyTitle: "शिक्षा सोपान के तीन स्तंभ",
    philosophySubtitle: "सच्चा विकास केवल सूचना भरने से नहीं होता; शिक्षा को श्रेष्ठ संस्कार और स्वावलंबन गढ़ना चाहिए।",
    pillar1Title: "शिक्षा (Shiksha)",
    pillar1Desc: "प्रकृति के सिद्धांतों को स्वयं करके समझना, प्रश्न पूछना और कक्षा की पढ़ाई को दैनिक जीवन से जोड़ना।",
    pillar2Title: "संस्कार (Sanskar)",
    pillar2Desc: "सहानुभूति, नैतिक निष्ठा, समाज के प्रति कृतज्ञता और नागरिक कर्तव्य की भावना का संवर्धन।",
    pillar3Title: "स्वावलंबन (Swavalamban)",
    pillar3Desc: "व्यावहारिक कौशल और आत्म-निर्भरता ताकि युवा स्वयं अपने और समाज के पैरों पर खड़े हो सकें।",
    testimonialsBadge: "नेतृत्व व अनुभव",
    testimonialsTitle: "मार्गदर्शक व अनुभव",
    testimonialsSubtitle: "आईआईटी कानपुर के प्राध्यापकों और पूर्व छात्रों के आत्मीय संस्मरण।",
    footerQuote: "अन्धकार को क्यों धिक्कारें, अच्छा हैं एक दीप जलायें",
    footerQuoteSub: "आईआईटी कानपुर समुदाय • स्था. २००१",
    footerDesc: "शिक्षा सोपान एक गैर-सरकारी संस्था है जो समाज के कमजोर वर्ग को संस्कारयुक्त शिक्षा, वैज्ञानिक दृष्टिकोण व स्वावलंबन प्रदान करती है।",
    footerColPrograms: "कार्यक्रम",
    footerColExperiments: "प्रयोग",
    footerColConnect: "संपर्क व भ्रमण",
    footerAddress: "सोपान आश्रम, आईआईटी कानपुर के पास, ननकारी, कानपुर, उ.प्र. २०८०१६",
    footerCopyright: "© २०२६ शिक्षा सोपान। सर्वाधिकार सुरक्षित। पंजीकृत संस्था (80G कर छूट प्राप्त)।"
  }
};

let currentLang = 'en';

function setLanguage(lang) {
  currentLang = lang;
  const dict = translations[lang] || translations.en;

  // Toggle active button UI
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.lang === lang);
  });

  // Apply to all elements with data-i18n
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.dataset.i18n;
    if (dict[key]) {
      el.innerHTML = dict[key];
    }
  });

  // Set document lang attribute
  document.documentElement.lang = lang;
}

// ==========================================================================
// 2. ANTI-GRAVITY HUB: TECHNICAL VECTOR SCHEMATIC & PHYSICS SIMULATION
// ==========================================================================
class AntiGravityChamber {
  constructor(canvasId) {
    this.canvas = document.getElementById(canvasId);
    if (!this.canvas) return;
    this.ctx = this.canvas.getContext('2d');
    
    // Core physical parameters
    this.fieldPower = 75; // percentage
    this.frequency = 42;  // Hz
    this.time = 0;
    
    // Core dynamic state (damped harmonic oscillator)
    this.coreY = 0; // displacement from equilibrium
    this.coreVelocity = 0;
    this.coreX = 0;
    this.isDragging = false;
    this.dragStartY = 0;

    // Telemetry DOM elements
    this.altEl = document.getElementById('telemetryAlt');
    this.fluxEl = document.getElementById('telemetryFlux');
    this.stabilityEl = document.getElementById('telemetryStability');
    this.dampingEl = document.getElementById('telemetryDamping');
    this.sliderPower = document.getElementById('fieldPowerSlider');

    this.initEvents();
    this.resize();
    window.addEventListener('resize', () => this.resize());
    this.animate();
  }

  resize() {
    const rect = this.canvas.parentElement.getBoundingClientRect();
    this.width = rect.width;
    this.height = rect.height;
    this.canvas.width = this.width * window.devicePixelRatio;
    this.canvas.height = this.height * window.devicePixelRatio;
    this.ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
  }

  initEvents() {
    if (this.sliderPower) {
      this.sliderPower.addEventListener('input', (e) => {
        this.fieldPower = parseFloat(e.target.value);
        this.perturb(1.5);
      });
    }

    const perturbBtn = document.getElementById('btnPerturbCore');
    if (perturbBtn) {
      perturbBtn.addEventListener('click', () => {
        this.perturb(18);
      });
    }

    const resetBtn = document.getElementById('btnResetChamber');
    if (resetBtn) {
      resetBtn.addEventListener('click', () => {
        this.fieldPower = 75;
        if (this.sliderPower) this.sliderPower.value = 75;
        this.coreY = 0;
        this.coreVelocity = 0;
        this.coreX = 0;
      });
    }

    // Interactive mouse / touch interaction
    const getPos = (e) => {
      const rect = this.canvas.getBoundingClientRect();
      const clientX = e.touches ? e.touches[0].clientX : e.clientX;
      const clientY = e.touches ? e.touches[0].clientY : e.clientY;
      return {
        x: clientX - rect.left,
        y: clientY - rect.top
      };
    };

    const onDown = (e) => {
      const pos = getPos(e);
      const centerX = this.width / 2;
      const centerY = this.height / 2 + this.coreY;
      const dist = Math.hypot(pos.x - centerX, pos.y - centerY);
      if (dist < 45) {
        this.isDragging = true;
        this.dragStartY = pos.y - this.coreY;
      }
    };

    const onMove = (e) => {
      if (!this.isDragging) return;
      const pos = getPos(e);
      this.coreY = Math.max(-90, Math.min(90, pos.y - this.dragStartY));
      this.coreVelocity = 0;
    };

    const onUp = () => {
      this.isDragging = false;
    };

    this.canvas.addEventListener('mousedown', onDown);
    window.addEventListener('mousemove', onMove);
    window.addEventListener('mouseup', onUp);

    this.canvas.addEventListener('touchstart', onDown, { passive: true });
    window.addEventListener('touchmove', onMove, { passive: true });
    window.addEventListener('touchend', onUp);
  }

  perturb(force = 15) {
    this.coreVelocity += (Math.random() > 0.5 ? 1 : -1) * force;
  }

  updatePhysics() {
    this.time += 0.04;

    if (!this.isDragging) {
      // Spring constant proportional to field power
      const k = 0.06 + (this.fieldPower / 100) * 0.08;
      // Damping coefficient
      const damping = 0.94;
      
      // Restorative force
      const force = -k * this.coreY;
      this.coreVelocity += force;
      this.coreVelocity *= damping;
      this.coreY += this.coreVelocity;

      // Subtle electromagnetic micro-vibration
      this.coreY += Math.sin(this.time * 6) * 0.4 * (this.fieldPower / 100);
    }

    // Telemetry updates
    if (this.altEl) {
      const heightMm = (18.4 - (this.coreY * 0.12)).toFixed(1);
      this.altEl.innerText = heightMm;
    }
    if (this.fluxEl) {
      const fluxT = (0.4 + (this.fieldPower / 100) * 1.35).toFixed(2);
      this.fluxEl.innerText = fluxT;
    }
    if (this.stabilityEl) {
      const stab = (99.8 - Math.abs(this.coreVelocity) * 1.8).toFixed(1);
      this.stabilityEl.innerText = Math.max(90, stab) + '%';
    }
    if (this.dampingEl) {
      this.dampingEl.innerText = (0.75 + (this.fieldPower / 200)).toFixed(2);
    }
  }

  draw() {
    const ctx = this.ctx;
    const w = this.width;
    const h = this.height;

    ctx.clearRect(0, 0, w, h);

    const centerX = w / 2;
    const centerY = h / 2;
    const chamberW = Math.min(340, w - 80);
    const chamberH = h - 60;
    const chamberX = centerX - chamberW / 2;
    const chamberY = 30;

    // -------------------------------------------------------------
    // A. Outer Drafting Blueprint Calibration Marks & Dimension Lines
    // -------------------------------------------------------------
    ctx.save();
    ctx.strokeStyle = '#CBD5E1';
    ctx.lineWidth = 1;
    ctx.setLineDash([4, 4]);

    // Vertical center line
    ctx.beginPath();
    ctx.moveTo(centerX, 15);
    ctx.lineTo(centerX, h - 15);
    ctx.stroke();

    // Horizontal equilibrium line
    ctx.beginPath();
    ctx.moveTo(chamberX - 30, centerY);
    ctx.lineTo(chamberX + chamberW + 30, centerY);
    ctx.stroke();
    ctx.setLineDash([]);

    // Technical ticks on chamber sides
    for (let y = chamberY + 20; y < chamberY + chamberH; y += 25) {
      ctx.beginPath();
      ctx.moveTo(chamberX - 8, y);
      ctx.lineTo(chamberX, y);
      ctx.moveTo(chamberX + chamberW, y);
      ctx.lineTo(chamberX + chamberW + 8, y);
      ctx.stroke();
    }
    ctx.restore();

    // -------------------------------------------------------------
    // B. Cylindrical Glass Vacuum Chamber Structure
    // -------------------------------------------------------------
    ctx.save();
    // Glass Chamber Fill (ultra faint tint)
    const glassGrad = ctx.createLinearGradient(chamberX, 0, chamberX + chamberW, 0);
    glassGrad.addColorStop(0, 'rgba(224, 242, 254, 0.45)');
    glassGrad.addColorStop(0.15, 'rgba(255, 255, 255, 0.6)');
    glassGrad.addColorStop(0.5, 'rgba(240, 249, 255, 0.15)');
    glassGrad.addColorStop(0.85, 'rgba(255, 255, 255, 0.6)');
    glassGrad.addColorStop(1, 'rgba(224, 242, 254, 0.45)');

    ctx.fillStyle = glassGrad;
    ctx.strokeStyle = 'rgba(14, 165, 233, 0.5)';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.roundRect(chamberX, chamberY, chamberW, chamberH, 16);
    ctx.fill();
    ctx.stroke();

    // Specular Reflection Curved Highlights (Glass sheen)
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.9)';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(chamberX + 16, chamberY + 30);
    ctx.lineTo(chamberX + 16, chamberY + chamberH - 30);
    ctx.stroke();

    ctx.lineWidth = 1.5;
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.6)';
    ctx.beginPath();
    ctx.moveTo(chamberX + 24, chamberY + 45);
    ctx.lineTo(chamberX + 24, chamberY + chamberH - 45);
    ctx.stroke();
    ctx.restore();

    // -------------------------------------------------------------
    // C. Top and Bottom Electromagnetic Magnetic Pole Coils
    // -------------------------------------------------------------
    const coilW = chamberW * 0.68;
    const coilH = 26;
    const coilX = centerX - coilW / 2;

    // Top Pole (Stator)
    ctx.save();
    ctx.fillStyle = '#0F172A';
    ctx.strokeStyle = '#0284C7';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.roundRect(coilX, chamberY + 12, coilW, coilH, 6);
    ctx.fill();
    ctx.stroke();

    // Copper winding grooves top
    ctx.strokeStyle = 'rgba(249, 115, 22, 0.7)';
    ctx.lineWidth = 2;
    for (let cx = coilX + 10; cx < coilX + coilW - 10; cx += 8) {
      ctx.beginPath();
      ctx.moveTo(cx, chamberY + 14);
      ctx.lineTo(cx, chamberY + 12 + coilH - 2);
      ctx.stroke();
    }

    // Bottom Pole (Levitation Base Ring)
    ctx.fillStyle = '#0F172A';
    ctx.strokeStyle = '#0284C7';
    ctx.beginPath();
    ctx.roundRect(coilX, chamberY + chamberH - 38, coilW, coilH, 6);
    ctx.fill();
    ctx.stroke();

    // Copper winding grooves bottom
    for (let cx = coilX + 10; cx < coilX + coilW - 10; cx += 8) {
      ctx.beginPath();
      ctx.moveTo(cx, chamberY + chamberH - 36);
      ctx.lineTo(cx, chamberY + chamberH - 14);
      ctx.stroke();
    }
    ctx.restore();

    // -------------------------------------------------------------
    // D. Glowing Electric Cyan & Plasma Blue Vector Magnetic Flux Lines
    // -------------------------------------------------------------
    const activePower = this.fieldPower / 100;
    const currentCoreY = centerY + this.coreY;

    ctx.save();
    ctx.lineWidth = 1.5;

    // Draw 7 symmetric field flow lines
    for (let i = -3; i <= 3; i++) {
      const offset = i * (coilW / 7);
      const intensity = 1 - (Math.abs(i) / 4);
      
      // Dynamic pulsing glow
      const alpha = (0.25 + 0.35 * Math.sin(this.time * 3 + Math.abs(i))) * activePower;
      ctx.strokeStyle = i === 0 ? 'rgba(0, 229, 255, 0.85)' : `rgba(37, 99, 235, ${alpha + 0.2})`;

      ctx.beginPath();
      const startX = centerX + offset * 0.75;
      const startY = chamberY + 12 + coilH;

      const midControlX = centerX + offset * 1.5;
      const midControlY = currentCoreY;

      const endX = centerX + offset * 0.75;
      const endY = chamberY + chamberH - 38;

      ctx.moveTo(startX, startY);
      ctx.bezierCurveTo(midControlX, centerY - 40, midControlX, centerY + 40, endX, endY);
      ctx.stroke();

      // Flowing quantum energy particles along field lines
      const particleProgress = (this.time * 0.6 + Math.abs(i) * 0.2) % 1;
      const py = startY + (endY - startY) * particleProgress;
      const px = centerX + Math.sin(particleProgress * Math.PI) * (offset * 1.4) + offset * 0.4;

      ctx.fillStyle = '#00E5FF';
      ctx.shadowColor = '#00E5FF';
      ctx.shadowBlur = 8;
      ctx.beginPath();
      ctx.arc(px, py, 2.2, 0, Math.PI * 2);
      ctx.fill();
      ctx.shadowBlur = 0;
    }
    ctx.restore();

    // -------------------------------------------------------------
    // E. Levitating Core (Diamagnetic / Superconducting Disc)
    // -------------------------------------------------------------
    ctx.save();
    const coreW = 100;
    const coreH = 28;
    const coreX = centerX - coreW / 2;

    // Subtle drop shadow on the bottom coil indicating float height
    const shadowDist = (chamberY + chamberH - 38) - (currentCoreY + coreH / 2);
    const shadowScale = Math.max(0.4, 1 - shadowDist / 200);
    ctx.fillStyle = 'rgba(15, 23, 42, 0.12)';
    ctx.beginPath();
    ctx.ellipse(centerX, chamberY + chamberH - 42, (coreW / 2) * shadowScale, 6 * shadowScale, 0, 0, Math.PI * 2);
    ctx.fill();

    // Core Glow Aura
    ctx.shadowColor = 'rgba(0, 229, 255, 0.7)';
    ctx.shadowBlur = 20;

    // Core Body Gradient (Titanium & Electric Rim)
    const coreGrad = ctx.createLinearGradient(coreX, currentCoreY - coreH / 2, coreX + coreW, currentCoreY + coreH / 2);
    coreGrad.addColorStop(0, '#0F172A');
    coreGrad.addColorStop(0.5, '#1E293B');
    coreGrad.addColorStop(1, '#0F172A');

    ctx.fillStyle = coreGrad;
    ctx.strokeStyle = '#00E5FF';
    ctx.lineWidth = 2.5;

    ctx.beginPath();
    ctx.roundRect(coreX, currentCoreY - coreH / 2, coreW, coreH, 8);
    ctx.fill();
    ctx.stroke();
    ctx.shadowBlur = 0;

    // Glowing Central Quantum Nucleus / Status Dot
    ctx.fillStyle = '#00E5FF';
    ctx.shadowColor = '#00E5FF';
    ctx.shadowBlur = 12;
    ctx.beginPath();
    ctx.arc(centerX, currentCoreY, 4, 0, Math.PI * 2);
    ctx.fill();
    ctx.shadowBlur = 0;

    // Core Center Technical Vector Reticle
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.8)';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(centerX - 16, currentCoreY);
    ctx.lineTo(centerX + 16, currentCoreY);
    ctx.moveTo(centerX, currentCoreY - 10);
    ctx.lineTo(centerX, currentCoreY + 10);
    ctx.stroke();

    // -------------------------------------------------------------
    // F. Technical Schematic Annotations & Calipers
    // -------------------------------------------------------------
    ctx.restore();
    ctx.save();
    ctx.font = '700 9px "SF Mono", Consolas, Menlo, monospace';
    ctx.fillStyle = '#0284C7';

    // Left Caliper: Height Metric
    const leftBracketX = chamberX - 18;
    ctx.strokeStyle = '#0284C7';
    ctx.lineWidth = 1.2;
    ctx.beginPath();
    ctx.moveTo(leftBracketX + 4, currentCoreY);
    ctx.lineTo(leftBracketX, currentCoreY);
    ctx.lineTo(leftBracketX, chamberY + chamberH - 38);
    ctx.lineTo(leftBracketX + 4, chamberY + chamberH - 38);
    ctx.stroke();

    ctx.textAlign = 'right';
    const altValue = (18.4 - (this.coreY * 0.12)).toFixed(1);
    ctx.fillText(`Δh = ${altValue} mm`, leftBracketX - 4, (currentCoreY + (chamberY + chamberH - 38)) / 2 + 3);

    // Right Caliper: Equilibrium Center
    const rightBracketX = chamberX + chamberW + 18;
    ctx.beginPath();
    ctx.moveTo(rightBracketX - 4, centerY);
    ctx.lineTo(rightBracketX, centerY);
    ctx.lineTo(rightBracketX, currentCoreY);
    ctx.lineTo(rightBracketX - 4, currentCoreY);
    ctx.stroke();

    ctx.textAlign = 'left';
    ctx.fillText(`F_net = ${(this.coreVelocity * -0.8).toFixed(2)} N`, rightBracketX + 4, (centerY + currentCoreY) / 2 + 3);

    ctx.restore();
  }

  animate() {
    this.updatePhysics();
    this.draw();
    requestAnimationFrame(() => this.animate());
  }
}

// ==========================================================================
// 3. COMPANION BENTO MINI-VISUALIZERS
// ==========================================================================

// A. Pendulum Waves Visualizer (12 harmonically tuned pendulums)
class PendulumWaveVisualizer {
  constructor(canvasId) {
    this.canvas = document.getElementById(canvasId);
    if (!this.canvas) return;
    this.ctx = this.canvas.getContext('2d');
    this.time = 0;
    this.bobs = 12;
    this.resize();
    window.addEventListener('resize', () => this.resize());
    this.animate();
  }

  resize() {
    const rect = this.canvas.getBoundingClientRect();
    this.width = rect.width;
    this.height = rect.height;
    this.canvas.width = this.width * window.devicePixelRatio;
    this.canvas.height = this.height * window.devicePixelRatio;
    this.ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
  }

  animate() {
    this.time += 0.025;
    const ctx = this.ctx;
    const w = this.width;
    const h = this.height;

    ctx.clearRect(0, 0, w, h);

    const startX = 24;
    const endX = w - 24;
    const stepX = (endX - startX) / (this.bobs - 1);
    const originY = 16;
    const maxAmplitude = 36;

    // Ceiling bar
    ctx.strokeStyle = '#CBD5E1';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(startX - 10, originY);
    ctx.lineTo(endX + 10, originY);
    ctx.stroke();

    for (let i = 0; i < this.bobs; i++) {
      const bx = startX + i * stepX;
      // Frequency increment per bob
      const freq = 1.0 + (i * 0.12);
      const angle = Math.sin(this.time * freq) * 0.45;
      const length = 55 + i * 4;

      const bobX = bx + Math.sin(angle) * maxAmplitude;
      const bobY = originY + Math.cos(angle) * length;

      // Suspension thread
      ctx.strokeStyle = 'rgba(148, 163, 184, 0.4)';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(bx, originY);
      ctx.lineTo(bobX, bobY);
      ctx.stroke();

      // Bob with fiery orange glow
      ctx.fillStyle = '#F97316';
      ctx.shadowColor = 'rgba(249, 115, 22, 0.5)';
      ctx.shadowBlur = 6;
      ctx.beginPath();
      ctx.arc(bobX, bobY, 4.5, 0, Math.PI * 2);
      ctx.fill();
      ctx.shadowBlur = 0;
    }

    requestAnimationFrame(() => this.animate());
  }
}

// B. Optics & Total Internal Reflection Visualizer
class OpticsVisualizer {
  constructor(canvasId) {
    this.canvas = document.getElementById(canvasId);
    if (!this.canvas) return;
    this.ctx = this.canvas.getContext('2d');
    this.time = 0;
    this.resize();
    window.addEventListener('resize', () => this.resize());
    this.animate();
  }

  resize() {
    const rect = this.canvas.getBoundingClientRect();
    this.width = rect.width;
    this.height = rect.height;
    this.canvas.width = this.width * window.devicePixelRatio;
    this.canvas.height = this.height * window.devicePixelRatio;
    this.ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
  }

  animate() {
    this.time += 0.03;
    const ctx = this.ctx;
    const w = this.width;
    const h = this.height;

    ctx.clearRect(0, 0, w, h);

    const midY = h * 0.55;

    // Dense Medium (Water / Acrylic block)
    ctx.fillStyle = 'rgba(224, 242, 254, 0.45)';
    ctx.fillRect(0, midY, w, h - midY);

    // Interface boundary
    ctx.strokeStyle = '#0284C7';
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(0, midY);
    ctx.lineTo(w, midY);
    ctx.stroke();

    // Normal line
    const normalX = w * 0.5;
    ctx.setLineDash([3, 3]);
    ctx.strokeStyle = '#94A3B8';
    ctx.beginPath();
    ctx.moveTo(normalX, 10);
    ctx.lineTo(normalX, h - 10);
    ctx.stroke();
    ctx.setLineDash([]);

    // Laser ray entering from bottom left at an oscillating incident angle
    const incidentAngle = 0.55 + Math.sin(this.time * 1.2) * 0.35; // radians
    const criticalAngle = 0.85; // ~48.7 degrees for water/air

    const sourceX = normalX - Math.sin(incidentAngle) * 70;
    const sourceY = midY + Math.cos(incidentAngle) * 70;

    // Incident Ray (Bright Cyan Laser)
    ctx.strokeStyle = '#00E5FF';
    ctx.lineWidth = 2.5;
    ctx.shadowColor = '#00E5FF';
    ctx.shadowBlur = 8;
    ctx.beginPath();
    ctx.moveTo(sourceX, sourceY);
    ctx.lineTo(normalX, midY);
    ctx.stroke();

    if (incidentAngle > criticalAngle) {
      // Total Internal Reflection (TIR) - fully reflects downward
      const reflectX = normalX + Math.sin(incidentAngle) * 70;
      const reflectY = midY + Math.cos(incidentAngle) * 70;

      ctx.strokeStyle = '#00E5FF';
      ctx.beginPath();
      ctx.moveTo(normalX, midY);
      ctx.lineTo(reflectX, reflectY);
      ctx.stroke();
    } else {
      // Snell's Law Refraction into Air
      const n1 = 1.33; // water
      const n2 = 1.00; // air
      const sinTheta2 = (n1 / n2) * Math.sin(incidentAngle);
      const theta2 = Math.asin(Math.min(0.999, sinTheta2));

      const refractX = normalX + Math.sin(theta2) * 75;
      const refractY = midY - Math.cos(theta2) * 75;

      ctx.strokeStyle = '#38BDF8';
      ctx.beginPath();
      ctx.moveTo(normalX, midY);
      ctx.lineTo(refractX, refractY);
      ctx.stroke();

      // Weak reflected ray
      ctx.strokeStyle = 'rgba(0, 229, 255, 0.25)';
      ctx.beginPath();
      ctx.moveTo(normalX, midY);
      ctx.lineTo(normalX + Math.sin(incidentAngle) * 50, midY + Math.cos(incidentAngle) * 50);
      ctx.stroke();
    }
    ctx.shadowBlur = 0;

    requestAnimationFrame(() => this.animate());
  }
}

// C. Eddy Current Magnetic Braking Visualizer
class EddyCurrentVisualizer {
  constructor(canvasId) {
    this.canvas = document.getElementById(canvasId);
    if (!this.canvas) return;
    this.ctx = this.canvas.getContext('2d');
    this.time = 0;
    this.magnetYCopper = 20;
    this.magnetYPlastic = 20;
    this.resize();
    window.addEventListener('resize', () => this.resize());
    this.animate();
  }

  resize() {
    const rect = this.canvas.getBoundingClientRect();
    this.width = rect.width;
    this.height = rect.height;
    this.canvas.width = this.width * window.devicePixelRatio;
    this.canvas.height = this.height * window.devicePixelRatio;
    this.ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
  }

  animate() {
    this.time += 0.02;
    const ctx = this.ctx;
    const w = this.width;
    const h = this.height;

    ctx.clearRect(0, 0, w, h);

    const tubeW = 28;
    const tubeH = h - 36;
    const tube1X = w * 0.3 - tubeW / 2;
    const tube2X = w * 0.7 - tubeW / 2;
    const tubeY = 18;

    // Tube 1: Clear Plastic (Free Fall)
    ctx.fillStyle = 'rgba(241, 245, 249, 0.6)';
    ctx.strokeStyle = '#CBD5E1';
    ctx.lineWidth = 1.5;
    ctx.fillRect(tube1X, tubeY, tubeW, tubeH);
    ctx.strokeRect(tube1X, tubeY, tubeW, tubeH);

    // Tube 2: Pure Copper (Eddy Current Braking)
    const copperGrad = ctx.createLinearGradient(tube2X, 0, tube2X + tubeW, 0);
    copperGrad.addColorStop(0, '#EA580C');
    copperGrad.addColorStop(0.5, '#FDBA74');
    copperGrad.addColorStop(1, '#C2410C');
    ctx.fillStyle = copperGrad;
    ctx.fillRect(tube2X, tubeY, tubeW, tubeH);

    // Update Magnet Positions
    this.magnetYPlastic += 3.2; // fast acceleration
    if (this.magnetYPlastic > tubeY + tubeH - 14) this.magnetYPlastic = tubeY + 4;

    this.magnetYCopper += 0.65; // slow terminal velocity due to Lenz's law
    if (this.magnetYCopper > tubeY + tubeH - 14) this.magnetYCopper = tubeY + 4;

    // Draw Magnet 1 (Plastic)
    this.drawMagnet(tube1X + 4, this.magnetYPlastic, tubeW - 8, 12);

    // Draw Magnet 2 (Copper - with eddy rings)
    this.drawMagnet(tube2X + 4, this.magnetYCopper, tubeW - 8, 12);

    // Swirling Eddy Current Rings around falling magnet in copper
    ctx.strokeStyle = '#FDE047';
    ctx.lineWidth = 1.2;
    ctx.setLineDash([2, 3]);
    ctx.beginPath();
    ctx.ellipse(tube2X + tubeW / 2, this.magnetYCopper + 6, tubeW * 0.8, 5, 0, 0, Math.PI * 2);
    ctx.stroke();
    ctx.setLineDash([]);

    requestAnimationFrame(() => this.animate());
  }

  drawMagnet(x, y, w, h) {
    const ctx = this.ctx;
    // North pole (red)
    ctx.fillStyle = '#EF4444';
    ctx.fillRect(x, y, w, h / 2);
    // South pole (blue)
    ctx.fillStyle = '#3B82F6';
    ctx.fillRect(x, y + h / 2, w, h / 2);
  }
}

// D. Rotational Dynamics Visualizer
class RotationVisualizer {
  constructor(canvasId) {
    this.canvas = document.getElementById(canvasId);
    if (!this.canvas) return;
    this.ctx = this.canvas.getContext('2d');
    this.time = 0;
    this.resize();
    window.addEventListener('resize', () => this.resize());
    this.animate();
  }

  resize() {
    const rect = this.canvas.getBoundingClientRect();
    this.width = rect.width;
    this.height = rect.height;
    this.canvas.width = this.width * window.devicePixelRatio;
    this.canvas.height = this.height * window.devicePixelRatio;
    this.ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
  }

  animate() {
    this.time += 0.03;
    const ctx = this.ctx;
    const w = this.width;
    const h = this.height;

    ctx.clearRect(0, 0, w, h);

    const centerX = w / 2;
    const centerY = h / 2;

    // Mass distance oscillates (in and out)
    const radius = 22 + Math.sin(this.time * 0.8) * 14;
    // Speed increases when radius decreases (L = I * omega = const)
    const spinSpeed = 0.08 / (radius / 28);
    this.rotationAngle = (this.rotationAngle || 0) + spinSpeed;

    // Platform Base
    ctx.strokeStyle = '#CBD5E1';
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.ellipse(centerX, centerY + 30, 40, 10, 0, 0, Math.PI * 2);
    ctx.stroke();

    // Central rotating axis
    ctx.strokeStyle = '#6366F1';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(centerX, centerY - 25);
    ctx.lineTo(centerX, centerY + 30);
    ctx.stroke();

    // Rotating weights
    const x1 = centerX + Math.cos(this.rotationAngle) * radius;
    const y1 = centerY + Math.sin(this.rotationAngle) * (radius * 0.4);
    const x2 = centerX - Math.cos(this.rotationAngle) * radius;
    const y2 = centerY - Math.sin(this.rotationAngle) * (radius * 0.4);

    // Crossbar
    ctx.strokeStyle = '#1E293B';
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y2);
    ctx.stroke();

    // Dumbbell Weights
    ctx.fillStyle = '#6366F1';
    ctx.shadowColor = 'rgba(99, 102, 241, 0.4)';
    ctx.shadowBlur = 6;
    ctx.beginPath();
    ctx.arc(x1, y1, 6, 0, Math.PI * 2);
    ctx.arc(x2, y2, 6, 0, Math.PI * 2);
    ctx.fill();
    ctx.shadowBlur = 0;

    requestAnimationFrame(() => this.animate());
  }
}

// ==========================================================================
// 4. EXPERIMENT MODAL & DIY LAB NOTES DATA
// ==========================================================================
const experimentGuides = {
  antigravity: {
    badge: "ADVANCED MECHANICS & FLUX",
    title: "Electromagnetic & Diamagnetic Levitation",
    theory: "According to Earnshaw's theorem, static magnetic and electric monopoles cannot maintain stable, static equilibrium without feedback. However, stability is readily attained through dynamic electrodynamic repulsion (Lenz's Law eddy currents), diamagnetism (pyrolytic graphite with negative magnetic susceptibility χ < 0), or high-frequency feedback dampening.",
    materials: [
      "Pyrolytic Graphite sheet or Bismuth cylinder",
      "4 Neodymium (NdFeB) cube magnets arranged in checkerboard N-S-N-S quadrupole",
      "Copper plate / tube for eddy-current dampening",
      "Wood ruler & non-magnetic tweezers"
    ],
    steps: [
      "Arrange the 4 Neodymium cube magnets in an alternating checkerboard pattern (N-S-N-S) to create a steep magnetic field gradient.",
      "Gently place a thin flake of pyrolytic graphite directly over the junction of the 4 magnets.",
      "Observe the graphite slice instantly rise and float freely in mid-air with zero power input, perfectly repelled by both magnetic poles.",
      "Perturb the floating flake gently with a wooden stick: observe the instantaneous restoring force and harmonic oscillations."
    ]
  },
  pendulum: {
    badge: "WAVE MECHANICS & HARMONICS",
    title: "Pendulum Wave Apparatus",
    theory: "When an array of independent pendulums of progressively longer lengths oscillate simultaneously, their individual frequencies (f = 1 / (2π) * √(g/L)) follow an arithmetic progression. Over time, their phase differences produce traveling waves, standing waves, beats, and apparent chaos before reconverging in perfect synchrony.",
    materials: [
      "12 to 15 identical steel nuts or lead sinkers",
      "Monofilament fishing line or strong sewing thread",
      "1-meter wooden horizontal support beam",
      "Stopwatch and millimeter ruler"
    ],
    steps: [
      "Calculate the required thread lengths so that the longest pendulum completes N oscillations in 60 seconds, and each subsequent shorter pendulum completes N+1, N+2, ... oscillations.",
      "Mount the 12 bobs along the wooden beam at equal 5 cm spacings.",
      "Use a flat wooden ruler to deflect all 12 pendulums to the exact same initial angle, then release them simultaneously.",
      "Observe the mesmerizing snake wave dance, winding helixes, and periodic phase reconvergence after exactly one cycle."
    ]
  },
  optics: {
    badge: "GEOMETRICAL OPTICS & FIBER PRINCIPLES",
    title: "Laser Stream Total Internal Reflection",
    theory: "When a light ray travels from an optically denser medium (water, n = 1.33) toward a rarer medium (air, n = 1.0) at an incident angle greater than the critical angle (θ_c = arcsin(1/1.33) ≈ 48.75°), light cannot escape into the air. Instead, 100% of the light is reflected back inside the water column, forming the foundation of modern fiber optic telecommunications.",
    materials: [
      "Clear plastic 1-liter water bottle",
      "Red or green diode laser pointer (Class 2 safe)",
      "Pushpin to create a clean hole",
      "Water and a pinch of cornstarch/milk (to scatter laser light for visibility)",
      "Catch basin / tray"
    ],
    steps: [
      "Punch a clean, smooth 4 mm hole in the side of the plastic bottle about 5 cm from the base.",
      "Fill the bottle with water while covering the hole with your finger.",
      "Align the laser pointer from the opposite side of the bottle directly through the water toward the exit hole.",
      "Release your finger so a smooth, laminar water stream arches into the basin.",
      "Watch the laser beam remain completely trapped inside the curving water stream, following the bend all the way into the bucket!"
    ]
  },
  eddy: {
    badge: "ELECTROMAGNETISM & INDUCTION",
    title: "Lenz's Law in Copper Tubes",
    theory: "As a strong magnet falls through a conductive copper pipe, the changing magnetic flux induces circular eddy currents in the pipe walls (Faraday's Law). In accordance with Lenz's Law, these induced currents generate a counter-magnetic field that opposes the motion of the magnet, resulting in a gentle, slow-motion terminal drift.",
    materials: [
      "1-meter long heavy-gauge copper pipe (clean and uncorroded)",
      "1-meter long acrylic or PVC plastic pipe of matching diameter",
      "Strong cylindrical Neodymium magnet (fits pipe with small clearance)",
      "Stopwatch"
    ],
    steps: [
      "Hold the plastic pipe vertically and drop the neodymium magnet through it. Note that it falls in under 0.45 seconds, accelerating at free-fall gravity g.",
      "Now hold the copper pipe vertically and drop the exact same magnet through it.",
      "Peer into the top of the pipe: observe the magnet drift slowly and serenely down the pipe, taking 4 to 6 seconds to exit without ever touching the walls!",
      "Explain how modern maglev bullet trains and rollercoasters utilize this exact contactless eddy-current magnetic braking."
    ]
  },
  rotation: {
    badge: "CLASSICAL MECHANICS",
    title: "Conservation of Angular Momentum",
    theory: "In the absence of external torque, the total angular momentum L = I * ω of a rotating system remains constant. When the moment of inertia I is reduced by drawing mass inward closer to the rotation axis, the angular velocity ω must proportionally increase to conserve momentum.",
    materials: [
      "Smooth-bearing swivel chair or rotating platform",
      "Two 1 kg or 2 kg weights (or full water bottles)",
      "Safe open floor area with an assistant"
    ],
    steps: [
      "Sit upright in the center of the swivel chair holding one weight in each hand with your arms fully outstretched horizontally.",
      "Have an assistant give you a gentle, slow initial spin.",
      "While rotating, suddenly pull your arms and the weights tightly into your chest.",
      "Feel the sudden, dramatic surge in rotational speed!",
      "Extend your arms back outward: observe your rotation immediately slow back down, demonstrating the physics of spinning figure skaters and collapsing neutron stars."
    ]
  }
};

function openExperimentModal(key) {
  const guide = experimentGuides[key] || experimentGuides.antigravity;
  const modal = document.getElementById('experimentModal');
  if (!modal) return;

  document.getElementById('modalBadge').innerText = guide.badge;
  document.getElementById('modalTitle').innerText = guide.title;
  document.getElementById('modalTheoryText').innerText = guide.theory;

  const matList = document.getElementById('modalApparatusList');
  matList.innerHTML = guide.materials.map(m => `
    <li class="apparatus-item">
      <span class="bullet">▸</span>
      <span>${m}</span>
    </li>
  `).join('');

  const procList = document.getElementById('modalProcedureSteps');
  procList.innerHTML = guide.steps.map(s => `<li>${s}</li>`).join('');

  modal.classList.add('active');
  document.body.style.overflow = 'hidden';
}

function closeExperimentModal() {
  const modal = document.getElementById('experimentModal');
  if (!modal) return;
  modal.classList.remove('active');
  document.body.style.overflow = '';
}

// ==========================================================================
// 5. INITIALIZATION ON DOM READY
// ==========================================================================
document.addEventListener('DOMContentLoaded', () => {
  // A. Language Switcher Buttons
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      setLanguage(btn.dataset.lang);
    });
  });

  // B. Initialize Anti-Gravity Chamber
  const antiGravityChamber = new AntiGravityChamber('antigravityCanvas');

  // C. Initialize Bento Companion Visualizers
  new PendulumWaveVisualizer('pendulumCanvas');
  new OpticsVisualizer('opticsCanvas');
  new EddyCurrentVisualizer('eddyCanvas');
  new RotationVisualizer('rotationCanvas');

  // D. Modal Trigger Buttons
  document.querySelectorAll('[data-experiment-trigger]').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      openExperimentModal(btn.dataset.experimentTrigger);
    });
  });

  const modalClose = document.getElementById('modalCloseBtn');
  if (modalClose) {
    modalClose.addEventListener('click', closeExperimentModal);
  }

  const modalBackdrop = document.getElementById('experimentModal');
  if (modalBackdrop) {
    modalBackdrop.addEventListener('click', (e) => {
      if (e.target === modalBackdrop) closeExperimentModal();
    });
  }

  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeExperimentModal();
  });

  // E. Mobile Navigation Drawer Toggle
  const mobileToggle = document.getElementById('mobileMenuToggle');
  const mobileDrawer = document.getElementById('mobileNavDrawer');
  if (mobileToggle && mobileDrawer) {
    mobileToggle.addEventListener('click', () => {
      mobileDrawer.classList.toggle('active');
    });
  }

  // F. Navbar Shadow on Scroll
  const navbar = document.getElementById('mainNavbar');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 20) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  });

  // Initial Language Set
  setLanguage('en');
});

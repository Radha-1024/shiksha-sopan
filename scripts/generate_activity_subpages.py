import os

BASE_DIR = "/Users/radha/.gemini/antigravity/scratch/shiksha-sopan-redesign"

ACTIVITIES = [
    {
        "id": "A",
        "slug": "sopan-anaupcharik-shikshan-kendra",
        "title": "Sopan Anaupcharik Shikshan Kendra (SASK)",
        "hindi_title": "सोपान अनौपचारिक शिक्षण केंद्र (सास्क)",
        "short_title": "SASK Informal School",
        "badge": "Primary & Informal Education",
        "lead": "Sopan Anaupcharik Shikshan Kendra (SASK) is our flagship informal school running in Barasirohi village during normal morning school hours, dedicated to educating children of migrant laborers and disadvantaged families who cannot afford private school fees.",
        "metrics": [
            ("75-80", "Children Enrolled"),
            ("Morning", "Regular School Hours"),
            ("Barasirohi", "Village Campus"),
            ("100%", "Free Tuition & Kits")
        ],
        "content_html": """
          <div class="bento-section">
            <span class="section-eyebrow">MISSION & BACKGROUND</span>
            <h2 class="section-h2">Bringing Quality Primary Education to Every Child</h2>
            <div class="card-grid-2">
              <div class="feature-card">
                <div class="card-icon-pill">🏫</div>
                <h3 class="card-title">Barasirohi Village Morning Center</h3>
                <p class="card-desc">
                  Unlike traditional tuition centers, SASK functions as a semi-formal school during standard morning hours. It was created to bridge the critical gap for children in Barasirohi village—most of whom belong to labor-class families unable to bear conventional private school fees.
                </p>
                <ul class="card-feature-list">
                  <li>Comprehensive foundational education in basic mathematics, Hindi, and English.</li>
                  <li>Value-based character building (Shiksha, Sanskar, Swavalamban).</li>
                  <li>Regular physical training, yoga, and interactive morning assemblies.</li>
                </ul>
              </div>

              <div class="feature-card">
                <div class="card-icon-pill">🍎</div>
                <h3 class="card-title">Holistic Nutrition & Health Care</h3>
                <p class="card-desc">
                  Education cannot flourish without proper health and nourishment. SASK integrates essential welfare programs supported by the IIT Kanpur community and benevolent donors.
                </p>
                <ul class="card-feature-list">
                  <li>Nutritional food and snacks distribution during school hours.</li>
                  <li>Regular health checkups and seasonal clothing/uniform distributions.</li>
                  <li>Free educational stationery, textbooks, and interactive learning toys.</li>
                </ul>
              </div>
            </div>
          </div>

          <div class="bento-section">
            <span class="section-eyebrow">COMMUNITY LIFE & CELEBRATIONS</span>
            <h2 class="section-h2">Celebrations, Science & Co-Curricular Growth</h2>
            <div class="card-grid-3">
              <div class="feature-card">
                <div class="card-icon-pill">🇮🇳</div>
                <h3 class="card-title">National Festivals</h3>
                <p class="card-desc">Children celebrate Independence Day, Republic Day, and Gandhi Jayanti with inspiring skits, parades, and cultural performances.</p>
              </div>
              <div class="feature-card">
                <div class="card-icon-pill">🔬</div>
                <h3 class="card-title">Hands-On Science Demonstrations</h3>
                <p class="card-desc">Weekly interactive physics and nature demonstrations conducted by IIT Kanpur student volunteers spark early scientific curiosity.</p>
              </div>
              <div class="feature-card">
                <div class="card-icon-pill">🎨</div>
                <h3 class="card-title">Art & Creative Workshops</h3>
                <p class="card-desc">Rangoli, drawing, origami, and dramatics allow children to express themselves and build lasting social confidence.</p>
              </div>
            </div>
          </div>
        """
    },
    {
        "id": "B",
        "slug": "evening-learning-centers",
        "title": "Evening Learning Centers",
        "hindi_title": "सांध्य शिक्षण केंद्र",
        "short_title": "Evening Centers",
        "badge": "After-School Tutoring & Mentorship",
        "lead": "Our Evening Learning Centers provide crucial after-school academic assistance to children from classes 4 to 12. Taught by enthusiastic IIT Kanpur student volunteers, these centers ensure students from financially constrained families never fall behind.",
        "metrics": [
            ("2", "Active Centers"),
            ("100+", "Total Students"),
            ("Classes 4-12", "Grade Coverage"),
            ("2 Hours", "Daily Evening Sessions")
        ],
        "content_html": """
          <div class="bento-section">
            <span class="section-eyebrow">CENTER LOCATIONS</span>
            <h2 class="section-h2">Two Vibrant Centers Serving Local Students</h2>
            <div class="card-grid-2">
              <div class="feature-card">
                <div class="card-icon-pill">🎓</div>
                <h3 class="card-title">Old SAC Center (IIT Kanpur Campus)</h3>
                <p class="card-desc">
                  Operating in the Students' Activity Centre (Old SAC) inside the IIT Kanpur campus, this center caters to children of campus staff and surrounding neighborhoods. About 50 students attend daily for rigorous guidance in mathematics, sciences, and languages.
                </p>
                <ul class="card-feature-list">
                  <li>Direct access to IIT Kanpur academic environment and mentorship.</li>
                  <li>Focused preparation for high school and board examinations.</li>
                  <li>Doubt-clearing sessions led by undergraduate and postgraduate IITians.</li>
                </ul>
              </div>

              <div class="feature-card">
                <div class="card-icon-pill">🏡</div>
                <h3 class="card-title">Barasirohi Evening Center (BEC)</h3>
                <p class="card-desc">
                  Located in Barasirohi village, this center serves roughly 50 local children who attend neighborhood government or semi-aided schools and need structured support to complete homework and strengthen concepts.
                </p>
                <ul class="card-feature-list">
                  <li>Neighborhood accessibility eliminating travel concerns for rural children.</li>
                  <li>Emphasis on arithmetic fluency, reading comprehension, and problem solving.</li>
                  <li>Close regular coordination with village parents and guardians.</li>
                </ul>
              </div>
            </div>
          </div>

          <div class="bento-section">
            <span class="section-eyebrow">PEDAGOGICAL APPROACH</span>
            <h2 class="section-h2">Why Evening Centers Make an Unmatched Difference</h2>
            <div class="card-grid-3">
              <div class="feature-card">
                <div class="card-icon-pill">💡</div>
                <h3 class="card-title">No Tuition Burdens</h3>
                <p class="card-desc">Private tuition is financially impossible for labor-class families. Evening centers level the playing field free of cost.</p>
              </div>
              <div class="feature-card">
                <div class="card-icon-pill">🤝</div>
                <h3 class="card-title">IIT Kanpur Mentorship</h3>
                <p class="card-desc">Student volunteers from IITK form empathetic bonds with children, acting as role models and lifelong academic guides.</p>
              </div>
              <div class="feature-card">
                <div class="card-icon-pill">📈</div>
                <h3 class="card-title">Measurable Academic Gains</h3>
                <p class="card-desc">Regular tests, grade monitoring, and individual mentoring ensure steady promotion and reduced school dropout rates.</p>
              </div>
            </div>
          </div>
        """
    },
    {
        "id": "C",
        "slug": "sopan-science-cell",
        "title": "Sopan Science Cell",
        "hindi_title": "सोपान विज्ञान प्रकोष्ठ",
        "short_title": "Science Cell",
        "badge": "Hands-On STEM & Low-Cost Kits",
        "lead": "The Sopan Science Cell develops and demonstrates low-cost physics experiments that connect scientific principles with everyday reality, led by Prof. H.C. Verma and passionate village youth.",
        "metrics": [
            ("100+", "Indigenous Experiments"),
            ("Dozens", "School Shows Every Year"),
            ("Prof. H.C. Verma", "Founder & Guide"),
            ("Zero Cost", "To Rural Schools")
        ],
        "content_html": """
          <div class="bento-section">
            <span class="section-eyebrow">OUR PHILOSOPHY</span>
            <h2 class="section-h2">Experiencing Science Through Touch & Observation</h2>
            <div class="card-grid-2">
              <div class="feature-card">
                <div class="card-icon-pill">🔬</div>
                <h3 class="card-title">Low-Cost Indigenous Experiments</h3>
                <p class="card-desc">
                  Science is often taught from dry textbooks with abstract equations. The Sopan Science Cell revolutionizes pedagogy by fabricating experiments out of discarded bottles, bicycle spokes, syringes, magnets, and lenses.
                </p>
                <ul class="card-feature-list">
                  <li>Mechanics, optics, electromagnetism, and fluid pressure demystified.</li>
                  <li>Every demonstration explains a direct real-world phenomenon.</li>
                  <li>Cost-effective kits assembled by local village technicians.</li>
                </ul>
              </div>

              <div class="feature-card">
                <div class="card-icon-pill">🚌</div>
                <h3 class="card-title">School Shows & Outreach Tours</h3>
                <p class="card-desc">
                  The team travels to government schools, rural colleges, and ashrams, staging interactive science stage shows that leave students spellbound and eager to ask questions.
                </p>
                <ul class="card-feature-list">
                  <li>Direct hands-on participation by schoolchildren on stage.</li>
                  <li>First Sunday Club workshops with SGM-IAPT Anveshika.</li>
                  <li>Residential teacher training camps at Sopan Ashram.</li>
                </ul>
              </div>
            </div>
          </div>
        """
    },
    {
        "id": "D",
        "slug": "v-n-kulkarni-merit-scholarship",
        "title": "Dr. V. N. Kulkarni Merit Scholarship",
        "hindi_title": "डॉ. वी. एन. कुलकर्णी मेधा छात्रवृत्ति परीक्षा",
        "short_title": "VNK Scholarship",
        "badge": "Merit-Cum-Means Scholarship",
        "lead": "Instituted in 2011 in memory of the revered experimental physicist late Prof. V. N. Kulkarni of IIT Kanpur, this scholarship recognizes and finances promising students from economically disadvantaged families in the IITK vicinity.",
        "metrics": [
            ("Classes 5, 8, 10", "Eligible Grades"),
            ("2-3 Years", "Scholarship Tenure"),
            ("3-6 km", "Radius from IITK"),
            ("2011", "Year Established")
        ],
        "content_html": """
          <div class="bento-section">
            <span class="section-eyebrow">SELECTION METHODOLOGY</span>
            <h2 class="section-h2">A Rigorous Two-Tier Selection Process</h2>
            <div class="card-grid-2">
              <div class="feature-card">
                <div class="card-icon-pill">📝</div>
                <h3 class="card-title">Stage 1: Written Examination</h3>
                <p class="card-desc">
                  Conducted annually across schools in the neighboring region. The examination tests conceptual clarity, basic mathematical reasoning, language comprehension, and scientific curiosity rather than rote memory.
                </p>
                <ul class="card-feature-list">
                  <li>Open to students of classes 5, 8, and 10 from local schools.</li>
                  <li>Objective and short-answer questions designed by IIT Kanpur educators.</li>
                  <li>Completely fee-free examination for all candidates.</li>
                </ul>
              </div>

              <div class="feature-card">
                <div class="card-icon-pill">🔍</div>
                <h3 class="card-title">Stage 2: Economic Ground Survey</h3>
                <p class="card-desc">
                  Merit alone is not enough—financial hardship is our decisive criterion. Shiksha Sopan volunteers visit the homes of shortlisted candidates to inspect economic conditions and verify genuine need.
                </p>
                <ul class="card-feature-list">
                  <li>Personal home visits by volunteer inspection teams.</li>
                  <li>Assessment of family income, living conditions, and educational expenses.</li>
                  <li>Guarantees that 100% of scholarship grants go to truly needy families.</li>
                </ul>
              </div>
            </div>
          </div>

          <div class="bento-section">
            <span class="section-eyebrow">SCHOLARSHIP TENURE</span>
            <h2 class="section-h2">Multi-Year Sustained Support</h2>
            <div class="card-grid-3">
              <div class="feature-card">
                <div class="card-icon-pill">5️⃣</div>
                <h3 class="card-title">Class 5 Awardees</h3>
                <p class="card-desc">Receive continuous financial backing for 3 complete academic years (covering classes 6, 7, and 8).</p>
              </div>
              <div class="feature-card">
                <div class="card-icon-pill">8️⃣</div>
                <h3 class="card-title">Class 8 Awardees</h3>
                <p class="card-desc">Supported for 2 crucial years (classes 9 and 10) to help clear high school matriculation.</p>
              </div>
              <div class="feature-card">
                <div class="card-icon-pill">🔟</div>
                <h3 class="card-title">Class 10 Awardees</h3>
                <p class="card-desc">Supported for 2 years (classes 11 and 12) through their intermediate pre-university journey.</p>
              </div>
            </div>
          </div>
        """
    },
    {
        "id": "E",
        "slug": "higher-education-cell",
        "title": "Higher Education Cell & SGPV",
        "hindi_title": "उच्च शिक्षा प्रकोष्ठ एवं श्री गणेश प्रसाद वर्मा उच्च शिक्षा प्रकल्प",
        "short_title": "Higher Education Cell",
        "badge": "College & Professional Degree Grants",
        "lead": "The Higher Education Cell, anchored by the Shree Ganesh Prasad Verma (SGPV) Uchch Shiksha Prakalp, ensures that financial distress never stops a talented underprivileged student from completing college, engineering, medical, or vocational diplomas.",
        "metrics": [
            ("Post-12th", "Target Level"),
            ("Grants & Loans", "Financial Models"),
            ("SGPV", "Memorial Project"),
            ("Quarterly", "Academic Review")
        ],
        "content_html": """
          <div class="bento-section">
            <span class="section-eyebrow">SHREE GANESH PRASAD VERMA PRAKALP</span>
            <h2 class="section-h2">Empowering Dreams of Higher Education</h2>
            <div class="card-grid-2">
              <div class="feature-card">
                <div class="card-icon-pill">👨‍🏫</div>
                <h3 class="card-title">In Memory of Shree Ganesh Prasad Verma</h3>
                <p class="card-desc">
                  Named in honor of the father of Prof. H.C. Verma, who was a dedicated teacher with a lifelong aspiration to carry knowledge to the most marginalized sections of society.
                </p>
                <ul class="card-feature-list">
                  <li>Assistance for students clearing entrance examinations into recognized degree programs.</li>
                  <li>Supports engineering (B.Tech/Diploma), basic sciences (B.Sc), humanities, and nursing.</li>
                  <li>Funds cover tuition, semester admission fees, textbooks, and equipment.</li>
                </ul>
              </div>

              <div class="feature-card">
                <div class="card-icon-pill">📋</div>
                <h3 class="card-title">Accountability & Mentorship</h3>
                <p class="card-desc">
                  The cell is managed by a faculty committee from IIT Kanpur that reviews candidate applications, conducts interviews, and follows student progress every step of the way.
                </p>
                <ul class="card-feature-list">
                  <li>Recipients submit academic progress reports every 3 months.</li>
                  <li>Mentorship provided by IIT faculty and professionals throughout the course.</li>
                  <li>Alumni often return as donors and volunteers to mentor younger scholars.</li>
                </ul>
              </div>
            </div>
          </div>
        """
    },
    {
        "id": "F",
        "slug": "sushree-shashikala-joshi-memorial-sopan-library",
        "title": "Sushree Shashikala Joshi Memorial Sopan Library",
        "hindi_title": "सुश्री शशिकला जोशी स्मृति सोपान पुस्तकालय",
        "short_title": "Sopan Library",
        "badge": "Community Library & Literacy",
        "lead": "Situated at the Type-1 Community Center on the IIT Kanpur campus, this vibrant community library was established to revive reading habits among young children through books, storytelling, and creative art workshops.",
        "metrics": [
            ("Type-1", "Campus Location"),
            ("Hundreds", "Books & Periodicals"),
            ("Story Sessions", "Weekly Programs"),
            ("All Ages", "Community Access")
        ],
        "content_html": """
          <div class="bento-section">
            <span class="section-eyebrow">LIBRARY OBJECTIVES</span>
            <h2 class="section-h2">Reviving the Joy of Reading & Creative Expression</h2>
            <div class="card-grid-2">
              <div class="feature-card">
                <div class="card-icon-pill">📚</div>
                <h3 class="card-title">Curated Reading Space</h3>
                <p class="card-desc">
                  With screens dominating daily life, the Sopan Library provides a serene sanctuary filled with illustrated storybooks, children's literature, science magazines, historical biographies, and reference volumes.
                </p>
                <ul class="card-feature-list">
                  <li>Free book borrowing for community children and student volunteers.</li>
                  <li>Children's classics in Hindi and English with rich pictorial illustrations.</li>
                  <li>Quiet study tables and friendly volunteer librarians.</li>
                </ul>
              </div>

              <div class="feature-card">
                <div class="card-icon-pill">🎭</div>
                <h3 class="card-title">Storytelling & Creative Sessions</h3>
                <p class="card-desc">
                  Led by dedicated coordinators Mrs. Pushpa Tripathi, Ms. Shipra, and campus volunteers, the library hosts interactive day-wise sessions.
                </p>
                <ul class="card-feature-list">
                  <li>Oral storytelling and moral value discussions.</li>
                  <li>Creative painting, drawing, and origami clubs.</li>
                  <li>Book review circles where children share what they read.</li>
                </ul>
              </div>
            </div>
          </div>
        """
    },
    {
        "id": "G",
        "slug": "functions",
        "title": "Annual & Occasional Functions",
        "hindi_title": "वार्षिक एवं विशेष समारोह",
        "short_title": "Functions",
        "badge": "Community Teamwork & Celebrations",
        "lead": "Functions play an essential role in developing management skills, teamwork, and national consciousness. Shiksha Sopan conducts regular annual and occasional functions bringing together students, IIT Kanpur faculty, and rural communities.",
        "metrics": [
            ("3 Major", "Annual Functions"),
            ("500-600", "Rally Participants"),
            ("2.5 Hours", "Cultural Stage Show"),
            ("L-7 IITK", "Independence Day Hall")
        ],
        "content_html": """
          <div class="bento-section">
            <span class="section-eyebrow">OUR THREE REGULAR FUNCTIONS</span>
            <h2 class="section-h2">Marking Important Milestones on the Annual Calendar</h2>

            <!-- Event 1: 12th January -->
            <div class="event-card">
              <div class="event-date-col">
                <div class="event-date-title">12 JAN</div>
                <div class="event-date-sub">Annual Function</div>
                <div style="font-size:0.75rem; color:#64748B; margin-top:0.35rem;">Vivekananda Jayanti Week</div>
              </div>
              <div class="event-main-col">
                <h3>Swami Vivekananda Birth Anniversary & Annual Cultural Week</h3>
                <p>
                  Celebrated during the week containing January 12th, this is Shiksha Sopan's flagship celebration. Programs are open to the entire village community around the IITK campus, fostering vibrant participation and cultural pride.
                </p>
                <ul class="card-feature-list">
                  <li><b>Week-Long Competitions:</b> Rangoli-making, debates, essay competitions, general & science quizzes, drawing/painting, and singing patriotic and nationalistic songs.</li>
                  <li><b>Social Awareness Rally:</b> 500 to 600 children and adults march through Barasirohi village carrying placards on girl-child education, clean environment, water conservation, and anti-tobacco awareness.</li>
                  <li><b>Grand Cultural Stage Show:</b> A 2.5-hour cultural extravaganza staged in Barasirohi where children showcase their talents in dramatics, folk dances, musical skits, and public oration.</li>
                </ul>
              </div>
            </div>

            <!-- Event 2: 15th August -->
            <div class="event-card">
              <div class="event-date-col">
                <div class="event-date-title">15 AUG</div>
                <div class="event-date-sub">Independence Day</div>
                <div style="font-size:0.75rem; color:#64748B; margin-top:0.35rem;">Lecture Hall L-7, IITK</div>
              </div>
              <div class="event-main-col">
                <h3>Independence Day Celebrations at IIT Kanpur</h3>
                <p>
                  Held inside the premier Lecture Hall L-7 at IIT Kanpur, this function is designed to foster a sense of national commitment and remember the sacrifices of freedom fighters.
                </p>
                <ul class="card-feature-list">
                  <li>Children from all Shiksha Sopan learning centers gather on the IITK campus.</li>
                  <li>Presentation of short theatrical skits related to the Indian freedom struggle and pivotal social reforms.</li>
                  <li>Patriotic songs and speeches by children and distinguished IITK faculty members.</li>
                </ul>
              </div>
            </div>

            <!-- Event 3: 2nd October -->
            <div class="event-card">
              <div class="event-date-col">
                <div class="event-date-title">02 OCT</div>
                <div class="event-date-sub">Gandhi Jayanti</div>
                <div style="font-size:0.75rem; color:#64748B; margin-top:0.35rem;">Barasirohi Vidyalaya</div>
              </div>
              <div class="event-main-col">
                <h3>Mahatma Gandhi & Lal Bahadur Shastri Jayanti</h3>
                <p>
                  A solemn day dedicated to reaffirming commitments to a corruption-free society based on truth, non-violence, simplicity, and national well-being.
                </p>
                <ul class="card-feature-list">
                  <li>Children at Barasirohi Vidyalaya stage skits illustrating key episodes from the lives of Mahatma Gandhi and Lal Bahadur Shastri.</li>
                  <li>Discussions on swachhata (cleanliness), ethical conduct, and social service.</li>
                  <li>Community pledges toward non-violence, mutual harmony, and truthfulness.</li>
                </ul>
              </div>
            </div>
          </div>

          <div class="bento-section">
            <span class="section-eyebrow">OCCASIONAL FUNCTIONS</span>
            <h2 class="section-h2">Building Lifelong Character Through Festive Events</h2>
            <div class="card-grid-3">
              <div class="feature-card">
                <div class="card-icon-pill">🧑‍🏫</div>
                <h3 class="card-title">Teachers' Day</h3>
                <p class="card-desc">Students honor their volunteer mentors and school teachers, expressing gratitude through handwritten cards and recitation.</p>
              </div>
              <div class="feature-card">
                <div class="card-icon-pill">🎉</div>
                <h3 class="card-title">Children's Day (Bal Diwas)</h3>
                <p class="card-desc">Fun sports, traditional games, science riddle contests, and special sweet distributions across all centers.</p>
              </div>
              <div class="feature-card">
                <div class="card-icon-pill">💡</div>
                <h3 class="card-title">Science Fairs & Exhibitions</h3>
                <p class="card-desc">Periodic science exhibition days where rural students present working scientific models to parents and visitors.</p>
              </div>
            </div>
          </div>
        """
    },
    {
        "id": "H",
        "slug": "finance-management",
        "title": "Finance Management & Transparency",
        "hindi_title": "वित्तीय प्रबंधन एवं पारदर्शिता",
        "short_title": "Finance Management",
        "badge": "Transparency, Audits & 80G Tax Exemption",
        "lead": "Financial management at Shiksha Sopan is guided by strict transparency and zero administrative overhead. Supported purely by open donations and sponsorship schemes, every single rupee directly impacts student learning and rural welfare.",
        "metrics": [
            ("~0%", "Office Overhead"),
            ("100%", "Direct Impact"),
            ("80G", "Tax Exemption"),
            ("Annual", "Statutory Audits")
        ],
        "content_html": """
          <div class="bento-section">
            <span class="section-eyebrow">GOVERNANCE & TRANSPARENCY</span>
            <h2 class="section-h2">Uncompromising Principles of Financial Stewardship</h2>
            <div class="card-grid-2">
              <div class="feature-card">
                <div class="card-icon-pill">🏛️</div>
                <h3 class="card-title">Near-Zero Administrative Overhead</h3>
                <p class="card-desc">
                  Shiksha Sopan has virtually zero office maintenance expenses. Because administration, management, and teaching are driven by passionate volunteers from the IIT Kanpur community, your donations do not go to rent, fancy offices, or high salaries.
                </p>
                <ul class="card-feature-list">
                  <li>Direct channeling of funds to student welfare, books, and science kits.</li>
                  <li>No lavish administrative expenses or intermediary overhead.</li>
                  <li>Meticulous record keeping maintained by student and faculty volunteers.</li>
                </ul>
              </div>

              <div class="feature-card">
                <div class="card-icon-pill">⚖️</div>
                <h3 class="card-title">Annual Auditing & Statutory Filing</h3>
                <p class="card-desc">
                  All accounts are audited every year by certified external Chartered Accountants. Detailed balance sheets and expenditure statements are finalized, after which statutory income tax returns are filed.
                </p>
                <ul class="card-feature-list">
                  <li>Annual financial reports detailing every receipt and disbursement.</li>
                  <li>Periodic internal reviews by the Executive Committee.</li>
                  <li>Clear reporting to general body members and donors.</li>
                </ul>
              </div>
            </div>
          </div>

          <!-- Official Bank Details Card -->
          <div class="bank-box">
            <h3>Support Shiksha Sopan: Official Banking Details</h3>
            <p>
              Contributions to Shiksha Sopan are 100% tax-free under Section 80/G of the Income Tax Act. You can make an open donation of any amount via direct bank transfer or cheque.
            </p>
            <div class="bank-details-grid">
              <div class="bank-detail-item">
                <div class="label">Beneficiary Name</div>
                <div class="val">SHIKSHA SOPAN</div>
              </div>
              <div class="bank-detail-item">
                <div class="label">Bank & Branch</div>
                <div class="val">State Bank of India (SBI), IIT Kanpur Branch</div>
              </div>
              <div class="bank-detail-item">
                <div class="label">Account Number</div>
                <div class="val">10426002488</div>
              </div>
              <div class="bank-detail-item">
                <div class="label">IFSC Code</div>
                <div class="val">SBIN0001161</div>
              </div>
            </div>
            <div style="margin-top: 1.5rem; font-size: 0.875rem; color: #CBD5E1;">
              <b>By Cheque / Draft:</b> Drawn in favor of <i>"Shiksha Sopan"</i> payable at Kanpur, mailed to: 
              <span style="color:#FFFFFF;">Prof. H.C. Verma, Sopan Ashram, Kanpur, U.P.</span>
            </div>
          </div>

          <div class="bento-section">
            <span class="section-eyebrow">CONTRIBUTION UTILIZATION</span>
            <h2 class="section-h2">Where Your Contributions Are Invested</h2>
            <div class="card-grid-3">
              <div class="feature-card">
                <div class="card-icon-pill">🎒</div>
                <h3 class="card-title">Student Sponsorships</h3>
                <p class="card-desc">Direct sponsorships for day scholars at SASK and Evening Centers, covering uniforms, bags, notebooks, and learning aids.</p>
              </div>
              <div class="feature-card">
                <div class="card-icon-pill">🏆</div>
                <h3 class="card-title">Merit & Higher Ed Funds</h3>
                <p class="card-desc">Corpus funds for the Dr. V.N. Kulkarni Merit Scholarship and the SGPV Higher Education Cell grants.</p>
              </div>
              <div class="feature-card">
                <div class="card-icon-pill">🎭</div>
                <h3 class="card-title">Functions & Community Events</h3>
                <p class="card-desc">Stage construction, sound systems, student awards, and refreshments for the Annual Function and Social Awareness Rally.</p>
              </div>
            </div>
          </div>
        """
    }
]

def make_subpage_html(act):
    # build other activities directory grid
    dir_links = ""
    for a in ACTIVITIES:
        is_cur = "current" if a["id"] == act["id"] else ""
        href = "#" if is_cur else f"{a['slug']}.html"
        dir_links += f"""        <a href="{href}" class="activity-dir-link {is_cur}">
          <span class="activity-dir-badge">{a['id']}</span>
          <span>{a['short_title']}</span>
        </a>\n"""

    # metrics chips
    metrics_html = ""
    for num, label in act["metrics"]:
        metrics_html += f"""        <div class="metric-chip">
          <div class="metric-chip-num">{num}</div>
          <div class="metric-chip-label">{label}</div>
        </div>\n"""

    from build_activity_subpages import get_shared_head, HEADER_AND_NAV, FOOTER_HTML

    head_html = get_shared_head(act["title"], act["lead"])

    html = f"""{head_html}
  {HEADER_AND_NAV}

  <!-- =======================================================================
       BREADCRUMB BAR
       ======================================================================= -->
  <div class="subpage-breadcrumb-bar">
    <div class="container breadcrumb-inner">
      <div class="breadcrumb-path">
        <a href="index.html">Home</a>
        <span>▸</span>
        <a href="activity.html">Activity</a>
        <span>▸</span>
        <span style="color: var(--text-primary); font-weight: 700;">({act['id']}) {act['short_title']}</span>
      </div>

      <a href="activity.html" class="btn-back-activities">
        ← Back to Activities Directory
      </a>
    </div>
  </div>

  <main id="mainContent">
    <!-- =======================================================================
         SUBPAGE HERO
         ======================================================================= -->
    <section class="subpage-hero" aria-labelledby="heroTitle">
      <div class="container">
        <span class="hero-badge-pill">ACTIVITY ({act['id']}) • {act['badge']}</span>
        <h1 class="subpage-title" id="heroTitle">
          <span>{act['title']}</span>
          <span class="hindi-title">{act['hindi_title']}</span>
        </h1>
        <p class="subpage-lead">
          {act['lead']}
        </p>

        <!-- Quick Metrics Bar -->
        <div class="metrics-bar-grid">
{metrics_html}        </div>
      </div>
    </section>

    <!-- =======================================================================
         CORE CONTENT BENTO
         ======================================================================= -->
    <div class="container content-container">
      {act['content_html']}
    </div>

    <!-- =======================================================================
         EXPLORE ALL 8 ACTIVITIES DIRECTORY
         ======================================================================= -->
    <section class="activity-directory-section" aria-labelledby="allActivitiesHead">
      <div class="container">
        <span class="section-eyebrow">EXPLORE SHIKSHA SOPAN</span>
        <h2 style="font-size: 1.35rem; font-weight: 850; color: #0F172A;" id="allActivitiesHead">
          All 8 Key Initiatives & Programs
        </h2>
        <div class="activity-dir-grid">
{dir_links}        </div>
      </div>
    </section>
  </main>

  {FOOTER_HTML}

  <!-- =======================================================================
       JAVASCRIPT: BILINGUAL ENGINE
       ======================================================================= -->
  <script>
    const translations = {{
      en: {{
        mottoText: "अंधकार को क्यों धिक्कारें, अच्छा हैं एक दीप जलायें",
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
        impLinksHead: "Important Links"
      }},
      hi: {{
        mottoText: "अंधकार को क्यों धिक्कारें, अच्छा हैं एक दीप जलायें",
        headerSub: "आईआईटी कानपुर समुदाय द्वारा एक शैक्षिक एवं सामाजिक पहल",
        navHome: "होम",
        navEC: "कार्यकारिणी समिति",
        navActivity: "गतिविधियां",
        navContribution: "सहयोग",
        navAchievements: "उपलब्धियां",
        navExperiments: "प्रयोग",
        navAbout: "हमारे बारे में",
        navContact: "संपर्क करें",
        joinBtn: "जुड़ें →",
        impLinksHead: "महत्वपूर्ण लिंक्स"
      }}
    }};

    let currentLang = 'en';

    function setLanguage(lang) {{
      if (!translations[lang]) return;
      currentLang = lang;
      
      const btnEn = document.getElementById('btnLangEn');
      const btnHi = document.getElementById('btnLangHi');
      if (btnEn && btnHi) {{
        btnEn.classList.toggle('active', lang === 'en');
        btnHi.classList.toggle('active', lang === 'hi');
      }}

      document.querySelectorAll('[data-i18n]').forEach(el => {{
        const key = el.getAttribute('data-i18n');
        if (translations[lang][key]) {{
          el.textContent = translations[lang][key];
        }}
      }});
      localStorage.setItem('sopan_lang', lang);
    }}

    document.addEventListener('DOMContentLoaded', () => {{
      const saved = localStorage.getItem('sopan_lang');
      if (saved && (saved === 'en' || saved === 'hi')) {{
        setLanguage(saved);
      }}
    }});
  </script>
</body>
</html>
"""
    return html

# Write out all 8 pages
for act in ACTIVITIES:
    filename = f"{act['slug']}.html"
    filepath = os.path.join(BASE_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(make_subpage_html(act))
    print(f"Generated {filename}")

print("All 8 subpages successfully generated.")

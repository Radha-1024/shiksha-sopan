import re

INDEX_PATH = "/Users/radha/.gemini/antigravity/scratch/shiksha-sopan-redesign/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    c = f.read()

# 1. Connect Workbench to experiments.html
workbench_btn = """          <button type="button" class="btn-sim-reset" id="btnResetPhysSim">
            ↺ Reset
          </button>
        </div>
        <div style="display: flex; justify-content: flex-end; margin-top: 1rem;">
          <a href="experiments.html" style="display: inline-flex; align-items: center; gap: 0.5rem; background: #E0F2FE; color: #0369A1; font-weight: 800; font-size: 0.85rem; padding: 0.5rem 1.15rem; border-radius: 9999px; text-decoration: none; border: 1px solid #BAE6FD;">
            🔬 Explore All 42 Hands-on Physics Experiments →
          </a>
        </div>"""

if "🔬 Explore All 42 Hands-on Physics Experiments" not in c:
    c = c.replace("""          <button type="button" class="btn-sim-reset" id="btnResetPhysSim">
            ↺ Reset
          </button>
        </div>""", workbench_btn)
    print("Added Experiments link to Workbench")

# 2. Connect Mission Pillars to about-us.html and executive-committee.html
pillars_end = """        <div class="pillar-box">
          <div class="pillar-icon-badge badge-swavalamban">🌱</div>
          <div class="pillar-hindi-head">स्वावलंबन</div>
          <div class="pillar-sub-head" data-i18n="pillar3Sub">Swavalamban • Self-Reliance</div>
          <p class="pillar-summary" data-i18n="pillar3Desc">
            Nurturing practical problem-solving skills so students become self-reliant and productive citizens.
          </p>
        </div>
      </div>
      <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap; margin-top: 1.75rem;">
        <a href="about-us.html" style="display: inline-flex; align-items: center; gap: 0.45rem; background: #E0F2FE; color: #0369A1; font-weight: 800; font-size: 0.9rem; padding: 0.6rem 1.4rem; border-radius: 9999px; text-decoration: none; border: 1px solid #BAE6FD;">
          📖 Discover Our Genesis & The 3 Pillars →
        </a>
        <a href="executive-committee.html" style="display: inline-flex; align-items: center; gap: 0.45rem; background: #F8FAFC; color: #0F172A; font-weight: 800; font-size: 0.9rem; padding: 0.6rem 1.4rem; border-radius: 9999px; text-decoration: none; border: 1px solid #CBD5E1;">
          🏛️ Meet the Executive Committee →
        </a>
      </div>"""

if "Discover Our Genesis & The 3 Pillars" not in c:
    old_pillars_end = """        <div class="pillar-box">
          <div class="pillar-icon-badge badge-swavalamban">🌱</div>
          <div class="pillar-hindi-head">स्वावलंबन</div>
          <div class="pillar-sub-head" data-i18n="pillar3Sub">Swavalamban • Self-Reliance</div>
          <p class="pillar-summary" data-i18n="pillar3Desc">
            Nurturing practical problem-solving skills so students become self-reliant and productive citizens.
          </p>
        </div>
      </div>"""
    c = c.replace(old_pillars_end, pillars_end)
    print("Added About Us & EC links to Mission section")

# 3. Add Contribution and Achievements sidebar cards
sidebar_addition = """        <!-- Support Our Cause Card -->
        <div class="sidebar-card" style="background: linear-gradient(135deg, #FEF3C7 0%, #FFFBEB 100%); border: 1.5px solid #FDE68A;">
          <div class="sidebar-card-header" style="color: #92400E;">
            <span>🤝</span>
            <span>Support Shiksha Sopan</span>
          </div>
          <p style="font-size: 0.88rem; color: #78350F; line-height: 1.55; margin-bottom: 0.85rem;">
            Shiksha Sopan runs purely on voluntary individual contributions. Tax-deductible under Section 80/G.
          </p>
          <a href="contribution.html" style="display:inline-flex; align-items:center; gap:0.4rem; background: #EA580C; color: #FFFFFF; font-size: 0.82rem; font-weight: 800; padding: 0.45rem 1rem; border-radius: 9999px; text-decoration: none;">
            Ways to Contribute →
          </a>
        </div>

        <!-- Student Achievements Card -->
        <div class="sidebar-card" style="background: linear-gradient(135deg, #F0F9FF 0%, #E0F2FE 100%); border: 1.5px solid #BAE6FD;">
          <div class="sidebar-card-header" style="color: #0369A1;">
            <span>🌟</span>
            <span>Student Achievements</span>
          </div>
          <p style="font-size: 0.88rem; color: #1E3A8A; line-height: 1.55; margin-bottom: 0.85rem;">
            Inspiring journeys of students nurtured at Sopan centers into defense, higher education & tech.
          </p>
          <a href="achievements.html" style="display:inline-flex; align-items:center; gap:0.4rem; background: #0284C7; color: #FFFFFF; font-size: 0.82rem; font-weight: 800; padding: 0.45rem 1rem; border-radius: 9999px; text-decoration: none;">
            Read Stories →
          </a>
        </div>"""

if "Support Shiksha Sopan" not in c:
    c = c.replace("""          <a href="https://www.shiksha-sopan.org/Newsletter" class="btn-view-more-news" data-i18n="viewMoreNews">
            View More Newsletters...
          </a>
        </div>
      </aside>""", f"""          <a href="https://www.shiksha-sopan.org/Newsletter" class="btn-view-more-news" data-i18n="viewMoreNews">
            View More Newsletters...
          </a>
        </div>
{sidebar_addition}
      </aside>""")
    print("Added Contribution and Achievements cards to sidebar")

# 4. Connect Science Tour section to Activity page
tour_btn = """          <div class="tour-actions-row">
            <a href="activity.html" class="btn-explore-naest" style="background: #0284C7;">
              🎯 Explore All 8 Activities & Centers →
            </a>
            <a href="contact-us.html" class="btn-secondary-link" data-i18n="btnTourDetails">
              Contact Sopan Ashram
            </a>
          </div>"""

if "Explore All 8 Activities & Centers" not in c:
    old_tour_btn = """          <div class="tour-actions-row">
            <a href="contact-us.html" class="btn-secondary-link" data-i18n="btnTourDetails">
              Contact Sopan Ashram
            </a>
          </div>"""
    c = c.replace(old_tour_btn, tour_btn)
    print("Added Activity link to Science Tour section")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(c)
print("Updated index.html with all in-page connections")


import os
import re
import glob

workspace_dir = "/Users/radha/.gemini/antigravity/scratch/shiksha-sopan-redesign"
html_files = sorted(glob.glob(os.path.join(workspace_dir, "*.html")))

mobile_css_target = """.desktop-join-btn {
        display: none !important;
      }"""

mobile_css_replacement = """.desktop-join-btn {
        display: inline-flex !important;
        font-size: 0.75rem;
        padding: 0.35rem 0.75rem;
        white-space: nowrap;
        font-weight: 700;
        margin-left: auto;
      }"""

universal_script = """  <!-- Guaranteed navigation for Join Us button and anti-cache protection -->
  <script>
  (function() {
    function routeJoinButtons() {
      var isJoinPage = window.location.pathname.endsWith('join.html') || window.location.pathname.endsWith('/join');
      document.querySelectorAll('a.btn-join-us, a.btn-hero-accent, a.mobile-btn-join').forEach(function(btn) {
        if (isJoinPage) {
          btn.setAttribute('href', '#joinForm');
          btn.onclick = function(e) {
            e.preventDefault();
            var target = document.getElementById('joinForm');
            if (target) target.scrollIntoView({ behavior: 'smooth' });
          };
        } else {
          btn.setAttribute('href', 'join.html');
          btn.onclick = function(e) {
            e.preventDefault();
            window.location.href = 'join.html';
          };
        }
      });
    }
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', routeJoinButtons);
    } else {
      routeJoinButtons();
    }
  })();
  </script>
"""

modified_count = 0

for file_path in html_files:
    if os.path.islink(file_path):
        continue
    
    filename = os.path.basename(file_path)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    orig_content = content

    # 1. Update responsive css so desktop-join-btn is visible on mobile and tablet
    if mobile_css_target in content:
        content = content.replace(mobile_css_target, mobile_css_replacement)

    # 2. Add inline onclick to join buttons
    if filename == "join.html":
        # in join.html, buttons should scroll to joinForm
        content = re.sub(
            r'<a\s+href="#joinForm"\s+class="btn-join-us mobile-btn-join active"',
            r'<a href="#joinForm" onclick="document.getElementById(\'joinForm\').scrollIntoView({behavior:\'smooth\'}); return false;" class="btn-join-us mobile-btn-join active"',
            content
        )
        content = re.sub(
            r'<a\s+href="#joinForm"\s+class="btn-join-us desktop-join-btn active"',
            r'<a href="#joinForm" onclick="document.getElementById(\'joinForm\').scrollIntoView({behavior:\'smooth\'}); return false;" class="btn-join-us desktop-join-btn active"',
            content
        )
        # Ensure back to home button has explicit onclick
        content = content.replace(
            '<a href="index.html" class="back-home-pill">',
            '<a href="index.html" onclick="window.location.href=\'index.html\'; return false;" class="back-home-pill">'
        )
    else:
        # in other files, buttons should navigate to join.html
        content = re.sub(
            r'<a\s+href="join\.html"\s+class="btn-join-us mobile-btn-join"',
            r'<a href="join.html" onclick="window.location.href=\'join.html\'; return false;" class="btn-join-us mobile-btn-join"',
            content
        )
        content = re.sub(
            r'<a\s+href="join\.html"\s+class="btn-join-us desktop-join-btn"',
            r'<a href="join.html" onclick="window.location.href=\'join.html\'; return false;" class="btn-join-us desktop-join-btn"',
            content
        )
        content = re.sub(
            r'<a\s+href="join\.html"\s+class="btn-hero-accent"',
            r'<a href="join.html" onclick="window.location.href=\'join.html\'; return false;" class="btn-hero-accent"',
            content
        )
        content = re.sub(
            r'<a\s+href="join\.html"\s+class="btn-join-us"',
            r'<a href="join.html" onclick="window.location.href=\'join.html\'; return false;" class="btn-join-us"',
            content
        )

    # 3. Add universal safety script before </body> if not already present
    if "routeJoinButtons" not in content:
        if "</body>" in content:
            content = content.replace("</body>", universal_script + "</body>")

    if content != orig_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        modified_count += 1
        print(f"Updated {filename}")
    else:
        print(f"No changes needed for {filename}")

print(f"\nTotal files updated: {modified_count}")

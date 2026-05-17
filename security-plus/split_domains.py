import re

with open('index.html', 'r') as f:
    html = f.read()

# Extract sections
# We know domains start with <section id="X-0" class="why-section"> and end with </section>
domains = []
for i in range(1, 6):
    pattern = re.compile(rf'(<section id=\"{i}-0\" class=\"why-section\">.*?</section>)', re.DOTALL)
    match = pattern.search(html)
    if match:
        domains.append(match.group(1))

# Template for new pages
template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>The Learning Lens | Security+ Domain {num}</title>
  <link rel="stylesheet" href="../styles.css" />
</head>
<body>
  <div id="shared-header"></div>
  <main class="page-shell">
    <section class="hero">
      <div class="hero-content">
        <p class="eyebrow">Security+</p>
        <h1>{title}</h1>
        <div class="hero-badges">
          <a href="../security-plus/index.html" class="hero-badge">⬅ Back to Security+</a>
        </div>
      </div>
    </section>

    {content}

  </main>
  <div id="shared-footer"></div>
  <script src="../scripts/headerFooter.js"></script>
</body>
</html>
"""

titles = [
    "General Security Concepts",
    "Threats, Vulnerabilities, and Mitigations",
    "Security Architecture",
    "Security Operations",
    "Security Program Management and Oversight"
]

for i in range(5):
    page_html = template.format(num=i+1, title=titles[i], content=domains[i])
    with open(f'domain-{i+1}.html', 'w') as f:
        f.write(page_html)

# Now rewrite index.html
# Remove the <nav class="local-nav">...</nav> completely
html = re.sub(r'<nav class=\"local-nav\">.*?</nav>', '', html, flags=re.DOTALL)

# Replace <div id="secure-concepts">...</div> with the new grid
grid_html = """
    <div class="interest-areas-grid" style="margin-bottom: 4rem;">
      <a href="domain-1.html" class="interest-area-card">
        <div class="card-inner">
          <div class="card-icon">🧠</div>
          <h3>General Concepts</h3>
          <div class="card-description">
            <p>1.0 General Security Concepts (12%)</p>
          </div>
        </div>
      </a>
      <a href="domain-2.html" class="interest-area-card">
        <div class="card-inner">
          <div class="card-icon">🦠</div>
          <h3>Threats & Mitigations</h3>
          <div class="card-description">
            <p>2.0 Threats, Vulnerabilities, and Mitigations (22%)</p>
          </div>
        </div>
      </a>
      <a href="domain-3.html" class="interest-area-card">
        <div class="card-inner">
          <div class="card-icon">🏛️</div>
          <h3>Security Architecture</h3>
          <div class="card-description">
            <p>3.0 Security Architecture (18%)</p>
          </div>
        </div>
      </a>
      <a href="domain-4.html" class="interest-area-card">
        <div class="card-inner">
          <div class="card-icon">🛠️</div>
          <h3>Security Operations</h3>
          <div class="card-description">
            <p>4.0 Security Operations (28%)</p>
          </div>
        </div>
      </a>
      <a href="domain-5.html" class="interest-area-card">
        <div class="card-inner">
          <div class="card-icon">📊</div>
          <h3>Program Management</h3>
          <div class="card-description">
            <p>5.0 Security Program Management and Oversight (20%)</p>
          </div>
        </div>
      </a>
    </div>
"""

html = re.sub(r'<div id=\"secure-concepts\">.*?</div>\n  <section id=\"exam-notes\"', grid_html + '  <section id="exam-notes"', html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)

print("Split complete")

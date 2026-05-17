import re

with open('index.html', 'r') as f:
    html = f.read()

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

new_html = re.sub(r'<div id=\"secure-concepts\">.*?<section id=\"exam-notes\"', grid_html + '    <section id=\"exam-notes\"', html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(new_html)

print('Updated index.html')

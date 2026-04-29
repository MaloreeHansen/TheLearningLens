const pathParts = window.location.pathname.replace(/\/$/, '').split('/').filter(Boolean);
const isFile = pathParts[pathParts.length - 1]?.includes('.') || false;
const rootDepth = Math.max(0, pathParts.length - (isFile ? 1 : 0) - 1);
const rootPath = rootDepth ? '../'.repeat(rootDepth) : './';

const navLinks = [
  { label: 'Home', href: `${rootPath}` },
  { label: 'About', href: `${rootPath}README.html` },
  { label: 'Security+', href: `${rootPath}security-plus/` },
  { label: 'Interview Prep', href: `${rootPath}job-interview-preparation/` },
  { label: 'Job Roles', href: `${rootPath}job-roles/` },
  { label: 'Tools', href: `${rootPath}technical-tools/` },
];

const normalizePath = path => path.replace(/\/$/, '');
const activePath = normalizePath(window.location.pathname);
const header = document.getElementById('shared-header');
const footer = document.getElementById('shared-footer');

if (header) {
  header.innerHTML = `
    <header class="site-header">
      <div class="header-brand">
        <a class="brand-link" href="${rootPath}">The Learning Lens</a>
        <p class="brand-tag">A cyber-aware technical learning hub</p>
      </div>
      <nav class="site-nav">
        ${navLinks
          .map(
            link => {
              const candidatePath = normalizePath(new URL(link.href, window.location.origin + window.location.pathname).pathname);
              return `
            <a class="site-nav-link${activePath === candidatePath ? ' active' : ''}" href="${link.href}">
              ${link.label}
            </a>`;
            }
          )
          .join('')}
      </nav>
    </header>
  `.trim();
}

if (footer) {
  footer.innerHTML = `
    <footer class="site-footer">
      <p>Shared header and footer components make the site easier to maintain.</p>
      <p>Converted README content into full HTML for GitHub Pages.</p>
    </footer>
  `.trim();
}

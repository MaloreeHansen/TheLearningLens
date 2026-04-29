const pathParts = window.location.pathname.replace(/\/$/, '').split('/').filter(Boolean);
const isFile = pathParts[pathParts.length - 1]?.includes('.') || false;
const rootDepth = Math.max(0, pathParts.length - (isFile ? 1 : 0) - 1);
const rootPath = rootDepth ? '../'.repeat(rootDepth) : './';

const navLinks = [
  { label: 'Home', href: `${rootPath}` },
  { label: 'About', href: `${rootPath}README.html` },
  { label: 'Security+', href: `${rootPath}security-plus/index.html` },
  { label: 'Interview Prep', href: `${rootPath}job-interview-preparation/index.html` },
  { label: 'Job Roles', href: `${rootPath}job-roles/index.html` },
  { label: 'Tools', href: `${rootPath}technical-tools/index.html` },
];

const normalizePath = path => path.replace(/\/$/, '');
const activePath = normalizePath(window.location.pathname);
const header = document.getElementById('shared-header');
const footer = document.getElementById('shared-footer');

if (header) {
  header.innerHTML = `
    <nav class="site-header">
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
    </nav>
  `.trim();
}

if (footer) {
  // Build breadcrumb trail
  const breadcrumbs = [{ label: 'Home', href: rootPath }];
  let currentPath = rootPath;
  pathParts.forEach((part, index) => {
    if (part !== 'index.html' && part !== 'README.html') {
      currentPath += part + '/';
      let label = part.replace(/\.html$/, '').replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
      if (part === 'job-interview-preparation') label = 'Interview Prep';
      if (part === 'job-roles') label = 'Job Roles';
      if (part === 'technical-tools') label = 'Tools';
      if (part === 'security-plus') label = 'Security+';
      breadcrumbs.push({ label, href: currentPath });
    }
  });

  footer.innerHTML = `
    <nav class="site-footer">
      <div class="breadcrumb">
        ${breadcrumbs.map((crumb, index) => 
          index === breadcrumbs.length - 1 
            ? `<span class="breadcrumb-current">${crumb.label}</span>` 
            : `<a href="${crumb.href}">${crumb.label}</a> › `
        ).join('')}
      </div>
    </nav>
  `.trim();
}

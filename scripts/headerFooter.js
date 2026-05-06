const scriptUrl = new URL(document.currentScript.src);
const rootUrl = new URL('../', scriptUrl.href).href;

const navLinks = [
  { label: 'Home', href: rootUrl + 'index.html' },
  { label: 'About', href: rootUrl + 'README.html' },
  { label: 'Security+', href: rootUrl + 'security-plus/index.html' },
  { label: 'Interview Prep', href: rootUrl + 'job-interview-preparation/index.html' },
  { label: 'Job Roles', href: rootUrl + 'job-roles/index.html' },
  { label: 'Tools', href: rootUrl + 'technical-tools/index.html' },
];

const currentUrlObj = new URL(window.location.href);
currentUrlObj.search = '';
currentUrlObj.hash = '';
const currentUrl = currentUrlObj.href;

const getCleanPath = (url) => {
  let u = new URL(url).href;
  u = u.replace(/\/$/, '');
  if (u.endsWith('/index.html')) u = u.slice(0, -11);
  return u;
};

const activePath = getCleanPath(currentUrl);

const header = document.getElementById('shared-header');
const footer = document.getElementById('shared-footer');

if (header) {
  header.innerHTML = `
    <nav class="site-header">
      <div class="header-brand">
        <a class="brand-link" href="${rootUrl}index.html">The Learning Lens</a>
        <p class="brand-tag">A cyber-aware technical learning hub</p>
      </div>
      <nav class="site-nav">
        ${navLinks
          .map(link => {
            const candidatePath = getCleanPath(link.href);
            const isActive = activePath === candidatePath;
            return `
            <a class="site-nav-link${isActive ? ' active' : ''}" href="${link.href}">
              ${link.label}
            </a>`;
          })
          .join('')}
      </nav>
    </nav>
  `.trim();
}

if (footer) {
  let relativePath = '';
  if (currentUrl.startsWith(rootUrl)) {
    relativePath = currentUrl.slice(rootUrl.length);
  }
  
  const pathParts = relativePath.split('/').filter(Boolean);
  
  const breadcrumbs = [{ label: 'Home', href: rootUrl + 'index.html' }];
  let currentBuildPath = rootUrl;
  
  pathParts.forEach((part, index) => {
    if (part !== 'index.html' && part !== 'README.html') {
      currentBuildPath += part + '/';
      let label = part.replace(/\.html$/, '').replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
      if (part === 'job-interview-preparation') label = 'Interview Prep';
      if (part === 'job-roles') label = 'Job Roles';
      if (part === 'technical-tools') label = 'Tools';
      if (part === 'security-plus') label = 'Security+';
      breadcrumbs.push({ label, href: currentBuildPath + 'index.html' });
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

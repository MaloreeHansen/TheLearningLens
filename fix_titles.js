const fs = require('fs');
const path = require('path');

const walkSync = function(dir, filelist) {
  const files = fs.readdirSync(dir);
  filelist = filelist || [];
  files.forEach(function(file) {
    if (fs.statSync(path.join(dir, file)).isDirectory()) {
      filelist = walkSync(path.join(dir, file), filelist);
    }
    else {
      if (file.endsWith('.html')) {
        filelist.push(path.join(dir, file));
      }
    }
  });
  return filelist;
};

const files = walkSync('/Users/mal/Projects/TheLearningLens');

const toSentenceCase = (text) => {
  if (!text) return text;
  text = text.trim();
  // Don't lower case proper nouns if we can avoid it. For now, simple sentence case:
  // First letter capitalized, rest lowercase.
  // Exception for "IT", "Security+", "The Learning Lens" etc if needed, but let's just do a basic one.
  return text.charAt(0).toUpperCase() + text.slice(1).toLowerCase();
};

files.forEach(file => {
  let content = fs.readFileSync(file, 'utf8');
  let changed = false;

  // Let's replace title tag format if needed
  
  // Let's replace h1, h2, h3, h4, h5, h6
  const headerRegex = /<h([1-6])[^>]*>(.*?)<\/h\1>/gi;
  content = content.replace(headerRegex, (match, p1, p2) => {
    if (p2.includes('<')) return match; // skip if contains nested tags for simplicity
    
    // Custom logic to handle some obvious proper nouns
    let text = p2.trim();
    if (text === "The Learning Lens") return match;
    if (text === "Security+") return match;
    if (text === "IT System Administration") return match;
    
    // Apply sentence case
    // text = toSentenceCase(text);
    // Actually, just logging for now to see what we have
    // console.log(`[${file}] ${match} -> <h${p1}>${text}</h${p1}>`);
    return match;
  });

});

console.log("Done");

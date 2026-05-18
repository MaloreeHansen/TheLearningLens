with open('domain-3.html', 'r') as f:
    html = f.read()

# Replace <br> with a styled span that has a small gap
# The <br> creates a full line break which is too much
# Instead, use a div wrapper approach in the innerHTML assignments
# Actually simplest: just replace <br> with a smaller spacer span

html = html.replace("</span><br>", "</span> <span style='display:block; margin-top:0.25rem;'>")

# We need to close those spans. Each status message ends with a ";
# The body text needs a closing </span>
# Let's find each pattern and fix it

import re

# Match the innerHTML assignments and wrap properly
def fix_inner_html(match):
    s = match.group(0)
    # Replace the block span we just added - need to close it
    # The text after the block span goes to the end quote
    s = s.replace("<span style='display:block; margin-top:0.25rem;'>", "<br style='line-height:0.5;'>")
    return s

# Actually let's just go simpler - reduce the br line-height
# Revert to br but with a tiny line-height
html2 = open('domain-3.html', 'r').read()  # re-read original

# The <br> tags were already inserted. Let's just replace them with a styled approach
# Actually the simplest fix: use CSS on the status panel to reduce the gap

# Let me just replace all <br> in innerHTML with a small-margin div
html = html.replace("</span><br>", "</span><div style='margin-top:0.15rem'></div>")

with open('domain-3.html', 'w') as f:
    f.write(html)

print("Fixed spacing")

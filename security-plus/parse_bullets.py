import re

with open('index.html', 'r') as f:
    html = f.read()

# We want to match lines like:
# <li><strong>Categories:</strong> Technical; Managerial; Operational; Physical</li>
# And replace them with:
# <li>
#   <strong>Categories:</strong>
#   <ul>
#     <li>Technical</li>
#     <li>Managerial</li>
#     <li>Operational</li>
#     <li>Physical</li>
#   </ul>
# </li>

def replace_semicolons(match):
    strong_tag = match.group(1) # e.g. <strong>Categories:</strong>
    content = match.group(2) # e.g. " Technical; Managerial; Operational; Physical"
    
    # Strip leading/trailing space
    content = content.strip()
    
    # Split on semicolon, but handle cases where semicolon might not exist
    if ';' in content:
        items = [item.strip() for item in content.split(';')]
        list_html = "\n".join([f"            <li>{item}</li>" for item in items])
        return f"<li>\n          {strong_tag}\n          <ul>\n{list_html}\n          </ul>\n        </li>"
    else:
        # if there are no semicolons, maybe leave it as is or wrap in a single li
        # The user said "add bullet points and spacing between semicolons"
        return match.group(0) # return original if no semicolon

# Regex to capture the strong tag and the text after it up to </li>
new_html = re.sub(r'<li>(<strong>.*?</strong>)(.*?)</li>', replace_semicolons, html)

with open('index.html', 'w') as f:
    f.write(new_html)

print("Updated index.html")

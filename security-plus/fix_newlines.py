import re

with open('domain-3.html', 'r') as f:
    html = f.read()

# We need to replace `</span> ` with `</span><br>` but ONLY inside the statusText innerHTML assignments.
# To be safe, we can just replace the specific strings.

replacements = {
    "</span> Malicious input is sent to the VM's buffer.": "</span><br>Malicious input is sent to the VM's buffer.",
    "</span> Strict logical segmentation is active at the hypervisor layer.": "</span><br>Strict logical segmentation is active at the hypervisor layer.",
    "</span> The payload exceeds allocated memory space.": "</span><br>The payload exceeds allocated memory space.",
    "</span> Memory boundaries fail; malicious code execution spills over.": "</span><br>Memory boundaries fail; malicious code execution spills over.",
    "</span> Without segmentation, the Host OS is fully exposed to the Guest's breach.": "</span><br>Without segmentation, the Host OS is fully exposed to the Guest's breach.",
    "</span> Malicious execution attempts to escape the VM.": "</span><br>Malicious execution attempts to escape the VM.",
    "</span> Strict logical segmentation and hardware isolation blocks the escape, protecting the Host OS.": "</span><br>Strict logical segmentation and hardware isolation blocks the escape, protecting the Host OS."
}

for old, new in replacements.items():
    html = html.replace(old, new)

with open('domain-3.html', 'w') as f:
    f.write(html)

print("Added newlines.")

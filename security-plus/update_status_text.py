import re

with open('domain-3.html', 'r') as f:
    html = f.read()

# Update the statusText div to have larger font and transition
old_div = '<div id="statusText" class="status-panel" style="margin-bottom: 1.5rem;">'
new_div = '<div id="statusText" class="status-panel" style="margin-bottom: 1.5rem; font-size: 1.35rem; border-width: 2px; transition: border-color 0.3s ease;">'
html = html.replace(old_div, new_div)

# Replace resetSim
old_reset = """      function resetSim(newMode) {
          cancelAnimationFrame(animationId);
          mode = newMode;
          frame = 0;
          particles = [];
          
          if(mode === 'vulnerable') {
              statusText.innerHTML = "<span style='color: #fca5a5;'>Vulnerable Mode:</span> Malicious input is sent to the VM's buffer.";
          } else if (mode === 'isolated') {
              statusText.innerHTML = "<span style='color: #86efac;'>Isolated Mode:</span> Strict logical segmentation is active at the hypervisor layer.";
          }
          
          animate();
      }"""

new_reset = """      function resetSim(newMode) {
          cancelAnimationFrame(animationId);
          mode = newMode;
          frame = 0;
          particles = [];
          
          if(mode === 'vulnerable') {
              statusText.innerHTML = "<span style='color: #fca5a5;'>Vulnerable Mode:</span> Malicious input is sent to the VM's buffer.";
              statusText.style.borderColor = '#fca5a5';
          } else if (mode === 'isolated') {
              statusText.innerHTML = "<span style='color: #86efac;'>Isolated Mode:</span> Strict logical segmentation is active at the hypervisor layer.";
              statusText.style.borderColor = '#86efac';
          }
          
          animate();
      }"""
html = html.replace(old_reset, new_reset)

# Replace animation timeline
old_timeline = """          // Update Status Text based on timeline
          if (mode === 'vulnerable') {
              if (frame === 300) statusText.innerHTML = "<span style='color: #fde047;'>Buffer Overflow:</span> The payload exceeds allocated memory space.";
              if (frame === 480) statusText.innerHTML = "<span style='color: #fb923c;'>VM Escape:</span> Memory boundaries fail; malicious code execution spills over.";
              if (frame === 640) statusText.innerHTML = "<span style='color: #ef4444; font-weight: bold;'>SYSTEM COMPROMISED:</span> Without segmentation, the Host OS is fully exposed to the Guest's breach.";
          }

          if (mode === 'isolated') {
              if (frame === 300) statusText.innerHTML = "<span style='color: #fde047;'>Buffer Overflow:</span> The payload exceeds allocated memory space.";
              if (frame === 480) statusText.innerHTML = "<span style='color: #60a5fa;'>Containment:</span> Malicious execution attempts to escape the VM.";
              if (frame === 640) statusText.innerHTML = "<span style='color: #4ade80; font-weight: bold;'>SYSTEM SECURED:</span> Strict logical segmentation and hardware isolation blocks the escape, protecting the Host OS.";
          }"""

new_timeline = """          // Update Status Text based on timeline
          if (mode === 'vulnerable') {
              if (frame === 300) {
                  statusText.innerHTML = "<span style='color: #fde047;'>Buffer Overflow:</span> The payload exceeds allocated memory space.";
                  statusText.style.borderColor = '#fde047';
              }
              if (frame === 480) {
                  statusText.innerHTML = "<span style='color: #fb923c;'>VM Escape:</span> Memory boundaries fail; malicious code execution spills over.";
                  statusText.style.borderColor = '#fb923c';
              }
              if (frame === 640) {
                  statusText.innerHTML = "<span style='color: #ef4444; font-weight: bold;'>SYSTEM COMPROMISED:</span> Without segmentation, the Host OS is fully exposed to the Guest's breach.";
                  statusText.style.borderColor = '#ef4444';
              }
          }

          if (mode === 'isolated') {
              if (frame === 300) {
                  statusText.innerHTML = "<span style='color: #fde047;'>Buffer Overflow:</span> The payload exceeds allocated memory space.";
                  statusText.style.borderColor = '#fde047';
              }
              if (frame === 480) {
                  statusText.innerHTML = "<span style='color: #60a5fa;'>Containment:</span> Malicious execution attempts to escape the VM.";
                  statusText.style.borderColor = '#60a5fa';
              }
              if (frame === 640) {
                  statusText.innerHTML = "<span style='color: #4ade80; font-weight: bold;'>SYSTEM SECURED:</span> Strict logical segmentation and hardware isolation blocks the escape, protecting the Host OS.";
                  statusText.style.borderColor = '#4ade80';
              }
          }"""
html = html.replace(old_timeline, new_timeline)

with open('domain-3.html', 'w') as f:
    f.write(html)

print("Status text dynamically updated.")

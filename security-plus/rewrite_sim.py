import re

with open('domain-3.html', 'r') as f:
    html = f.read()

# Define the new script
new_script = """  <script>
      const canvas = document.getElementById('simCanvas');
      const ctx = canvas.getContext('2d');
      const statusText = document.getElementById('statusText');

      // Animation State
      let mode = 'idle'; // idle, vulnerable, isolated
      let frame = 0;
      let particles = [];
      let animationId;

      // Colors matching site palette
      const colors = {
          host: '#1a1a1c', // bg-surface-elevated
          hostUI: '#27272a', // zinc-800 for taskbar
          vm: '#121212',   // bg-surface
          vmUI: '#27272a', // titlebar
          buffer: 'rgba(255, 255, 255, 0.1)',
          dataValid: '#86efac',
          dataMalicious: '#fca5a5',
          isolation: '#84a98c', // accent-color
          compromised: '#450a0a'
      };

      // Layout Geometry (Canvas is 800x450)
      const layout = {
          host: { x: 0, y: 0, w: 800, h: 450 },
          taskbar: { x: 0, y: 410, w: 800, h: 40 },
          vm: { x: 250, y: 60, w: 500, h: 320 },
          vmTitlebar: { h: 30 },
          buffer: { x: 350, y: 220, w: 300, h: 40 }
      };

      class Particle {
          constructor(x, y, color, isMalicious) {
              this.x = x;
              this.y = y;
              this.color = color;
              this.isMalicious = isMalicious;
              this.vx = 2 + Math.random() * 2;
              this.vy = (Math.random() - 0.5) * 1;
              this.active = true;
              this.escaped = false;
          }

          update(frame) {
              if (!this.active) return;
              
              this.x += this.vx;
              this.y += this.vy;

              // Buffer limits
              if (this.x > layout.buffer.x + layout.buffer.w - 10 && !this.isMalicious) {
                  this.active = false; // Valid data stays in buffer
              }

              // Malicious data overflows
              if (this.isMalicious && this.x > layout.buffer.x + layout.buffer.w) {
                  this.vx = 4;
                  this.vy = (Math.random() - 0.5) * 6;
                  
                  // Hit VM boundary (right side or top/bottom)
                  if (this.x > layout.vm.x + layout.vm.w - 10 || this.y < layout.vm.y + 10 || this.y > layout.vm.y + layout.vm.h - 10) {
                      if (mode === 'isolated') {
                          // Blocked by isolation - bounce back
                          this.vx = -1 * Math.abs(this.vx); 
                          if (this.x > layout.vm.x + layout.vm.w - 15) this.x = layout.vm.x + layout.vm.w - 15;
                          if (this.y < layout.vm.y + 15) this.vy = Math.abs(this.vy);
                          if (this.y > layout.vm.y + layout.vm.h - 15) this.vy = -1 * Math.abs(this.vy);
                      } else {
                          // Escape VM
                          this.escaped = true;
                      }
                  }
              }
          }

          draw() {
              ctx.fillStyle = this.color;
              ctx.fillRect(this.x, this.y, 8, 8);
          }
      }

      function resetSim(newMode) {
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
      }

      function drawRoundedRect(x, y, w, h, radius) {
          ctx.beginPath();
          ctx.moveTo(x + radius, y);
          ctx.lineTo(x + w - radius, y);
          ctx.quadraticCurveTo(x + w, y, x + w, y + radius);
          ctx.lineTo(x + w, y + h - radius);
          ctx.quadraticCurveTo(x + w, y + h, x + w - radius, y + h);
          ctx.lineTo(x + radius, y + h);
          ctx.quadraticCurveTo(x, y + h, x, y + h - radius);
          ctx.lineTo(x, y + radius);
          ctx.quadraticCurveTo(x, y, x + radius, y);
          ctx.closePath();
          ctx.fill();
      }

      function drawEnvironment() {
          ctx.clearRect(0, 0, canvas.width, canvas.height);

          // Draw Host OS (Fills entire canvas)
          let hostColor = colors.host;
          if (mode === 'vulnerable' && frame > 300) hostColor = colors.compromised;
          
          ctx.fillStyle = hostColor;
          ctx.fillRect(layout.host.x, layout.host.y, layout.host.w, layout.host.h);
          
          // Host Taskbar
          ctx.fillStyle = colors.hostUI;
          ctx.fillRect(layout.taskbar.x, layout.taskbar.y, layout.taskbar.w, layout.taskbar.h);
          
          // Start Button / Logo
          ctx.fillStyle = '#a1a1aa';
          ctx.fillRect(15, layout.taskbar.y + 10, 20, 20);
          
          ctx.fillStyle = '#a1a1aa'; // text-secondary
          ctx.font = '14px Outfit, sans-serif';
          ctx.fillText('Host OS Environment', 50, layout.taskbar.y + 25);

          // Draw Isolation Layer (if active, behind VM)
          if (mode === 'isolated') {
              ctx.strokeStyle = colors.isolation;
              ctx.lineWidth = 6;
              ctx.strokeRect(layout.vm.x - 3, layout.vm.y - 3, layout.vm.w + 6, layout.vm.h + 6);
              // Glow effect
              ctx.shadowColor = colors.isolation;
              ctx.shadowBlur = 15;
              ctx.strokeRect(layout.vm.x - 3, layout.vm.y - 3, layout.vm.w + 6, layout.vm.h + 6);
              ctx.shadowBlur = 0; // reset
          }

          // Draw Guest VM (App Window)
          ctx.fillStyle = colors.vm;
          drawRoundedRect(layout.vm.x, layout.vm.y, layout.vm.w, layout.vm.h, 8);
          ctx.strokeStyle = '#3f3f46';
          ctx.lineWidth = 1;
          ctx.strokeRect(layout.vm.x, layout.vm.y, layout.vm.w, layout.vm.h); // Add border
          
          // VM Titlebar
          ctx.fillStyle = colors.vmUI;
          ctx.beginPath();
          ctx.moveTo(layout.vm.x + 8, layout.vm.y);
          ctx.lineTo(layout.vm.x + layout.vm.w - 8, layout.vm.y);
          ctx.quadraticCurveTo(layout.vm.x + layout.vm.w, layout.vm.y, layout.vm.x + layout.vm.w, layout.vm.y + 8);
          ctx.lineTo(layout.vm.x + layout.vm.w, layout.vm.y + layout.vmTitlebar.h);
          ctx.lineTo(layout.vm.x, layout.vm.y + layout.vmTitlebar.h);
          ctx.lineTo(layout.vm.x, layout.vm.y + 8);
          ctx.quadraticCurveTo(layout.vm.x, layout.vm.y, layout.vm.x + 8, layout.vm.y);
          ctx.closePath();
          ctx.fill();

          // Window controls (macOS style dots)
          ctx.fillStyle = '#ef4444'; ctx.beginPath(); ctx.arc(layout.vm.x + 20, layout.vm.y + 15, 5, 0, Math.PI*2); ctx.fill();
          ctx.fillStyle = '#eab308'; ctx.beginPath(); ctx.arc(layout.vm.x + 35, layout.vm.y + 15, 5, 0, Math.PI*2); ctx.fill();
          ctx.fillStyle = '#22c55e'; ctx.beginPath(); ctx.arc(layout.vm.x + 50, layout.vm.y + 15, 5, 0, Math.PI*2); ctx.fill();

          ctx.fillStyle = '#ededed'; // text-primary
          ctx.textAlign = "center";
          ctx.fillText('Guest Virtual Machine', layout.vm.x + (layout.vm.w/2), layout.vm.y + 20);
          ctx.textAlign = "left";

          // Draw Buffer
          ctx.fillStyle = colors.buffer;
          ctx.fillRect(layout.buffer.x, layout.buffer.y, layout.buffer.w, layout.buffer.h);
          ctx.fillStyle = '#ededed';
          ctx.fillText('Memory Buffer', layout.buffer.x + 10, layout.buffer.y + 25);
      }

      function animate() {
          frame++;
          drawEnvironment();

          // Spawn Particles
          if (frame > 20 && frame < 100 && frame % 5 === 0) {
              // Normal data
              particles.push(new Particle(50, layout.buffer.y + 15, colors.dataValid, false));
          }

          if (frame > 120 && frame < 220 && frame % 2 === 0) {
              // Malicious payload causing overflow
              particles.push(new Particle(50, layout.buffer.y + 15, colors.dataMalicious, true));
          }

          // Update & Draw Particles
          let escapedCount = 0;
          particles.forEach(p => {
              p.update(frame);
              p.draw();
              if (p.escaped) escapedCount++;
          });

          // Update Status Text based on timeline
          if (mode === 'vulnerable') {
              if (frame === 150) statusText.innerHTML = "<span style='color: #fde047;'>Buffer Overflow:</span> The payload exceeds allocated memory space.";
              if (frame === 240) statusText.innerHTML = "<span style='color: #fb923c;'>VM Escape:</span> Memory boundaries fail; malicious code execution spills over.";
              if (frame === 320) statusText.innerHTML = "<span style='color: #ef4444; font-weight: bold;'>SYSTEM COMPROMISED:</span> Without segmentation, the Host OS is fully exposed to the Guest's breach.";
          }

          if (mode === 'isolated') {
              if (frame === 150) statusText.innerHTML = "<span style='color: #fde047;'>Buffer Overflow:</span> The payload exceeds allocated memory space.";
              if (frame === 240) statusText.innerHTML = "<span style='color: #60a5fa;'>Containment:</span> Malicious execution attempts to escape the VM.";
              if (frame === 320) statusText.innerHTML = "<span style='color: #4ade80; font-weight: bold;'>SYSTEM SECURED:</span> Strict logical segmentation and hardware isolation blocks the escape, protecting the Host OS.";
          }

          // Connection line from external to VM
          ctx.beginPath();
          ctx.moveTo(0, layout.buffer.y + 20);
          ctx.lineTo(layout.vm.x, layout.buffer.y + 20);
          ctx.strokeStyle = 'rgba(255, 255, 255, 0.12)';
          ctx.lineWidth = 2;
          ctx.stroke();
          ctx.fillStyle = '#a1a1aa';
          ctx.fillText('Network Input', 10, layout.buffer.y + 15);

          if (frame < 500) {
              animationId = requestAnimationFrame(animate);
          }
      }

      // Event Listeners
      document.getElementById('btnVulnerable').addEventListener('click', () => resetSim('vulnerable'));
      document.getElementById('btnIsolated').addEventListener('click', () => resetSim('isolated'));

      // Initial Draw
      drawEnvironment();
  </script>"""

# Using regex to replace the old script block
pattern = re.compile(r'<script>\s*const canvas = document.getElementById\(\'simCanvas\'\);.*?</script>', re.DOTALL)
new_html = pattern.sub(new_script, html)

with open('domain-3.html', 'w') as f:
    f.write(new_html)

print("Updated script block.")

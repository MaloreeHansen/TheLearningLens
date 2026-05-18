import re

with open('domain-3.html', 'r') as f:
    html = f.read()

animation_html = """
  <section class="why-section" style="margin-top: 4rem;">
    <h2>Interactive Simulations</h2>
    <details class="faq-item">
      <summary>VM Escape & Logical Segmentation</summary>
      <div class="sim-wrapper">
        <div style="margin-bottom: 1rem;">
          <p style="margin-bottom: 0;">Observing how a Buffer Overflow leads to a VM Escape reveals the necessity of Logical Segmentation.</p>
        </div>

        <div class="aspect-video">
            <canvas id="simCanvas" width="800" height="450" class="canvas-element"></canvas>
        </div>

        <div class="sim-controls">
            <button id="btnVulnerable" class="button btn-vulnerable">
                Simulate Vulnerable Architecture
            </button>
            <button id="btnIsolated" class="button btn-secured">
                Simulate Segmented Architecture
            </button>
        </div>
        
        <div id="statusText" class="status-panel">
            Select a simulation mode to begin.
        </div>
      </div>
    </details>
  </section>

  <script>
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
          vm: '#121212',   // bg-surface
          buffer: 'rgba(255, 255, 255, 0.1)',
          dataValid: '#86efac',
          dataMalicious: '#fca5a5',
          isolation: '#84a98c', // accent-color
          compromised: '#450a0a'
      };

      // Layout Geometry
      const layout = {
          host: { x: 50, y: 50, w: 700, h: 350 },
          vm: { x: 400, y: 100, w: 300, h: 250 },
          buffer: { x: 450, y: 220, w: 200, h: 40 }
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
                  this.vx = 3;
                  this.vy = (Math.random() - 0.5) * 4;
                  
                  // Hit VM boundary
                  if (this.x > layout.vm.x + layout.vm.w - 10) {
                      if (mode === 'isolated') {
                          // Blocked by isolation
                          this.vx = -1 * Math.abs(this.vx); 
                          this.x = layout.vm.x + layout.vm.w - 15;
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

      function drawEnvironment() {
          ctx.clearRect(0, 0, canvas.width, canvas.height);

          // Draw Host OS
          let hostColor = colors.host;
          if (mode === 'vulnerable' && frame > 300) hostColor = colors.compromised;
          
          ctx.fillStyle = hostColor;
          ctx.fillRect(layout.host.x, layout.host.y, layout.host.w, layout.host.h);
          ctx.strokeStyle = 'rgba(255, 255, 255, 0.12)'; // border-strong
          ctx.lineWidth = 2;
          ctx.strokeRect(layout.host.x, layout.host.y, layout.host.w, layout.host.h);
          
          ctx.fillStyle = '#a1a1aa'; // text-secondary
          ctx.font = '16px Outfit, sans-serif';
          ctx.fillText('Host OS / Hypervisor Layer', layout.host.x + 20, layout.host.y + 30);

          // Draw Isolation Layer (if active)
          if (mode === 'isolated') {
              ctx.strokeStyle = colors.isolation;
              ctx.lineWidth = 8;
              ctx.strokeRect(layout.vm.x - 4, layout.vm.y - 4, layout.vm.w + 8, layout.vm.h + 8);
              // Glow effect
              ctx.shadowColor = colors.isolation;
              ctx.shadowBlur = 15;
              ctx.strokeRect(layout.vm.x - 4, layout.vm.y - 4, layout.vm.w + 8, layout.vm.h + 8);
              ctx.shadowBlur = 0; // reset
          }

          // Draw Guest VM
          ctx.fillStyle = colors.vm;
          ctx.fillRect(layout.vm.x, layout.vm.y, layout.vm.w, layout.vm.h);
          ctx.fillStyle = '#ededed'; // text-primary
          ctx.fillText('Guest Virtual Machine', layout.vm.x + 20, layout.vm.y + 30);

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
              particles.push(new Particle(100, layout.buffer.y + 15, colors.dataValid, false));
          }

          if (frame > 120 && frame < 220 && frame % 2 === 0) {
              // Malicious payload causing overflow
              particles.push(new Particle(100, layout.buffer.y + 15, colors.dataMalicious, true));
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
          ctx.moveTo(layout.host.x, layout.buffer.y + 20);
          ctx.lineTo(layout.vm.x, layout.buffer.y + 20);
          ctx.strokeStyle = 'rgba(255, 255, 255, 0.12)';
          ctx.lineWidth = 2;
          ctx.stroke();
          ctx.fillStyle = '#a1a1aa';
          ctx.fillText('Network Input', layout.host.x + 20, layout.buffer.y + 15);

          if (frame < 500) {
              animationId = requestAnimationFrame(animate);
          }
      }

      // Event Listeners
      document.getElementById('btnVulnerable').addEventListener('click', () => resetSim('vulnerable'));
      document.getElementById('btnIsolated').addEventListener('click', () => resetSim('isolated'));

      // Initial Draw
      drawEnvironment();
  </script>
"""

# Replace </main> with the animation + </main>
new_html = html.replace('  </main>', animation_html + '\n  </main>')

with open('domain-3.html', 'w') as f:
    f.write(new_html)

print("Injected animation.")

import sys

with open('domain-3.html', 'r') as f:
    html = f.read()

explanation_html = """
        <div class="simulation-explanation" style="margin-top: 2rem; border-top: 1px solid var(--border-subtle); padding-top: 2rem;">
            <h3 style="font-size: 1.3rem; margin-bottom: 1rem;">The Architecture of an Exploit: Buffer Overflows and VM Escapes</h3>
            <p>The accompanying animation demonstrates how a localized vulnerability (a buffer overflow) can escalate into a system-wide compromise (a VM escape) if proper architectural defenses are missing.</p>
            <p>This breakdown explains the simulation mechanics and the necessity of logical segmentation and isolation.</p>

            <h4 style="margin-top: 1.5rem; color: var(--accent-color);">Phase 1: The Initial Breach (Buffer Overflow)</h4>
            <p>The simulation begins with data flowing into the Guest Virtual Machine (VM) via network input. A vulnerability exists in the guest application's memory handling.</p>
            <p><strong>Mechanics:</strong></p>
            <ul>
                <li><strong>Memory Allocation:</strong> Applications receive specific memory blocks (buffers) to store temporary data.</li>
                <li><strong>The Flaw:</strong> A buffer overflow happens when incoming data exceeds buffer capacity, and the application fails to verify the size.</li>
                <li><strong>The Overwrite:</strong> Excess data (red particles) spills over, overwriting adjacent memory spaces.</li>
                <li><strong>Execution Hijacking:</strong> Attackers craft this data to overwrite control addresses. This forces the application to execute malicious instructions instead of its intended code.</li>
            </ul>
            <p style="color: var(--text-muted); font-style: italic;">In the animation: Green "valid" data stays within bounds; red "malicious" payload forces past buffer limits, taking control within the Guest VM.</p>

            <h4 style="margin-top: 1.5rem; color: var(--accent-color);">Phase 2: The Escalation (VM Escape)</h4>
            <p>A compromised VM application is problematic, but the core promise of virtualization is sandbox containment. A "VM Escape" breaks this containment.</p>
            <p><strong>Mechanics:</strong></p>
            <ul>
                <li><strong>The Shared Layer:</strong> VMs run on a Hypervisor (or Host OS), which manages resources and provides virtual hardware.</li>
                <li><strong>Exploiting the Interface:</strong> The hypervisor and guest VM communicate. An attacker (now running code within the guest) targets vulnerabilities in this interface or virtual device drivers.</li>
                <li><strong>Breaking the Boundary:</strong> By sending malformed requests, the attacker forces the hypervisor to execute malicious instructions on the Host OS.</li>
                <li><strong>Total Compromise:</strong> Executing code at the hypervisor/host OS level grants access to physical hardware, the host OS, and potentially other VMs on the server.</li>
            </ul>
            <p><strong>Real-World Examples:</strong></p>
            <ul>
                <li><strong>VENOM (CVE-2015-3456):</strong> Exploited a flaw in the virtual floppy disk controller (FDC) code used by many hypervisors. This allowed an attacker in a guest VM to crash the hypervisor or execute code on the host.</li>
                <li><strong>Cloudburst (CVE-2009-1244):</strong> Targeted a vulnerability in VMware's virtual video adapter. It enabled code execution on the host OS from within a guest VM.</li>
            </ul>
            <p style="color: var(--text-muted); font-style: italic;">In the "Vulnerable" animation mode: Red particles breach the Guest VM boundary, flooding the Host OS space. The environment turns dark red, indicating total compromise.</p>

            <h4 style="margin-top: 1.5rem; color: var(--accent-color);">Phase 3: Architectural Defense (Segmentation & Isolation)</h4>
            <p>The second mode demonstrates why architectural design choices are critical to preventing escalation.</p>
            <p><strong>Defenses:</strong></p>
            <ul>
                <li><strong>1. Logical Segmentation (The "VM Firewall" Concept):</strong> Dividing systems into isolated segments limits communication pathways.
                <br><em>Mechanism:</em> Strict firewall rules and Virtual LANs (VLANs) restrict lateral movement and host communication attempts.</li>
                <li><strong>2. Strict Isolation (The Glowing Boundary):</strong> Containing processes and memory using hardware-assisted virtualization (e.g., Intel VT-x, AMD-V).
                <br><em>Mechanism:</em> The hypervisor's Memory Management Unit (MMU) strictly enforces boundaries. If a compromised guest attempts unauthorized memory writes, the hardware intercepts and denies the action, protecting the host.</li>
            </ul>
            <p style="color: var(--text-muted); font-style: italic;">In the "Isolated" animation mode: The green isolation barrier activates. The buffer overflow occurs, but malicious execution is blocked from leaving the guest environment. The Host OS remains secure.</p>

            <h4 style="margin-top: 1.5rem; color: var(--accent-color);">Summary</h4>
            <p>Relying solely on application-level security is insufficient. A defense-in-depth strategy requires architectural boundaries—logical segmentation and strict isolation—to contain breaches when they inevitably occur.</p>
        </div>
"""

target = '''        <div id="statusText" class="status-panel">
            Select a simulation mode to begin.
        </div>'''

new_html = html.replace(target, target + '\n' + explanation_html)

with open('domain-3.html', 'w') as f:
    f.write(new_html)

print("Added explanation HTML.")

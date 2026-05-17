import re

text = """
1.0 General Security Concepts (12%)   

1.1 Compare and contrast various types of security controls   

Categories: Technical; Managerial; Operational; Physical   

Control Types: Preventive; Deterrent; Detective; Corrective; Compensating; Directive   

1.2 Summarize fundamental security concepts   

Core Principles: Confidentiality, Integrity, and Availability (CIA); Non-repudiation   

AAA Framework: Authentication, Authorization, and Accounting (AAA); Authenticating people; Authenticating systems; Authorization models   

Analysis: Gap analysis   

Zero Trust Architecture: Control Plane; Adaptive identity; Threat scope reduction; Policy-driven access control; Policy Administrator; Policy Engine; Data Plane; Implicit trust zones; Subject/System; Policy Enforcement Point   

Physical Security Measures: Bollards; Access control vestibule; Fencing; Video surveillance; Security guard; Access badge; Lighting; Sensors (Infrared, Pressure, Microwave, Ultrasonic)   

Deception and Disruption: Honeypot; Honeynet; Honeyfile; Honeytoken   

1.3 Explain the importance of change management processes and the impact to security   

Business Processes: Approval process; Ownership; Stakeholders; Impact analysis; Test results; Backout plan; Maintenance window; Standard operating procedure   

Technical Implications: Allow lists/deny lists; Restricted activities; Downtime; Service restart; Application restart; Legacy applications; Dependencies   

Documentation Management: Updating diagrams; Updating policies/procedures; Version control   

1.4 Explain the importance of using appropriate cryptographic solutions   

Public Key Infrastructure (PKI): Public key; Private key; Key escrow   

Encryption Levels: Full-disk; Partition; File; Volume; Database; Record; Transport/communication   

Encryption Types: Asymmetric; Symmetric; Key exchange; Algorithms; Key length   

Cryptographic Tools: Trusted Platform Module (TPM); Hardware security module (HSM); Key management system; Secure enclave   

Obfuscation Methods: Steganography; Tokenization; Data masking   

Data Integrity & Validation: Hashing; Salting; Digital signatures; Key stretching   

Ledger Technology: Blockchain; Open public ledger   

Certificates Infrastructure: Certificate authorities; Certificate revocation lists (CRLs); Online Certificate Status Protocol (OCSP); Self-signed; Third-party; Root of trust; Certificate signing request (CSR) generation; Wildcard   

2.0 Threats, Vulnerabilities, and Mitigations (22%)   

2.1 Compare and contrast common threat actors and motivations   

Threat Actors: Nation-state; Unskilled attacker; Hacktivist; Insider threat; Organized crime; Shadow IT   

Attributes of Actors: Internal/external; Resources/funding; Level of sophistication/capability   

Motivations: Data exfiltration; Espionage; Service disruption; Blackmail; Financial gain; Philosophical/political beliefs; Ethical; Revenge; Disruption/chaos; War   

2.2 Explain common threat vectors and attack surfaces   

Message-Based Vectors: Email; Short Message Service (SMS); Instant messaging (IM)   

Communication & Media Vectors: Image-based; File-based; Voice call; Removable device   

Software Vulnerabilities: Vulnerable software (Client-based vs. agentless); Unsupported systems and applications   

Network Vectors: Unsecure networks (Wireless, Wired, Bluetooth); Open service ports; Default credentials   

Supply Chain Vectors: Managed service providers (MSPs); Vendors; Suppliers   

Human Vectors / Social Engineering: Phishing; Vishing; Smishing; Misinformation/disinformation; Impersonation; Business email compromise; Pretexting; Watering hole; Brand impersonation; Typosquatting   

2.3 Explain various types of vulnerabilities   

Application-Level: Memory injection; Buffer overflow; Race conditions; Time-of-check (TOC); Time-of-use (TOU); Malicious update   

System & Web Infrastructure: Operating system (OS)-based; Web-based; Structured Query Language injection (SQLI); Cross-site scripting (XSS)   

Hardware & Firmware: Hardware; Firmware; End-of-life; Legacy   

Virtualization & Cloud: Virtual machine (VM) escape; Resource reuse; Cloud-specific   

Supply Chain Dependencies: Supply chain; Service provider; Hardware provider; Software provider   

Operational Flaws: Cryptographic; Misconfiguration; Mobile device; Side loading; Jailbreaking; Zero-day   

2.4 Given a scenario, analyze indicators of malicious activity   

Malware Attacks: Ransomware; Trojan; Worm; Spyware; Bloatware; Virus; Keylogger; Logic bomb; Rootkit   

Physical Attacks: Brute force; Radio frequency identification (RFID) cloning; Environmental   

Network Attacks: Distributed denial-of-service (DDoS) (Amplified, Reflected); Domain Name System (DNS) attacks; Wireless; On-path; Credential replay; Malicious code   

Application Attacks: Injection; Buffer overflow; Replay; Privilege escalation; Forgery; Directory traversal   

Cryptographic Attacks: Downgrade; Collision; Birthday   

Password Exploits: Spraying; Brute force   

System Indicators: Account lockout; Concurrent session usage; Blocked content; Impossible travel; Resource consumption; Resource inaccessibility; Out-of-cycle logging; Published/documented anomalies; Missing logs   

2.5 Explain the purpose of mitigation techniques used to secure the enterprise   

Access & Boundary Security: Segmentation; Access control; Access control list (ACL); Permissions; Application allow list; Isolation   

System Integrity: Patching; Encryption; Monitoring; Least privilege; Configuration enforcement; Decommissioning   

Hardening Techniques: Encryption; Installation of endpoint protection; Host-based firewall; Host-based intrusion prevention system (HIPS); Disabling ports/protocols; Default password changes; Removal of unnecessary software   

3.0 Security Architecture (18%)   

3.1 Compare and contrast security implications of different architecture models   

Architecture & Infrastructure Concepts: Cloud (Responsibility matrix, Hybrid considerations); Third-party vendors; Infrastructure as code (IaC); Serverless; Microservices   

Network Isolation Models: Network infrastructure; Physical isolation (Air-gapped); Logical segmentation; Software-defined networking (SDN); On-premises; Centralized vs. decentralized   

Deployment Systems: Containerization; Virtualization; IoT; Industrial control systems (ICS)/supervisory control and data acquisition (SCADA); Real-time operating system (RTOS); Embedded systems; High availability   

Architectural Considerations: Availability; Resilience; Cost; Responsiveness; Scalability; Ease of deployment; Risk transference; Ease of recovery; Patch availability; Inability to patch; Power; Compute   

3.2 Given a scenario, apply security principles to secure enterprise infrastructure   

Infrastructure Factors: Device placement; Security zones; Attack surface; Connectivity; Failure modes (Fail-open, Fail-closed)   

Device Attributes: Active vs. passive; Inline vs. tap/monitor   

Network Appliances: Jump server; Proxy server; Intrusion prevention system (IPS)/intrusion detection system (IDS); Load balancer; Sensors; Port security   

Access Authentication: 802.1X; Extensible Authentication Protocol (EAP)   

Firewall Deployments: Web application firewall (WAF); Unified threat management (UTM); Next-generation firewall (NGFW); Layer 4/Layer 7   

Secure Communication & Access: Virtual private network (VPN); Remote access; Tunneling; Transport Layer Security (TLS); Internet protocol security (IPSec); Software-defined wide area network (SD-WAN); Secure access service edge (SASE); Selection of effective controls   

3.3 Compare and contrast concepts and strategies to protect data   

Data Types: Regulated; Trade secret; Intellectual property; Legal information; Financial information; Human- and non-human-readable   

Data Classifications: Sensitive; Confidential; Public; Restricted; Private; Critical   

General Considerations: Data states (Data at rest, Data in transit, Data in use); Data sovereignty; Geolocation   

Security Methods: Geographic restrictions; Encryption; Hashing; Masking; Tokenization; Obfuscation; Segmentation; Permission restrictions   

3.4 Explain the importance of resilience and recovery in security architecture   

High Availability & Platforms: Load balancing vs. clustering; Platform diversity; Multi-cloud systems; Continuity of operations   

Disaster Recovery Sites: Site considerations (Hot, Cold, Warm); Geographic dispersion   

Capacity Planning Elements: People; Technology; Infrastructure   

Testing Strategies: Tabletop exercises; Fail over; Simulation; Parallel processing   

Backup Systems: Onsite/offsite; Frequency; Encryption; Snapshots; Recovery; Replication; Journaling   

Power Redundancy: Generators; Uninterruptible power supply (UPS)   

4.0 Security Operations (28%)   

4.1 Given a scenario, apply common security techniques to computing resources   

Secure Baselines Lifecycle: Establish; Deploy; Maintain   

Hardening Targets: Mobile devices; Workstations; Switches; Routers; Cloud infrastructure; Servers; ICS/SCADA; Embedded systems; RTOS; IoT devices; Wireless devices   

Installation & Deployment: Site surveys; Heat maps; Mobile solutions (Mobile device management (MDM))   

Mobile Models & Connectivity: Bring your own device (BYOD); Corporate-owned, personally enabled (COPE); Choose your own device (CYOD); Connection methods (Cellular, Wi-Fi, Bluetooth)   

Wireless Security Configurations: Wi-Fi Protected Access 3 (WPA3); AAA/Remote Authentication Dial-In User Service (RADIUS); Cryptographic protocols; Authentication protocols   

Application-Level Security: Input validation; Secure cookies; Static code analysis; Code signing; Sandboxing; Monitoring   

4.2 Explain the security implications of proper hardware, software, and data asset management   

Asset Lifecycle & Accounting: Acquisition/procurement process; Assignment/accounting; Ownership; Classification; Monitoring/asset tracking; Inventory; Enumeration   

Decommissioning & Lifecycle Protection: Disposal/decommissioning; Sanitization; Destruction; Certification; Data retention   

4.3 Explain various activities associated with vulnerability management   

Identification Methodologies: Vulnerability scan; Application security (Static analysis, Dynamic analysis, Package monitoring); Threat feed (Open-source intelligence (OSINT), Proprietary/third-party, Information-sharing organization, Dark web); Penetration testing; Responsible disclosure program; Bug bounty program; System/process audit   

Analysis & Categorization: Confirmation; False positive; False negative; Prioritize; Common Vulnerability Scoring System (CVSS); Common Vulnerability Enumeration (CVE); Vulnerability classification; Exposure factor; Environmental variables; Industry/organizational impact; Risk tolerance   

Response, Remediation, & Validation: Vulnerability response and remediation; Patching; Insurance; Segmentation; Compensating controls; Exceptions and exemptions; Validation of remediation; Rescanning; Audit; Verification; Reporting   

4.4 Explain security alerting and monitoring concepts and tools   

Resource Monitoring Operations: Systems; Applications; Infrastructure; Activities (Log aggregation, Alerting, Scanning, Reporting, Archiving)   

Alert Handling: Alert response and remediation/validation; Quarantine; Alert tuning   

Operations Toolsets: Security Content Automation Protocol (SCAP); Benchmarks; Agents/agentless; Security information and event management (SIEM); Antivirus; Data loss prevention (DLP); Simple Network Management Protocol (SNMP) traps; NetFlow; Vulnerability scanners   

4.5 Given a scenario, modify enterprise capabilities to enhance security   

Network Layer Protections: Firewall (Rules, Access lists, Ports/protocols, Screened subnets); IDS/IPS (Trends, Signatures)   

Web & OS Defenses: Web filter (Agent-based, Centralized proxy, Universal Resource Locator (URL) scanning, Content categorization, Block rules, Reputation); Operating system security (Group Policy, SELinux)   

Protocol & Communications Security: Implementation of secure protocols (Protocol selection, Port selection, Transport method); DNS filtering; Gateway; File integrity monitoring   

Email Domain Protections: Domain-based Message Authentication Reporting and Conformance (DMARC); Domainkeys Identified Mail (DKIM); Sender Policy Framework (SPF)   

Advanced Endpoint & Access Controls: DLP; Network access control (NAC); Endpoint detection and response (EDR)/extended detection and response (XDR); User behavior analytics   

4.6 Given a scenario, implement and maintain identity and access management   

Identity Governance: Provisioning/de-provisioning user accounts; Permission assignments and implications; Identity proofing   

Federation & Directory Services: Federation; Single sign-on (SSO); Lightweight Directory Access Protocol (LDAP); Open authorization (OAuth); Security Assertions Markup Language (SAML); Interoperability; Attestation   

Access Models: Mandatory; Discretionary; Role-based; Rule-based; Attribute-based; Time-of-day restrictions; Least privilege   

Multifactor Authentication (MFA): Implementations; Biometrics; Hard/soft authentication tokens; Security keys; Factors (Something you know, Something you have, Something you are, Somewhere you are)   

Password Controls: Password concepts; Password best practices; Length; Complexity; Reuse; Expiration; Age; Password managers; Passwordless   

Privileged Access Frameworks: Privileged access management tools; Just-in-time permissions; Password vaulting; Ephemeral credentials   

4.7 Explain the importance of automation and orchestration related to secure operations   

Automation Use Cases: Scripting use cases; User provisioning; Resource provisioning; Guard rails; Security groups; Ticket creation; Escalation; Enabling/disabling services and access; Continuous integration and testing; Integrations and Application programming interfaces (APIs)   

Operational Benefits: Efficiency/time saving; Enforcing baselines; Standard infrastructure configurations; Scaling in a secure manner; Employee retention; Reaction time; Workforce multiplier   

System Considerations: Complexity; Cost; Single point of failure; Technical debt; Ongoing supportability   

4.8 Explain appropriate incident response activities   

Lifecycle Process: Preparation; Detection; Analysis; Containment; Eradication; Recovery; Lessons learned   

Testing & Readiness: Training; Testing; Tabletop exercise; Simulation; Root cause analysis; Threat hunting   

Digital Forensics Procedures: Digital forensics; Legal hold; Chain of custody; Acquisition; Reporting; Preservation; E-discovery   

4.9 Given a scenario, use data sources to support an investigation   

Log Data Analysis: Firewall logs; Application logs; Endpoint logs; OS-specific security logs; IPS/IDS logs; Network logs; Metadata   

Investigative Sources: Data sources; Vulnerability scans; Automated reports; Dashboards; Packet captures   

5.0 Security Program Management and Oversight (20%)   

5.1 Summarize elements of effective security governance   

Framework Components: Guidelines; Policies (Acceptable use policy (AUP), Information security policies, Business continuity, Disaster recovery, Incident response, Software development lifecycle (SDLC), Change management)   

Operational Controls: Standards (Password, Access control, Physical security, Encryption); Procedures (Change management, Onboarding/offboarding, Playbooks)   

External Environments: Regulatory; Legal; Industry; Local/regional; National; Global; Monitoring and revision   

Governance Typologies: Boards; Committees; Government entities; Centralized/decentralized   

Data & System Ownership: Roles and responsibilities for systems and data; Owners; Controllers; Processors; Custodians/stewards   

5.2 Explain elements of the risk management process   

Risk Evaluation Lifecycle: Risk identification; Risk assessment (Ad hoc, Recurring, One-time, Continuous)   

Analysis Approaches: Risk analysis; Qualitative; Quantitative; Single loss expectancy (SLE); Annualized loss expectancy (ALE); Annualized rate of occurrence (ARO); Probability; Likelihood; Exposure factor; Impact   

Risk Registers & Metrics: Risk register; Key risk indicators; Risk owners; Risk threshold; Risk tolerance; Risk appetite (Expansionary, Conservative, Neutral); Risk reporting   

Strategic Responses: Risk management strategies; Transfer; Accept; Exemption; Exception; Avoid; Mitigate   

Business Resilience Metrics: Business impact analysis; Recovery time objective (RTO); Recovery point objective (RPO); Mean time to repair (MTTR); Mean time between failures (MTBF)   

5.3 Explain the processes associated with third-party risk assessment and management   

Vendor Due Diligence: Vendor assessment; Penetration testing; Right-to-audit clause; Evidence of internal audits; Independent assessments; Supply chain analysis; Vendor selection; Due diligence; Conflict of interest   

Legal & Contractual Frameworks: Agreement types; Service-level agreement (SLA); Memorandum of agreement (MOA); Memorandum of understanding (MOU); Master service agreement (MSA); Work order (WO)/statement of work (SOW); Non-disclosure agreement (NDA); Business partners agreement (BPA)   

Ongoing Monitoring: Vendor monitoring; Questionnaires; Rules of engagement   

5.4 Summarize elements of effective security compliance   

Reporting & Governance: Compliance reporting (Internal, External); Compliance monitoring; Due diligence/care; Attestation and acknowledgement (Internal and external); Automation   

Consequences of Non-Compliance: Fines; Sanctions; Reputational damage; Loss of license; Contractual impacts   

Privacy Frameworks: Privacy; Legal implications; Local/regional; National; Global; Data subject; Controller vs. processor; Ownership; Data inventory and retention; Right to be forgotten   

5.5 Explain types and purposes of audits and assessments   

Internal Oversight: Attestation; Internal compliance; Audit committee; Self-assessments   

External Validation: External regulatory; Examinations; Assessment; Independent third-party audit   

Penetration Testing Frameworks: Penetration testing; Physical; Offensive; Defensive; Integrated; Known environment; Partially known environment; Unknown environment; Reconnaissance (Passive, Active)   

5.6 Given a scenario, implement security awareness practices   

Phishing Readiness: Phishing campaigns; Recognizing a phishing attempt; Responding to reported suspicious messages   

Behavioral & Threat Analysis: Anomalous behavior recognition (Risky, Unexpected, Unintentional); Insider threat   

User Training Contexts: User guidance and training; Policy/handbooks; Situational awareness; Password management; Removable media and cables; Social engineering; Operational security; Hybrid/remote work environments   

Program Assessment: Reporting and monitoring; Initial; Recurring; Development; Execution
"""

lines = [l.strip() for l in text.split('\n') if l.strip()]

output = []
current_domain = None
current_sub = None

for line in lines:
    if line.startswith(('1.0', '2.0', '3.0', '4.0', '5.0')):
        if current_domain:
            if current_sub:
                output.append('        </ul>\n      </details>')
            output.append('    </div>\n  </section>')
        
        domain_id = line.split(' ')[0].replace('.', '-')
        output.append(f'  <section id="{domain_id}" class="why-section">')
        output.append(f'    <h2>{line}</h2>')
        output.append('    <div class="faq-grid">')
        current_domain = line
        current_sub = None
    elif re.match(r'^\d\.\d ', line):
        if current_sub:
            output.append('        </ul>\n      </details>')
        output.append('      <details class="faq-item">')
        output.append(f'        <summary>{line}</summary>')
        output.append('        <ul>')
        current_sub = line
    else:
        # Check if it has a colon for strong
        if ':' in line:
            parts = line.split(':', 1)
            output.append(f'          <li><strong>{parts[0]}:</strong>{parts[1]}</li>')
        else:
            output.append(f'          <li>{line}</li>')

if current_domain:
    if current_sub:
        output.append('        </ul>\n      </details>')
    output.append('    </div>\n  </section>')

with open('formatted_output.html', 'w') as f:
    f.write('\n'.join(output))


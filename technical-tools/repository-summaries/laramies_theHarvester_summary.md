# laramies/theHarvester

## Repository overview

| Field | Details |
|-------|--------|
| **Source** | https://github.com/laramies/theHarvester |
| **Description** | No description provided. |
| **Topics** | `python`, `osint`, `discovery`, `emails`, `recon`, `information-gathering`, `blueteam`, `reconnaissance`, `redteam`, `subdomain-enumeration` |

---

## Repository health

| Metric | Value |
|--------|-------|
| **Stars** | 16.2k |
| **Forks** | 2.5k |
| **Open issues** | 2 |
| **License** | N/A |
| **Last commit** | 2026-05-12T19:49:48.000Z |

---

## Language breakdown

| Language | Percentage |
|----------|-----------|
| Python | 99.8% |
| Dockerfile | 0.2% |

---

## Dependencies

### Python (pyproject)

- `aiodns`
- `aiofiles`
- `aiohttp`
- `aiohttp-socks`
- `aiomultiprocess`
- `aiosqlite`
- `beautifulsoup4`
- `censys`
- `certifi`
- `dnspython`
- `fastapi`
- `lxml`
- `netaddr`
- `playwright`
- `PyYAML`
- `python-dateutil`
- `httpx`
- `retrying`
- `shodan`
- `slowapi`
- `ujson`
- `uvicorn`
- `uvloop`
- `winloop`

---

## README contents

> The following content was extracted from the repository's README file.

[![theHarvester](https://github.com/laramies/theHarvester/raw/master/theHarvester-logo.webp)](https://github.com/laramies/theHarvester/blob/master/theHarvester-logo.webp)

[![TheHarvester CI](https://github.com/laramies/theHarvester/workflows/TheHarvester%20Python%20CI/badge.svg)](https://github.com/laramies/theHarvester/workflows/TheHarvester%20Python%20CI/badge.svg) [![TheHarvester Docker Image CI](https://github.com/laramies/theHarvester/workflows/TheHarvester%20Docker%20Image%20CI/badge.svg)](https://github.com/laramies/theHarvester/workflows/TheHarvester%20Docker%20Image%20CI/badge.svg)
[![Rawsec's CyberSecurity Inventory](https://camo.githubusercontent.com/1023d6a715feeb577a2e4a64743222b0f8b1cf11d6d1da7ea46bc2223f41dcec/68747470733a2f2f696e76656e746f72792e7261772e706d2f696d672f6261646765732f5261777365632d696e76656e746f726965642d4646353035305f666c61745f776974686f75745f6c6f676f2e737667)](https://inventory.raw.pm/)

## About

theHarvester is a simple to use, yet powerful tool designed to be used during the reconnaissance stage of a red
team assessment or penetration test. It performs open source intelligence (OSINT) gathering to help determine
a domain's external threat landscape. The tool gathers names, emails, IPs, subdomains, and URLs by using
multiple public resources that include:

## Package versions

[![Packaging status](https://camo.githubusercontent.com/0cc26c8ddbb095d96094ab3d5275f2905fb0dc0c20ab4d8eb1d7ece4c8e23c02/68747470733a2f2f7265706f6c6f67792e6f72672f62616467652f766572746963616c2d616c6c7265706f732f7468656861727665737465722e737667)](https://repology.org/project/theharvester/versions)

## Install and dependencies

* Python 3.12 or higher.
* <https://github.com/laramies/theHarvester/wiki/Installation>

Install uv:

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Clone the repository:

```
git clone https://github.com/laramies/theHarvester
cd theHarvester
```

Install dependencies and create a virtual environment:

```
uv sync
```

Run theHarvester:

```
uv run theHarvester
```

## Development

To install development dependencies:

```
uv sync --all-groups
```

To run tests:

```
uv run pytest
```

To run linting and formatting:

```
uv run ruff check
```

```
uv run ruff format
```

To protect the optional `/additional/*` REST API routes, set `THEHARVESTER_API_KEY` and pass the same value in the `X-API-Key` header. Those routes return `503` when the key is not configured.

## Passive modules

* baidu: Baidu search engine (<https://www.baidu.com>)
* bevigil: CloudSEK BeVigil scans mobile application for OSINT assets (<https://bevigil.com/osint-api>)
* brave: Brave search engine - now uses official Brave Search API (<https://api-dashboard.search.brave.com>)
* bufferoverun: Fast domain name lookups for TLS certificates in IPv4 space (<https://tls.bufferover.run>)
* builtwith: Find out what websites are built with (<https://builtwith.com>)
* censys: Uses certificates searches to enumerate subdomains and gather emails (<https://censys.io>)
* certspotter: Cert Spotter monitors Certificate Transparency logs (<https://sslmate.com/certspotter>)
* criminalip: Specialized Cyber Threat Intelligence (CTI) search engine (<https://www.criminalip.io>)
* crtsh: Comodo Certificate search (<https://crt.sh>)
* dehashed: Take your data security to the next level is (<https://dehashed.com>)
* dnsdumpster: Domain research tool that can discover hosts related to a domain (<https://dnsdumpster.com>)
* duckduckgo: DuckDuckGo search engine (<https://duckduckgo.com>)
* dymo: Dymo API data verifier - confirms domains, surfaces typo suggestions and MX/fraud signals (<https://dymo.tpeoficial.com>)
* fofa: FOFA search eingine (<https://en.fofa.info>)
* fullhunt: Next-generation attack surface security platform (<https://fullhunt.io>)
* github-code: GitHub code search engine (<https://www.github.com>)
* hackertarget: Online vulnerability scanners and network intelligence to help organizations (<https://hackertarget.com>)
* haveibeenpwned: Check if your email address is in a data breach (<https://haveibeenpwned.com>)
* hunter: Hunter search engine (<https://hunter.io>)
* hunterhow: Internet search engines for security researchers (<https://hunter.how>)
* intelx: Intelx search engine (<https://intelx.io>)
* leakix: LeakIX search engine (<https://leakix.net>)
* leaklookup: Data breach search engine (<https://leak-lookup.com>)
* mojeek: Mojeek search engine (<https://www.mojeek.com>)
* netlas: A Shodan or Censys competitor (<https://app.netlas.io>)
* onyphe: Cyber defense search engine (<https://www.onyphe.io>)
* otx: AlienVault open threat exchange (<https://otx.alienvault.com>)
* pentesttools: Cloud-based toolkit for offensive security testing, focused on web applications and network penetration testing (<https://pentest-tools.com>)
* projecdiscovery: Actively collects and maintains internet-wide assets data, to enhance research and analyse changes around DNS for better insights (<https://chaos.projectdiscovery.io>)
* rapiddns: DNS query tool which make querying subdomains or sites of a same IP easy (<https://rapiddns.io>)
* rocketreach: Access real-time verified personal/professional emails, phone numbers, and social media links (<https://rocketreach.co>)
* securityscorecard: helps TPRM and SOC teams detect, prioritize, and remediate vendor risk across their entire supplier ecosystem at scale (<https://securityscorecard.com>)
* securityTrails: Security Trails search engine, the world's largest repository of historical DNS data (<https://securitytrails.com>)
* -s, --shodan: Shodan search engine will search for ports and banners from discovered hosts (<https://shodan.io>)
* subdomaincenter: A subdomain finder tool used to find subdomains of a given domain (<https://www.subdomain.center>)
* subdomainfinderc99: A subdomain finder is a tool used to find the subdomains of a given domain (<https://subdomainfinder.c99.nl>)
* thc: Free subdomain enumeration service with no API key required (<https://ip.thc.org>)
* threatminer: Data mining for threat intelligence (<https://www.threatminer.org>)
* tomba: Tomba search engine (<https://tomba.io>)
* urlscan: A sandbox for the web that is a URL and website scanner (<https://urlscan.io>)
* venacus: Venacus search engine (<https://venacus.com>)
* virustotal: Domain search (<https://www.virustotal.com>)
* whoisxml: Subdomain search (<https://subdomains.whoisxmlapi.com/api/pricing>)
* yahoo: Yahoo search engine (<https://www.yahoo.com>)
* windvane: Windvane search engine (<https://windvane.lichoin.com>)
* zoomeye: China's version of Shodan (<https://www.zoomeye.org>)

## Active modules

* DNS brute force: dictionary brute force enumeration
* Screenshots: Take screenshots of subdomains that were found

## Modules that require an API key

Documentation to setup API keys can be found at - <https://github.com/laramies/theHarvester/wiki/Installation#api-keys>

* bevigil - 50 free queries/month. 1k queries/month $50
* brave - free plan available. Pro plans for higher limits
* bufferoverun - 100 free queries/month. 10k/month $25
* builtwith - 50 free queries ever. $2950/yr
* censys - 500 credits $100
* criminalip - 100 free queries/month. 700k/month $59
* dehashed - 500 credts $15, 5k credits $150
* dnsdumpster - 50 free querries/day, $49
* dymo - free tier available, paid plans for higher limits
* fofa - query credits 10,000/month. 100k results/month $25
* fullhunt - 50 free queries. 200 queries $29/month, 500 queries $59
* github-code
* haveibeenpwned - 10 email searches/min $4.50, 50 email searches/min $22
* hunter - 50 free credits/month. 12k credits/yr $34
* hunterhow - 10k free API results per 30 days. 50k API results per 30 days $10
* intelx - free account is very limited. Business acount $2900
* leakix - free 25 results pages, 3000 API requests/month. Bounty Hunter $29
* leaklookup - 20 credits $10, 50 credits $20, 140 credits $50, 300 credits $100
* mojeek - 5000 free credits $6.50, $1.30 CPM (Personal), $2.60 CPM (Startup), $3.90 CPM (Business)
* netlas - 50 free requests/day. 1k requests $49, 10k requests $249
* onyphe - 10M results/month $587
* pentesttools - 5 assets netsec $95/month, 5 assets webnetsec $140/month
* projecdiscovery - requires work email. Free monthly discovery and vulnerability scans on sign-up email domain, enterprise $
* rocketreach - 100 email lookups/month $48, 250 email lookups/month $108
* securityscorecard - requires a work email
* securityTrails - 50 free queries/month. 20k queries/month $500
* shodan - Freelancer $69 month, Small Business $359 month
* tomba - 25 free searches/month. 1k searches/month $39, 5k searches/month $89
* venacus - 1 free search/day. 10 searches/day $12, 30 searches/day $36
* virustotal - 500 free lookups/day, 15.5k lookups/month. Busines accounts requires a work email
* whoisxml - 2k queries $50, 5k queries $105
* windvane - 100 free queries
* zoomeye - 5 free results/day. 30/results/day $190/yr

## Comments, bugs, and requests

* [![Twitter Follow](https://camo.githubusercontent.com/782391797e5d7c748789a5d9f32a33c1f9013948194e7e063262d708000d05c9/68747470733a2f2f696d672e736869656c64732e696f2f747769747465722f666f6c6c6f772f6c6172616d6965732e7376673f7374796c653d736f6369616c266c6162656c3d466f6c6c6f77)](https://twitter.com/laramies) Christian Martorella @laramies
  [cmartorella@edge-security.com](mailto:cmartorella@edge-security.com)
* [![Twitter Follow](https://camo.githubusercontent.com/82da0893ea6a67a6e8bd29d659d33dd4d35cb6d9186f557f3a6133c4e4895bce/68747470733a2f2f696d672e736869656c64732e696f2f747769747465722f666f6c6c6f772f4e6f746f72696f7573526562656c312e7376673f7374796c653d736f6369616c266c6162656c3d466f6c6c6f77)](https://twitter.com/NotoriousRebel1) Matthew Brown @NotoriousRebel1
* [![Twitter Follow](https://camo.githubusercontent.com/69ffc16ca59464e73d08396b8d1485008a4f2f2a3eb695d2d19a71b6becd04c4/68747470733a2f2f696d672e736869656c64732e696f2f747769747465722f666f6c6c6f772f6a61795f746f776e73656e64312e7376673f7374796c653d736f6369616c266c6162656c3d466f6c6c6f77)](https://twitter.com/jay_townsend1) Jay "L1ghtn1ng" Townsend @jay\_townsend1

## Main contributors

* [![Twitter Follow](https://camo.githubusercontent.com/82da0893ea6a67a6e8bd29d659d33dd4d35cb6d9186f557f3a6133c4e4895bce/68747470733a2f2f696d672e736869656c64732e696f2f747769747465722f666f6c6c6f772f4e6f746f72696f7573526562656c312e7376673f7374796c653d736f6369616c266c6162656c3d466f6c6c6f77)](https://twitter.com/NotoriousRebel1) Matthew Brown @NotoriousRebel1
* [![Twitter Follow](https://camo.githubusercontent.com/69ffc16ca59464e73d08396b8d1485008a4f2f2a3eb695d2d19a71b6becd04c4/68747470733a2f2f696d672e736869656c64732e696f2f747769747465722f666f6c6c6f772f6a61795f746f776e73656e64312e7376673f7374796c653d736f6369616c266c6162656c3d466f6c6c6f77)](https://twitter.com/jay_townsend1) Jay "L1ghtn1ng" Townsend @jay\_townsend1
* [![Twitter Follow](https://camo.githubusercontent.com/1c0ab6788ad3533c1d00f6f8ec29eeee80b5cda69a98dcdff0df1265530c18d8/68747470733a2f2f696d672e736869656c64732e696f2f747769747465722f666f6c6c6f772f646973636f766572736372697074732e7376673f7374796c653d736f6369616c266c6162656c3d466f6c6c6f77)](https://twitter.com/discoverscripts) Lee Baird @discoverscripts

## Thanks

* John Matherly - Shodan project
* Ahmed Aboul Ela - subdomain names dictionaries (big and small)

---

*This summary was auto-generated by [GitHub Repository Scraper](https://github.com/) from `https://github.com/laramies/theHarvester`.*

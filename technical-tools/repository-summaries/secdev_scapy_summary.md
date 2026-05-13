# secdev/scapy

## Repository overview

| Field | Details |
|-------|--------|
| **Source** | https://github.com/secdev/scapy |
| **Description** | No description provided. |
| **Topics** | `python`, `security`, `pcap`, `network`, `packet-analyser`, `network-visualization`, `scapy`, `packet-sniffer`, `network-discovery`, `network-analysis`, `hacktoberfest`, `packet-crafting`, `packet-capture`, `network-security`, `security-tools` |

---

## Repository health

| Metric | Value |
|--------|-------|
| **Stars** | 12.3k |
| **Forks** | 2.2k |
| **Open issues** | 70 |
| **License** | GPL-2.0 license |
| **Last commit** | 2026-05-09T11:54:50.000Z |

---

## Language breakdown

| Language | Percentage |
|----------|-----------|
| Python | 99.8% |

---

## Dependencies

### Python (pyproject)

- `cli`
- `all`
- `ipython`
- `pyx`
- `cryptography`
- `matplotlib`
- `doc`
- `cryptography`
- `sphinx`
- `sphinx_rtd_theme`
- `tox`

---

## README contents

> The following content was extracted from the repository's README file.

# [Scapy](https://github.com/secdev/scapy/raw/master/doc/scapy/graphics/scapy_logo.png)   Scapy

[![Scapy unit tests](https://github.com/secdev/scapy/actions/workflows/unittests.yml/badge.svg?branch=master&event=push)](https://github.com/secdev/scapy/actions/workflows/unittests.yml?query=event%3Apush)
[![Codecov Status](https://camo.githubusercontent.com/c4f974fa86cc434e85728ab4a486d6176bd9ad54ab390339a6ef3de248020d35/68747470733a2f2f636f6465636f762e696f2f67682f7365636465762f73636170792f6272616e63682f6d61737465722f67726170682f62616467652e737667)](https://codecov.io/gh/secdev/scapy)
[![Codacy Badge](https://camo.githubusercontent.com/649f41bfb7d08bed1c3985f4444131643a9c7569af81f904c6e2fb382e2214c6/68747470733a2f2f6170692e636f646163792e636f6d2f70726f6a6563742f62616467652f47726164652f3330656536373732626232363461363839613236303466356364623034333762)](https://app.codacy.com/gh/secdev/scapy/dashboard)
[![PyPI Version](https://camo.githubusercontent.com/16374dede0274c5e5641dfcb8c1bdca22ff94b11024415a4a689ecaffdc5e3a2/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f73636170792e737667)](https://pypi.python.org/pypi/scapy/)
[![License: GPL v2](https://camo.githubusercontent.com/77e900ae34f8da9ccccc42662fce61a94ab07ddbfe3f7d066178e824f3673dbd/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d47504c25323076322d626c75652e737667)](/secdev/scapy/blob/master/LICENSE)
[![Join the chat at https://gitter.im/secdev/scapy](https://camo.githubusercontent.com/611bebc05bf60143d699b9f092d396a2f0a32df09af146aa4df73dfb12631442/68747470733a2f2f6261646765732e6769747465722e696d2f7365636465762f73636170792e737667)](https://gitter.im/secdev/scapy)

Scapy is a powerful Python-based interactive packet manipulation program and
library.

It is able to forge or decode packets of a wide number of protocols, send them
on the wire, capture them, store or read them using pcap files, match requests
and replies, and much more. It is designed to allow fast packet prototyping by
using default values that work.

It can easily handle most classical tasks like scanning, tracerouting, probing,
unit tests, attacks or network discovery (it can replace `hping`, 85% of `nmap`,
`arpspoof`, `arp-sk`, `arping`, `tcpdump`, `wireshark`, `p0f`, etc.). It also
performs very well at a lot of other specific tasks that most other tools can't
handle, like sending invalid frames, injecting your own 802.11 frames, combining
techniques (VLAN hopping+ARP cache poisoning, VoIP decoding on WEP protected
channel, ...), etc.

Scapy supports Python 3.7+. It's intended to
be cross platform, and runs on many different platforms (Linux, OSX,
\*BSD, and Windows).

## Getting started

Scapy is usable either as a **shell** or as a **library**.
For further details, please head over to [Getting started with Scapy](https://scapy.readthedocs.io/en/latest/introduction.html), which is part of the documentation.

### Shell demo

[![Scapy install demo](https://camo.githubusercontent.com/bb7fa7e8d0069d4d89bd92eb5d2eeed23bf29e560194379c1ac373458b9fccc5/68747470733a2f2f7365636465762e6769746875622e696f2f66696c65732f646f632f616e696d6174696f6e2d73636170792d696e7374616c6c2e737667)](https://camo.githubusercontent.com/bb7fa7e8d0069d4d89bd92eb5d2eeed23bf29e560194379c1ac373458b9fccc5/68747470733a2f2f7365636465762e6769746875622e696f2f66696c65732f646f632f616e696d6174696f6e2d73636170792d696e7374616c6c2e737667)

Scapy can easily be used as an interactive shell to interact with the network.
The following example shows how to send an ICMP Echo Request message to
`github.com`, then display the reply source IP address:

```
sudo ./run_scapy
Welcome to Scapy
>>> p = IP(dst="github.com")/ICMP()
>>> r = sr1(p)
Begin emission:
.Finished to send 1 packets.
*
Received 2 packets, got 1 answers, remaining 0 packets
>>> r[IP].src
'192.30.253.113'
```

### Resources

The [documentation](https://scapy.readthedocs.io/en/latest/) contains more
advanced use cases, and examples.

Other useful resources:

* [Scapy in 20 minutes](https://github.com/secdev/scapy/blob/master/doc/notebooks/Scapy%20in%2015%20minutes.ipynb)
* [Interactive tutorial](https://scapy.readthedocs.io/en/latest/usage.html#interactive-tutorial) (part of the documentation)
* [The quick demo: an interactive session](https://scapy.readthedocs.io/en/latest/introduction.html#quick-demo) (some examples may be outdated)
* [HTTP/2 notebook](https://github.com/secdev/scapy/blob/master/doc/notebooks/HTTP_2_Tuto.ipynb)
* [TLS notebooks](https://github.com/secdev/scapy/blob/master/doc/notebooks/tls)

## [Installation](https://scapy.readthedocs.io/en/latest/installation.html)

Scapy works without any external Python modules on Linux and BSD like operating
systems. On Windows, you need to install some mandatory dependencies as
described in [the
documentation](http://scapy.readthedocs.io/en/latest/installation.html#windows).

On most systems, using Scapy is as simple as running the following commands:

```
git clone https://github.com/secdev/scapy
cd scapy
./run_scapy
```

To benefit from all Scapy features, such as plotting, you might want to install
Python modules, such as `matplotlib` or `cryptography`. See the
[documentation](http://scapy.readthedocs.io/en/latest/installation.html) and
follow the instructions to install them.

## License

Scapy's code, tests and tools are licensed under GPL v2.
The documentation (everything unless marked otherwise in `doc/`, and except the logo) is licensed under CC BY-NC-SA 2.5.

## Contributing

Want to contribute? Great! Please take a few minutes to
[read this](/secdev/scapy/blob/master/CONTRIBUTING.md)!

---

*This summary was auto-generated by [GitHub Repository Scraper](https://github.com/) from `https://github.com/secdev/scapy`.*

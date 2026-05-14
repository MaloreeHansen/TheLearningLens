# juice-shop/juice-shop

## Repository overview

| Field | Details |
|-------|--------|
| **Source** | https://github.com/juice-shop/juice-shop |
| **Description** | No description provided. |
| **Topics** | `javascript`, `security`, `hacking`, `owasp`, `application-security`, `pentesting`, `ctf`, `vulnerable`, `appsec`, `hacktoberfest`, `owasp-top-10`, `owasp-top-ten`, `24pullrequests`, `vulnapp` |

---

## Repository health

| Metric | Value |
|--------|-------|
| **Stars** | 13.1k |
| **Forks** | 17.9k |
| **Open issues** | 10 |
| **License** | MIT license |
| **Last commit** | 2026-05-12T21:10:30.000Z |

---

## Language breakdown

| Language | Percentage |
|----------|-----------|
| TypeScript | 61.3% |
| JavaScript | 26.7% |
| HTML | 6.7% |
| SCSS | 3.8% |
| Solidity | 0.7% |
| Pug | 0.3% |

---

## Dependencies

### JavaScript (npm)

- `@ai-sdk/openai-compatible`
- `@fontsource/roboto`
- `ai`
- `beercss`
- `body-parser`
- `check-dependencies`
- `clarinet`
- `colors`
- `compression`
- `config`
- `cookie-parser`
- `cookieconsent`
- `cors`
- `download`
- `errorhandler`
- `ethers`
- `express`
- `express-ipfilter`
- `express-jwt`
- `express-rate-limit`
- `express-robots-txt`
- `express-security.txt`
- `feature-policy`
- `file-stream-rotator`
- `file-type`
- `finale-rest`
- `fs-extra`
- `glob`
- `graceful-fs`
- `grunt`
- `grunt-contrib-compress`
- `grunt-replace-json`
- `hashids`
- `hbs`
- `helmet`
- `html-entities`
- `i18n`
- `js-yaml`
- `jsonwebtoken`
- `libxmljs2`
- `marsdb`
- `material-icons`
- `median`
- `morgan`
- `multer`
- `node-pre-gyp`
- `notevil`
- `on-finished`
- `otplib`
- `pdfkit`
- `portscanner`
- `prom-client`
- `pug`
- `replace`
- `sanitize-filename`
- `@types/config`
- `@types/cookie-parser`
- `@types/cors`
- `@types/cross-spawn`
- `@types/cypress`
- `@types/diff`
- `@types/download`
- `@types/errorhandler`
- `@types/exif`
- `@types/express`
- `@types/express-jwt`
- `@types/fs-extra`
- `@types/glob`
- `@types/graceful-fs`
- `@types/i18n`
- `@types/js-yaml`
- `@types/jsonwebtoken`
- `@types/jws`
- `@types/lodash`
- `@types/mocha`
- `@types/morgan`
- `@types/multer`
- `@types/node`
- `@types/on-finished`
- `@types/pdfkit`
- `@types/portscanner`
- `@types/pug`
- `@types/sanitize-html`
- `@types/semver`
- `@types/sequelize`
- `@types/serve-index`
- `@types/sinon`
- `@types/sinon-chai`
- `@types/socket.io`
- `@types/socket.io-client`
- `@types/supertest`
- `@types/swagger-ui-express`
- `@types/unzipper`
- `chai`
- `concurrently`
- `cypress`
- `eslint`
- `exif`
- `globals`
- `grunt-cli`
- `mocha`
- `neostandard`
- `nyc`
- `sinon`
- `sinon-chai`
- `socket.io-client`
- `supertest`
- `tsx`
- `typescript`
- `typescript-eslint`

---

## README contents

> The following content was extracted from the repository's README file.

# [Juice Shop Logo](https://raw.githubusercontent.com/juice-shop/juice-shop/master/frontend/src/assets/public/images/JuiceShop_Logo_100px.png) OWASP Juice Shop

[![OWASP Flagship](https://camo.githubusercontent.com/a4d9b6a13bd97dbe23c3f56d39423165de1f40fc3e850500be7e80e0e007e56b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6f776173702d666c61677368697025323070726f6a6563742d3438413634362e737667)](https://owasp.org/projects/#sec-flagships)
[![GitHub release](https://camo.githubusercontent.com/7426eabb0342adad0388a46003484973c3f0f96b0e66a5c94c0fae908368685d/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f72656c656173652f6a756963652d73686f702f6a756963652d73686f702e737667)](https://github.com/juice-shop/juice-shop/releases/latest)
[![Twitter Follow](https://camo.githubusercontent.com/b130c82fc62abf6a1c9ac71134b91be1b9c73f409f2bceb10906170e260e7645/68747470733a2f2f696d672e736869656c64732e696f2f747769747465722f666f6c6c6f772f6f776173705f6a7569636573686f702e7376673f7374796c653d736f6369616c266c6162656c3d466f6c6c6f77)](https://twitter.com/owasp_juiceshop)
[![Subreddit subscribers](https://camo.githubusercontent.com/c5542f15df742e62c98595f12a873acd890e285981d09e913702de138bd6e27e/68747470733a2f2f696d672e736869656c64732e696f2f7265646469742f7375627265646469742d73756273637269626572732f6f776173705f6a7569636573686f703f7374796c653d736f6369616c)](https://reddit.com/r/owasp_juiceshop)

[![CI/CD Pipeline](https://github.com/juice-shop/juice-shop/actions/workflows/ci.yml/badge.svg?branch=develop)](https://github.com/juice-shop/juice-shop/actions/workflows/ci.yml)
[![Release Pipeline](https://github.com/juice-shop/juice-shop/actions/workflows/release.yml/badge.svg)](https://github.com/juice-shop/juice-shop/actions/workflows/release.yml)
[![Coverage Status](https://camo.githubusercontent.com/36ac52383034300173b784da90ac32ea7f845be0df822642e1053f222affe150/68747470733a2f2f636f766572616c6c732e696f2f7265706f732f6769746875622f6a756963652d73686f702f6a756963652d73686f702f62616467652e7376673f6272616e63683d646576656c6f70)](https://coveralls.io/github/juice-shop/juice-shop?branch=develop)
[![Cypress tests](https://camo.githubusercontent.com/a7bee59aff087da48a860443c91b55b734a3665d5558f8be650a968dfa752d47/68747470733a2f2f696d672e736869656c64732e696f2f656e64706f696e743f75726c3d68747470733a2f2f64617368626f6172642e637970726573732e696f2f62616467652f73696d706c652f3368726b68752f646576656c6f70267374796c653d666c6174266c6f676f3d63797072657373)](https://dashboard.cypress.io/projects/3hrkhu/runs)
[![OpenSSF Best Practices](https://camo.githubusercontent.com/2e5de7e765300a9e24b31f30a4a96baafcd774633754cc66590671e27c6d81a3/68747470733a2f2f7777772e626573747072616374696365732e6465762f70726f6a656374732f3232332f6261646765)](https://www.bestpractices.dev/projects/223)
[![GitHub stars](https://camo.githubusercontent.com/b0f34811772cbd89409a8331e0dadcfa17912d9e2e853c2a60d7a2be9fa04aaf/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f6a756963652d73686f702f6a756963652d73686f702e7376673f6c6162656c3d476974487562253230254532253938253835267374796c653d666c6174)](https://camo.githubusercontent.com/b0f34811772cbd89409a8331e0dadcfa17912d9e2e853c2a60d7a2be9fa04aaf/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f6a756963652d73686f702f6a756963652d73686f702e7376673f6c6162656c3d476974487562253230254532253938253835267374796c653d666c6174)
[![Static Badge](https://camo.githubusercontent.com/da2f2650834e4fe0a66443c55f7a8162de97f14ca160a34eab7dba1139bc2372/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4f574153502d436f64655f6f665f436f6e647563742d626c7565)](/juice-shop/juice-shop/blob/master/CODE_OF_CONDUCT.md)

> [The most trustworthy online shop out there.](https://twitter.com/dschadow/status/706781693504589824)
> ([@dschadow](https://github.com/dschadow)) —
> [The best juice shop on the whole internet!](https://twitter.com/shehackspurple/status/907335357775085568)
> ([@shehackspurple](https://twitter.com/shehackspurple)) —
> [Actually the most bug-free vulnerable application in existence!](https://youtu.be/TXAztSpYpvE?t=26m35s)
> ([@vanderaj](https://twitter.com/vanderaj)) —
> [First you 😂😂then you 😢](https://twitter.com/kramse/status/1073168529405472768)
> ([@kramse](https://twitter.com/kramse)) —
> [But this doesn't have anything to do with juice.](https://twitter.com/coderPatros/status/1199268774626488320)
> ([@coderPatros' wife](https://twitter.com/coderPatros))

OWASP Juice Shop is probably the most modern and sophisticated insecure web application! It can be used in security
trainings, awareness demos, CTFs and as a guinea pig for security tools! Juice Shop encompasses vulnerabilities from the
entire
[OWASP Top Ten](https://owasp.org/www-project-top-ten) along with many other security flaws found in real-world
applications!

[![Juice Shop Screenshot Slideshow](/juice-shop/juice-shop/raw/master/screenshots/slideshow.gif)](/juice-shop/juice-shop/blob/master/screenshots/slideshow.gif)

[![Juice Shop Screenshot Slideshow](https://github.com/juice-shop/juice-shop/raw/master/screenshots/slideshow.gif)](https://github.com/juice-shop/juice-shop/blob/master/screenshots/slideshow.gif)

For a detailed introduction, full list of features and architecture overview please visit the official project page:
<https://owasp-juice.shop>

## Table of contents

* [Setup](#setup)
  + [From Sources](#from-sources)
  + [Packaged Distributions](#packaged-distributions)
  + [Docker Container](#docker-container)
  + [Vagrant](#vagrant)
* [Demo](#demo)
* [Documentation](#documentation)
  + [Node.js version compatibility](#nodejs-version-compatibility)
  + [Troubleshooting](#troubleshooting)
  + [Official companion guide](#official-companion-guide)
* [Contributing](#contributing)
* [References](#references)
* [Merchandise](#merchandise)
* [Donations](#donations)
* [Contributors](#contributors)
* [Licensing](#licensing)

## Setup

> You can find some less common installation variations as well as instructions to run Juice Shop on a variety of cloud computing providers in
> [the *Running OWASP Juice Shop* documentation](https://pwning.owasp-juice.shop/companion-guide/latest/part1/running.html).

> Some challenges require an AI/LLM provider to work properly. Check the
> [*Setting up external dependencies* documentation](https://pwning.owasp-juice.shop/companion-guide/snapshot/part1/running.html#_setting_up_external_dependencies)
> for instructions on configuring local or cloud-based AI providers.

### From Sources

[![GitHub repo size](https://camo.githubusercontent.com/e93c84b2c31f65074c323425665fa4a94603fa8952aebc747bbb24b135c24df2/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f7265706f2d73697a652f6a756963652d73686f702f6a756963652d73686f702e737667)](https://camo.githubusercontent.com/e93c84b2c31f65074c323425665fa4a94603fa8952aebc747bbb24b135c24df2/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f7265706f2d73697a652f6a756963652d73686f702f6a756963652d73686f702e737667)

1. Install [node.js](#nodejs-version-compatibility)
2. Run `git clone https://github.com/juice-shop/juice-shop.git --depth 1` (or
   clone [your own fork](https://github.com/juice-shop/juice-shop/fork)
   of the repository)
3. Go into the cloned folder with `cd juice-shop`
4. Run `npm install` (only has to be done before first start or when you change the source code)
5. Run `npm start`
6. Browse to <http://localhost:3000>

### Packaged Distributions

[![GitHub release](https://camo.githubusercontent.com/cfbaa52ba702fee9c27209a2d415dcc0b09a8da1473afdec3eeea6e36e623264/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f646f776e6c6f6164732f6a756963652d73686f702f6a756963652d73686f702f746f74616c2e737667)](https://github.com/juice-shop/juice-shop/releases/latest)
[![SourceForge](https://camo.githubusercontent.com/a0fece238311dc6063f314e7ae10e93345bcadc2325b09288c61536007c12e9a/68747470733a2f2f696d672e736869656c64732e696f2f736f75726365666f7267652f646d2f6a756963652d73686f703f6c6162656c3d736f75726365666f726765253230646f776e6c6f616473)](https://sourceforge.net/projects/juice-shop/)
[![SourceForge](https://camo.githubusercontent.com/1f30df1016a5c4d7e632e82c71dadf11523b5cae40b3d997d1fd2f9a68ca2fca/68747470733a2f2f696d672e736869656c64732e696f2f736f75726365666f7267652f64742f6a756963652d73686f703f6c6162656c3d736f75726365666f726765253230646f776e6c6f616473)](https://sourceforge.net/projects/juice-shop/)

1. Install a 64bit [node.js](#nodejs-version-compatibility) on your Windows, MacOS or Linux machine
2. Download `juice-shop-<version>_<node-version>_<os>_x64.zip` (or
   `.tgz`) attached to
   [latest release](https://github.com/juice-shop/juice-shop/releases/latest)
3. Unpack and `cd` into the unpacked folder
4. Run `npm start`
5. Browse to <http://localhost:3000>

> Each packaged distribution includes some binaries for `sqlite3` and
> `libxmljs2` bound to the OS and node.js version which `npm install` was
> executed on.

### Docker Container

[![Docker Pulls](https://camo.githubusercontent.com/afcfae17fbf0fca2fcc584bdde9674fd16444ed50d9d6281037e6f6ae6dc3fe1/68747470733a2f2f696d672e736869656c64732e696f2f646f636b65722f70756c6c732f626b696d6d696e6963682f6a756963652d73686f702e737667)](https://hub.docker.com/r/bkimminich/juice-shop)
[![Docker Stars](https://camo.githubusercontent.com/f38811fd7ef59904fffeaba4c7cf523fee7002c20281de609c6ec697190fae06/68747470733a2f2f696d672e736869656c64732e696f2f646f636b65722f73746172732f626b696d6d696e6963682f6a756963652d73686f702e737667)](https://camo.githubusercontent.com/f38811fd7ef59904fffeaba4c7cf523fee7002c20281de609c6ec697190fae06/68747470733a2f2f696d672e736869656c64732e696f2f646f636b65722f73746172732f626b696d6d696e6963682f6a756963652d73686f702e737667)
[![](https://camo.githubusercontent.com/430e534c375f29ae0709d88564f9d0f7cd9bce1dba8888d82f63ed055c4635dd/68747470733a2f2f696d616765732e6d6963726f6261646765722e636f6d2f6261646765732f696d6167652f626b696d6d696e6963682f6a756963652d73686f702e737667)](https://microbadger.com/images/bkimminich/juice-shop "Get your own image badge on microbadger.com")
[![](https://camo.githubusercontent.com/9ab9da0bc653fe0677dac168e128f422036a6d5de8ed0e942a6706d474c2f9e4/68747470733a2f2f696d616765732e6d6963726f6261646765722e636f6d2f6261646765732f76657273696f6e2f626b696d6d696e6963682f6a756963652d73686f702e737667)](https://microbadger.com/images/bkimminich/juice-shop "Get your own version badge on microbadger.com")

1. Install [Docker](https://www.docker.com)
2. Run `docker pull bkimminich/juice-shop`
3. Run `docker run --rm -p 127.0.0.1:3000:3000 bkimminich/juice-shop`
4. Browse to <http://localhost:3000> (on macOS and Windows browse to
   <http://192.168.99.100:3000> if you are using docker-machine instead of the native docker installation)

### Vagrant

1. Install [Vagrant](https://www.vagrantup.com/downloads.html) and
   [Virtualbox](https://www.virtualbox.org/wiki/Downloads)
2. Run `git clone https://github.com/juice-shop/juice-shop.git` (or
   clone [your own fork](https://github.com/juice-shop/juice-shop/fork)
   of the repository)
3. Run `cd vagrant && vagrant up`
4. Browse to [192.168.56.110](http://192.168.56.110)

## Demo

Feel free to have a look at the latest version of OWASP Juice Shop:
<http://demo.owasp-juice.shop>

> This is a deployment-test and sneak-peek instance only! You are **not
> supposed** to use this instance for your own hacking endeavours! No
> guaranteed uptime! Guaranteed stern looks if you break it!

## Documentation

### Node.js version compatibility

[![GitHub package.json dynamic](https://camo.githubusercontent.com/56377c1a053faae550393ba2cb60bc3cf802def3f3304430bccc28a6475835ec/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f7061636b6167652d6a736f6e2f6370752f6a756963652d73686f702f6a756963652d73686f70)](https://camo.githubusercontent.com/56377c1a053faae550393ba2cb60bc3cf802def3f3304430bccc28a6475835ec/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f7061636b6167652d6a736f6e2f6370752f6a756963652d73686f702f6a756963652d73686f70)
[![GitHub package.json dynamic](https://camo.githubusercontent.com/7f902048c103c3a59f0eac2a659794dad8be660ca2a2aad09844bd1fb84e9d70/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f7061636b6167652d6a736f6e2f6f732f6a756963652d73686f702f6a756963652d73686f70)](https://camo.githubusercontent.com/7f902048c103c3a59f0eac2a659794dad8be660ca2a2aad09844bd1fb84e9d70/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f7061636b6167652d6a736f6e2f6f732f6a756963652d73686f702f6a756963652d73686f70)

OWASP Juice Shop officially supports the following versions of
[node.js](http://nodejs.org) in line with the official
[node.js LTS schedule](https://github.com/nodejs/LTS) as close as possible. Docker images and packaged distributions are
offered accordingly.

| node.js | Supported | Tested | [Packaged Distributions](#packaged-distributions) | [Docker images](#docker-container) from `master` | [Docker images](#docker-container) from `develop` |
| --- | --- | --- | --- | --- | --- |
| 26.x | ❌ | ❌ |  |  |  |
| 25.x | ( ✔️ ) | ❌ |  |  |  |
| 24.x | ✔️ | ✔️ | Windows (`x64`), MacOS (`x64`), Linux (`x64`) | `latest` (`linux/amd64`, `linux/arm64`) |  |
| 23.x | ( ✔️ ) | ❌ |  |  |  |
| 22.x | ✔️ | ✔️ | Windows (`x64`), MacOS (`x64`), Linux (`x64`) |  | `snapshot` (`linux/amd64`, `linux/arm64`) |
| <22.x | ❌ | ❌ |  |  |  |

Juice Shop is automatically tested *only on the latest `.x` minor version* of each node.js version mentioned above!
There is no guarantee that older minor node.js releases will always work with Juice Shop!
Please make sure you stay up to date with your chosen version.

### Troubleshooting

[![Gitter](https://camo.githubusercontent.com/fa0dcf30ee39c7f8aa7cbe1bb2527ff0a91ab9f1255efd9fda39ad4d59df1242/687474703a2f2f696d672e736869656c64732e696f2f62616467652f6769747465722d6a6f696e253230636861742d3164636537332e737667)](https://gitter.im/bkimminich/juice-shop)

If you need help with the application setup please check
[our existing *Troubleshooting*](https://pwning.owasp-juice.shop/companion-guide/latest/part4/troubleshooting.html)
guide. If this does not solve your issue please post your specific problem or question in the
[Gitter Chat](https://gitter.im/bkimminich/juice-shop) where community members can best try to help you.

🛑 **Please avoid opening GitHub issues for support requests or questions!**

### Official companion guide

[![Write Goodreads Review](https://camo.githubusercontent.com/22d4e3abb65751eff3a77f51c5591198d44c752ba95c2f66c22167b745cd2a52/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f676f6f6472656164732d77726974652532307265766965772d34393535373234302e737667)](https://www.goodreads.com/review/edit/49557240)

OWASP Juice Shop comes with an official companion guide eBook. It will give you a complete overview of all
vulnerabilities found in the application including hints how to spot and exploit them. In the appendix you will even
find complete step-by-step solutions to every challenge. Extensive documentation of
[custom re-branding](https://pwning.owasp-juice.shop/companion-guide/latest/part4/customization.html),
[CTF-support](https://pwning.owasp-juice.shop/companion-guide/latest/part4/ctf.html),
[trainer's guide](https://pwning.owasp-juice.shop/companion-guide/latest/part4/trainers.html)
and much more is also included.

[Pwning OWASP Juice Shop](https://leanpub.com/juice-shop) is published under
[CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)
and is available **for free** in PDF, Kindle and ePub format on LeanPub. You can also
[browse the full content online](https://pwning.owasp-juice.shop)!

[![Pwning OWASP Juice Shop cover](https://raw.githubusercontent.com/juice-shop/pwning-juice-shop/master/docs/modules/ROOT/assets/images/cover.jpg)](https://leanpub.com/juice-shop)
[![Pwning OWASP Juice Shop back cover](https://raw.githubusercontent.com/juice-shop/pwning-juice-shop/master/docs/modules/ROOT/assets/images/introduction/back.jpg)](https://leanpub.com/juice-shop)

## Contributing

[![GitHub contributors](https://camo.githubusercontent.com/cd9b761593be1acc02a67f4ce18c4fc61029cc29ed150b51f1d523f55e5f3d3e/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f636f6e7472696275746f72732f6a756963652d73686f702f6a756963652d73686f702e737667)](https://github.com/juice-shop/juice-shop/graphs/contributors)
[![JavaScript Style Guide](https://camo.githubusercontent.com/d429b06ef11476d7ddad760f59fa8030052e35275444e21f1d4ad52fe9daf207/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f64652532307374796c652d7374616e646172642d627269676874677265656e2e737667)](http://standardjs.com/)
[![Crowdin](https://camo.githubusercontent.com/735d9ef5ed635c9060df821f93b6024b23ca8932b0af639ea840c337aceb94a0/68747470733a2f2f64333232637174353834626f346f2e636c6f756466726f6e742e6e65742f6f776173702d6a756963652d73686f702f6c6f63616c697a65642e737667)](https://crowdin.com/project/owasp-juice-shop)
[![GitHub issues by-label](https://camo.githubusercontent.com/4559ef654fead1f6ad83d5b68da7cbd7e2c7b459d9723c7077488586fd7668a9/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732f6a756963652d73686f702f6a756963652d73686f702f68656c7025323077616e7465642e737667)](https://camo.githubusercontent.com/4559ef654fead1f6ad83d5b68da7cbd7e2c7b459d9723c7077488586fd7668a9/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732f6a756963652d73686f702f6a756963652d73686f702f68656c7025323077616e7465642e737667)
[![GitHub issues by-label](https://camo.githubusercontent.com/206317980388c202d744195cb2487aa582a966fd999290a6f7192b1aea879654/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732f6a756963652d73686f702f6a756963652d73686f702f676f6f64253230666972737425323069737375652e737667)](https://camo.githubusercontent.com/206317980388c202d744195cb2487aa582a966fd999290a6f7192b1aea879654/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732f6a756963652d73686f702f6a756963652d73686f702f676f6f64253230666972737425323069737375652e737667)

We are always happy to get new contributors on board! Please check
[CONTRIBUTING.md](/juice-shop/juice-shop/blob/master/CONTRIBUTING.md) to learn how to
[contribute to our codebase](/juice-shop/juice-shop/blob/master/CONTRIBUTING.md#code-contributions) or the
[translation into different languages](/juice-shop/juice-shop/blob/master/CONTRIBUTING.md#i18n-contributions)!

## References

Did you write a blog post, magazine article or do a podcast about or mentioning OWASP Juice Shop? Or maybe you held or
joined a conference talk or meetup session, a hacking workshop or public training where this project was mentioned?

Add it to our ever-growing list of [REFERENCES.md](/juice-shop/juice-shop/blob/master/REFERENCES.md) by forking and opening a Pull Request!

## Merchandise

* On [Spreadshirt.com](http://shop.spreadshirt.com/juiceshop) and
  [Spreadshirt.de](http://shop.spreadshirt.de/juiceshop) you can get some swag (Shirts, Hoodies, Mugs) with the official
  OWASP Juice Shop logo
* On
  [StickerYou.com](https://www.stickeryou.com/products/owasp-juice-shop/794)
  you can get variants of the OWASP Juice Shop logo as single stickers to decorate your laptop with. They can also print
  magnets, iron-ons, sticker sheets and temporary tattoos.

## Donations

[![](https://camo.githubusercontent.com/3cb35407c95a900bc631b8ee05eafe8f23969e38f2d1b152434d427e5867fafc/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f737570706f72742d6f776173702532306a7569636525323073686f702d626c7565)](https://owasp.org/donate/?reponame=www-project-juice-shop&title=OWASP+Juice+Shop)

The OWASP Foundation gratefully accepts donations via Stripe. Projects such as Juice Shop can then request reimbursement
for expenses from the Foundation. If you'd like to express your support of the Juice Shop project, please make sure to
tick the "Publicly list me as a supporter of OWASP Juice Shop" checkbox on the donation form. You can find our more
about donations and how they are used here:

<https://pwning.owasp-juice.shop/companion-guide/latest/part3/donations.html>

## Contributors

The OWASP Juice Shop Project Leaders are:

* [Björn Kimminich](https://github.com/bkimminich) aka `bkimminich` [![Keybase PGP](https://camo.githubusercontent.com/87f67e1a0df45ffe82ca1c833f3fd792c442157d3e255d455d0a95c76c47e9f6/68747470733a2f2f696d672e736869656c64732e696f2f6b6579626173652f7067702f626b696d6d696e696368)](https://keybase.io/bkimminich)
* [Jannik Hollenbach](https://github.com/J12934) aka `J12934`

For a list of all contributors to the OWASP Juice Shop please visit our
[HALL\_OF\_FAME.md](/juice-shop/juice-shop/blob/master/HALL_OF_FAME.md).

## Licensing

[![license](https://camo.githubusercontent.com/11461f0de59380c9e9a375fc1f78cc92b98fc2f084a1da2735c384f62946f214/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f6a756963652d73686f702f6a756963652d73686f702e737667)](/juice-shop/juice-shop/blob/master/LICENSE)

This program is free software: you can redistribute it and/or modify it under the terms of the [MIT license](/juice-shop/juice-shop/blob/master/LICENSE).
OWASP Juice Shop and any contributions are Copyright © by Bjoern Kimminich & the OWASP Juice Shop contributors
2014-2026.

[![Juice Shop Logo](https://raw.githubusercontent.com/juice-shop/juice-shop/master/frontend/src/assets/public/images/JuiceShop_Logo_400px.png)](https://raw.githubusercontent.com/juice-shop/juice-shop/master/frontend/src/assets/public/images/JuiceShop_Logo_400px.png)

---

*This summary was auto-generated by [GitHub Repository Scraper](https://github.com/) from `https://github.com/juice-shop/juice-shop`.*

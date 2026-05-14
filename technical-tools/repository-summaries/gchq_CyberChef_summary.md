# gchq/CyberChef

## Repository overview

| Field | Details |
|-------|--------|
| **Source** | https://github.com/gchq/CyberChef |
| **Description** | No description provided. |
| **Topics** | `hashing`, `encoding`, `compression`, `encryption`, `parsing`, `data-analysis`, `data-manipulation` |

---

## Repository health

| Metric | Value |
|--------|-------|
| **Stars** | 34.8k |
| **Forks** | 3.9k |
| **Open issues** | 431 |
| **License** | Apache-2.0 license |
| **Last commit** | 2026-05-11T08:52:59.000Z |

---

## Language breakdown

| Language | Percentage |
|----------|-----------|
| JavaScript | 97.3% |
| HTML | 1.4% |
| CSS | 1.3% |

---

## Dependencies

### JavaScript (npm)

- `@alexaltea/capstone-js`
- `@astronautlabs/amf`
- `@blu3r4y/lzma`
- `@noble/hashes`
- `@wavesenterprise/crypto-gost-js`
- `@xmldom/xmldom`
- `argon2-browser`
- `arrive`
- `assert`
- `avsc`
- `bcryptjs`
- `bignumber.js`
- `blakejs`
- `bootstrap`
- `bootstrap-colorpicker`
- `bootstrap-material-design`
- `browserify-zlib`
- `bson`
- `buffer`
- `cbor`
- `chi-squared`
- `codepage`
- `crypto-api`
- `crypto-browserify`
- `crypto-js`
- `ctph.js`
- `d3`
- `d3-hexbin`
- `diff`
- `dompurify`
- `es6-promisify`
- `escodegen`
- `esprima`
- `events`
- `exif-parser`
- `fernet`
- `file-saver`
- `flat`
- `geodesy`
- `handlebars`
- `highlight.js`
- `ieee754`
- `jimp`
- `jq-web`
- `jquery`
- `js-sha3`
- `jsesc`
- `json5`
- `jsonata`
- `jsonpath-plus`
- `jsonwebtoken`
- `jsqr`
- `jsrsasign`
- `kbpgp`
- `libbzip2-wasm`
- `libyara-wasm`
- `lodash`
- `loglevel`
- `loglevel-message-prefix`
- `lz-string`
- `lz4js`
- `markdown-it`
- `moment`
- `moment-timezone`
- `ngeohash`
- `node-forge`
- `node-md6`
- `nodom`
- `notepack.io`
- `ntlm`
- `nwmatcher`
- `otpauth`
- `path`
- `popper.js`
- `process`
- `protobufjs`
- `punycode.js`
- `qr-image`
- `reflect-metadata`
- `rison`
- `scryptsy`
- `snackbarjs`
- `sortablejs`
- `split.js`
- `sql-formatter`
- `ssdeep.js`
- `stream-browserify`
- `tesseract.js`
- `ua-parser-js`
- `unorm`
- `url`
- `utf8`
- `uuid`
- `vkbeautify`
- `xpath`
- `xregexp`
- `zlibjs`
- `@babel/eslint-parser`
- `@babel/plugin-syntax-import-assertions`
- `@babel/plugin-transform-runtime`
- `@babel/preset-env`
- `@babel/runtime`
- `@codemirror/commands`
- `@codemirror/language`
- `@codemirror/search`
- `@codemirror/state`
- `@codemirror/view`
- `autoprefixer`
- `babel-loader`
- `base64-loader`
- `chromedriver`
- `cli-progress`
- `colors`
- `compression-webpack-plugin`
- `copy-webpack-plugin`
- `core-js`
- `cspell`
- `css-loader`
- `eslint`
- `eslint-plugin-jsdoc`
- `globals`
- `grunt`
- `grunt-chmod`
- `grunt-concurrent`
- `grunt-contrib-clean`
- `grunt-contrib-connect`
- `grunt-contrib-copy`
- `grunt-contrib-watch`
- `grunt-eslint`
- `grunt-exec`
- `grunt-webpack`
- `grunt-zip`
- `html-webpack-plugin`
- `imports-loader`
- `mini-css-extract-plugin`
- `modify-source-webpack-plugin`
- `nightwatch`
- `postcss`
- `postcss-css-variables`
- `postcss-import`
- `postcss-loader`
- `prompt`
- `sitemap`
- `terser`
- `webpack`
- `webpack-bundle-analyzer`
- `webpack-dev-server`
- `webpack-node-externals`
- `worker-loader`

---

## README contents

> The following content was extracted from the repository's README file.

# CyberChef

[![](https://github.com/gchq/CyberChef/workflows/Master%20Build,%20Test%20&%20Deploy/badge.svg)](https://github.com/gchq/CyberChef/actions?query=workflow%3A%22Master+Build%2C+Test+%26+Deploy%22)
[![npm](https://camo.githubusercontent.com/f8f9219a3f1ed03f26ea167831f6a3db0e1d93be5ced140b7bad03a6f8e2bdec/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f6379626572636865662e737667)](https://www.npmjs.com/package/cyberchef)
[![](https://camo.githubusercontent.com/b29de0acdfd19013f1f02689b15c933e4a6c145be9efa718288f88ba3280b1c5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d417061636865253230322e302d626c75652e737667)](https://github.com/gchq/CyberChef/blob/master/LICENSE)
[![Gitter](https://camo.githubusercontent.com/cab7ce8e21b79e7e2a4622f3161670f848552169d4dba0a089650b6843f737e2/68747470733a2f2f6261646765732e6769747465722e696d2f676368712f4379626572436865662e737667)](https://gitter.im/gchq/CyberChef?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

#### *The Cyber Swiss Army Knife*

CyberChef is a simple, intuitive web app for carrying out all manner of "cyber" operations within a web browser. These operations include simple encoding like XOR and Base64, more complex encryption like AES, DES and Blowfish, creating binary and hexdumps, compression and decompression of data, calculating hashes and checksums, IPv6 and X.509 parsing, changing character encodings, and much more.

The tool is designed to enable both technical and non-technical analysts to manipulate data in complex ways without having to deal with complex tools or algorithms. It was conceived, designed, built and incrementally improved by an analyst in their 10% innovation time over several years.

## Live demo

CyberChef is still under active development. As a result, it shouldn't be considered a finished product. There is still testing and bug fixing to do, new features to be added and additional documentation to write. Please contribute!

Cryptographic operations in CyberChef should not be relied upon to provide security in any situation. No guarantee is offered for their correctness.

[A live demo can be found here](https://gchq.github.io/CyberChef) - have fun!

## Running Locally with Docker

**Prerequisites**

* [Docker](https://www.docker.com/products/docker-desktop/)
  + Docker Desktop must be open and running on your machine

#### Option 1: Build the Docker Image Yourself

1. Build the docker image

```
docker build --tag cyberchef --ulimit nofile=10000 .
```

2. Run the docker container

```
docker run -it -p 8080:8080 cyberchef
```

3. Navigate to `http://localhost:8080` in your browser

#### Option 2: Use the pre-built Docker Image

If you prefer to skip the build process, you can use the pre-built image

```
docker run -it -p 8080:8080 ghcr.io/gchq/cyberchef:latest
```

Just like before, navigate to `http://localhost:8080` in your browser.

This image is built and published through our [GitHub Workflows](/gchq/CyberChef/blob/master/.github/workflows/releases.yml)

## How it works

There are four main areas in CyberChef:

1. The **input** box in the top right, where you can paste, type or drag the text or file you want to operate on.
2. The **output** box in the bottom right, where the outcome of your processing will be displayed.
3. The **operations** list on the far left, where you can find all the operations that CyberChef is capable of in categorised lists, or by searching.
4. The **recipe** area in the middle, where you can drag the operations that you want to use and specify arguments and options.

You can use as many operations as you like in simple or complex ways. Some examples are as follows:

* [Decode a Base64-encoded string](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)&input=VTI4Z2JHOXVaeUJoYm1RZ2RHaGhibXR6SUdadmNpQmhiR3dnZEdobElHWnBjMmd1)
* [Convert a date and time to a different time zone](https://gchq.github.io/CyberChef/#recipe=Translate_DateTime_Format('Standard%20date%20and%20time','DD/MM/YYYY%20HH:mm:ss','UTC','dddd%20Do%20MMMM%20YYYY%20HH:mm:ss%20Z%20z','Australia/Queensland')&input=MTUvMDYvMjAxNSAyMDo0NTowMA)
* [Parse a Teredo IPv6 address](https://gchq.github.io/CyberChef/#recipe=Parse_IPv6_address()&input=MjAwMTowMDAwOjQxMzY6ZTM3ODo4MDAwOjYzYmY6M2ZmZjpmZGQy)
* [Convert data from a hexdump, then decompress](https://gchq.github.io/CyberChef/#recipe=From_Hexdump()Gunzip()&input=MDAwMDAwMDAgIDFmIDhiIDA4IDAwIDEyIGJjIGYzIDU3IDAwIGZmIDBkIGM3IGMxIDA5IDAwIDIwICB8Li4uLi6881cu/y7HwS4uIHwKMDAwMDAwMTAgIDA4IDA1IGQwIDU1IGZlIDA0IDJkIGQzIDA0IDFmIGNhIDhjIDQ0IDIxIDViIGZmICB8Li7QVf4uLdMuLsouRCFb/3wKMDAwMDAwMjAgIDYwIGM3IGQ3IDAzIDE2IGJlIDQwIDFmIDc4IDRhIDNmIDA5IDg5IDBiIDlhIDdkICB8YMfXLi6%2BQC54Sj8uLi4ufXwKMDAwMDAwMzAgIDRlIGM4IDRlIDZkIDA1IDFlIDAxIDhiIDRjIDI0IDAwIDAwIDAwICAgICAgICAgICB8TshObS4uLi5MJC4uLnw)
* [Decrypt and disassemble shellcode](https://gchq.github.io/CyberChef/#recipe=RC4(%7B'option':'UTF8','string':'secret'%7D,'Hex','Hex')Disassemble_x86('64','Full%20x86%20architecture',16,0,true,true)&input=MjFkZGQyNTQwMTYwZWU2NWZlMDc3NzEwM2YyYTM5ZmJlNWJjYjZhYTBhYWJkNDE0ZjkwYzZjYWY1MzEyNzU0YWY3NzRiNzZiM2JiY2QxOTNjYjNkZGZkYmM1YTI2NTMzYTY4NmI1OWI4ZmVkNGQzODBkNDc0NDIwMWFlYzIwNDA1MDcxMzhlMmZlMmIzOTUwNDQ2ZGIzMWQyYmM2MjliZTRkM2YyZWIwMDQzYzI5M2Q3YTVkMjk2MmMwMGZlNmRhMzAwNzJkOGM1YTZiNGZlN2Q4NTlhMDQwZWVhZjI5OTczMzYzMDJmNWEwZWMxOQ)
* [Display multiple timestamps as full dates](https://gchq.github.io/CyberChef/#recipe=Fork('%5C%5Cn','%5C%5Cn',false)From_UNIX_Timestamp('Seconds%20(s)')&input=OTc4MzQ2ODAwCjEwMTI2NTEyMDAKMTA0NjY5NjQwMAoxMDgxMDg3MjAwCjExMTUzMDUyMDAKMTE0OTYwOTYwMA)
* [Carry out different operations on data of different types](https://gchq.github.io/CyberChef/#recipe=Fork('%5C%5Cn','%5C%5Cn',false)Conditional_Jump('1',false,'base64',10)To_Hex('Space')Return()Label('base64')To_Base64('A-Za-z0-9%2B/%3D')&input=U29tZSBkYXRhIHdpdGggYSAxIGluIGl0ClNvbWUgZGF0YSB3aXRoIGEgMiBpbiBpdA)
* [Use parts of the input as arguments to operations](https://gchq.github.io/CyberChef/#recipe=Register('key%3D(%5B%5C%5Cda-f%5D*)',true,false)Find_/_Replace(%7B'option':'Regex','string':'.*data%3D(.*)'%7D,'$1',true,false,true)RC4(%7B'option':'Hex','string':'$R0'%7D,'Hex','Latin1')&input=aHR0cDovL21hbHdhcmV6LmJpei9iZWFjb24ucGhwP2tleT0wZTkzMmE1YyZkYXRhPThkYjdkNWViZTM4NjYzYTU0ZWNiYjMzNGUzZGIxMQ)
* [Perform AES decryption, extracting the IV from the beginning of the cipher stream](https://gchq.github.io/CyberChef/#recipe=Register('(.%7B32%7D)',true,false)Drop_bytes(0,32,false)AES_Decrypt(%7B'option':'Hex','string':'1748e7179bd56570d51fa4ba287cc3e5'%7D,%7B'option':'Hex','string':'$R0'%7D,'CTR','Hex','Raw',%7B'option':'Hex','string':''%7D)&input=NTFlMjAxZDQ2MzY5OGVmNWY3MTdmNzFmNWI0NzEyYWYyMGJlNjc0YjNiZmY1M2QzODU0NjM5NmVlNjFkYWFjNDkwOGUzMTljYTNmY2Y3MDg5YmZiNmIzOGVhOTllNzgxZDI2ZTU3N2JhOWRkNmYzMTFhMzk0MjBiODk3OGU5MzAxNGIwNDJkNDQ3MjZjYWVkZjU0MzZlYWY2NTI0MjljMGRmOTRiNTIxNjc2YzdjMmNlODEyMDk3YzI3NzI3M2M3YzcyY2Q4OWFlYzhkOWZiNGEyNzU4NmNjZjZhYTBhZWUyMjRjMzRiYTNiZmRmN2FlYjFkZGQ0Nzc2MjJiOTFlNzJjOWU3MDlhYjYwZjhkYWY3MzFlYzBjYzg1Y2UwZjc0NmZmMTU1NGE1YTNlYzI5MWNhNDBmOWU2MjlhODcyNTkyZDk4OGZkZDgzNDUzNGFiYTc5YzFhZDE2NzY3NjlhN2MwMTBiZjA0NzM5ZWNkYjY1ZDk1MzAyMzcxZDYyOWQ5ZTM3ZTdiNGEzNjFkYTQ2OGYxZWQ1MzU4OTIyZDJlYTc1MmRkMTFjMzY2ZjMwMTdiMTRhYTAxMWQyYWYwM2M0NGY5NTU3OTA5OGExNWUzY2Y5YjQ0ODZmOGZmZTljMjM5ZjM0ZGU3MTUxZjZjYTY1MDBmZTRiODUwYzNmMWMwMmU4MDFjYWYzYTI0NDY0NjE0ZTQyODAxNjE1YjhmZmFhMDdhYzgyNTE0OTNmZmRhN2RlNWRkZjMzNjg4ODBjMmI5NWIwMzBmNDFmOGYxNTA2NmFkZDA3MWE2NmNmNjBlNWY0NmYzYTIzMGQzOTdiNjUyOTYzYTIxYTUzZg)
* [Automagically detect several layers of nested encoding](https://gchq.github.io/CyberChef/#recipe=Magic(3,false,false)&input=V1VhZ3dzaWFlNm1QOGdOdENDTFVGcENwQ0IyNlJtQkRvREQ4UGFjZEFtekF6QlZqa0syUXN0RlhhS2hwQzZpVVM3UkhxWHJKdEZpc29SU2dvSjR3aGptMWFybTg2NHFhTnE0UmNmVW1MSHJjc0FhWmM1VFhDWWlmTmRnUzgzZ0RlZWpHWDQ2Z2FpTXl1QlY2RXNrSHQxc2NnSjg4eDJ0TlNvdFFEd2JHWTFtbUNvYjJBUkdGdkNLWU5xaU45aXBNcTFaVTFtZ2tkYk51R2NiNzZhUnRZV2hDR1VjOGc5M1VKdWRoYjhodHNoZVpud1RwZ3FoeDgzU1ZKU1pYTVhVakpUMnptcEM3dVhXdHVtcW9rYmRTaTg4WXRrV0RBYzFUb291aDJvSDRENGRkbU5LSldVRHBNd21uZ1VtSzE0eHdtb21jY1BRRTloTTE3MkFQblNxd3hkS1ExNzJSa2NBc3lzbm1qNWdHdFJtVk5OaDJzMzU5d3I2bVMyUVJQ)

## Features

* Drag and drop
  + Operations can be dragged in and out of the recipe list, or reorganised.
  + Files up to 2GB can be dragged over the input box to load them directly into the browser.
* Auto Bake
  + Whenever you modify the input or the recipe, CyberChef will automatically "bake" for you and produce the output immediately.
  + This can be turned off and operated manually if it is affecting performance (if the input is very large, for instance).
* Automated encoding detection
  + CyberChef uses [a number of techniques](https://github.com/gchq/CyberChef/wiki/Automatic-detection-of-encoded-data-using-CyberChef-Magic) to attempt to automatically detect which encodings your data is under. If it finds a suitable operation that make sense of your data, it displays the 'magic' icon in the Output field which you can click to decode your data.
* Breakpoints
  + You can set breakpoints on any operation in your recipe to pause execution before running it.
  + You can also step through the recipe one operation at a time to see what the data looks like at each stage.
* Save and load recipes
  + If you come up with an awesome recipe that you know you’ll want to use again, just click "Save recipe" and add it to your local storage. It'll be waiting for you next time you visit CyberChef.
  + You can also copy the URL, which includes your recipe and input, to easily share it with others.
* Search
  + If you know the name of the operation you want or a word associated with it, start typing it into the search field and any matching operations will immediately be shown.
* Highlighting
  + When you highlight text in the input or output, the offset and length values will be displayed and, if possible, the corresponding data will be highlighted in the output or input respectively (example: [highlight the word 'question' in the input to see where it appears in the output](https://gchq.github.io/CyberChef/#recipe=XOR(%7B'option':'Hex','string':'3a'%7D,'Standard',false)To_Hexdump(16,false,false)&input=VGhlIGFuc3dlciB0byB0aGUgdWx0aW1hdGUgcXVlc3Rpb24gb2YgbGlmZSwgdGhlIFVuaXZlcnNlLCBhbmQgZXZlcnl0aGluZyBpcyA0Mi4)).
* Save to file and load from file
  + You can save the output to a file at any time or load a file by dragging and dropping it into the input field. Files up to around 2GB are supported (depending on your browser), however, some operations may take a very long time to run over this much data.
* CyberChef is entirely client-side
  + It should be noted that none of your recipe configuration or input (either text or files) is ever sent to the CyberChef web server - all processing is carried out within your browser, on your own computer.
  + Due to this feature, CyberChef can be downloaded and run locally. You can use the link in the top left corner of the app to download a full copy of CyberChef and drop it into a virtual machine, share it with other people, or host it in a closed network.

## Deep linking

By manipulating CyberChef's URL hash, you can change the initial settings with which the page opens.
The format is `https://gchq.github.io/CyberChef/#recipe=Operation()&input=...`

Supported arguments are `recipe`, `input` (encoded in Base64), and `theme`.

## Browser support

CyberChef is built to support

* Google Chrome 50+
* Mozilla Firefox 38+

## Node.js support

CyberChef is built to fully support Node.js `v24`. For more information, see the ["Node API" wiki page](https://github.com/gchq/CyberChef/wiki/Node-API)

## Contributing

Contributing a new operation to CyberChef is super easy! The quickstart script will walk you through the process. If you can write basic JavaScript, you can write a CyberChef operation.

An installation walkthrough, how-to guides for adding new operations and themes, descriptions of the repository structure, available data types and coding conventions can all be found in the ["Contributing" wiki page](https://github.com/gchq/CyberChef/wiki/Contributing).

* Push your changes to your fork.
* Submit a pull request. If you are doing this for the first time, you will be prompted to sign the [GCHQ Contributor Licence Agreement](https://cla-assistant.io/gchq/CyberChef) via the CLA assistant on the pull request. This will also ask whether you are happy for GCHQ to contact you about a token of thanks for your contribution, or about job opportunities at GCHQ.

## Licencing

CyberChef is released under the [Apache 2.0 Licence](https://www.apache.org/licenses/LICENSE-2.0) and is covered by [Crown Copyright](https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/).

---

*This summary was auto-generated by [GitHub Repository Scraper](https://github.com/) from `https://github.com/gchq/CyberChef`.*

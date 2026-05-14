# PostHog/posthog

## Repository overview

| Field | Details |
|-------|--------|
| **Source** | https://github.com/PostHog/posthog |
| **Description** | No description provided. |
| **Topics** | `react`, `javascript`, `python`, `typescript`, `analytics`, `web-analytics`, `feature-flags`, `data-warehouse`, `ab-testing`, `surveys`, `experiments`, `cdp`, `product-analytics`, `session-replay`, `ai-analytics` |

---

## Repository health

| Metric | Value |
|--------|-------|
| **Stars** | 34.5k |
| **Forks** | 2.7k |
| **Open issues** | 3k |
| **License** | View license |
| **Last commit** | 2026-05-14T18:43:13.000Z |

---

## Language breakdown

| Language | Percentage |
|----------|-----------|
| Python | 51.2% |
| TypeScript | 39.6% |
| Rust | 7.1% |
| JavaScript | 0.5% |
| Go | 0.5% |
| HTML | 0.3% |

---

## Dependencies

### Python (pyproject)

- `aioboto3`
- `aiohttp`
- `aiokafka`
- `anthropic`
- `antlr4-python3-runtime`
- `asyncstdlib`
- `beautifulsoup4`
- `boto3`
- `brotli`
- `celery`
- `celery-redbeat`
- `certifi`
- `clickhouse-connect`
- `clickhouse-driver`
- `clickhouse-pool`
- `circular-dict`
- `cryptography`
- `dagster`
- `dagster-cloud`
- `dagster-aws`
- `dagster-celery`
- `dagster-docker`
- `dagster-k8s`
- `dagster-pipes`
- `dagster-postgres`
- `dagster-slack`
- `dagster-webserver`
- `deltalake`
- `dj-database-url`
- `django`
- `django-axes`
- `django-cors-headers`
- `django-deprecate-fields`
- `django-extensions`
- `django-filter`
- `django-loginas`
- `django-prometheus`
- `django-redis`
- `django-structlog`
- `django-two-factor-auth`
- `djangorestframework`
- `djangorestframework-csv`
- `djangorestframework-dataclasses`
- `dlt`
- `dnspython`
- `drf-exceptions-hog`
- `drf-extensions`
- `drf-spectacular`
- `geoip2`
- `google-ads`
- `google-cloud-bigquery`
- `google-cloud-bigquery-storage`
- `google-cloud-iam`
- `google-genai`
- `grimp`
- `grpcio`
- `gspread`
- `hogql-parser`
- `humanize`
- `infi-clickhouse-orm`
- `jsonref`
- `kafka-python`
- `kombu`
- `langchain`
- `langchain-community`
- `langchain-core`
- `langchain-openai`
- `langchain-anthropic`
- `langgraph`
- `lxml`
- `lzstring`
- `markdown-it-py`
- `mcp`
- `mimesis`
- `mistralai`
- `more-itertools`
- `nanoid`
- `natsort`
- `nh3`
- `numpy`
- `openai`
- `openpyxl`
- `orjson`
- `pandas`
- `paramiko`
- `pillow`
- `protobuf`
- `posthoganalytics`
- `polars`
- `psycopg2-binary`
- `psycopg`
- `pyarrow`
- `pydantic`
- `pypdf`
- `pyod`
- `pyjwt`
- `pymssql`
- `pymysql`
- `pymongo`
- `pyroscope-io`
- `croniter`
- `python-dateutil`
- `python-docx`
- `python-snappy`
- `python3-saml`
- `pytz`
- `redis`
- `requests`
- `retry`
- `s3fs`
- `scikit-learn`
- `selenium`
- `semantic-version`
- `simple-salesforce`
- `slack-sdk`
- `snowflake-connector-python`
- `social-auth-app-django`
- `social-auth-core`
- `django-scim2`
- `sqlparse`
- `sshtunnel`
- `statshog`
- `stripe`
- `structlog`
- `temporalio`
- `tenacity`
- `tiktoken`
- `tldextract`
- `trafilatura`
- `types-cachetools`
- `css-inline`
- `click`
- `umap-learn`
- `tbb`
- `webdriver-manager`
- `whitenoise`
- `forbidden_modules`
- `products`
- `allow_indirect_imports`
- `ignore_imports`
- `products`
- `products`
- `products`
- `products`
- `products`
- `products`
- `products`
- `products`
- `products`
- `products`
- `products`
- `products`
- `products`

### JavaScript (npm)

- `concurrently`
- `fuse.js`
- `husky`
- `lint-staged`
- `uuid`
- `zod`
- `@parcel/packager-ts`
- `@parcel/transformer-typescript-types`
- `@types/uuid`
- `markdownlint-cli2`
- `oxfmt`
- `oxlint`
- `playwright`
- `stylelint`
- `stylelint-config-recess-order`
- `stylelint-config-standard-scss`
- `stylelint-order`
- `syncpack`
- `turbo`

---

## README contents

> The following content was extracted from the repository's README file.

[![posthoglogo](https://user-images.githubusercontent.com/65415371/205059737-c8a4f836-4889-4654-902e-f302b187b6a0.png)](https://user-images.githubusercontent.com/65415371/205059737-c8a4f836-4889-4654-902e-f302b187b6a0.png)

[![GitHub contributors](https://camo.githubusercontent.com/043d7deaf398bd6ec7888fe9a32d93925e891a20e10e8a3350d0d96e07e5203e/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f636f6e7472696275746f72732f706f7374686f672f706f7374686f67)](https://posthog.com/contributors)
[![PRs Welcome](https://camo.githubusercontent.com/2b429ff8971105c9cdce0abcda00a1dc3d8df4ed613afa5bd9e8369272be4ef4/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5052732d77656c636f6d652d627269676874677265656e2e7376673f7374796c653d736869656c6473)](http://makeapullrequest.com)
[![Docker Pulls](https://camo.githubusercontent.com/da86f646db081d1580fd53dc9b30b372391c14f0dddad8e0b4b62569d1df2d75/68747470733a2f2f696d672e736869656c64732e696f2f646f636b65722f70756c6c732f706f7374686f672f706f7374686f67)](https://camo.githubusercontent.com/da86f646db081d1580fd53dc9b30b372391c14f0dddad8e0b4b62569d1df2d75/68747470733a2f2f696d672e736869656c64732e696f2f646f636b65722f70756c6c732f706f7374686f672f706f7374686f67)
[![GitHub commit activity](https://camo.githubusercontent.com/8d59b2a329e0cfaa4e01506c4a827b729350476672e93dc40c091df11b39f607/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f636f6d6d69742d61637469766974792f6d2f706f7374686f672f706f7374686f67)](https://github.com/PostHog/posthog/commits/master) 
[![GitHub closed issues](https://camo.githubusercontent.com/a3d770057f38f572ead88cd3ccac6ca483d20079a5e2ab38c3c3957cc326f682/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732d636c6f7365642f706f7374686f672f706f7374686f67)](https://github.com/PostHog/posthog/issues?q=is%3Aissue%20state%3Aclosed)

[Docs](https://posthog.com/docs) - [Community](https://posthog.com/community) - [Roadmap](https://posthog.com/roadmap) - [Why PostHog?](https://posthog.com/why) - [Changelog](https://posthog.com/changelog) - [Bug reports](https://github.com/PostHog/posthog/issues/new?assignees=&labels=bug&template=bug_report.yml)

[![PostHog Demonstration](https://camo.githubusercontent.com/aa64ed41b69965cb82fe455b21dcbb3670dcac45587ba63f4a314606fd9348c0/68747470733a2f2f7265732e636c6f7564696e6172792e636f6d2f646d756b756b7770362f696d6167652f75706c6f61642f64656d6f5f7468756d625f36386430643864353664)](https://www.youtube.com/watch?v=1FZji2L-LmM)

## PostHog is an all-in-one, open source platform for building successful products

[PostHog](https://posthog.com/) provides every tool you need to build a successful product including:

* [Product Analytics](https://posthog.com/product-analytics): Autocapture or manually instrument event-based analytics to understand user behavior and analyze data with visualization or SQL.
* [Web Analytics](https://posthog.com/web-analytics): Monitor web traffic and user sessions with a GA-like dashboard. Easily monitor conversion, web vitals, and revenue.
* [Session Replays](https://posthog.com/session-replay): Watch real user sessions of interactions with your website or mobile app to diagnose issues and understand user behavior.
* [Feature Flags](https://posthog.com/feature-flags): Safely roll out features to select users or cohorts with feature flags.
* [Experiments](https://posthog.com/experiments): Test changes and measure their statistical impact on goal metrics. Set up experiments with no-code too.
* [Error Tracking](https://posthog.com/error-tracking): Track errors, get alerts, and resolve issues to improve your product.
* [Surveys](https://posthog.com/surveys): Ask anything with our collection of no-code survey templates, or build custom surveys with our survey builder.
* [Data warehouse](https://posthog.com/data-warehouse): Sync data from external tools like Stripe, Hubspot, your data warehouse, and more. Query it alongside your product data.
* [Data pipelines](https://posthog.com/cdp): Run custom filters and transformations on your incoming data. Send it to 25+ tools or any webhook in real time or batch export large amounts to your warehouse.
* [LLM analytics](https://posthog.com/docs/llm-analytics): Capture traces, generations, latency, and cost for your LLM-powered app.
* [Workflows](https://posthog.com/docs/workflows): Create workflows that automate actions or send messages to your users.

Best of all, all of this is free to use with a [generous monthly free tier](https://posthog.com/pricing) for each product. Get started by signing up for [PostHog Cloud US](https://us.posthog.com/signup) or [PostHog Cloud EU](https://eu.posthog.com/signup).

## Table of Contents

* [PostHog is an all-in-one, open source platform for building successful products](#posthog-is-an-all-in-one-open-source-platform-for-building-successful-products)
* [Table of Contents](#table-of-contents)
* [Getting started with PostHog](#getting-started-with-posthog)
  + [PostHog Cloud (Recommended)](#posthog-cloud-recommended)
  + [Self-hosting the open-source hobby deploy (Advanced)](#self-hosting-the-open-source-hobby-deploy-advanced)
* [Setting up PostHog](#setting-up-posthog)
* [Learning more about PostHog](#learning-more-about-posthog)
* [Contributing](#contributing)
* [Open-source vs. paid](#open-source-vs-paid)
* [We’re hiring!](#were-hiring)

## Getting started with PostHog

### PostHog Cloud (Recommended)

The fastest and most reliable way to get started with PostHog is signing up for free to [PostHog Cloud](https://us.posthog.com/signup) or [PostHog Cloud EU](https://eu.posthog.com/signup). Your first 1 million events, 5k recordings, 1M flag requests, 100k exceptions, and 1500 survey responses are free every month, after which you pay based on usage.

### Self-hosting the open-source hobby deploy (Advanced)

If you want to self-host PostHog, you can deploy a hobby instance in one line on Linux with Docker (recommended 4GB memory):

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/posthog/posthog/HEAD/bin/deploy-hobby)"
```

Open source deployments should scale to approximately 100k events per month, after which we recommend [migrating to a PostHog Cloud](https://posthog.com/docs/migrate/migrate-to-cloud).

We *do not* provide customer support or offer guarantees for open source deployments. See our [self-hosting docs](https://posthog.com/docs/self-host), [troubleshooting guide](https://posthog.com/docs/self-host/deploy/troubleshooting), and [disclaimer](https://posthog.com/docs/self-host/open-source/disclaimer) for more info.

## Setting up PostHog

Once you've got a PostHog instance, you can set it up by installing our [JavaScript web snippet](https://posthog.com/docs/getting-started/install?tab=snippet), one of [our SDKs](https://posthog.com/docs/getting-started/install?tab=sdks), or by [using our API](https://posthog.com/docs/getting-started/install?tab=api).

We have SDKs and libraries for popular languages and frameworks like:

| Frontend | Mobile | Backend |
| --- | --- | --- |
| [JavaScript](https://posthog.com/docs/libraries/js) | [React Native](https://posthog.com/docs/libraries/react-native) | [Python](https://posthog.com/docs/libraries/python) |
| [Next.js](https://posthog.com/docs/libraries/next-js) | [Android](https://posthog.com/docs/libraries/android) | [Node](https://posthog.com/docs/libraries/node) |
| [React](https://posthog.com/docs/libraries/react) | [iOS](https://posthog.com/docs/libraries/ios) | [PHP](https://posthog.com/docs/libraries/php) |
| [Vue](https://posthog.com/docs/libraries/vue-js) | [Flutter](https://posthog.com/docs/libraries/flutter) | [Ruby](https://posthog.com/docs/libraries/ruby) |

Beyond this, we have docs and guides for [Go](https://posthog.com/docs/libraries/go), [.NET/C#](https://posthog.com/docs/libraries/dotnet), [Django](https://posthog.com/docs/libraries/django), [Angular](https://posthog.com/docs/libraries/angular), [WordPress](https://posthog.com/docs/libraries/wordpress), [Webflow](https://posthog.com/docs/libraries/webflow), and more.

Once you've installed PostHog, see our [product docs](https://posthog.com/docs/product-os) for more information on how to set up [product analytics](https://posthog.com/docs/product-analytics/capture-events), [web analytics](https://posthog.com/docs/web-analytics/getting-started), [session replays](https://posthog.com/docs/session-replay/how-to-watch-recordings), [feature flags](https://posthog.com/docs/feature-flags/creating-feature-flags), [experiments](https://posthog.com/docs/experiments/creating-an-experiment), [error tracking](https://posthog.com/docs/error-tracking/installation#setting-up-exception-autocapture), [surveys](https://posthog.com/docs/surveys/installation), [data warehouse](https://posthog.com/docs/cdp/sources), and more.

## Learning more about PostHog

Our code isn't the only thing that's open source 😳. We also open source our [company handbook](https://posthog.com/handbook) which details our [strategy](https://posthog.com/handbook/why-does-posthog-exist), [ways of working](https://posthog.com/handbook/company/culture), and [processes](https://posthog.com/handbook/team-structure).

Curious about how to make the most of PostHog? We wrote a guide to [winning with PostHog](https://posthog.com/docs/new-to-posthog/getting-hogpilled) which walks you through the basics of [measuring activation](https://posthog.com/docs/new-to-posthog/activation), [tracking retention](https://posthog.com/docs/new-to-posthog/retention), and [capturing revenue](https://posthog.com/docs/new-to-posthog/revenue).

## Contributing

We <3 contributions big and small:

* Vote on features or get early access to beta functionality in our [roadmap](https://posthog.com/roadmap)
* Open a PR (see our instructions on [developing PostHog locally](https://posthog.com/handbook/engineering/developing-locally))
* Submit a [feature request](https://github.com/PostHog/posthog/issues/new?assignees=&labels=enhancement%2C+feature&template=feature_request.yml) or [bug report](https://github.com/PostHog/posthog/issues/new?assignees=&labels=bug&template=bug_report.yml)

For an overview of the codebase structure, see [monorepo layout](/PostHog/posthog/blob/master/docs/internal/monorepo-layout.md) and [products](/PostHog/posthog/blob/master/products/README.md).

## Open-source vs. paid

This repo is available under the [MIT expat license](https://github.com/PostHog/posthog/blob/master/LICENSE), except for the `ee` directory (which has its [license here](https://github.com/PostHog/posthog/blob/master/ee/LICENSE)) if applicable.

Need *absolutely 💯% FOSS*? Check out our [posthog-foss](https://github.com/PostHog/posthog-foss) repository, which is purged of all proprietary code and features.

The pricing for our paid plan is completely transparent and available on [our pricing page](https://posthog.com/pricing).

## We're hiring!

[![Hedgehog working on a Mission Control Center](https://camo.githubusercontent.com/b968ecbb1b3e0add48fb78210675aad1d025a818fefbd1f50801eb7eced2f2ae/68747470733a2f2f7265732e636c6f7564696e6172792e636f6d2f646d756b756b7770362f696d6167652f75706c6f61642f76312f706f7374686f672e636f6d2f7372632f636f6d706f6e656e74732f486f6d652f696d616765732f6d697373696f6e2d636f6e74726f6c2d686f67)](https://camo.githubusercontent.com/b968ecbb1b3e0add48fb78210675aad1d025a818fefbd1f50801eb7eced2f2ae/68747470733a2f2f7265732e636c6f7564696e6172792e636f6d2f646d756b756b7770362f696d6167652f75706c6f61642f76312f706f7374686f672e636f6d2f7372632f636f6d706f6e656e74732f486f6d652f696d616765732f6d697373696f6e2d636f6e74726f6c2d686f67)

Hey! If you're reading this, you've proven yourself as a dedicated README reader.

You might also make a great addition to our team. We're growing fast [and would love for you to join us](https://posthog.com/careers).

---

*This summary was auto-generated by [GitHub Repository Scraper](https://github.com/) from `https://github.com/PostHog/posthog`.*

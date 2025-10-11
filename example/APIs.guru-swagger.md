# APIs.guru
**Version:** 2.2.0

Wikipedia for Web APIs. Repository of API definitions in OpenAPI format.
**Warning**: If you want to be notified about changes in advance please join our [Slack channel](https://join.slack.com/t/mermade/shared_invite/zt-g78g7xir-MLE_CTCcXCdfJfG3CJe9qA).
Client sample: [[Demo]](https://apis.guru/simple-ui) [[Repo]](https://github.com/APIs-guru/simple-ui)


## Base URLs
  - https://api.apis.guru/v2

## Endpoints by Tag

### APIs
- **GET** `/list.json` — List all APIs
- **GET** `/metrics.json` — Get basic metrics
- **GET** `/providers.json` — List all providers
- **GET** `/specs/{provider}/{api}.json` — Retrieve one version of a particular API
- **GET** `/specs/{provider}/{service}/{api}.json` — Retrieve one version of a particular API with a serviceName.
- **GET** `/{provider}.json` — List all APIs for a particular provider
- **GET** `/{provider}/services.json` — List all serviceNames for a particular provider


## Endpoint Details

### Tag: APIs
================================================================================
ENDPOINT: [GET] /list.json
TAGS: APIs
SUMMARY: List all APIs
DESCRIPTION: List all APIs in the directory.
Returns links to the OpenAPI definitions for each API in the directory.
If API exist in multiple versions `preferred` one is explicitly marked.
Some basic info from the... (see full docs)
AUTH: None

REQUEST
  none

RESPONSES
  - 200 (application/json): OK
        (empty)

EXAMPLE (curl)
curl -X GET \
  "https://api.apis.guru/v2/list.json"
================================================================================
================================================================================
ENDPOINT: [GET] /metrics.json
TAGS: APIs
SUMMARY: Get basic metrics
DESCRIPTION: Some basic metrics for the entire directory.
Just stunning numbers to put on a front page and are intended purely for WoW effect :)

AUTH: None

REQUEST
  none

RESPONSES
  - 200 (application/json): OK
        - datasets: array<any> (optional) — Data used for charting etc
        - fixedPct: integer (optional) — Percentage of all APIs where auto fixes have been applied
        - fixes: integer (optional) — Total number of fixes applied across all APIs
        - invalid: integer (optional) — Number of newly invalid APIs
        - issues: integer (optional) — Open GitHub issues on our main repo
        - numAPIs: integer (required) — Number of unique APIs
        - numDrivers: integer (optional) — Number of methods of API retrieval
        - numEndpoints: integer (required) — Total number of endpoints inside all definitions
        - numProviders: integer (optional) — Number of API providers in directory
        - numSpecs: integer (required) — Number of API definitions including different versions of th...
        - stars: integer (optional) — GitHub stars for our main repo
        - thisWeek: object (2 fields) (optional) — Summary totals for the last 7 days
        - unofficial: integer (optional) — Number of unofficial APIs
        - unreachable: integer (optional) — Number of unreachable (4XX,5XX status) APIs

EXAMPLE (curl)
curl -X GET \
  "https://api.apis.guru/v2/metrics.json"
================================================================================
================================================================================
ENDPOINT: [GET] /providers.json
TAGS: APIs
SUMMARY: List all providers
DESCRIPTION: List all the providers in the directory

AUTH: None

REQUEST
  none

RESPONSES
  - 200 (application/json): OK
        - data: array<string> (optional)

EXAMPLE (curl)
curl -X GET \
  "https://api.apis.guru/v2/providers.json"
================================================================================
================================================================================
ENDPOINT: [GET] /specs/{provider}/{api}.json
TAGS: APIs
SUMMARY: Retrieve one version of a particular API
DESCRIPTION: Returns the API entry for one specific version of an API where there is no serviceName.
AUTH: None

REQUEST
  Path params:
  - provider (string, required)
  - api (string, required)

RESPONSES
  - 200 (application/json): OK
        - added: string (date-time) (required) — Timestamp when the API was first added to the directory
        - preferred: string (required) — Recommended version
        - versions: object (required) — List of supported versions of the API

EXAMPLE (curl)
curl -X GET \
  "https://api.apis.guru/v2/specs/apis.guru/2.1.0.json"
================================================================================
================================================================================
ENDPOINT: [GET] /specs/{provider}/{service}/{api}.json
TAGS: APIs
SUMMARY: Retrieve one version of a particular API with a serviceName.
DESCRIPTION: Returns the API entry for one specific version of an API where there is a serviceName.
AUTH: None

REQUEST
  Path params:
  - provider (string, required)
  - service (string, required)
  - api (string, required)

RESPONSES
  - 200 (application/json): OK
        - added: string (date-time) (required) — Timestamp when the API was first added to the directory
        - preferred: string (required) — Recommended version
        - versions: object (required) — List of supported versions of the API

EXAMPLE (curl)
curl -X GET \
  "https://api.apis.guru/v2/specs/apis.guru/graph/2.1.0.json"
================================================================================
================================================================================
ENDPOINT: [GET] /{provider}.json
TAGS: APIs
SUMMARY: List all APIs for a particular provider
DESCRIPTION: List all APIs in the directory for a particular providerName
Returns links to the individual API entry for each API.

AUTH: None

REQUEST
  Path params:
  - provider (string, required)

RESPONSES
  - 200 (application/json): OK
        (empty)

EXAMPLE (curl)
curl -X GET \
  "https://api.apis.guru/v2/apis.guru.json"
================================================================================
================================================================================
ENDPOINT: [GET] /{provider}/services.json
TAGS: APIs
SUMMARY: List all serviceNames for a particular provider
DESCRIPTION: List all serviceNames in the directory for a particular providerName

AUTH: None

REQUEST
  Path params:
  - provider (string, required)

RESPONSES
  - 200 (application/json): OK
        - data: array<string> (optional)

EXAMPLE (curl)
curl -X GET \
  "https://api.apis.guru/v2/apis.guru/services.json"
================================================================================


================================================================================
## COMPONENTS APPENDIX
================================================================================

Shared schemas referenced throughout the API:

### API
Type: object
Description: Meta information about API

- added: string (date-time) (required) — Timestamp when the API was first added to the directory
- preferred: string (required) — Recommended version
- versions: object (required) — List of supported versions of the API

### APIs
Type: object
Description: List of API details.
It is a JSON object with API IDs(`<provider>[:<service>]`) as keys.


(empty)

### ApiVersion
Type: object

- added: string (date-time) (required) — Timestamp when the version was added
- externalDocs: object (optional) — Copy of `externalDocs` section from OpenAPI definition
- info: object (required) — Copy of `info` section from OpenAPI definition
- link: string (url) (optional) — Link to the individual API entry for this API
- openapiVer: string (required) — The value of the `openapi` or `swagger` property of the sour...
- swaggerUrl: string (url) (required) — URL to OpenAPI definition in JSON format
- swaggerYamlUrl: string (url) (required) — URL to OpenAPI definition in YAML format
- updated: string (date-time) (required) — Timestamp when the version was updated

### Metrics
Type: object
Description: List of basic metrics

- datasets: array<any> (optional) — Data used for charting etc
- fixedPct: integer (optional) — Percentage of all APIs where auto fixes have been applied
- fixes: integer (optional) — Total number of fixes applied across all APIs
- invalid: integer (optional) — Number of newly invalid APIs
- issues: integer (optional) — Open GitHub issues on our main repo
- numAPIs: integer (required) — Number of unique APIs
- numDrivers: integer (optional) — Number of methods of API retrieval
- numEndpoints: integer (required) — Total number of endpoints inside all definitions
- numProviders: integer (optional) — Number of API providers in directory
- numSpecs: integer (required) — Number of API definitions including different versions of th...
- stars: integer (optional) — GitHub stars for our main repo
- thisWeek: object (2 fields) (optional) — Summary totals for the last 7 days
- unofficial: integer (optional) — Number of unofficial APIs
- unreachable: integer (optional) — Number of unreachable (4XX,5XX status) APIs

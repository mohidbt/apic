# OpenAI API
**Version:** 2.3.0

The OpenAI REST API. Please see https://platform.openai.com/docs/api-reference for more details.

## Base URLs
  - https://api.openai.com/v1

## Authentication
  - ApiKeyAuth: HTTP BEARER

## Endpoints by Tag

### Assistants
- **DELETE** `/assistants/{assistant_id}` — Delete assistant
- **DELETE** `/threads/{thread_id}` — Delete thread
- **DELETE** `/threads/{thread_id}/messages/{message_id}` — Delete message
- **GET** `/assistants` — List assistants
- **GET** `/assistants/{assistant_id}` — Retrieve assistant
- **GET** `/threads/{thread_id}` — Retrieve thread
- **GET** `/threads/{thread_id}/messages` — List messages
- **GET** `/threads/{thread_id}/messages/{message_id}` — Retrieve message
- **GET** `/threads/{thread_id}/runs` — List runs
- **GET** `/threads/{thread_id}/runs/{run_id}` — Retrieve run
- **GET** `/threads/{thread_id}/runs/{run_id}/steps` — List run steps
- **GET** `/threads/{thread_id}/runs/{run_id}/steps/{step_id}` — Retrieve run step
- **POST** `/assistants` — Create assistant
- **POST** `/assistants/{assistant_id}` — Modify assistant
- **POST** `/threads` — Create thread
- **POST** `/threads/runs` — Create thread and run
- **POST** `/threads/{thread_id}` — Modify thread
- **POST** `/threads/{thread_id}/messages` — Create message
- **POST** `/threads/{thread_id}/messages/{message_id}` — Modify message
- **POST** `/threads/{thread_id}/runs` — Create run
- **POST** `/threads/{thread_id}/runs/{run_id}` — Modify run
- **POST** `/threads/{thread_id}/runs/{run_id}/cancel` — Cancel a run
- **POST** `/threads/{thread_id}/runs/{run_id}/submit_tool_outputs` — Submit tool outputs to run

### Audio
- **POST** `/audio/speech` — Create speech
- **POST** `/audio/transcriptions` — Create transcription
- **POST** `/audio/translations` — Create translation

### Audit Logs
- **GET** `/organization/audit_logs` — List audit logs

### Batch
- **GET** `/batches` — List batch
- **GET** `/batches/{batch_id}` — Retrieve batch
- **POST** `/batches` — Create batch
- **POST** `/batches/{batch_id}/cancel` — Cancel batch

### Certificates
- **DELETE** `/organization/certificates/{certificate_id}` — Delete certificate
- **GET** `/organization/certificates` — List organization certificates
- **GET** `/organization/certificates/{certificate_id}` — Get certificate
- **GET** `/organization/projects/{project_id}/certificates` — List project certificates
- **POST** `/organization/certificates` — Upload certificate
- **POST** `/organization/certificates/activate` — Activate certificates for organization
- **POST** `/organization/certificates/deactivate` — Deactivate certificates for organization
- **POST** `/organization/certificates/{certificate_id}` — Modify certificate
- **POST** `/organization/projects/{project_id}/certificates/activate` — Activate certificates for project
- **POST** `/organization/projects/{project_id}/certificates/deactivate` — Deactivate certificates for project

### Chat
- **DELETE** `/chat/completions/{completion_id}` — Delete chat completion
- **GET** `/chat/completions` — List Chat Completions
- **GET** `/chat/completions/{completion_id}` — Get chat completion
- **GET** `/chat/completions/{completion_id}/messages` — Get chat messages
- **POST** `/chat/completions` — Create chat completion
- **POST** `/chat/completions/{completion_id}` — Update chat completion

### Completions
- **POST** `/completions` — Create completion

### Conversations
- **DELETE** `/conversations/{conversation_id}` — Delete a conversation
- **DELETE** `/conversations/{conversation_id}/items/{item_id}` — Delete an item
- **GET** `/conversations/{conversation_id}` — Retrieve a conversation
- **GET** `/conversations/{conversation_id}/items` — List items
- **GET** `/conversations/{conversation_id}/items/{item_id}` — Retrieve an item
- **POST** `/conversations` — Create a conversation
- **POST** `/conversations/{conversation_id}` — Update a conversation
- **POST** `/conversations/{conversation_id}/items` — Create items

### Embeddings
- **POST** `/embeddings` — Create embeddings

### Evals
- **DELETE** `/evals/{eval_id}` — Delete an eval
- **DELETE** `/evals/{eval_id}/runs/{run_id}` — Delete eval run
- **GET** `/evals` — List evals
- **GET** `/evals/{eval_id}` — Get an eval
- **GET** `/evals/{eval_id}/runs` — Get eval runs
- **GET** `/evals/{eval_id}/runs/{run_id}` — Get an eval run
- **GET** `/evals/{eval_id}/runs/{run_id}/output_items` — Get eval run output items
- **GET** `/evals/{eval_id}/runs/{run_id}/output_items/{output_item_id}` — Get an output item of an eval run
- **POST** `/evals` — Create eval
- **POST** `/evals/{eval_id}` — Update an eval
- **POST** `/evals/{eval_id}/runs` — Create eval run
- **POST** `/evals/{eval_id}/runs/{run_id}` — Cancel eval run

### Files
- **DELETE** `/files/{file_id}` — Delete file
- **GET** `/files` — List files
- **GET** `/files/{file_id}` — Retrieve file
- **GET** `/files/{file_id}/content` — Retrieve file content
- **POST** `/files` — Upload file

### Fine-tuning
- **DELETE** `/fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions/{permission_id}` — Delete checkpoint permission
- **GET** `/fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions` — List checkpoint permissions
- **GET** `/fine_tuning/jobs` — List fine-tuning jobs
- **GET** `/fine_tuning/jobs/{fine_tuning_job_id}` — Retrieve fine-tuning job
- **GET** `/fine_tuning/jobs/{fine_tuning_job_id}/checkpoints` — List fine-tuning checkpoints
- **GET** `/fine_tuning/jobs/{fine_tuning_job_id}/events` — List fine-tuning events
- **POST** `/fine_tuning/alpha/graders/run` — Run grader
- **POST** `/fine_tuning/alpha/graders/validate` — Validate grader
- **POST** `/fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions` — Create checkpoint permissions
- **POST** `/fine_tuning/jobs` — Create fine-tuning job
- **POST** `/fine_tuning/jobs/{fine_tuning_job_id}/cancel` — Cancel fine-tuning
- **POST** `/fine_tuning/jobs/{fine_tuning_job_id}/pause` — Pause fine-tuning
- **POST** `/fine_tuning/jobs/{fine_tuning_job_id}/resume` — Resume fine-tuning

### Images
- **POST** `/images/edits` — Create image edit
- **POST** `/images/generations` — Create image
- **POST** `/images/variations` — Create image variation

### Invites
- **DELETE** `/organization/invites/{invite_id}` — Delete invite
- **GET** `/organization/invites` — List invites
- **GET** `/organization/invites/{invite_id}` — Retrieve invite
- **POST** `/organization/invites` — Create invite

### Models
- **DELETE** `/models/{model}` — Delete a fine-tuned model
- **GET** `/models` — List models
- **GET** `/models/{model}` — Retrieve model

### Moderations
- **POST** `/moderations` — Create moderation

### Projects
- **DELETE** `/organization/projects/{project_id}/api_keys/{key_id}` — Delete project API key
- **DELETE** `/organization/projects/{project_id}/service_accounts/{service_account_id}` — Delete project service account
- **DELETE** `/organization/projects/{project_id}/users/{user_id}` — Delete project user
- **GET** `/organization/projects` — List projects
- **GET** `/organization/projects/{project_id}` — Retrieve project
- **GET** `/organization/projects/{project_id}/api_keys` — List project API keys
- **GET** `/organization/projects/{project_id}/api_keys/{key_id}` — Retrieve project API key
- **GET** `/organization/projects/{project_id}/rate_limits` — List project rate limits
- **GET** `/organization/projects/{project_id}/service_accounts` — List project service accounts
- **GET** `/organization/projects/{project_id}/service_accounts/{service_account_id}` — Retrieve project service account
- **GET** `/organization/projects/{project_id}/users` — List project users
- **GET** `/organization/projects/{project_id}/users/{user_id}` — Retrieve project user
- **POST** `/organization/projects` — Create project
- **POST** `/organization/projects/{project_id}` — Modify project
- **POST** `/organization/projects/{project_id}/archive` — Archive project
- **POST** `/organization/projects/{project_id}/rate_limits/{rate_limit_id}` — Modify project rate limit
- **POST** `/organization/projects/{project_id}/service_accounts` — Create project service account
- **POST** `/organization/projects/{project_id}/users` — Create project user
- **POST** `/organization/projects/{project_id}/users/{user_id}` — Modify project user

### Realtime
- **POST** `/realtime/calls` — Create call
- **POST** `/realtime/calls/{call_id}/accept` — Accept call
- **POST** `/realtime/calls/{call_id}/hangup` — Hang up call
- **POST** `/realtime/calls/{call_id}/refer` — Refer call
- **POST** `/realtime/calls/{call_id}/reject` — Reject call
- **POST** `/realtime/client_secrets` — Create client secret
- **POST** `/realtime/sessions` — Create session
- **POST** `/realtime/transcription_sessions` — Create transcription session

### Responses
- **DELETE** `/responses/{response_id}` — Delete a model response
- **GET** `/responses/{response_id}` — Get a model response
- **GET** `/responses/{response_id}/input_items` — List input items
- **POST** `/responses` — Create a model response
- **POST** `/responses/{response_id}/cancel` — Cancel a response

### Untagged
- **DELETE** `/chatkit/threads/{thread_id}` — Delete ChatKit thread
- **DELETE** `/containers/{container_id}` — Delete a container
- **DELETE** `/containers/{container_id}/files/{file_id}` — Delete a container file
- **DELETE** `/organization/admin_api_keys/{key_id}` — Delete admin API key
- **GET** `/chatkit/threads` — List ChatKit threads
- **GET** `/chatkit/threads/{thread_id}` — Retrieve ChatKit thread
- **GET** `/chatkit/threads/{thread_id}/items` — List ChatKit thread items
- **GET** `/containers` — List containers
- **GET** `/containers/{container_id}` — Retrieve container
- **GET** `/containers/{container_id}/files` — List container files
- **GET** `/containers/{container_id}/files/{file_id}` — Retrieve container file
- **GET** `/containers/{container_id}/files/{file_id}/content` — Retrieve container file content
- **GET** `/organization/admin_api_keys` — List all organization and project API keys.
- **GET** `/organization/admin_api_keys/{key_id}` — Retrieve admin API key
- **POST** `/chatkit/files` — Upload file to ChatKit
- **POST** `/chatkit/sessions` — Create ChatKit session
- **POST** `/chatkit/sessions/{session_id}/cancel` — Cancel chat session
- **POST** `/containers` — Create container
- **POST** `/containers/{container_id}/files` — Create container file
- **POST** `/organization/admin_api_keys` — Create admin API key

### Uploads
- **POST** `/uploads` — Create upload
- **POST** `/uploads/{upload_id}/cancel` — Cancel upload
- **POST** `/uploads/{upload_id}/complete` — Complete upload
- **POST** `/uploads/{upload_id}/parts` — Add upload part

### Usage
- **GET** `/organization/costs` — Costs
- **GET** `/organization/usage/audio_speeches` — Audio speeches
- **GET** `/organization/usage/audio_transcriptions` — Audio transcriptions
- **GET** `/organization/usage/code_interpreter_sessions` — Code interpreter sessions
- **GET** `/organization/usage/completions` — Completions
- **GET** `/organization/usage/embeddings` — Embeddings
- **GET** `/organization/usage/images` — Images
- **GET** `/organization/usage/moderations` — Moderations
- **GET** `/organization/usage/vector_stores` — Vector stores

### Users
- **DELETE** `/organization/users/{user_id}` — Delete user
- **GET** `/organization/users` — List users
- **GET** `/organization/users/{user_id}` — Retrieve user
- **POST** `/organization/users/{user_id}` — Modify user

### Vector stores
- **DELETE** `/vector_stores/{vector_store_id}` — Delete vector store
- **DELETE** `/vector_stores/{vector_store_id}/files/{file_id}` — Delete vector store file
- **GET** `/vector_stores` — List vector stores
- **GET** `/vector_stores/{vector_store_id}` — Retrieve vector store
- **GET** `/vector_stores/{vector_store_id}/file_batches/{batch_id}` — Retrieve vector store file batch
- **GET** `/vector_stores/{vector_store_id}/file_batches/{batch_id}/files` — List vector store files in a batch
- **GET** `/vector_stores/{vector_store_id}/files` — List vector store files
- **GET** `/vector_stores/{vector_store_id}/files/{file_id}` — Retrieve vector store file
- **GET** `/vector_stores/{vector_store_id}/files/{file_id}/content` — Retrieve vector store file content
- **POST** `/vector_stores` — Create vector store
- **POST** `/vector_stores/{vector_store_id}` — Modify vector store
- **POST** `/vector_stores/{vector_store_id}/file_batches` — Create vector store file batch
- **POST** `/vector_stores/{vector_store_id}/file_batches/{batch_id}/cancel` — Cancel vector store file batch
- **POST** `/vector_stores/{vector_store_id}/files` — Create vector store file
- **POST** `/vector_stores/{vector_store_id}/files/{file_id}` — Update vector store file attributes
- **POST** `/vector_stores/{vector_store_id}/search` — Search vector store

### Videos
- **DELETE** `/videos/{video_id}` — Delete video
- **GET** `/videos` — List videos
- **GET** `/videos/{video_id}` — Retrieve video
- **GET** `/videos/{video_id}/content` — Retrieve video content
- **POST** `/videos` — Create video
- **POST** `/videos/{video_id}/remix` — Remix video


## Endpoint Details

### Tag: Assistants
================================================================================
ENDPOINT: [DELETE] /assistants/{assistant_id}
TAGS: Assistants
SUMMARY: Delete assistant
DESCRIPTION: Delete an assistant.
AUTH: BEARER token

REQUEST
  Path params:
  - assistant_id (string, required)

RESPONSES
  - 200 (application/json): OK
        - id: string (required)
        - deleted: boolean (required)
        - object: string (enum: assistant.deleted) (required)

EXAMPLE (curl)
curl -X DELETE \
  "https://api.openai.com/v1/assistants/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [DELETE] /threads/{thread_id}
TAGS: Assistants
SUMMARY: Delete thread
DESCRIPTION: Delete a thread.
AUTH: BEARER token

REQUEST
  Path params:
  - thread_id (string, required)

RESPONSES
  - 200 (application/json): OK
        - id: string (required)
        - deleted: boolean (required)
        - object: string (enum: thread.deleted) (required)

EXAMPLE (curl)
curl -X DELETE \
  "https://api.openai.com/v1/threads/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [DELETE] /threads/{thread_id}/messages/{message_id}
TAGS: Assistants
SUMMARY: Delete message
DESCRIPTION: Deletes a message.
AUTH: BEARER token

REQUEST
  Path params:
  - thread_id (string, required)
  - message_id (string, required)

RESPONSES
  - 200 (application/json): OK
        - id: string (required)
        - deleted: boolean (required)
        - object: string (enum: thread.message.deleted) (required)

EXAMPLE (curl)
curl -X DELETE \
  "https://api.openai.com/v1/threads/123/messages/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /assistants
TAGS: Assistants
SUMMARY: List assistants
DESCRIPTION: Returns a list of assistants.
AUTH: BEARER token

REQUEST
  Query params:
  - limit (integer, optional)
  - order (string (enum: asc, desc), optional)
  - after (string, optional)
  - before (string, optional)

RESPONSES
  - 200 (application/json): OK
        - object: string (required)
        - data: array<object (13 fields)> (required)
        - first_id: string (required)
        - last_id: string (required)
        - has_more: boolean (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/assistants?limit=example&order=example&after=example&before=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /assistants/{assistant_id}
TAGS: Assistants
SUMMARY: Retrieve assistant
DESCRIPTION: Retrieves an assistant.
AUTH: BEARER token

REQUEST
  Path params:
  - assistant_id (string, required)

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The identifier, which can be referenced in API endpoints.
        - object: string (enum: assistant) (required) — The object type, which is always `assistant`.
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the assistant was c...
        - name: object (required)
        - description: object (required)
        - model: string (required) — ID of the model to use. You can use the [List models](https:...
        - instructions: object (required)
        - tools: array<object> (required) — A list of tool enabled on the assistant. There can be a maxi...
        - tool_resources: object (optional)
        - metadata: object (required)
        - temperature: object (optional)
        - top_p: object (optional)
        - response_format: object (optional)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/assistants/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /threads/{thread_id}
TAGS: Assistants
SUMMARY: Retrieve thread
DESCRIPTION: Retrieves a thread.
AUTH: BEARER token

REQUEST
  Path params:
  - thread_id (string, required)

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The identifier, which can be referenced in API endpoints.
        - object: string (enum: thread) (required) — The object type, which is always `thread`.
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the thread was crea...
        - tool_resources: object (required)
        - metadata: object (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/threads/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /threads/{thread_id}/messages
TAGS: Assistants
SUMMARY: List messages
DESCRIPTION: Returns a list of messages for a given thread.
AUTH: BEARER token

REQUEST
  Path params:
  - thread_id (string, required)
  Query params:
  - limit (integer, optional)
  - order (string (enum: asc, desc), optional)
  - after (string, optional)
  - before (string, optional)
  - run_id (string, optional)

RESPONSES
  - 200 (application/json): OK
        - object: string (required)
        - data: array<object (14 fields)> (required)
        - first_id: string (required)
        - last_id: string (required)
        - has_more: boolean (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/threads/123/messages?limit=example&order=example&after=example&before=example&run_id=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /threads/{thread_id}/messages/{message_id}
TAGS: Assistants
SUMMARY: Retrieve message
DESCRIPTION: Retrieve a message.
AUTH: BEARER token

REQUEST
  Path params:
  - thread_id (string, required)
  - message_id (string, required)

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The identifier, which can be referenced in API endpoints.
        - object: string (enum: thread.message) (required) — The object type, which is always `thread.message`.
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the message was cre...
        - thread_id: string (required) — The [thread](https://platform.openai.com/docs/api-reference/...
        - status: string (enum: in_progress, incomplete, completed) (required) — The status of the message, which can be either `in_progress`...
        - incomplete_details: object (required)
        - completed_at: object (required)
        - incomplete_at: object (required)
        - role: string (enum: user, assistant) (required) — The entity that produced the message. One of `user` or `assi...
        - content: array<object> (required) — The content of the message in array of text and/or images.
        - assistant_id: object (required)
        - run_id: object (required)
        - attachments: object (required)
        - metadata: object (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/threads/123/messages/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /threads/{thread_id}/runs
TAGS: Assistants
SUMMARY: List runs
DESCRIPTION: Returns a list of runs belonging to a thread.
AUTH: BEARER token

REQUEST
  Path params:
  - thread_id (string, required)
  Query params:
  - limit (integer, optional)
  - order (string (enum: asc, desc), optional)
  - after (string, optional)
  - before (string, optional)

RESPONSES
  - 200 (application/json): OK
        - object: string (required)
        - data: array<object (27 fields)> (required)
        - first_id: string (required)
        - last_id: string (required)
        - has_more: boolean (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/threads/123/runs?limit=example&order=example&after=example&before=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /threads/{thread_id}/runs/{run_id}
TAGS: Assistants
SUMMARY: Retrieve run
DESCRIPTION: Retrieves a run.
AUTH: BEARER token

REQUEST
  Path params:
  - thread_id (string, required)
  - run_id (string, required)

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The identifier, which can be referenced in API endpoints.
        - object: string (enum: thread.run) (required) — The object type, which is always `thread.run`.
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the run was created...
        - thread_id: string (required) — The ID of the [thread](https://platform.openai.com/docs/api-...
        - assistant_id: string (required) — The ID of the [assistant](https://platform.openai.com/docs/a...
        - status: string (enum: queued, in_progress, requires_action, cancelling, cancelled...) (required) — The status of the run, which can be either `queued`, `in_pro...
        - required_action: object (2 fields) (required) — Details on the action required to continue the run. Will be ...
        - last_error: object (2 fields) (required) — The last error associated with this run. Will be `null` if t...
        - expires_at: integer (required) — The Unix timestamp (in seconds) for when the run will expire...
        - started_at: integer (required) — The Unix timestamp (in seconds) for when the run was started...
        - cancelled_at: integer (required) — The Unix timestamp (in seconds) for when the run was cancell...
        - failed_at: integer (required) — The Unix timestamp (in seconds) for when the run failed.
        - completed_at: integer (required) — The Unix timestamp (in seconds) for when the run was complet...
        - incomplete_details: object (1 fields) (required) — Details on why the run is incomplete. Will be `null` if the ...
        - model: string (required) — The model that the [assistant](https://platform.openai.com/d...
        - instructions: string (required) — The instructions that the [assistant](https://platform.opena...
        - tools: array<object> (required) — The list of tools that the [assistant](https://platform.open...
        - metadata: object (required)
        - usage: object (required)
        - temperature: number (optional) — The sampling temperature used for this run. If not set, defa...
        - top_p: number (optional) — The nucleus sampling value used for this run. If not set, de...
        - max_prompt_tokens: integer (required) — The maximum number of prompt tokens specified to have been u...
        - max_completion_tokens: integer (required) — The maximum number of completion tokens specified to have be...
        - truncation_strategy: object (required)
        - tool_choice: object (required)
        - parallel_tool_calls: boolean (required) — Whether to enable [parallel function calling](https://platfo...
        - response_format: object (required) — Specifies the format that the model must output. Compatible ...

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/threads/123/runs/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /threads/{thread_id}/runs/{run_id}/steps
TAGS: Assistants
SUMMARY: List run steps
DESCRIPTION: Returns a list of run steps belonging to a run.
AUTH: BEARER token

REQUEST
  Path params:
  - thread_id (string, required)
  - run_id (string, required)
  Query params:
  - limit (integer, optional)
  - order (string (enum: asc, desc), optional)
  - after (string, optional)
  - before (string, optional)
  - include[] (array<string (enum: step_details.tool_calls[*].file_search.results[*].content)>, optional)

RESPONSES
  - 200 (application/json): OK
        - object: string (required)
        - data: array<object (16 fields)> (required)
        - first_id: string (required)
        - last_id: string (required)
        - has_more: boolean (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/threads/123/runs/123/steps?limit=example&order=example&after=example&before=example&include[]=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /threads/{thread_id}/runs/{run_id}/steps/{step_id}
TAGS: Assistants
SUMMARY: Retrieve run step
DESCRIPTION: Retrieves a run step.
AUTH: BEARER token

REQUEST
  Path params:
  - thread_id (string, required)
  - run_id (string, required)
  - step_id (string, required)
  Query params:
  - include[] (array<string (enum: step_details.tool_calls[*].file_search.results[*].content)>, optional)

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The identifier of the run step, which can be referenced in A...
        - object: string (enum: thread.run.step) (required) — The object type, which is always `thread.run.step`.
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the run step was cr...
        - assistant_id: string (required) — The ID of the [assistant](https://platform.openai.com/docs/a...
        - thread_id: string (required) — The ID of the [thread](https://platform.openai.com/docs/api-...
        - run_id: string (required) — The ID of the [run](https://platform.openai.com/docs/api-ref...
        - type: string (enum: message_creation, tool_calls) (required) — The type of run step, which can be either `message_creation`...
        - status: string (enum: in_progress, cancelled, failed, completed, expired) (required) — The status of the run step, which can be either `in_progress...
        - step_details: object (required) — The details of the run step.
        - last_error: object (required)
        - expired_at: object (required)
        - cancelled_at: object (required)
        - failed_at: object (required)
        - completed_at: object (required)
        - metadata: object (required)
        - usage: object (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/threads/123/runs/123/steps/123?include[]=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [POST] /assistants
TAGS: Assistants
SUMMARY: Create assistant
DESCRIPTION: Create an assistant with a model and instructions.
AUTH: BEARER token

REQUEST
  Body:
  Content-Type: application/json
    - model: object (required) — ID of the model to use. You can use the [List models](https:...
    - name: object (optional)
    - description: object (optional)
    - instructions: object (optional)
    - reasoning_effort: object (optional)
    - tools: array<object> (optional) — A list of tool enabled on the assistant. There can be a maxi...
    - tool_resources: object (optional)
    - metadata: object (optional)
    - temperature: object (optional)
    - top_p: object (optional)
    - response_format: object (optional)

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The identifier, which can be referenced in API endpoints.
        - object: string (enum: assistant) (required) — The object type, which is always `assistant`.
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the assistant was c...
        - name: object (required)
        - description: object (required)
        - model: string (required) — ID of the model to use. You can use the [List models](https:...
        - instructions: object (required)
        - tools: array<object> (required) — A list of tool enabled on the assistant. There can be a maxi...
        - tool_resources: object (optional)
        - metadata: object (required)
        - temperature: object (optional)
        - top_p: object (optional)
        - response_format: object (optional)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/assistants" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /assistants/{assistant_id}
TAGS: Assistants
SUMMARY: Modify assistant
DESCRIPTION: Modifies an assistant.
AUTH: BEARER token

REQUEST
  Path params:
  - assistant_id (string, required)
  Body:
  Content-Type: application/json
    - model: object (optional) — ID of the model to use. You can use the [List models](https:...
    - reasoning_effort: object (optional)
    - name: object (optional)
    - description: object (optional)
    - instructions: object (optional)
    - tools: array<object> (optional) — A list of tool enabled on the assistant. There can be a maxi...
    - tool_resources: object (optional)
    - metadata: object (optional)
    - temperature: object (optional)
    - top_p: object (optional)
    - response_format: object (optional)

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The identifier, which can be referenced in API endpoints.
        - object: string (enum: assistant) (required) — The object type, which is always `assistant`.
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the assistant was c...
        - name: object (required)
        - description: object (required)
        - model: string (required) — ID of the model to use. You can use the [List models](https:...
        - instructions: object (required)
        - tools: array<object> (required) — A list of tool enabled on the assistant. There can be a maxi...
        - tool_resources: object (optional)
        - metadata: object (required)
        - temperature: object (optional)
        - top_p: object (optional)
        - response_format: object (optional)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/assistants/123" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /threads
TAGS: Assistants
SUMMARY: Create thread
DESCRIPTION: Create a thread.
AUTH: BEARER token

REQUEST
  Body:
  Content-Type: application/json
    - messages: array<object (4 fields)> (optional) — A list of [messages](https://platform.openai.com/docs/api-re...
    - tool_resources: object (optional)
    - metadata: object (optional)

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The identifier, which can be referenced in API endpoints.
        - object: string (enum: thread) (required) — The object type, which is always `thread`.
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the thread was crea...
        - tool_resources: object (required)
        - metadata: object (required)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/threads" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /threads/runs
TAGS: Assistants
SUMMARY: Create thread and run
DESCRIPTION: Create a thread and run it in one request.
AUTH: BEARER token

REQUEST
  Body:
  Content-Type: application/json
    - assistant_id: string (required) — The ID of the [assistant](https://platform.openai.com/docs/a...
    - thread: object (3 fields) (optional) — Options to create a new thread. If no thread is provided whe...
    - model: object (optional) — The ID of the [Model](https://platform.openai.com/docs/api-r...
    - instructions: string (optional) — Override the default system message of the assistant. This i...
    - tools: array<object> (optional) — Override the tools the assistant can use for this run. This ...
    - tool_resources: object (2 fields) (optional) — A set of resources that are used by the assistant's tools. T...
    - metadata: object (optional)
    - temperature: number (optional) — What sampling temperature to use, between 0 and 2. Higher va...
    - top_p: number (optional) — An alternative to sampling with temperature, called nucleus ...
    - stream: boolean (optional) — If `true`, returns a stream of events that happen during the...
    - max_prompt_tokens: integer (optional) — The maximum number of prompt tokens that may be used over th...
    - max_completion_tokens: integer (optional) — The maximum number of completion tokens that may be used ove...
    - truncation_strategy: object (optional)
    - tool_choice: object (optional)
    - parallel_tool_calls: boolean (optional) — Whether to enable [parallel function calling](https://platfo...
    - response_format: object (optional) — Specifies the format that the model must output. Compatible ...

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The identifier, which can be referenced in API endpoints.
        - object: string (enum: thread.run) (required) — The object type, which is always `thread.run`.
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the run was created...
        - thread_id: string (required) — The ID of the [thread](https://platform.openai.com/docs/api-...
        - assistant_id: string (required) — The ID of the [assistant](https://platform.openai.com/docs/a...
        - status: string (enum: queued, in_progress, requires_action, cancelling, cancelled...) (required) — The status of the run, which can be either `queued`, `in_pro...
        - required_action: object (2 fields) (required) — Details on the action required to continue the run. Will be ...
        - last_error: object (2 fields) (required) — The last error associated with this run. Will be `null` if t...
        - expires_at: integer (required) — The Unix timestamp (in seconds) for when the run will expire...
        - started_at: integer (required) — The Unix timestamp (in seconds) for when the run was started...
        - cancelled_at: integer (required) — The Unix timestamp (in seconds) for when the run was cancell...
        - failed_at: integer (required) — The Unix timestamp (in seconds) for when the run failed.
        - completed_at: integer (required) — The Unix timestamp (in seconds) for when the run was complet...
        - incomplete_details: object (1 fields) (required) — Details on why the run is incomplete. Will be `null` if the ...
        - model: string (required) — The model that the [assistant](https://platform.openai.com/d...
        - instructions: string (required) — The instructions that the [assistant](https://platform.opena...
        - tools: array<object> (required) — The list of tools that the [assistant](https://platform.open...
        - metadata: object (required)
        - usage: object (required)
        - temperature: number (optional) — The sampling temperature used for this run. If not set, defa...
        - top_p: number (optional) — The nucleus sampling value used for this run. If not set, de...
        - max_prompt_tokens: integer (required) — The maximum number of prompt tokens specified to have been u...
        - max_completion_tokens: integer (required) — The maximum number of completion tokens specified to have be...
        - truncation_strategy: object (required)
        - tool_choice: object (required)
        - parallel_tool_calls: boolean (required) — Whether to enable [parallel function calling](https://platfo...
        - response_format: object (required) — Specifies the format that the model must output. Compatible ...

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/threads/runs" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /threads/{thread_id}
TAGS: Assistants
SUMMARY: Modify thread
DESCRIPTION: Modifies a thread.
AUTH: BEARER token

REQUEST
  Path params:
  - thread_id (string, required)
  Body:
  Content-Type: application/json
    - tool_resources: object (optional)
    - metadata: object (optional)

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The identifier, which can be referenced in API endpoints.
        - object: string (enum: thread) (required) — The object type, which is always `thread`.
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the thread was crea...
        - tool_resources: object (required)
        - metadata: object (required)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/threads/123" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /threads/{thread_id}/messages
TAGS: Assistants
SUMMARY: Create message
DESCRIPTION: Create a message.
AUTH: BEARER token

REQUEST
  Path params:
  - thread_id (string, required)
  Body:
  Content-Type: application/json
    - role: string (enum: user, assistant) (required) — The role of the entity that is creating the message. Allowed...
    - content: object (required)
    - attachments: object (optional)
    - metadata: object (optional)

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The identifier, which can be referenced in API endpoints.
        - object: string (enum: thread.message) (required) — The object type, which is always `thread.message`.
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the message was cre...
        - thread_id: string (required) — The [thread](https://platform.openai.com/docs/api-reference/...
        - status: string (enum: in_progress, incomplete, completed) (required) — The status of the message, which can be either `in_progress`...
        - incomplete_details: object (required)
        - completed_at: object (required)
        - incomplete_at: object (required)
        - role: string (enum: user, assistant) (required) — The entity that produced the message. One of `user` or `assi...
        - content: array<object> (required) — The content of the message in array of text and/or images.
        - assistant_id: object (required)
        - run_id: object (required)
        - attachments: object (required)
        - metadata: object (required)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/threads/123/messages" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /threads/{thread_id}/messages/{message_id}
TAGS: Assistants
SUMMARY: Modify message
DESCRIPTION: Modifies a message.
AUTH: BEARER token

REQUEST
  Path params:
  - thread_id (string, required)
  - message_id (string, required)
  Body:
  Content-Type: application/json
    - metadata: object (optional)

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The identifier, which can be referenced in API endpoints.
        - object: string (enum: thread.message) (required) — The object type, which is always `thread.message`.
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the message was cre...
        - thread_id: string (required) — The [thread](https://platform.openai.com/docs/api-reference/...
        - status: string (enum: in_progress, incomplete, completed) (required) — The status of the message, which can be either `in_progress`...
        - incomplete_details: object (required)
        - completed_at: object (required)
        - incomplete_at: object (required)
        - role: string (enum: user, assistant) (required) — The entity that produced the message. One of `user` or `assi...
        - content: array<object> (required) — The content of the message in array of text and/or images.
        - assistant_id: object (required)
        - run_id: object (required)
        - attachments: object (required)
        - metadata: object (required)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/threads/123/messages/123" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /threads/{thread_id}/runs
TAGS: Assistants
SUMMARY: Create run
DESCRIPTION: Create a run.
AUTH: BEARER token

REQUEST
  Path params:
  - thread_id (string, required)
  Query params:
  - include[] (array<string (enum: step_details.tool_calls[*].file_search.results[*].content)>, optional)
  Body:
  Content-Type: application/json
    - assistant_id: string (required) — The ID of the [assistant](https://platform.openai.com/docs/a...
    - model: object (optional) — The ID of the [Model](https://platform.openai.com/docs/api-r...
    - reasoning_effort: object (optional)
    - instructions: string (optional) — Overrides the [instructions](https://platform.openai.com/doc...
    - additional_instructions: string (optional) — Appends additional instructions at the end of the instructio...
    - additional_messages: array<object (4 fields)> (optional) — Adds additional messages to the thread before creating the r...
    - tools: array<object> (optional) — Override the tools the assistant can use for this run. This ...
    - metadata: object (optional)
    - temperature: number (optional) — What sampling temperature to use, between 0 and 2. Higher va...
    - top_p: number (optional) — An alternative to sampling with temperature, called nucleus ...
    - stream: boolean (optional) — If `true`, returns a stream of events that happen during the...
    - max_prompt_tokens: integer (optional) — The maximum number of prompt tokens that may be used over th...
    - max_completion_tokens: integer (optional) — The maximum number of completion tokens that may be used ove...
    - truncation_strategy: object (optional)
    - tool_choice: object (optional)
    - parallel_tool_calls: boolean (optional) — Whether to enable [parallel function calling](https://platfo...
    - response_format: object (optional) — Specifies the format that the model must output. Compatible ...

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The identifier, which can be referenced in API endpoints.
        - object: string (enum: thread.run) (required) — The object type, which is always `thread.run`.
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the run was created...
        - thread_id: string (required) — The ID of the [thread](https://platform.openai.com/docs/api-...
        - assistant_id: string (required) — The ID of the [assistant](https://platform.openai.com/docs/a...
        - status: string (enum: queued, in_progress, requires_action, cancelling, cancelled...) (required) — The status of the run, which can be either `queued`, `in_pro...
        - required_action: object (2 fields) (required) — Details on the action required to continue the run. Will be ...
        - last_error: object (2 fields) (required) — The last error associated with this run. Will be `null` if t...
        - expires_at: integer (required) — The Unix timestamp (in seconds) for when the run will expire...
        - started_at: integer (required) — The Unix timestamp (in seconds) for when the run was started...
        - cancelled_at: integer (required) — The Unix timestamp (in seconds) for when the run was cancell...
        - failed_at: integer (required) — The Unix timestamp (in seconds) for when the run failed.
        - completed_at: integer (required) — The Unix timestamp (in seconds) for when the run was complet...
        - incomplete_details: object (1 fields) (required) — Details on why the run is incomplete. Will be `null` if the ...
        - model: string (required) — The model that the [assistant](https://platform.openai.com/d...
        - instructions: string (required) — The instructions that the [assistant](https://platform.opena...
        - tools: array<object> (required) — The list of tools that the [assistant](https://platform.open...
        - metadata: object (required)
        - usage: object (required)
        - temperature: number (optional) — The sampling temperature used for this run. If not set, defa...
        - top_p: number (optional) — The nucleus sampling value used for this run. If not set, de...
        - max_prompt_tokens: integer (required) — The maximum number of prompt tokens specified to have been u...
        - max_completion_tokens: integer (required) — The maximum number of completion tokens specified to have be...
        - truncation_strategy: object (required)
        - tool_choice: object (required)
        - parallel_tool_calls: boolean (required) — Whether to enable [parallel function calling](https://platfo...
        - response_format: object (required) — Specifies the format that the model must output. Compatible ...

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/threads/123/runs?include[]=example" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /threads/{thread_id}/runs/{run_id}
TAGS: Assistants
SUMMARY: Modify run
DESCRIPTION: Modifies a run.
AUTH: BEARER token

REQUEST
  Path params:
  - thread_id (string, required)
  - run_id (string, required)
  Body:
  Content-Type: application/json
    - metadata: object (optional)

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The identifier, which can be referenced in API endpoints.
        - object: string (enum: thread.run) (required) — The object type, which is always `thread.run`.
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the run was created...
        - thread_id: string (required) — The ID of the [thread](https://platform.openai.com/docs/api-...
        - assistant_id: string (required) — The ID of the [assistant](https://platform.openai.com/docs/a...
        - status: string (enum: queued, in_progress, requires_action, cancelling, cancelled...) (required) — The status of the run, which can be either `queued`, `in_pro...
        - required_action: object (2 fields) (required) — Details on the action required to continue the run. Will be ...
        - last_error: object (2 fields) (required) — The last error associated with this run. Will be `null` if t...
        - expires_at: integer (required) — The Unix timestamp (in seconds) for when the run will expire...
        - started_at: integer (required) — The Unix timestamp (in seconds) for when the run was started...
        - cancelled_at: integer (required) — The Unix timestamp (in seconds) for when the run was cancell...
        - failed_at: integer (required) — The Unix timestamp (in seconds) for when the run failed.
        - completed_at: integer (required) — The Unix timestamp (in seconds) for when the run was complet...
        - incomplete_details: object (1 fields) (required) — Details on why the run is incomplete. Will be `null` if the ...
        - model: string (required) — The model that the [assistant](https://platform.openai.com/d...
        - instructions: string (required) — The instructions that the [assistant](https://platform.opena...
        - tools: array<object> (required) — The list of tools that the [assistant](https://platform.open...
        - metadata: object (required)
        - usage: object (required)
        - temperature: number (optional) — The sampling temperature used for this run. If not set, defa...
        - top_p: number (optional) — The nucleus sampling value used for this run. If not set, de...
        - max_prompt_tokens: integer (required) — The maximum number of prompt tokens specified to have been u...
        - max_completion_tokens: integer (required) — The maximum number of completion tokens specified to have be...
        - truncation_strategy: object (required)
        - tool_choice: object (required)
        - parallel_tool_calls: boolean (required) — Whether to enable [parallel function calling](https://platfo...
        - response_format: object (required) — Specifies the format that the model must output. Compatible ...

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/threads/123/runs/123" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /threads/{thread_id}/runs/{run_id}/cancel
TAGS: Assistants
SUMMARY: Cancel a run
DESCRIPTION: Cancels a run that is `in_progress`.
AUTH: BEARER token

REQUEST
  Path params:
  - thread_id (string, required)
  - run_id (string, required)

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The identifier, which can be referenced in API endpoints.
        - object: string (enum: thread.run) (required) — The object type, which is always `thread.run`.
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the run was created...
        - thread_id: string (required) — The ID of the [thread](https://platform.openai.com/docs/api-...
        - assistant_id: string (required) — The ID of the [assistant](https://platform.openai.com/docs/a...
        - status: string (enum: queued, in_progress, requires_action, cancelling, cancelled...) (required) — The status of the run, which can be either `queued`, `in_pro...
        - required_action: object (2 fields) (required) — Details on the action required to continue the run. Will be ...
        - last_error: object (2 fields) (required) — The last error associated with this run. Will be `null` if t...
        - expires_at: integer (required) — The Unix timestamp (in seconds) for when the run will expire...
        - started_at: integer (required) — The Unix timestamp (in seconds) for when the run was started...
        - cancelled_at: integer (required) — The Unix timestamp (in seconds) for when the run was cancell...
        - failed_at: integer (required) — The Unix timestamp (in seconds) for when the run failed.
        - completed_at: integer (required) — The Unix timestamp (in seconds) for when the run was complet...
        - incomplete_details: object (1 fields) (required) — Details on why the run is incomplete. Will be `null` if the ...
        - model: string (required) — The model that the [assistant](https://platform.openai.com/d...
        - instructions: string (required) — The instructions that the [assistant](https://platform.opena...
        - tools: array<object> (required) — The list of tools that the [assistant](https://platform.open...
        - metadata: object (required)
        - usage: object (required)
        - temperature: number (optional) — The sampling temperature used for this run. If not set, defa...
        - top_p: number (optional) — The nucleus sampling value used for this run. If not set, de...
        - max_prompt_tokens: integer (required) — The maximum number of prompt tokens specified to have been u...
        - max_completion_tokens: integer (required) — The maximum number of completion tokens specified to have be...
        - truncation_strategy: object (required)
        - tool_choice: object (required)
        - parallel_tool_calls: boolean (required) — Whether to enable [parallel function calling](https://platfo...
        - response_format: object (required) — Specifies the format that the model must output. Compatible ...

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/threads/123/runs/123/cancel" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [POST] /threads/{thread_id}/runs/{run_id}/submit_tool_outputs
TAGS: Assistants
SUMMARY: Submit tool outputs to run
DESCRIPTION: When a run has the `status: "requires_action"` and `required_action.type` is `submit_tool_outputs`, this endpoint can be used to submit the outputs from the tool calls once they're all completed. All ... (see full docs)
AUTH: BEARER token

REQUEST
  Path params:
  - thread_id (string, required)
  - run_id (string, required)
  Body:
  Content-Type: application/json
    - tool_outputs: array<object (2 fields)> (required) — A list of tools for which the outputs are being submitted.
    - stream: object (optional)

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The identifier, which can be referenced in API endpoints.
        - object: string (enum: thread.run) (required) — The object type, which is always `thread.run`.
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the run was created...
        - thread_id: string (required) — The ID of the [thread](https://platform.openai.com/docs/api-...
        - assistant_id: string (required) — The ID of the [assistant](https://platform.openai.com/docs/a...
        - status: string (enum: queued, in_progress, requires_action, cancelling, cancelled...) (required) — The status of the run, which can be either `queued`, `in_pro...
        - required_action: object (2 fields) (required) — Details on the action required to continue the run. Will be ...
        - last_error: object (2 fields) (required) — The last error associated with this run. Will be `null` if t...
        - expires_at: integer (required) — The Unix timestamp (in seconds) for when the run will expire...
        - started_at: integer (required) — The Unix timestamp (in seconds) for when the run was started...
        - cancelled_at: integer (required) — The Unix timestamp (in seconds) for when the run was cancell...
        - failed_at: integer (required) — The Unix timestamp (in seconds) for when the run failed.
        - completed_at: integer (required) — The Unix timestamp (in seconds) for when the run was complet...
        - incomplete_details: object (1 fields) (required) — Details on why the run is incomplete. Will be `null` if the ...
        - model: string (required) — The model that the [assistant](https://platform.openai.com/d...
        - instructions: string (required) — The instructions that the [assistant](https://platform.opena...
        - tools: array<object> (required) — The list of tools that the [assistant](https://platform.open...
        - metadata: object (required)
        - usage: object (required)
        - temperature: number (optional) — The sampling temperature used for this run. If not set, defa...
        - top_p: number (optional) — The nucleus sampling value used for this run. If not set, de...
        - max_prompt_tokens: integer (required) — The maximum number of prompt tokens specified to have been u...
        - max_completion_tokens: integer (required) — The maximum number of completion tokens specified to have be...
        - truncation_strategy: object (required)
        - tool_choice: object (required)
        - parallel_tool_calls: boolean (required) — Whether to enable [parallel function calling](https://platfo...
        - response_format: object (required) — Specifies the format that the model must output. Compatible ...

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/threads/123/runs/123/submit_tool_outputs" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================

### Tag: Audio
================================================================================
ENDPOINT: [POST] /audio/speech
TAGS: Audio
SUMMARY: Create speech
DESCRIPTION: Generates audio from the input text.
AUTH: BEARER token

REQUEST
  Body:
  Content-Type: application/json
    - model: object (required) — One of the available [TTS models](https://platform.openai.co...
    - input: string (required) — The text to generate audio for. The maximum length is 4096 c...
    - instructions: string (optional) — Control the voice of your generated audio with additional in...
    - voice: object (required)
    - response_format: string (enum: mp3, opus, aac, flac, wav...) (optional) — The format to audio in. Supported formats are `mp3`, `opus`,...
    - speed: number (optional) — The speed of the generated audio. Select a value from `0.25`...
    - stream_format: string (enum: sse, audio) (optional) — The format to stream the audio in. Supported formats are `ss...

RESPONSES
  - 200 (application/octet-stream): OK
        string (binary)
  - 200 (text/event-stream): OK
        (empty)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/audio/speech" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /audio/transcriptions
TAGS: Audio
SUMMARY: Create transcription
DESCRIPTION: Transcribes audio into the input language.
AUTH: BEARER token

REQUEST
  Body:
  Content-Type: multipart/form-data
    - file: string (binary) (required) — The audio file object (not file name) to transcribe, in one ...
    - model: object (required) — ID of the model to use. The options are `gpt-4o-transcribe`,...
    - language: string (optional) — The language of the input audio. Supplying the input languag...
    - prompt: string (optional) — An optional text to guide the model's style or continue a pr...
    - response_format: string (enum: json, text, srt, verbose_json, vtt) (optional) — The format of the output, in one of these options: `json`, `...
    - temperature: number (optional) — The sampling temperature, between 0 and 1. Higher values lik...
    - stream: object (optional)
    - chunking_strategy: object (optional)
    - timestamp_granularities: array<string (enum: word, segment)> (optional) — The timestamp granularities to populate for this transcripti...
    - include: array<string (enum: logprobs)> (optional) — Additional information to include in the transcription respo...

RESPONSES
  - 200 (application/json): OK
        (empty)
  - 200 (text/event-stream): OK
        (empty)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/audio/transcriptions" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [POST] /audio/translations
TAGS: Audio
SUMMARY: Create translation
DESCRIPTION: Translates audio into English.
AUTH: BEARER token

REQUEST
  Body:
  Content-Type: multipart/form-data
    - file: string (binary) (required) — The audio file object (not file name) translate, in one of t...
    - model: object (required) — ID of the model to use. Only `whisper-1` (which is powered b...
    - prompt: string (optional) — An optional text to guide the model's style or continue a pr...
    - response_format: string (enum: json, text, srt, verbose_json, vtt) (optional) — The format of the output, in one of these options: `json`, `...
    - temperature: number (optional) — The sampling temperature, between 0 and 1. Higher values lik...

RESPONSES
  - 200 (application/json): OK
        (empty)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/audio/translations" \
  -H "Authorization: Bearer $TOKEN"
================================================================================

### Tag: Audit Logs
================================================================================
ENDPOINT: [GET] /organization/audit_logs
TAGS: Audit Logs
SUMMARY: List audit logs
DESCRIPTION: List user actions and configuration changes within this organization.
AUTH: BEARER token

REQUEST
  Query params:
  - effective_at (object (4 fields), optional)
  - project_ids[] (array<string>, optional)
  - event_types[] (array<string (enum: api_key.created, api_key.updated, api_key.deleted, certificate.created, certificate.updated...)>, optional)
  - actor_ids[] (array<string>, optional)
  - actor_emails[] (array<string>, optional)
  - resource_ids[] (array<string>, optional)
  - limit (integer, optional)
  - after (string, optional)
  - before (string, optional)

RESPONSES
  - 200 (application/json): Audit logs listed successfully.
        - object: string (enum: list) (required)
        - data: array<object (52 fields)> (required)
        - first_id: string (required)
        - last_id: string (required)
        - has_more: boolean (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/organization/audit_logs?effective_at=example&project_ids[]=example&event_types[]=example&actor_ids[]=example&actor_emails[]=example&resource_ids[]=example&limit=example&after=example&before=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================

### Tag: Batch
================================================================================
ENDPOINT: [GET] /batches
TAGS: Batch
SUMMARY: List batch
DESCRIPTION: List your organization's batches.
AUTH: BEARER token

REQUEST
  Query params:
  - after (string, optional)
  - limit (integer, optional)

RESPONSES
  - 200 (application/json): Batch listed successfully.
        - data: array<object (22 fields)> (required)
        - first_id: string (optional)
        - last_id: string (optional)
        - has_more: boolean (required)
        - object: string (enum: list) (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/batches?after=example&limit=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /batches/{batch_id}
TAGS: Batch
SUMMARY: Retrieve batch
DESCRIPTION: Retrieves a batch.
AUTH: BEARER token

REQUEST
  Path params:
  - batch_id (string, required)

RESPONSES
  - 200 (application/json): Batch retrieved successfully.
        - id: string (required)
        - object: string (enum: batch) (required) — The object type, which is always `batch`.
        - endpoint: string (required) — The OpenAI API endpoint used by the batch.
        - model: string (optional) — Model ID used to process the batch, like `gpt-5-2025-08-07`....
        - errors: object (2 fields) (optional)
        - input_file_id: string (required) — The ID of the input file for the batch.
        - completion_window: string (required) — The time frame within which the batch should be processed.
        - status: string (enum: validating, failed, in_progress, finalizing, completed...) (required) — The current status of the batch.
        - output_file_id: string (optional) — The ID of the file containing the outputs of successfully ex...
        - error_file_id: string (optional) — The ID of the file containing the outputs of requests with e...
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the batch was creat...
        - in_progress_at: integer (optional) — The Unix timestamp (in seconds) for when the batch started p...
        - expires_at: integer (optional) — The Unix timestamp (in seconds) for when the batch will expi...
        - finalizing_at: integer (optional) — The Unix timestamp (in seconds) for when the batch started f...
        - completed_at: integer (optional) — The Unix timestamp (in seconds) for when the batch was compl...
        - failed_at: integer (optional) — The Unix timestamp (in seconds) for when the batch failed.
        - expired_at: integer (optional) — The Unix timestamp (in seconds) for when the batch expired.
        - cancelling_at: integer (optional) — The Unix timestamp (in seconds) for when the batch started c...
        - cancelled_at: integer (optional) — The Unix timestamp (in seconds) for when the batch was cance...
        - request_counts: object (3 fields) (optional) — The request counts for different statuses within the batch.
        - usage: object (5 fields) (optional) — Represents token usage details including input tokens, outpu...
        - metadata: object (optional)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/batches/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [POST] /batches
TAGS: Batch
SUMMARY: Create batch
DESCRIPTION: Creates and executes a batch from an uploaded file of requests
AUTH: BEARER token

REQUEST
  Body:
  Content-Type: application/json
    - input_file_id: string (required) — The ID of an uploaded file that contains requests for the ne...
    - endpoint: string (enum: /v1/responses, /v1/chat/completions, /v1/embeddings, /v1/completions) (required) — The endpoint to be used for all requests in the batch. Curre...
    - completion_window: string (enum: 24h) (required) — The time frame within which the batch should be processed. C...
    - metadata: object (optional)
    - output_expires_after: object (2 fields) (optional) — The expiration policy for the output and/or error file that ...

RESPONSES
  - 200 (application/json): Batch created successfully.
        - id: string (required)
        - object: string (enum: batch) (required) — The object type, which is always `batch`.
        - endpoint: string (required) — The OpenAI API endpoint used by the batch.
        - model: string (optional) — Model ID used to process the batch, like `gpt-5-2025-08-07`....
        - errors: object (2 fields) (optional)
        - input_file_id: string (required) — The ID of the input file for the batch.
        - completion_window: string (required) — The time frame within which the batch should be processed.
        - status: string (enum: validating, failed, in_progress, finalizing, completed...) (required) — The current status of the batch.
        - output_file_id: string (optional) — The ID of the file containing the outputs of successfully ex...
        - error_file_id: string (optional) — The ID of the file containing the outputs of requests with e...
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the batch was creat...
        - in_progress_at: integer (optional) — The Unix timestamp (in seconds) for when the batch started p...
        - expires_at: integer (optional) — The Unix timestamp (in seconds) for when the batch will expi...
        - finalizing_at: integer (optional) — The Unix timestamp (in seconds) for when the batch started f...
        - completed_at: integer (optional) — The Unix timestamp (in seconds) for when the batch was compl...
        - failed_at: integer (optional) — The Unix timestamp (in seconds) for when the batch failed.
        - expired_at: integer (optional) — The Unix timestamp (in seconds) for when the batch expired.
        - cancelling_at: integer (optional) — The Unix timestamp (in seconds) for when the batch started c...
        - cancelled_at: integer (optional) — The Unix timestamp (in seconds) for when the batch was cance...
        - request_counts: object (3 fields) (optional) — The request counts for different statuses within the batch.
        - usage: object (5 fields) (optional) — Represents token usage details including input tokens, outpu...
        - metadata: object (optional)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/batches" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /batches/{batch_id}/cancel
TAGS: Batch
SUMMARY: Cancel batch
DESCRIPTION: Cancels an in-progress batch. The batch will be in status `cancelling` for up to 10 minutes, before changing to `cancelled`, where it will have partial results (if any) available in the output file.
AUTH: BEARER token

REQUEST
  Path params:
  - batch_id (string, required)

RESPONSES
  - 200 (application/json): Batch is cancelling. Returns the cancelling batch's details.
        - id: string (required)
        - object: string (enum: batch) (required) — The object type, which is always `batch`.
        - endpoint: string (required) — The OpenAI API endpoint used by the batch.
        - model: string (optional) — Model ID used to process the batch, like `gpt-5-2025-08-07`....
        - errors: object (2 fields) (optional)
        - input_file_id: string (required) — The ID of the input file for the batch.
        - completion_window: string (required) — The time frame within which the batch should be processed.
        - status: string (enum: validating, failed, in_progress, finalizing, completed...) (required) — The current status of the batch.
        - output_file_id: string (optional) — The ID of the file containing the outputs of successfully ex...
        - error_file_id: string (optional) — The ID of the file containing the outputs of requests with e...
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the batch was creat...
        - in_progress_at: integer (optional) — The Unix timestamp (in seconds) for when the batch started p...
        - expires_at: integer (optional) — The Unix timestamp (in seconds) for when the batch will expi...
        - finalizing_at: integer (optional) — The Unix timestamp (in seconds) for when the batch started f...
        - completed_at: integer (optional) — The Unix timestamp (in seconds) for when the batch was compl...
        - failed_at: integer (optional) — The Unix timestamp (in seconds) for when the batch failed.
        - expired_at: integer (optional) — The Unix timestamp (in seconds) for when the batch expired.
        - cancelling_at: integer (optional) — The Unix timestamp (in seconds) for when the batch started c...
        - cancelled_at: integer (optional) — The Unix timestamp (in seconds) for when the batch was cance...
        - request_counts: object (3 fields) (optional) — The request counts for different statuses within the batch.
        - usage: object (5 fields) (optional) — Represents token usage details including input tokens, outpu...
        - metadata: object (optional)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/batches/123/cancel" \
  -H "Authorization: Bearer $TOKEN"
================================================================================

### Tag: Certificates
================================================================================
ENDPOINT: [DELETE] /organization/certificates/{certificate_id}
TAGS: Certificates
SUMMARY: Delete certificate
DESCRIPTION: Delete a certificate from the organization.

The certificate must be inactive for the organization and all projects.

AUTH: BEARER token

REQUEST
  none

RESPONSES
  - 200 (application/json): Certificate deleted successfully.
        - object: object (required) — The object type, must be `certificate.deleted`.
        - id: string (required) — The ID of the certificate that was deleted.

EXAMPLE (curl)
curl -X DELETE \
  "https://api.openai.com/v1/organization/certificates/{certificate_id}" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /organization/certificates
TAGS: Certificates
SUMMARY: List organization certificates
DESCRIPTION: List uploaded certificates for this organization.
AUTH: BEARER token

REQUEST
  Query params:
  - limit (integer, optional)
  - after (string, optional)
  - order (string (enum: asc, desc), optional)

RESPONSES
  - 200 (application/json): Certificates listed successfully.
        - data: array<object (6 fields)> (required)
        - first_id: string (optional)
        - last_id: string (optional)
        - has_more: boolean (required)
        - object: string (enum: list) (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/organization/certificates?limit=example&after=example&order=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /organization/certificates/{certificate_id}
TAGS: Certificates
SUMMARY: Get certificate
DESCRIPTION: Get a certificate that has been uploaded to the organization.

You can get a certificate regardless of whether it is active or not.

AUTH: BEARER token

REQUEST
  Path params:
  - certificate_id (string, required)
  Query params:
  - include (array<string (enum: content)>, optional)

RESPONSES
  - 200 (application/json): Certificate retrieved successfully.
        - object: string (enum: certificate, organization.certificate, organization.project.certificate) (required) — The object type.

- If creating, updating, or getting a spec...
        - id: string (required) — The identifier, which can be referenced in API endpoints
        - name: string (required) — The name of the certificate.
        - created_at: integer (required) — The Unix timestamp (in seconds) of when the certificate was ...
        - certificate_details: object (3 fields) (required)
        - active: boolean (optional) — Whether the certificate is currently active at the specified...

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/organization/certificates/123?include=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /organization/projects/{project_id}/certificates
TAGS: Certificates
SUMMARY: List project certificates
DESCRIPTION: List certificates for this project.
AUTH: BEARER token

REQUEST
  Path params:
  - project_id (string, required)
  Query params:
  - limit (integer, optional)
  - after (string, optional)
  - order (string (enum: asc, desc), optional)

RESPONSES
  - 200 (application/json): Certificates listed successfully.
        - data: array<object (6 fields)> (required)
        - first_id: string (optional)
        - last_id: string (optional)
        - has_more: boolean (required)
        - object: string (enum: list) (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/organization/projects/123/certificates?limit=example&after=example&order=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [POST] /organization/certificates
TAGS: Certificates
SUMMARY: Upload certificate
DESCRIPTION: Upload a certificate to the organization. This does **not** automatically activate the certificate.

Organizations can upload up to 50 certificates.

AUTH: BEARER token

REQUEST
  Body:
  Content-Type: application/json
    - name: string (optional) — An optional name for the certificate
    - content: string (required) — The certificate content in PEM format

RESPONSES
  - 200 (application/json): Certificate uploaded successfully.
        - object: string (enum: certificate, organization.certificate, organization.project.certificate) (required) — The object type.

- If creating, updating, or getting a spec...
        - id: string (required) — The identifier, which can be referenced in API endpoints
        - name: string (required) — The name of the certificate.
        - created_at: integer (required) — The Unix timestamp (in seconds) of when the certificate was ...
        - certificate_details: object (3 fields) (required)
        - active: boolean (optional) — Whether the certificate is currently active at the specified...

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/organization/certificates" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /organization/certificates/activate
TAGS: Certificates
SUMMARY: Activate certificates for organization
DESCRIPTION: Activate certificates at the organization level.

You can atomically and idempotently activate up to 10 certificates at a time.

AUTH: BEARER token

REQUEST
  Body:
  Content-Type: application/json
    - certificate_ids: array<string> (required)

RESPONSES
  - 200 (application/json): Certificates activated successfully.
        - data: array<object (6 fields)> (required)
        - first_id: string (optional)
        - last_id: string (optional)
        - has_more: boolean (required)
        - object: string (enum: list) (required)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/organization/certificates/activate" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /organization/certificates/deactivate
TAGS: Certificates
SUMMARY: Deactivate certificates for organization
DESCRIPTION: Deactivate certificates at the organization level.

You can atomically and idempotently deactivate up to 10 certificates at a time.

AUTH: BEARER token

REQUEST
  Body:
  Content-Type: application/json
    - certificate_ids: array<string> (required)

RESPONSES
  - 200 (application/json): Certificates deactivated successfully.
        - data: array<object (6 fields)> (required)
        - first_id: string (optional)
        - last_id: string (optional)
        - has_more: boolean (required)
        - object: string (enum: list) (required)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/organization/certificates/deactivate" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /organization/certificates/{certificate_id}
TAGS: Certificates
SUMMARY: Modify certificate
DESCRIPTION: Modify a certificate. Note that only the name can be modified.

AUTH: BEARER token

REQUEST
  Body:
  Content-Type: application/json
    - name: string (required) — The updated name for the certificate

RESPONSES
  - 200 (application/json): Certificate modified successfully.
        - object: string (enum: certificate, organization.certificate, organization.project.certificate) (required) — The object type.

- If creating, updating, or getting a spec...
        - id: string (required) — The identifier, which can be referenced in API endpoints
        - name: string (required) — The name of the certificate.
        - created_at: integer (required) — The Unix timestamp (in seconds) of when the certificate was ...
        - certificate_details: object (3 fields) (required)
        - active: boolean (optional) — Whether the certificate is currently active at the specified...

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/organization/certificates/{certificate_id}" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /organization/projects/{project_id}/certificates/activate
TAGS: Certificates
SUMMARY: Activate certificates for project
DESCRIPTION: Activate certificates at the project level.

You can atomically and idempotently activate up to 10 certificates at a time.

AUTH: BEARER token

REQUEST
  Path params:
  - project_id (string, required)
  Body:
  Content-Type: application/json
    - certificate_ids: array<string> (required)

RESPONSES
  - 200 (application/json): Certificates activated successfully.
        - data: array<object (6 fields)> (required)
        - first_id: string (optional)
        - last_id: string (optional)
        - has_more: boolean (required)
        - object: string (enum: list) (required)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/organization/projects/123/certificates/activate" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /organization/projects/{project_id}/certificates/deactivate
TAGS: Certificates
SUMMARY: Deactivate certificates for project
DESCRIPTION: Deactivate certificates at the project level. You can atomically and 
idempotently deactivate up to 10 certificates at a time.

AUTH: BEARER token

REQUEST
  Path params:
  - project_id (string, required)
  Body:
  Content-Type: application/json
    - certificate_ids: array<string> (required)

RESPONSES
  - 200 (application/json): Certificates deactivated successfully.
        - data: array<object (6 fields)> (required)
        - first_id: string (optional)
        - last_id: string (optional)
        - has_more: boolean (required)
        - object: string (enum: list) (required)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/organization/projects/123/certificates/deactivate" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================

### Tag: Chat
================================================================================
ENDPOINT: [DELETE] /chat/completions/{completion_id}
TAGS: Chat
SUMMARY: Delete chat completion
DESCRIPTION: Delete a stored chat completion. Only Chat Completions that have been
created with the `store` parameter set to `true` can be deleted.

AUTH: BEARER token

REQUEST
  Path params:
  - completion_id (string, required)

RESPONSES
  - 200 (application/json): The chat completion was deleted successfully.
        - object: string (enum: chat.completion.deleted) (required) — The type of object being deleted.
        - id: string (required) — The ID of the chat completion that was deleted.
        - deleted: boolean (required) — Whether the chat completion was deleted.

EXAMPLE (curl)
curl -X DELETE \
  "https://api.openai.com/v1/chat/completions/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /chat/completions
TAGS: Chat
SUMMARY: List Chat Completions
DESCRIPTION: List stored Chat Completions. Only Chat Completions that have been stored
with the `store` parameter set to `true` will be returned.

AUTH: BEARER token

REQUEST
  Query params:
  - model (string, optional)
  - metadata (object, optional)
  - after (string, optional)
  - limit (integer, optional)
  - order (string (enum: asc, desc), optional)

RESPONSES
  - 200 (application/json): A list of Chat Completions
        - object: string (enum: list) (required) — The type of this object. It is always set to "list".

        - data: array<object (8 fields)> (required) — An array of chat completion objects.

        - first_id: string (required) — The identifier of the first chat completion in the data arra...
        - last_id: string (required) — The identifier of the last chat completion in the data array...
        - has_more: boolean (required) — Indicates whether there are more Chat Completions available.

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/chat/completions?model=example&metadata=example&after=example&limit=example&order=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /chat/completions/{completion_id}
TAGS: Chat
SUMMARY: Get chat completion
DESCRIPTION: Get a stored chat completion. Only Chat Completions that have been created
with the `store` parameter set to `true` will be returned.

AUTH: BEARER token

REQUEST
  Path params:
  - completion_id (string, required)

RESPONSES
  - 200 (application/json): A chat completion
        - id: string (required) — A unique identifier for the chat completion.
        - choices: array<object (4 fields)> (required) — A list of chat completion choices. Can be more than one if `...
        - created: integer (required) — The Unix timestamp (in seconds) of when the chat completion ...
        - model: string (required) — The model used for the chat completion.
        - service_tier: object (optional)
        - system_fingerprint: string (optional) — This fingerprint represents the backend configuration that t...
        - object: string (enum: chat.completion) (required) — The object type, which is always `chat.completion`.
        - usage: object (5 fields) (optional) — Usage statistics for the completion request.

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/chat/completions/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /chat/completions/{completion_id}/messages
TAGS: Chat
SUMMARY: Get chat messages
DESCRIPTION: Get the messages in a stored chat completion. Only Chat Completions that
have been created with the `store` parameter set to `true` will be
returned.

AUTH: BEARER token

REQUEST
  Path params:
  - completion_id (string, required)
  Query params:
  - after (string, optional)
  - limit (integer, optional)
  - order (string (enum: asc, desc), optional)

RESPONSES
  - 200 (application/json): A list of messages
        - object: string (enum: list) (required) — The type of this object. It is always set to "list".

        - data: array<object> (required) — An array of chat completion message objects.

        - first_id: string (required) — The identifier of the first chat message in the data array.
        - last_id: string (required) — The identifier of the last chat message in the data array.
        - has_more: boolean (required) — Indicates whether there are more chat messages available.

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/chat/completions/123/messages?after=example&limit=example&order=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [POST] /chat/completions
TAGS: Chat
SUMMARY: Create chat completion
DESCRIPTION: **Starting a new project?** We recommend trying [Responses](https://platform.openai.com/docs/api-reference/responses) 
to take advantage of the latest OpenAI platform features. Compare
[Chat Completio... (see full docs)
AUTH: BEARER token

REQUEST
  Body:
  Content-Type: application/json
    (empty)

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — A unique identifier for the chat completion.
        - choices: array<object (4 fields)> (required) — A list of chat completion choices. Can be more than one if `...
        - created: integer (required) — The Unix timestamp (in seconds) of when the chat completion ...
        - model: string (required) — The model used for the chat completion.
        - service_tier: object (optional)
        - system_fingerprint: string (optional) — This fingerprint represents the backend configuration that t...
        - object: string (enum: chat.completion) (required) — The object type, which is always `chat.completion`.
        - usage: object (5 fields) (optional) — Usage statistics for the completion request.
  - 200 (text/event-stream): OK
        - id: string (required) — A unique identifier for the chat completion. Each chunk has ...
        - choices: array<object (4 fields)> (required) — A list of chat completion choices. Can contain more than one...
        - created: integer (required) — The Unix timestamp (in seconds) of when the chat completion ...
        - model: string (required) — The model to generate the completion.
        - service_tier: object (optional)
        - system_fingerprint: string (optional) — This fingerprint represents the backend configuration that t...
        - object: string (enum: chat.completion.chunk) (required) — The object type, which is always `chat.completion.chunk`.
        - usage: object (5 fields) (optional) — Usage statistics for the completion request.

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/chat/completions" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /chat/completions/{completion_id}
TAGS: Chat
SUMMARY: Update chat completion
DESCRIPTION: Modify a stored chat completion. Only Chat Completions that have been
created with the `store` parameter set to `true` can be modified. Currently,
the only supported modification is to update the `met... (see full docs)
AUTH: BEARER token

REQUEST
  Path params:
  - completion_id (string, required)
  Body:
  Content-Type: application/json
    - metadata: object (required)

RESPONSES
  - 200 (application/json): A chat completion
        - id: string (required) — A unique identifier for the chat completion.
        - choices: array<object (4 fields)> (required) — A list of chat completion choices. Can be more than one if `...
        - created: integer (required) — The Unix timestamp (in seconds) of when the chat completion ...
        - model: string (required) — The model used for the chat completion.
        - service_tier: object (optional)
        - system_fingerprint: string (optional) — This fingerprint represents the backend configuration that t...
        - object: string (enum: chat.completion) (required) — The object type, which is always `chat.completion`.
        - usage: object (5 fields) (optional) — Usage statistics for the completion request.

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/chat/completions/123" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================

### Tag: Completions
================================================================================
ENDPOINT: [POST] /completions
TAGS: Completions
SUMMARY: Create completion
DESCRIPTION: Creates a completion for the provided prompt and parameters.
AUTH: BEARER token

REQUEST
  Body:
  Content-Type: application/json
    - model: object (required) — ID of the model to use. You can use the [List models](https:...
    - prompt: object (required) — The prompt(s) to generate completions for, encoded as a stri...
    - best_of: integer (optional) — Generates `best_of` completions server-side and returns the ...
    - echo: boolean (optional) — Echo back the prompt in addition to the completion

    - frequency_penalty: number (optional) — Number between -2.0 and 2.0. Positive values penalize new to...
    - logit_bias: object (optional) — Modify the likelihood of specified tokens appearing in the c...
    - logprobs: integer (optional) — Include the log probabilities on the `logprobs` most likely ...
    - max_tokens: integer (optional) — The maximum number of [tokens](/tokenizer) that can be gener...
    - n: integer (optional) — How many completions to generate for each prompt.

**Note:**...
    - presence_penalty: number (optional) — Number between -2.0 and 2.0. Positive values penalize new to...
    - seed: integer (int64) (optional) — If specified, our system will make a best effort to sample d...
    - stop: object (optional) — Not supported with latest reasoning models `o3` and `o4-mini...
    - stream: boolean (optional) — Whether to stream back partial progress. If set, tokens will...
    - stream_options: object (optional)
    - suffix: string (optional) — The suffix that comes after a completion of inserted text.

...
    - temperature: number (optional) — What sampling temperature to use, between 0 and 2. Higher va...
    - top_p: number (optional) — An alternative to sampling with temperature, called nucleus ...
    - user: string (optional) — A unique identifier representing your end-user, which can he...

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — A unique identifier for the completion.
        - choices: array<object (4 fields)> (required) — The list of completion choices the model generated for the i...
        - created: integer (required) — The Unix timestamp (in seconds) of when the completion was c...
        - model: string (required) — The model used for completion.
        - system_fingerprint: string (optional) — This fingerprint represents the backend configuration that t...
        - object: string (enum: text_completion) (required) — The object type, which is always "text_completion"
        - usage: object (5 fields) (optional) — Usage statistics for the completion request.

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/completions" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================

### Tag: Conversations
================================================================================
ENDPOINT: [DELETE] /conversations/{conversation_id}
TAGS: Conversations
SUMMARY: Delete a conversation
DESCRIPTION: Delete a conversation. Items in the conversation will not be deleted.
AUTH: BEARER token

REQUEST
  Path params:
  - conversation_id (string, required)

RESPONSES
  - 200 (application/json): Success
        - object: string (enum: conversation.deleted) (required)
        - deleted: boolean (required)
        - id: string (required)

EXAMPLE (curl)
curl -X DELETE \
  "https://api.openai.com/v1/conversations/conv_123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [DELETE] /conversations/{conversation_id}/items/{item_id}
TAGS: Conversations
SUMMARY: Delete an item
DESCRIPTION: Delete an item from a conversation with the given IDs.
AUTH: BEARER token

REQUEST
  Path params:
  - conversation_id (string, required)
  - item_id (string, required)

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The unique ID of the conversation.
        - object: string (enum: conversation) (required) — The object type, which is always `conversation`.
        - metadata: object (required) — Set of 16 key-value pairs that can be attached to an object....
        - created_at: integer (required) — The time at which the conversation was created, measured in ...

EXAMPLE (curl)
curl -X DELETE \
  "https://api.openai.com/v1/conversations/conv_123/items/msg_abc" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /conversations/{conversation_id}
TAGS: Conversations
SUMMARY: Retrieve a conversation
DESCRIPTION: Get a conversation
AUTH: BEARER token

REQUEST
  Path params:
  - conversation_id (string, required)

RESPONSES
  - 200 (application/json): Success
        - id: string (required) — The unique ID of the conversation.
        - object: string (enum: conversation) (required) — The object type, which is always `conversation`.
        - metadata: object (required) — Set of 16 key-value pairs that can be attached to an object....
        - created_at: integer (required) — The time at which the conversation was created, measured in ...

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/conversations/conv_123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /conversations/{conversation_id}/items
TAGS: Conversations
SUMMARY: List items
DESCRIPTION: List all items for a conversation with the given ID.
AUTH: BEARER token

REQUEST
  Path params:
  - conversation_id (string, required)
  Query params:
  - limit (integer, optional)
  - order (string (enum: asc, desc), optional)
  - after (string, optional)
  - include (array<string (enum: code_interpreter_call.outputs, computer_call_output.output.image_url, file_search_call.results, message.input_image.image_url, message.output_text.logprobs...)>, optional)

RESPONSES
  - 200 (application/json): OK
        - object: object (required) — The type of object returned, must be `list`.
        - data: array<object> (required) — A list of conversation items.
        - has_more: boolean (required) — Whether there are more items available.
        - first_id: string (required) — The ID of the first item in the list.
        - last_id: string (required) — The ID of the last item in the list.

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/conversations/conv_123/items?limit=example&order=example&after=example&include=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /conversations/{conversation_id}/items/{item_id}
TAGS: Conversations
SUMMARY: Retrieve an item
DESCRIPTION: Get a single item from a conversation with the given IDs.
AUTH: BEARER token

REQUEST
  Path params:
  - conversation_id (string, required)
  - item_id (string, required)
  Query params:
  - include (array<string (enum: code_interpreter_call.outputs, computer_call_output.output.image_url, file_search_call.results, message.input_image.image_url, message.output_text.logprobs...)>, optional)

RESPONSES
  - 200 (application/json): OK
        (empty)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/conversations/conv_123/items/msg_abc?include=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [POST] /conversations
TAGS: Conversations
SUMMARY: Create a conversation
DESCRIPTION: Create a conversation.
AUTH: BEARER token

REQUEST
  Body:
  Content-Type: application/json
    - metadata: object (optional)
    - items: object (optional)

RESPONSES
  - 200 (application/json): Success
        - id: string (required) — The unique ID of the conversation.
        - object: string (enum: conversation) (required) — The object type, which is always `conversation`.
        - metadata: object (required) — Set of 16 key-value pairs that can be attached to an object....
        - created_at: integer (required) — The time at which the conversation was created, measured in ...

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/conversations" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /conversations/{conversation_id}
TAGS: Conversations
SUMMARY: Update a conversation
AUTH: BEARER token

REQUEST
  Path params:
  - conversation_id (string, required)
  Body:
  Content-Type: application/json
    - metadata: object (required)

RESPONSES
  - 200 (application/json): Success
        - id: string (required) — The unique ID of the conversation.
        - object: string (enum: conversation) (required) — The object type, which is always `conversation`.
        - metadata: object (required) — Set of 16 key-value pairs that can be attached to an object....
        - created_at: integer (required) — The time at which the conversation was created, measured in ...

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/conversations/conv_123" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /conversations/{conversation_id}/items
TAGS: Conversations
SUMMARY: Create items
DESCRIPTION: Create items in a conversation with the given ID.
AUTH: BEARER token

REQUEST
  Path params:
  - conversation_id (string, required)
  Query params:
  - include (array<string (enum: code_interpreter_call.outputs, computer_call_output.output.image_url, file_search_call.results, message.input_image.image_url, message.output_text.logprobs...)>, optional)
  Body:
  Content-Type: application/json
    - items: array<object> (required) — The items to add to the conversation. You may add up to 20 i...

RESPONSES
  - 200 (application/json): OK
        - object: object (required) — The type of object returned, must be `list`.
        - data: array<object> (required) — A list of conversation items.
        - has_more: boolean (required) — Whether there are more items available.
        - first_id: string (required) — The ID of the first item in the list.
        - last_id: string (required) — The ID of the last item in the list.

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/conversations/conv_123/items?include=example" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================

### Tag: Embeddings
================================================================================
ENDPOINT: [POST] /embeddings
TAGS: Embeddings
SUMMARY: Create embeddings
DESCRIPTION: Creates an embedding vector representing the input text.
AUTH: BEARER token

REQUEST
  Body:
  Content-Type: application/json
    - input: object (required) — Input text to embed, encoded as a string or array of tokens....
    - model: object (required) — ID of the model to use. You can use the [List models](https:...
    - encoding_format: string (enum: float, base64) (optional) — The format to return the embeddings in. Can be either `float...
    - dimensions: integer (optional) — The number of dimensions the resulting output embeddings sho...
    - user: string (optional) — A unique identifier representing your end-user, which can he...

RESPONSES
  - 200 (application/json): OK
        - data: array<object (3 fields)> (required) — The list of embeddings generated by the model.
        - model: string (required) — The name of the model used to generate the embedding.
        - object: string (enum: list) (required) — The object type, which is always "list".
        - usage: object (2 fields) (required) — The usage information for the request.

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/embeddings" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================

### Tag: Evals
================================================================================
ENDPOINT: [DELETE] /evals/{eval_id}
TAGS: Evals
SUMMARY: Delete an eval
DESCRIPTION: Delete an evaluation.

AUTH: BEARER token

REQUEST
  Path params:
  - eval_id (string, required)

RESPONSES
  - 200 (application/json): Successfully deleted the evaluation.
        - object: string (required)
        - deleted: boolean (required)
        - eval_id: string (required)
  - 404 (application/json): Evaluation not found.
        - code: object (required)
        - message: string (required)
        - param: object (required)
        - type: string (required)

EXAMPLE (curl)
curl -X DELETE \
  "https://api.openai.com/v1/evals/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [DELETE] /evals/{eval_id}/runs/{run_id}
TAGS: Evals
SUMMARY: Delete eval run
DESCRIPTION: Delete an eval run.

AUTH: BEARER token

REQUEST
  Path params:
  - eval_id (string, required)
  - run_id (string, required)

RESPONSES
  - 200 (application/json): Successfully deleted the eval run
        - object: string (optional)
        - deleted: boolean (optional)
        - run_id: string (optional)
  - 404 (application/json): Run not found
        - code: object (required)
        - message: string (required)
        - param: object (required)
        - type: string (required)

EXAMPLE (curl)
curl -X DELETE \
  "https://api.openai.com/v1/evals/123/runs/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /evals
TAGS: Evals
SUMMARY: List evals
DESCRIPTION: List evaluations for a project.

AUTH: BEARER token

REQUEST
  Query params:
  - after (string, optional)
  - limit (integer, optional)
  - order (string (enum: asc, desc), optional)
  - order_by (string (enum: created_at, updated_at), optional)

RESPONSES
  - 200 (application/json): A list of evals
        - object: string (enum: list) (required) — The type of this object. It is always set to "list".

        - data: array<object (7 fields)> (required) — An array of eval objects.

        - first_id: string (required) — The identifier of the first eval in the data array.
        - last_id: string (required) — The identifier of the last eval in the data array.
        - has_more: boolean (required) — Indicates whether there are more evals available.

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/evals?after=example&limit=example&order=example&order_by=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /evals/{eval_id}
TAGS: Evals
SUMMARY: Get an eval
DESCRIPTION: Get an evaluation by ID.

AUTH: BEARER token

REQUEST
  Path params:
  - eval_id (string, required)

RESPONSES
  - 200 (application/json): The evaluation
        - object: string (enum: eval) (required) — The object type.
        - id: string (required) — Unique identifier for the evaluation.
        - name: string (required) — The name of the evaluation.
        - data_source_config: object (required) — Configuration of data sources used in runs of the evaluation...
        - testing_criteria: array<object> (required) — A list of testing criteria.
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the eval was create...
        - metadata: object (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/evals/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /evals/{eval_id}/runs
TAGS: Evals
SUMMARY: Get eval runs
DESCRIPTION: Get a list of runs for an evaluation.

AUTH: BEARER token

REQUEST
  Path params:
  - eval_id (string, required)
  Query params:
  - after (string, optional)
  - limit (integer, optional)
  - order (string (enum: asc, desc), optional)
  - status (string (enum: queued, in_progress, completed, canceled, failed), optional)

RESPONSES
  - 200 (application/json): A list of runs for the evaluation
        - object: string (enum: list) (required) — The type of this object. It is always set to "list".

        - data: array<object (14 fields)> (required) — An array of eval run objects.

        - first_id: string (required) — The identifier of the first eval run in the data array.
        - last_id: string (required) — The identifier of the last eval run in the data array.
        - has_more: boolean (required) — Indicates whether there are more evals available.

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/evals/123/runs?after=example&limit=example&order=example&status=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /evals/{eval_id}/runs/{run_id}
TAGS: Evals
SUMMARY: Get an eval run
DESCRIPTION: Get an evaluation run by ID.

AUTH: BEARER token

REQUEST
  Path params:
  - eval_id (string, required)
  - run_id (string, required)

RESPONSES
  - 200 (application/json): The evaluation run
        - object: string (enum: eval.run) (required) — The type of the object. Always "eval.run".
        - id: string (required) — Unique identifier for the evaluation run.
        - eval_id: string (required) — The identifier of the associated evaluation.
        - status: string (required) — The status of the evaluation run.
        - model: string (required) — The model that is evaluated, if applicable.
        - name: string (required) — The name of the evaluation run.
        - created_at: integer (required) — Unix timestamp (in seconds) when the evaluation run was crea...
        - report_url: string (required) — The URL to the rendered evaluation run report on the UI dash...
        - result_counts: object (4 fields) (required) — Counters summarizing the outcomes of the evaluation run.
        - per_model_usage: array<object (6 fields)> (required) — Usage statistics for each model during the evaluation run.
        - per_testing_criteria_results: array<object (3 fields)> (required) — Results per testing criteria applied during the evaluation r...
        - data_source: object (required) — Information about the run's data source.
        - metadata: object (required)
        - error: object (2 fields) (required) — An object representing an error response from the Eval API.


EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/evals/123/runs/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /evals/{eval_id}/runs/{run_id}/output_items
TAGS: Evals
SUMMARY: Get eval run output items
DESCRIPTION: Get a list of output items for an evaluation run.

AUTH: BEARER token

REQUEST
  Path params:
  - eval_id (string, required)
  - run_id (string, required)
  Query params:
  - after (string, optional)
  - limit (integer, optional)
  - status (string (enum: fail, pass), optional)
  - order (string (enum: asc, desc), optional)

RESPONSES
  - 200 (application/json): A list of output items for the evaluation run
        - object: string (enum: list) (required) — The type of this object. It is always set to "list".

        - data: array<object (10 fields)> (required) — An array of eval run output item objects.

        - first_id: string (required) — The identifier of the first eval run output item in the data...
        - last_id: string (required) — The identifier of the last eval run output item in the data ...
        - has_more: boolean (required) — Indicates whether there are more eval run output items avail...

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/evals/123/runs/123/output_items?after=example&limit=example&status=example&order=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /evals/{eval_id}/runs/{run_id}/output_items/{output_item_id}
TAGS: Evals
SUMMARY: Get an output item of an eval run
DESCRIPTION: Get an evaluation run output item by ID.

AUTH: BEARER token

REQUEST
  Path params:
  - eval_id (string, required)
  - run_id (string, required)
  - output_item_id (string, required)

RESPONSES
  - 200 (application/json): The evaluation run output item
        - object: string (enum: eval.run.output_item) (required) — The type of the object. Always "eval.run.output_item".
        - id: string (required) — Unique identifier for the evaluation run output item.
        - run_id: string (required) — The identifier of the evaluation run associated with this ou...
        - eval_id: string (required) — The identifier of the evaluation group.
        - created_at: integer (required) — Unix timestamp (in seconds) when the evaluation run was crea...
        - status: string (required) — The status of the evaluation run.
        - datasource_item_id: integer (required) — The identifier for the data source item.
        - datasource_item: object (required) — Details of the input data source item.
        - results: array<object (5 fields)> (required) — A list of grader results for this output item.
        - sample: object (10 fields) (required) — A sample containing the input and output of the evaluation r...

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/evals/123/runs/123/output_items/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [POST] /evals
TAGS: Evals
SUMMARY: Create eval
DESCRIPTION: Create the structure of an evaluation that can be used to test a model's performance.
An evaluation is a set of testing criteria and the config for a data source, which dictates the schema of the data... (see full docs)
AUTH: BEARER token

REQUEST
  Body:
  Content-Type: application/json
    - name: string (optional) — The name of the evaluation.
    - metadata: object (optional)
    - data_source_config: object (required) — The configuration for the data source used for the evaluatio...
    - testing_criteria: array<object> (required) — A list of graders for all eval runs in this group. Graders c...

RESPONSES
  - 201 (application/json): OK
        - object: string (enum: eval) (required) — The object type.
        - id: string (required) — Unique identifier for the evaluation.
        - name: string (required) — The name of the evaluation.
        - data_source_config: object (required) — Configuration of data sources used in runs of the evaluation...
        - testing_criteria: array<object> (required) — A list of testing criteria.
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the eval was create...
        - metadata: object (required)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/evals" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /evals/{eval_id}
TAGS: Evals
SUMMARY: Update an eval
DESCRIPTION: Update certain properties of an evaluation.

AUTH: BEARER token

REQUEST
  Path params:
  - eval_id (string, required)
  Body:
  Content-Type: application/json
    - name: string (optional) — Rename the evaluation.
    - metadata: object (optional)

RESPONSES
  - 200 (application/json): The updated evaluation
        - object: string (enum: eval) (required) — The object type.
        - id: string (required) — Unique identifier for the evaluation.
        - name: string (required) — The name of the evaluation.
        - data_source_config: object (required) — Configuration of data sources used in runs of the evaluation...
        - testing_criteria: array<object> (required) — A list of testing criteria.
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the eval was create...
        - metadata: object (required)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/evals/123" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /evals/{eval_id}/runs
TAGS: Evals
SUMMARY: Create eval run
DESCRIPTION: Kicks off a new run for a given evaluation, specifying the data source, and what model configuration to use to test. The datasource will be validated against the schema specified in the config of the ... (see full docs)
AUTH: BEARER token

REQUEST
  Path params:
  - eval_id (string, required)
  Body:
  Content-Type: application/json
    - name: string (optional) — The name of the run.
    - metadata: object (optional)
    - data_source: object (required) — Details about the run's data source.

RESPONSES
  - 201 (application/json): Successfully created a run for the evaluation
        - object: string (enum: eval.run) (required) — The type of the object. Always "eval.run".
        - id: string (required) — Unique identifier for the evaluation run.
        - eval_id: string (required) — The identifier of the associated evaluation.
        - status: string (required) — The status of the evaluation run.
        - model: string (required) — The model that is evaluated, if applicable.
        - name: string (required) — The name of the evaluation run.
        - created_at: integer (required) — Unix timestamp (in seconds) when the evaluation run was crea...
        - report_url: string (required) — The URL to the rendered evaluation run report on the UI dash...
        - result_counts: object (4 fields) (required) — Counters summarizing the outcomes of the evaluation run.
        - per_model_usage: array<object (6 fields)> (required) — Usage statistics for each model during the evaluation run.
        - per_testing_criteria_results: array<object (3 fields)> (required) — Results per testing criteria applied during the evaluation r...
        - data_source: object (required) — Information about the run's data source.
        - metadata: object (required)
        - error: object (2 fields) (required) — An object representing an error response from the Eval API.

  - 400 (application/json): Bad request (for example, missing eval object)
        - code: object (required)
        - message: string (required)
        - param: object (required)
        - type: string (required)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/evals/123/runs" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /evals/{eval_id}/runs/{run_id}
TAGS: Evals
SUMMARY: Cancel eval run
DESCRIPTION: Cancel an ongoing evaluation run.

AUTH: BEARER token

REQUEST
  Path params:
  - eval_id (string, required)
  - run_id (string, required)

RESPONSES
  - 200 (application/json): The canceled eval run object
        - object: string (enum: eval.run) (required) — The type of the object. Always "eval.run".
        - id: string (required) — Unique identifier for the evaluation run.
        - eval_id: string (required) — The identifier of the associated evaluation.
        - status: string (required) — The status of the evaluation run.
        - model: string (required) — The model that is evaluated, if applicable.
        - name: string (required) — The name of the evaluation run.
        - created_at: integer (required) — Unix timestamp (in seconds) when the evaluation run was crea...
        - report_url: string (required) — The URL to the rendered evaluation run report on the UI dash...
        - result_counts: object (4 fields) (required) — Counters summarizing the outcomes of the evaluation run.
        - per_model_usage: array<object (6 fields)> (required) — Usage statistics for each model during the evaluation run.
        - per_testing_criteria_results: array<object (3 fields)> (required) — Results per testing criteria applied during the evaluation r...
        - data_source: object (required) — Information about the run's data source.
        - metadata: object (required)
        - error: object (2 fields) (required) — An object representing an error response from the Eval API.


EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/evals/123/runs/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================

### Tag: Files
================================================================================
ENDPOINT: [DELETE] /files/{file_id}
TAGS: Files
SUMMARY: Delete file
DESCRIPTION: Delete a file and remove it from all vector stores.
AUTH: BEARER token

REQUEST
  Path params:
  - file_id (string, required)

RESPONSES
  - 200 (application/json): OK
        - id: string (required)
        - object: string (enum: file) (required)
        - deleted: boolean (required)

EXAMPLE (curl)
curl -X DELETE \
  "https://api.openai.com/v1/files/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /files
TAGS: Files
SUMMARY: List files
DESCRIPTION: Returns a list of files.
AUTH: BEARER token

REQUEST
  Query params:
  - purpose (string, optional)
  - limit (integer, optional)
  - order (string (enum: asc, desc), optional)
  - after (string, optional)

RESPONSES
  - 200 (application/json): OK
        - object: string (required)
        - data: array<object (9 fields)> (required)
        - first_id: string (required)
        - last_id: string (required)
        - has_more: boolean (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/files?purpose=example&limit=example&order=example&after=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /files/{file_id}
TAGS: Files
SUMMARY: Retrieve file
DESCRIPTION: Returns information about a specific file.
AUTH: BEARER token

REQUEST
  Path params:
  - file_id (string, required)

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The file identifier, which can be referenced in the API endp...
        - bytes: integer (required) — The size of the file, in bytes.
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the file was create...
        - expires_at: integer (optional) — The Unix timestamp (in seconds) for when the file will expir...
        - filename: string (required) — The name of the file.
        - object: string (enum: file) (required) — The object type, which is always `file`.
        - purpose: string (enum: assistants, assistants_output, batch, batch_output, fine-tune...) (required) — The intended purpose of the file. Supported values are `assi...
        - status: string (enum: uploaded, processed, error) (required) — Deprecated. The current status of the file, which can be eit...
        - status_details: string (optional) — Deprecated. For details on why a fine-tuning training file f...

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/files/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /files/{file_id}/content
TAGS: Files
SUMMARY: Retrieve file content
DESCRIPTION: Returns the contents of the specified file.
AUTH: BEARER token

REQUEST
  Path params:
  - file_id (string, required)

RESPONSES
  - 200 (application/json): OK
        string

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/files/123/content" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [POST] /files
TAGS: Files
SUMMARY: Upload file
DESCRIPTION: Upload a file that can be used across various endpoints. Individual files can be up to 512 MB, and the size of all files uploaded by one organization can be up to 1 TB.

The Assistants API supports fi... (see full docs)
AUTH: BEARER token

REQUEST
  Body:
  Content-Type: multipart/form-data
    - file: string (binary) (required) — The File object (not file name) to be uploaded.

    - purpose: string (enum: assistants, batch, fine-tune, vision, user_data...) (required) — The intended purpose of the uploaded file. One of: - `assist...
    - expires_after: object (2 fields) (optional) — The expiration policy for a file. By default, files with `pu...

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The file identifier, which can be referenced in the API endp...
        - bytes: integer (required) — The size of the file, in bytes.
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the file was create...
        - expires_at: integer (optional) — The Unix timestamp (in seconds) for when the file will expir...
        - filename: string (required) — The name of the file.
        - object: string (enum: file) (required) — The object type, which is always `file`.
        - purpose: string (enum: assistants, assistants_output, batch, batch_output, fine-tune...) (required) — The intended purpose of the file. Supported values are `assi...
        - status: string (enum: uploaded, processed, error) (required) — Deprecated. The current status of the file, which can be eit...
        - status_details: string (optional) — Deprecated. For details on why a fine-tuning training file f...

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/files" \
  -H "Authorization: Bearer $TOKEN"
================================================================================

### Tag: Fine-tuning
================================================================================
ENDPOINT: [DELETE] /fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions/{permission_id}
TAGS: Fine-tuning
SUMMARY: Delete checkpoint permission
DESCRIPTION: **NOTE:** This endpoint requires an [admin API key](../admin-api-keys).

Organization owners can use this endpoint to delete a permission for a fine-tuned model checkpoint.

AUTH: BEARER token

REQUEST
  Path params:
  - fine_tuned_model_checkpoint (string, required)
  - permission_id (string, required)

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The ID of the fine-tuned model checkpoint permission that wa...
        - object: string (enum: checkpoint.permission) (required) — The object type, which is always "checkpoint.permission".
        - deleted: boolean (required) — Whether the fine-tuned model checkpoint permission was succe...

EXAMPLE (curl)
curl -X DELETE \
  "https://api.openai.com/v1/fine_tuning/checkpoints/ft:gpt-4o-mini-2024-07-18:org:weather:B7R9VjQd/permissions/cp_zc4Q7MP6XxulcVzj4MZdwsAB" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions
TAGS: Fine-tuning
SUMMARY: List checkpoint permissions
DESCRIPTION: **NOTE:** This endpoint requires an [admin API key](../admin-api-keys).

Organization owners can use this endpoint to view all permissions for a fine-tuned model checkpoint.

AUTH: BEARER token

REQUEST
  Path params:
  - fine_tuned_model_checkpoint (string, required)
  Query params:
  - project_id (string, optional)
  - after (string, optional)
  - limit (integer, optional)
  - order (string (enum: ascending, descending), optional)

RESPONSES
  - 200 (application/json): OK
        - data: array<object (4 fields)> (required)
        - object: string (enum: list) (required)
        - first_id: object (optional)
        - last_id: object (optional)
        - has_more: boolean (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/fine_tuning/checkpoints/ft-AF1WoRqd3aJAHsqc9NY7iL8F/permissions?project_id=example&after=example&limit=example&order=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /fine_tuning/jobs
TAGS: Fine-tuning
SUMMARY: List fine-tuning jobs
DESCRIPTION: List your organization's fine-tuning jobs

AUTH: BEARER token

REQUEST
  Query params:
  - after (string, optional)
  - limit (integer, optional)
  - metadata (object, optional)

RESPONSES
  - 200 (application/json): OK
        - data: array<object (19 fields)> (required)
        - has_more: boolean (required)
        - object: string (enum: list) (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/fine_tuning/jobs?after=example&limit=example&metadata=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /fine_tuning/jobs/{fine_tuning_job_id}
TAGS: Fine-tuning
SUMMARY: Retrieve fine-tuning job
DESCRIPTION: Get info about a fine-tuning job.

[Learn more about fine-tuning](https://platform.openai.com/docs/guides/model-optimization)

AUTH: BEARER token

REQUEST
  Path params:
  - fine_tuning_job_id (string, required)

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The object identifier, which can be referenced in the API en...
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the fine-tuning job...
        - error: object (required)
        - fine_tuned_model: object (required)
        - finished_at: object (required)
        - hyperparameters: object (3 fields) (required) — The hyperparameters used for the fine-tuning job. This value...
        - model: string (required) — The base model that is being fine-tuned.
        - object: string (enum: fine_tuning.job) (required) — The object type, which is always "fine_tuning.job".
        - organization_id: string (required) — The organization that owns the fine-tuning job.
        - result_files: array<string> (required) — The compiled results file ID(s) for the fine-tuning job. You...
        - status: string (enum: validating_files, queued, running, succeeded, failed...) (required) — The current status of the fine-tuning job, which can be eith...
        - trained_tokens: object (required)
        - training_file: string (required) — The file ID used for training. You can retrieve the training...
        - validation_file: object (required)
        - integrations: object (optional)
        - seed: integer (required) — The seed used for the fine-tuning job.
        - estimated_finish: object (optional)
        - method: object (4 fields) (optional) — The method used for fine-tuning.
        - metadata: object (optional)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/fine_tuning/jobs/ft-AF1WoRqd3aJAHsqc9NY7iL8F" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /fine_tuning/jobs/{fine_tuning_job_id}/checkpoints
TAGS: Fine-tuning
SUMMARY: List fine-tuning checkpoints
DESCRIPTION: List checkpoints for a fine-tuning job.

AUTH: BEARER token

REQUEST
  Path params:
  - fine_tuning_job_id (string, required)
  Query params:
  - after (string, optional)
  - limit (integer, optional)

RESPONSES
  - 200 (application/json): OK
        - data: array<object (7 fields)> (required)
        - object: string (enum: list) (required)
        - first_id: object (optional)
        - last_id: object (optional)
        - has_more: boolean (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/fine_tuning/jobs/ft-AF1WoRqd3aJAHsqc9NY7iL8F/checkpoints?after=example&limit=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /fine_tuning/jobs/{fine_tuning_job_id}/events
TAGS: Fine-tuning
SUMMARY: List fine-tuning events
DESCRIPTION: Get status updates for a fine-tuning job.

AUTH: BEARER token

REQUEST
  Path params:
  - fine_tuning_job_id (string, required)
  Query params:
  - after (string, optional)
  - limit (integer, optional)

RESPONSES
  - 200 (application/json): OK
        - data: array<object (7 fields)> (required)
        - object: string (enum: list) (required)
        - has_more: boolean (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/fine_tuning/jobs/ft-AF1WoRqd3aJAHsqc9NY7iL8F/events?after=example&limit=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [POST] /fine_tuning/alpha/graders/run
TAGS: Fine-tuning
SUMMARY: Run grader
DESCRIPTION: Run a grader.

AUTH: BEARER token

REQUEST
  Body:
  Content-Type: application/json
    - grader: object (required) — The grader used for the fine-tuning job.
    - item: object (optional) — The dataset item provided to the grader. This will be used t...
    - model_sample: string (required) — The model sample to be evaluated. This value will be used to...

RESPONSES
  - 200 (application/json): OK
        - reward: number (required)
        - metadata: object (7 fields) (required)
        - sub_rewards: object (required)
        - model_grader_token_usage_per_model: object (required)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/fine_tuning/alpha/graders/run" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /fine_tuning/alpha/graders/validate
TAGS: Fine-tuning
SUMMARY: Validate grader
DESCRIPTION: Validate a grader.

AUTH: BEARER token

REQUEST
  Body:
  Content-Type: application/json
    - grader: object (required) — The grader used for the fine-tuning job.

RESPONSES
  - 200 (application/json): OK
        - grader: object (optional) — The grader used for the fine-tuning job.

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/fine_tuning/alpha/graders/validate" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions
TAGS: Fine-tuning
SUMMARY: Create checkpoint permissions
DESCRIPTION: **NOTE:** Calling this endpoint requires an [admin API key](../admin-api-keys).

This enables organization owners to share fine-tuned models with other projects in their organization.

AUTH: BEARER token

REQUEST
  Path params:
  - fine_tuned_model_checkpoint (string, required)
  Body:
  Content-Type: application/json
    - project_ids: array<string> (required) — The project identifiers to grant access to.

RESPONSES
  - 200 (application/json): OK
        - data: array<object (4 fields)> (required)
        - object: string (enum: list) (required)
        - first_id: object (optional)
        - last_id: object (optional)
        - has_more: boolean (required)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/fine_tuning/checkpoints/ft:gpt-4o-mini-2024-07-18:org:weather:B7R9VjQd/permissions" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /fine_tuning/jobs
TAGS: Fine-tuning
SUMMARY: Create fine-tuning job
DESCRIPTION: Creates a fine-tuning job which begins the process of creating a new model from a given dataset.

Response includes details of the enqueued job including job status and the name of the fine-tuned mode... (see full docs)
AUTH: BEARER token

REQUEST
  Body:
  Content-Type: application/json
    - model: object (required) — The name of the model to fine-tune. You can select one of th...
    - training_file: string (required) — The ID of an uploaded file that contains training data.

See...
    - hyperparameters: object (3 fields) (optional) — The hyperparameters used for the fine-tuning job.
This value...
    - suffix: string (optional) — A string of up to 64 characters that will be added to your f...
    - validation_file: string (optional) — The ID of an uploaded file that contains validation data.

I...
    - integrations: array<object (2 fields)> (optional) — A list of integrations to enable for your fine-tuning job.
    - seed: integer (optional) — The seed controls the reproducibility of the job. Passing in...
    - method: object (4 fields) (optional) — The method used for fine-tuning.
    - metadata: object (optional)

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The object identifier, which can be referenced in the API en...
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the fine-tuning job...
        - error: object (required)
        - fine_tuned_model: object (required)
        - finished_at: object (required)
        - hyperparameters: object (3 fields) (required) — The hyperparameters used for the fine-tuning job. This value...
        - model: string (required) — The base model that is being fine-tuned.
        - object: string (enum: fine_tuning.job) (required) — The object type, which is always "fine_tuning.job".
        - organization_id: string (required) — The organization that owns the fine-tuning job.
        - result_files: array<string> (required) — The compiled results file ID(s) for the fine-tuning job. You...
        - status: string (enum: validating_files, queued, running, succeeded, failed...) (required) — The current status of the fine-tuning job, which can be eith...
        - trained_tokens: object (required)
        - training_file: string (required) — The file ID used for training. You can retrieve the training...
        - validation_file: object (required)
        - integrations: object (optional)
        - seed: integer (required) — The seed used for the fine-tuning job.
        - estimated_finish: object (optional)
        - method: object (4 fields) (optional) — The method used for fine-tuning.
        - metadata: object (optional)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/fine_tuning/jobs" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /fine_tuning/jobs/{fine_tuning_job_id}/cancel
TAGS: Fine-tuning
SUMMARY: Cancel fine-tuning
DESCRIPTION: Immediately cancel a fine-tune job.

AUTH: BEARER token

REQUEST
  Path params:
  - fine_tuning_job_id (string, required)

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The object identifier, which can be referenced in the API en...
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the fine-tuning job...
        - error: object (required)
        - fine_tuned_model: object (required)
        - finished_at: object (required)
        - hyperparameters: object (3 fields) (required) — The hyperparameters used for the fine-tuning job. This value...
        - model: string (required) — The base model that is being fine-tuned.
        - object: string (enum: fine_tuning.job) (required) — The object type, which is always "fine_tuning.job".
        - organization_id: string (required) — The organization that owns the fine-tuning job.
        - result_files: array<string> (required) — The compiled results file ID(s) for the fine-tuning job. You...
        - status: string (enum: validating_files, queued, running, succeeded, failed...) (required) — The current status of the fine-tuning job, which can be eith...
        - trained_tokens: object (required)
        - training_file: string (required) — The file ID used for training. You can retrieve the training...
        - validation_file: object (required)
        - integrations: object (optional)
        - seed: integer (required) — The seed used for the fine-tuning job.
        - estimated_finish: object (optional)
        - method: object (4 fields) (optional) — The method used for fine-tuning.
        - metadata: object (optional)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/fine_tuning/jobs/ft-AF1WoRqd3aJAHsqc9NY7iL8F/cancel" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [POST] /fine_tuning/jobs/{fine_tuning_job_id}/pause
TAGS: Fine-tuning
SUMMARY: Pause fine-tuning
DESCRIPTION: Pause a fine-tune job.

AUTH: BEARER token

REQUEST
  Path params:
  - fine_tuning_job_id (string, required)

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The object identifier, which can be referenced in the API en...
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the fine-tuning job...
        - error: object (required)
        - fine_tuned_model: object (required)
        - finished_at: object (required)
        - hyperparameters: object (3 fields) (required) — The hyperparameters used for the fine-tuning job. This value...
        - model: string (required) — The base model that is being fine-tuned.
        - object: string (enum: fine_tuning.job) (required) — The object type, which is always "fine_tuning.job".
        - organization_id: string (required) — The organization that owns the fine-tuning job.
        - result_files: array<string> (required) — The compiled results file ID(s) for the fine-tuning job. You...
        - status: string (enum: validating_files, queued, running, succeeded, failed...) (required) — The current status of the fine-tuning job, which can be eith...
        - trained_tokens: object (required)
        - training_file: string (required) — The file ID used for training. You can retrieve the training...
        - validation_file: object (required)
        - integrations: object (optional)
        - seed: integer (required) — The seed used for the fine-tuning job.
        - estimated_finish: object (optional)
        - method: object (4 fields) (optional) — The method used for fine-tuning.
        - metadata: object (optional)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/fine_tuning/jobs/ft-AF1WoRqd3aJAHsqc9NY7iL8F/pause" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [POST] /fine_tuning/jobs/{fine_tuning_job_id}/resume
TAGS: Fine-tuning
SUMMARY: Resume fine-tuning
DESCRIPTION: Resume a fine-tune job.

AUTH: BEARER token

REQUEST
  Path params:
  - fine_tuning_job_id (string, required)

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The object identifier, which can be referenced in the API en...
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the fine-tuning job...
        - error: object (required)
        - fine_tuned_model: object (required)
        - finished_at: object (required)
        - hyperparameters: object (3 fields) (required) — The hyperparameters used for the fine-tuning job. This value...
        - model: string (required) — The base model that is being fine-tuned.
        - object: string (enum: fine_tuning.job) (required) — The object type, which is always "fine_tuning.job".
        - organization_id: string (required) — The organization that owns the fine-tuning job.
        - result_files: array<string> (required) — The compiled results file ID(s) for the fine-tuning job. You...
        - status: string (enum: validating_files, queued, running, succeeded, failed...) (required) — The current status of the fine-tuning job, which can be eith...
        - trained_tokens: object (required)
        - training_file: string (required) — The file ID used for training. You can retrieve the training...
        - validation_file: object (required)
        - integrations: object (optional)
        - seed: integer (required) — The seed used for the fine-tuning job.
        - estimated_finish: object (optional)
        - method: object (4 fields) (optional) — The method used for fine-tuning.
        - metadata: object (optional)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/fine_tuning/jobs/ft-AF1WoRqd3aJAHsqc9NY7iL8F/resume" \
  -H "Authorization: Bearer $TOKEN"
================================================================================

### Tag: Images
================================================================================
ENDPOINT: [POST] /images/edits
TAGS: Images
SUMMARY: Create image edit
DESCRIPTION: Creates an edited or extended image given one or more source images and a prompt. This endpoint only supports `gpt-image-1` and `dall-e-2`.
AUTH: BEARER token

REQUEST
  Body:
  Content-Type: multipart/form-data
    - image: object (required) — The image(s) to edit. Must be a supported image file or an a...
    - prompt: string (required) — A text description of the desired image(s). The maximum leng...
    - mask: string (binary) (optional) — An additional image whose fully transparent areas (e.g. wher...
    - background: string (enum: transparent, opaque, auto) (optional) — Allows to set transparency for the background of the generat...
    - model: object (optional) — The model to use for image generation. Only `dall-e-2` and `...
    - n: integer (optional) — The number of images to generate. Must be between 1 and 10.
    - size: string (enum: 256x256, 512x512, 1024x1024, 1536x1024, 1024x1536...) (optional) — The size of the generated images. Must be one of `1024x1024`...
    - response_format: string (enum: url, b64_json) (optional) — The format in which the generated images are returned. Must ...
    - output_format: string (enum: png, jpeg, webp) (optional) — The format in which the generated images are returned. This ...
    - output_compression: integer (optional) — The compression level (0-100%) for the generated images. Thi...
    - user: string (optional) — A unique identifier representing your end-user, which can he...
    - input_fidelity: object (optional)
    - stream: boolean (optional) — Edit the image in streaming mode. Defaults to `false`. See t...
    - partial_images: object (optional)
    - quality: string (enum: standard, low, medium, high, auto) (optional) — The quality of the image that will be generated. `high`, `me...

RESPONSES
  - 200 (application/json): OK
        - created: integer (required) — The Unix timestamp (in seconds) of when the image was create...
        - data: array<object (3 fields)> (optional) — The list of generated images.
        - background: string (enum: transparent, opaque) (optional) — The background parameter used for the image generation. Eith...
        - output_format: string (enum: png, webp, jpeg) (optional) — The output format of the image generation. Either `png`, `we...
        - size: string (enum: 1024x1024, 1024x1536, 1536x1024) (optional) — The size of the image generated. Either `1024x1024`, `1024x1...
        - quality: string (enum: low, medium, high) (optional) — The quality of the image generated. Either `low`, `medium`, ...
        - usage: object (4 fields) (optional) — For `gpt-image-1` only, the token usage information for the ...
  - 200 (text/event-stream): OK
        (empty)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/images/edits" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [POST] /images/generations
TAGS: Images
SUMMARY: Create image
DESCRIPTION: Creates an image given a prompt. [Learn more](https://platform.openai.com/docs/guides/images).

AUTH: BEARER token

REQUEST
  Body:
  Content-Type: application/json
    - prompt: string (required) — A text description of the desired image(s). The maximum leng...
    - model: object (optional) — The model to use for image generation. One of `dall-e-2`, `d...
    - n: integer (optional) — The number of images to generate. Must be between 1 and 10. ...
    - quality: string (enum: standard, hd, low, medium, high...) (optional) — The quality of the image that will be generated.

- `auto` (...
    - response_format: string (enum: url, b64_json) (optional) — The format in which generated images with `dall-e-2` and `da...
    - output_format: string (enum: png, jpeg, webp) (optional) — The format in which the generated images are returned. This ...
    - output_compression: integer (optional) — The compression level (0-100%) for the generated images. Thi...
    - stream: boolean (optional) — Generate the image in streaming mode. Defaults to `false`. S...
    - partial_images: object (optional)
    - size: string (enum: auto, 1024x1024, 1536x1024, 1024x1536, 256x256...) (optional) — The size of the generated images. Must be one of `1024x1024`...
    - moderation: string (enum: low, auto) (optional) — Control the content-moderation level for images generated by...
    - background: string (enum: transparent, opaque, auto) (optional) — Allows to set transparency for the background of the generat...
    - style: string (enum: vivid, natural) (optional) — The style of the generated images. This parameter is only su...
    - user: string (optional) — A unique identifier representing your end-user, which can he...

RESPONSES
  - 200 (application/json): OK
        - created: integer (required) — The Unix timestamp (in seconds) of when the image was create...
        - data: array<object (3 fields)> (optional) — The list of generated images.
        - background: string (enum: transparent, opaque) (optional) — The background parameter used for the image generation. Eith...
        - output_format: string (enum: png, webp, jpeg) (optional) — The output format of the image generation. Either `png`, `we...
        - size: string (enum: 1024x1024, 1024x1536, 1536x1024) (optional) — The size of the image generated. Either `1024x1024`, `1024x1...
        - quality: string (enum: low, medium, high) (optional) — The quality of the image generated. Either `low`, `medium`, ...
        - usage: object (4 fields) (optional) — For `gpt-image-1` only, the token usage information for the ...
  - 200 (text/event-stream): OK
        (empty)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/images/generations" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /images/variations
TAGS: Images
SUMMARY: Create image variation
DESCRIPTION: Creates a variation of a given image. This endpoint only supports `dall-e-2`.
AUTH: BEARER token

REQUEST
  Body:
  Content-Type: multipart/form-data
    - image: string (binary) (required) — The image to use as the basis for the variation(s). Must be ...
    - model: object (optional) — The model to use for image generation. Only `dall-e-2` is su...
    - n: integer (optional) — The number of images to generate. Must be between 1 and 10.
    - response_format: string (enum: url, b64_json) (optional) — The format in which the generated images are returned. Must ...
    - size: string (enum: 256x256, 512x512, 1024x1024) (optional) — The size of the generated images. Must be one of `256x256`, ...
    - user: string (optional) — A unique identifier representing your end-user, which can he...

RESPONSES
  - 200 (application/json): OK
        - created: integer (required) — The Unix timestamp (in seconds) of when the image was create...
        - data: array<object (3 fields)> (optional) — The list of generated images.
        - background: string (enum: transparent, opaque) (optional) — The background parameter used for the image generation. Eith...
        - output_format: string (enum: png, webp, jpeg) (optional) — The output format of the image generation. Either `png`, `we...
        - size: string (enum: 1024x1024, 1024x1536, 1536x1024) (optional) — The size of the image generated. Either `1024x1024`, `1024x1...
        - quality: string (enum: low, medium, high) (optional) — The quality of the image generated. Either `low`, `medium`, ...
        - usage: object (4 fields) (optional) — For `gpt-image-1` only, the token usage information for the ...

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/images/variations" \
  -H "Authorization: Bearer $TOKEN"
================================================================================

### Tag: Invites
================================================================================
ENDPOINT: [DELETE] /organization/invites/{invite_id}
TAGS: Invites
SUMMARY: Delete invite
DESCRIPTION: Delete an invite. If the invite has already been accepted, it cannot be deleted.
AUTH: BEARER token

REQUEST
  Path params:
  - invite_id (string, required)

RESPONSES
  - 200 (application/json): Invite deleted successfully.
        - object: string (enum: organization.invite.deleted) (required) — The object type, which is always `organization.invite.delete...
        - id: string (required)
        - deleted: boolean (required)

EXAMPLE (curl)
curl -X DELETE \
  "https://api.openai.com/v1/organization/invites/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /organization/invites
TAGS: Invites
SUMMARY: List invites
DESCRIPTION: Returns a list of invites in the organization.
AUTH: BEARER token

REQUEST
  Query params:
  - limit (integer, optional)
  - after (string, optional)

RESPONSES
  - 200 (application/json): Invites listed successfully.
        - object: string (enum: list) (required) — The object type, which is always `list`
        - data: array<object (9 fields)> (required)
        - first_id: string (optional) — The first `invite_id` in the retrieved `list`
        - last_id: string (optional) — The last `invite_id` in the retrieved `list`
        - has_more: boolean (optional) — The `has_more` property is used for pagination to indicate t...

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/organization/invites?limit=example&after=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /organization/invites/{invite_id}
TAGS: Invites
SUMMARY: Retrieve invite
DESCRIPTION: Retrieves an invite.
AUTH: BEARER token

REQUEST
  Path params:
  - invite_id (string, required)

RESPONSES
  - 200 (application/json): Invite retrieved successfully.
        - object: string (enum: organization.invite) (required) — The object type, which is always `organization.invite`
        - id: string (required) — The identifier, which can be referenced in API endpoints
        - email: string (required) — The email address of the individual to whom the invite was s...
        - role: string (enum: owner, reader) (required) — `owner` or `reader`
        - status: string (enum: accepted, expired, pending) (required) — `accepted`,`expired`, or `pending`
        - invited_at: integer (required) — The Unix timestamp (in seconds) of when the invite was sent.
        - expires_at: integer (required) — The Unix timestamp (in seconds) of when the invite expires.
        - accepted_at: integer (optional) — The Unix timestamp (in seconds) of when the invite was accep...
        - projects: array<object (2 fields)> (optional) — The projects that were granted membership upon acceptance of...

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/organization/invites/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [POST] /organization/invites
TAGS: Invites
SUMMARY: Create invite
DESCRIPTION: Create an invite for a user to the organization. The invite must be accepted by the user before they have access to the organization.
AUTH: BEARER token

REQUEST
  Body:
  Content-Type: application/json
    - email: string (required) — Send an email to this address
    - role: string (enum: reader, owner) (required) — `owner` or `reader`
    - projects: array<object (2 fields)> (optional) — An array of projects to which membership is granted at the s...

RESPONSES
  - 200 (application/json): User invited successfully.
        - object: string (enum: organization.invite) (required) — The object type, which is always `organization.invite`
        - id: string (required) — The identifier, which can be referenced in API endpoints
        - email: string (required) — The email address of the individual to whom the invite was s...
        - role: string (enum: owner, reader) (required) — `owner` or `reader`
        - status: string (enum: accepted, expired, pending) (required) — `accepted`,`expired`, or `pending`
        - invited_at: integer (required) — The Unix timestamp (in seconds) of when the invite was sent.
        - expires_at: integer (required) — The Unix timestamp (in seconds) of when the invite expires.
        - accepted_at: integer (optional) — The Unix timestamp (in seconds) of when the invite was accep...
        - projects: array<object (2 fields)> (optional) — The projects that were granted membership upon acceptance of...

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/organization/invites" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================

### Tag: Models
================================================================================
ENDPOINT: [DELETE] /models/{model}
TAGS: Models
SUMMARY: Delete a fine-tuned model
DESCRIPTION: Delete a fine-tuned model. You must have the Owner role in your organization to delete a model.
AUTH: BEARER token

REQUEST
  Path params:
  - model (string, required)

RESPONSES
  - 200 (application/json): OK
        - id: string (required)
        - deleted: boolean (required)
        - object: string (required)

EXAMPLE (curl)
curl -X DELETE \
  "https://api.openai.com/v1/models/ft:gpt-4o-mini:acemeco:suffix:abc123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /models
TAGS: Models
SUMMARY: List models
DESCRIPTION: Lists the currently available models, and provides basic information about each one such as the owner and availability.
AUTH: BEARER token

REQUEST
  none

RESPONSES
  - 200 (application/json): OK
        - object: string (enum: list) (required)
        - data: array<object (4 fields)> (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/models" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /models/{model}
TAGS: Models
SUMMARY: Retrieve model
DESCRIPTION: Retrieves a model instance, providing basic information about the model such as the owner and permissioning.
AUTH: BEARER token

REQUEST
  Path params:
  - model (string, required)

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The model identifier, which can be referenced in the API end...
        - created: integer (required) — The Unix timestamp (in seconds) when the model was created.
        - object: string (enum: model) (required) — The object type, which is always "model".
        - owned_by: string (required) — The organization that owns the model.

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/models/gpt-4o-mini" \
  -H "Authorization: Bearer $TOKEN"
================================================================================

### Tag: Moderations
================================================================================
ENDPOINT: [POST] /moderations
TAGS: Moderations
SUMMARY: Create moderation
DESCRIPTION: Classifies if text and/or image inputs are potentially harmful. Learn
more in the [moderation guide](https://platform.openai.com/docs/guides/moderation).

AUTH: BEARER token

REQUEST
  Body:
  Content-Type: application/json
    - input: object (required) — Input (or inputs) to classify. Can be a single string, an ar...
    - model: object (optional) — The content moderation model you would like to use. Learn mo...

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The unique identifier for the moderation request.
        - model: string (required) — The model used to generate the moderation results.
        - results: array<object (4 fields)> (required) — A list of moderation objects.

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/moderations" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================

### Tag: Projects
================================================================================
ENDPOINT: [DELETE] /organization/projects/{project_id}/api_keys/{key_id}
TAGS: Projects
SUMMARY: Delete project API key
DESCRIPTION: Deletes an API key from the project.
AUTH: BEARER token

REQUEST
  Path params:
  - project_id (string, required)
  - key_id (string, required)

RESPONSES
  - 200 (application/json): Project API key deleted successfully.
        - object: string (enum: organization.project.api_key.deleted) (required)
        - id: string (required)
        - deleted: boolean (required)
  - 400 (application/json): Error response for various conditions.
        - error: object (4 fields) (required)

EXAMPLE (curl)
curl -X DELETE \
  "https://api.openai.com/v1/organization/projects/123/api_keys/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [DELETE] /organization/projects/{project_id}/service_accounts/{service_account_id}
TAGS: Projects
SUMMARY: Delete project service account
DESCRIPTION: Deletes a service account from the project.
AUTH: BEARER token

REQUEST
  Path params:
  - project_id (string, required)
  - service_account_id (string, required)

RESPONSES
  - 200 (application/json): Project service account deleted successfully.
        - object: string (enum: organization.project.service_account.deleted) (required)
        - id: string (required)
        - deleted: boolean (required)

EXAMPLE (curl)
curl -X DELETE \
  "https://api.openai.com/v1/organization/projects/123/service_accounts/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [DELETE] /organization/projects/{project_id}/users/{user_id}
TAGS: Projects
SUMMARY: Delete project user
DESCRIPTION: Deletes a user from the project.
AUTH: BEARER token

REQUEST
  Path params:
  - project_id (string, required)
  - user_id (string, required)

RESPONSES
  - 200 (application/json): Project user deleted successfully.
        - object: string (enum: organization.project.user.deleted) (required)
        - id: string (required)
        - deleted: boolean (required)
  - 400 (application/json): Error response for various conditions.
        - error: object (4 fields) (required)

EXAMPLE (curl)
curl -X DELETE \
  "https://api.openai.com/v1/organization/projects/123/users/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /organization/projects
TAGS: Projects
SUMMARY: List projects
DESCRIPTION: Returns a list of projects.
AUTH: BEARER token

REQUEST
  Query params:
  - limit (integer, optional)
  - after (string, optional)
  - include_archived (boolean, optional)

RESPONSES
  - 200 (application/json): Projects listed successfully.
        - object: string (enum: list) (required)
        - data: array<object (6 fields)> (required)
        - first_id: string (required)
        - last_id: string (required)
        - has_more: boolean (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/organization/projects?limit=example&after=example&include_archived=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /organization/projects/{project_id}
TAGS: Projects
SUMMARY: Retrieve project
DESCRIPTION: Retrieves a project.
AUTH: BEARER token

REQUEST
  Path params:
  - project_id (string, required)

RESPONSES
  - 200 (application/json): Project retrieved successfully.
        - id: string (required) — The identifier, which can be referenced in API endpoints
        - object: string (enum: organization.project) (required) — The object type, which is always `organization.project`
        - name: string (required) — The name of the project. This appears in reporting.
        - created_at: integer (required) — The Unix timestamp (in seconds) of when the project was crea...
        - archived_at: object (optional)
        - status: string (enum: active, archived) (required) — `active` or `archived`

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/organization/projects/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /organization/projects/{project_id}/api_keys
TAGS: Projects
SUMMARY: List project API keys
DESCRIPTION: Returns a list of API keys in the project.
AUTH: BEARER token

REQUEST
  Path params:
  - project_id (string, required)
  Query params:
  - limit (integer, optional)
  - after (string, optional)

RESPONSES
  - 200 (application/json): Project API keys listed successfully.
        - object: string (enum: list) (required)
        - data: array<object (7 fields)> (required)
        - first_id: string (required)
        - last_id: string (required)
        - has_more: boolean (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/organization/projects/123/api_keys?limit=example&after=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /organization/projects/{project_id}/api_keys/{key_id}
TAGS: Projects
SUMMARY: Retrieve project API key
DESCRIPTION: Retrieves an API key in the project.
AUTH: BEARER token

REQUEST
  Path params:
  - project_id (string, required)
  - key_id (string, required)

RESPONSES
  - 200 (application/json): Project API key retrieved successfully.
        - object: string (enum: organization.project.api_key) (required) — The object type, which is always `organization.project.api_k...
        - redacted_value: string (required) — The redacted value of the API key
        - name: string (required) — The name of the API key
        - created_at: integer (required) — The Unix timestamp (in seconds) of when the API key was crea...
        - last_used_at: integer (required) — The Unix timestamp (in seconds) of when the API key was last...
        - id: string (required) — The identifier, which can be referenced in API endpoints
        - owner: object (3 fields) (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/organization/projects/123/api_keys/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /organization/projects/{project_id}/rate_limits
TAGS: Projects
SUMMARY: List project rate limits
DESCRIPTION: Returns the rate limits per model for a project.
AUTH: BEARER token

REQUEST
  Path params:
  - project_id (string, required)
  Query params:
  - limit (integer, optional)
  - after (string, optional)
  - before (string, optional)

RESPONSES
  - 200 (application/json): Project rate limits listed successfully.
        - object: string (enum: list) (required)
        - data: array<object (9 fields)> (required)
        - first_id: string (required)
        - last_id: string (required)
        - has_more: boolean (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/organization/projects/123/rate_limits?limit=example&after=example&before=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /organization/projects/{project_id}/service_accounts
TAGS: Projects
SUMMARY: List project service accounts
DESCRIPTION: Returns a list of service accounts in the project.
AUTH: BEARER token

REQUEST
  Path params:
  - project_id (string, required)
  Query params:
  - limit (integer, optional)
  - after (string, optional)

RESPONSES
  - 200 (application/json): Project service accounts listed successfully.
        - object: string (enum: list) (required)
        - data: array<object (5 fields)> (required)
        - first_id: string (required)
        - last_id: string (required)
        - has_more: boolean (required)
  - 400 (application/json): Error response when project is archived.
        - error: object (4 fields) (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/organization/projects/123/service_accounts?limit=example&after=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /organization/projects/{project_id}/service_accounts/{service_account_id}
TAGS: Projects
SUMMARY: Retrieve project service account
DESCRIPTION: Retrieves a service account in the project.
AUTH: BEARER token

REQUEST
  Path params:
  - project_id (string, required)
  - service_account_id (string, required)

RESPONSES
  - 200 (application/json): Project service account retrieved successfully.
        - object: string (enum: organization.project.service_account) (required) — The object type, which is always `organization.project.servi...
        - id: string (required) — The identifier, which can be referenced in API endpoints
        - name: string (required) — The name of the service account
        - role: string (enum: owner, member) (required) — `owner` or `member`
        - created_at: integer (required) — The Unix timestamp (in seconds) of when the service account ...

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/organization/projects/123/service_accounts/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /organization/projects/{project_id}/users
TAGS: Projects
SUMMARY: List project users
DESCRIPTION: Returns a list of users in the project.
AUTH: BEARER token

REQUEST
  Path params:
  - project_id (string, required)
  Query params:
  - limit (integer, optional)
  - after (string, optional)

RESPONSES
  - 200 (application/json): Project users listed successfully.
        - object: string (required)
        - data: array<object (6 fields)> (required)
        - first_id: string (required)
        - last_id: string (required)
        - has_more: boolean (required)
  - 400 (application/json): Error response when project is archived.
        - error: object (4 fields) (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/organization/projects/123/users?limit=example&after=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /organization/projects/{project_id}/users/{user_id}
TAGS: Projects
SUMMARY: Retrieve project user
DESCRIPTION: Retrieves a user in the project.
AUTH: BEARER token

REQUEST
  Path params:
  - project_id (string, required)
  - user_id (string, required)

RESPONSES
  - 200 (application/json): Project user retrieved successfully.
        - object: string (enum: organization.project.user) (required) — The object type, which is always `organization.project.user`
        - id: string (required) — The identifier, which can be referenced in API endpoints
        - name: string (required) — The name of the user
        - email: string (required) — The email address of the user
        - role: string (enum: owner, member) (required) — `owner` or `member`
        - added_at: integer (required) — The Unix timestamp (in seconds) of when the project was adde...

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/organization/projects/123/users/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [POST] /organization/projects
TAGS: Projects
SUMMARY: Create project
DESCRIPTION: Create a new project in the organization. Projects can be created and archived, but cannot be deleted.
AUTH: BEARER token

REQUEST
  Body:
  Content-Type: application/json
    - name: string (required) — The friendly name of the project, this name appears in repor...
    - geography: string (enum: US, EU, JP, IN, KR...) (optional) — Create the project with the specified data residency region....

RESPONSES
  - 200 (application/json): Project created successfully.
        - id: string (required) — The identifier, which can be referenced in API endpoints
        - object: string (enum: organization.project) (required) — The object type, which is always `organization.project`
        - name: string (required) — The name of the project. This appears in reporting.
        - created_at: integer (required) — The Unix timestamp (in seconds) of when the project was crea...
        - archived_at: object (optional)
        - status: string (enum: active, archived) (required) — `active` or `archived`

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/organization/projects" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /organization/projects/{project_id}
TAGS: Projects
SUMMARY: Modify project
DESCRIPTION: Modifies a project in the organization.
AUTH: BEARER token

REQUEST
  Path params:
  - project_id (string, required)
  Body:
  Content-Type: application/json
    - name: string (required) — The updated name of the project, this name appears in report...

RESPONSES
  - 200 (application/json): Project updated successfully.
        - id: string (required) — The identifier, which can be referenced in API endpoints
        - object: string (enum: organization.project) (required) — The object type, which is always `organization.project`
        - name: string (required) — The name of the project. This appears in reporting.
        - created_at: integer (required) — The Unix timestamp (in seconds) of when the project was crea...
        - archived_at: object (optional)
        - status: string (enum: active, archived) (required) — `active` or `archived`
  - 400 (application/json): Error response when updating the default project.
        - error: object (4 fields) (required)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/organization/projects/123" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /organization/projects/{project_id}/archive
TAGS: Projects
SUMMARY: Archive project
DESCRIPTION: Archives a project in the organization. Archived projects cannot be used or updated.
AUTH: BEARER token

REQUEST
  Path params:
  - project_id (string, required)

RESPONSES
  - 200 (application/json): Project archived successfully.
        - id: string (required) — The identifier, which can be referenced in API endpoints
        - object: string (enum: organization.project) (required) — The object type, which is always `organization.project`
        - name: string (required) — The name of the project. This appears in reporting.
        - created_at: integer (required) — The Unix timestamp (in seconds) of when the project was crea...
        - archived_at: object (optional)
        - status: string (enum: active, archived) (required) — `active` or `archived`

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/organization/projects/123/archive" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [POST] /organization/projects/{project_id}/rate_limits/{rate_limit_id}
TAGS: Projects
SUMMARY: Modify project rate limit
DESCRIPTION: Updates a project rate limit.
AUTH: BEARER token

REQUEST
  Path params:
  - project_id (string, required)
  - rate_limit_id (string, required)
  Body:
  Content-Type: application/json
    - max_requests_per_1_minute: integer (optional) — The maximum requests per minute.
    - max_tokens_per_1_minute: integer (optional) — The maximum tokens per minute.
    - max_images_per_1_minute: integer (optional) — The maximum images per minute. Only relevant for certain mod...
    - max_audio_megabytes_per_1_minute: integer (optional) — The maximum audio megabytes per minute. Only relevant for ce...
    - max_requests_per_1_day: integer (optional) — The maximum requests per day. Only relevant for certain mode...
    - batch_1_day_max_input_tokens: integer (optional) — The maximum batch input tokens per day. Only relevant for ce...

RESPONSES
  - 200 (application/json): Project rate limit updated successfully.
        - object: string (enum: project.rate_limit) (required) — The object type, which is always `project.rate_limit`
        - id: string (required) — The identifier, which can be referenced in API endpoints.
        - model: string (required) — The model this rate limit applies to.
        - max_requests_per_1_minute: integer (required) — The maximum requests per minute.
        - max_tokens_per_1_minute: integer (required) — The maximum tokens per minute.
        - max_images_per_1_minute: integer (optional) — The maximum images per minute. Only present for relevant mod...
        - max_audio_megabytes_per_1_minute: integer (optional) — The maximum audio megabytes per minute. Only present for rel...
        - max_requests_per_1_day: integer (optional) — The maximum requests per day. Only present for relevant mode...
        - batch_1_day_max_input_tokens: integer (optional) — The maximum batch input tokens per day. Only present for rel...
  - 400 (application/json): Error response for various conditions.
        - error: object (4 fields) (required)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/organization/projects/123/rate_limits/123" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /organization/projects/{project_id}/service_accounts
TAGS: Projects
SUMMARY: Create project service account
DESCRIPTION: Creates a new service account in the project. This also returns an unredacted API key for the service account.
AUTH: BEARER token

REQUEST
  Path params:
  - project_id (string, required)
  Body:
  Content-Type: application/json
    - name: string (required) — The name of the service account being created.

RESPONSES
  - 200 (application/json): Project service account created successfully.
        - object: string (enum: organization.project.service_account) (required)
        - id: string (required)
        - name: string (required)
        - role: string (enum: member) (required) — Service accounts can only have one role of type `member`
        - created_at: integer (required)
        - api_key: object (5 fields) (required)
  - 400 (application/json): Error response when project is archived.
        - error: object (4 fields) (required)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/organization/projects/123/service_accounts" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /organization/projects/{project_id}/users
TAGS: Projects
SUMMARY: Create project user
DESCRIPTION: Adds a user to the project. Users must already be members of the organization to be added to a project.
AUTH: BEARER token

REQUEST
  Path params:
  - project_id (string, required)
  Body:
  Content-Type: application/json
    - user_id: string (required) — The ID of the user.
    - role: string (enum: owner, member) (required) — `owner` or `member`

RESPONSES
  - 200 (application/json): User added to project successfully.
        - object: string (enum: organization.project.user) (required) — The object type, which is always `organization.project.user`
        - id: string (required) — The identifier, which can be referenced in API endpoints
        - name: string (required) — The name of the user
        - email: string (required) — The email address of the user
        - role: string (enum: owner, member) (required) — `owner` or `member`
        - added_at: integer (required) — The Unix timestamp (in seconds) of when the project was adde...
  - 400 (application/json): Error response for various conditions.
        - error: object (4 fields) (required)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/organization/projects/123/users" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /organization/projects/{project_id}/users/{user_id}
TAGS: Projects
SUMMARY: Modify project user
DESCRIPTION: Modifies a user's role in the project.
AUTH: BEARER token

REQUEST
  Path params:
  - project_id (string, required)
  - user_id (string, required)
  Body:
  Content-Type: application/json
    - role: string (enum: owner, member) (required) — `owner` or `member`

RESPONSES
  - 200 (application/json): Project user's role updated successfully.
        - object: string (enum: organization.project.user) (required) — The object type, which is always `organization.project.user`
        - id: string (required) — The identifier, which can be referenced in API endpoints
        - name: string (required) — The name of the user
        - email: string (required) — The email address of the user
        - role: string (enum: owner, member) (required) — `owner` or `member`
        - added_at: integer (required) — The Unix timestamp (in seconds) of when the project was adde...
  - 400 (application/json): Error response for various conditions.
        - error: object (4 fields) (required)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/organization/projects/123/users/123" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================

### Tag: Realtime
================================================================================
ENDPOINT: [POST] /realtime/calls
TAGS: Realtime
SUMMARY: Create call
DESCRIPTION: Create a new Realtime API call over WebRTC and receive the SDP answer needed
to complete the peer connection.
AUTH: BEARER token

REQUEST
  Body:
  Content-Type: multipart/form-data
    - sdp: string (required) — WebRTC Session Description Protocol (SDP) offer generated by...
    - session: object (optional) — Optional session configuration to apply before the realtime ...
  Content-Type: application/sdp
    string

RESPONSES
  - 201 (application/sdp): Realtime call created successfully.
        string

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/realtime/calls" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [POST] /realtime/calls/{call_id}/accept
TAGS: Realtime
SUMMARY: Accept call
DESCRIPTION: Accept an incoming SIP call and configure the realtime session that will
handle it.
AUTH: BEARER token

REQUEST
  Path params:
  - call_id (string, required)
  Body:
  Content-Type: application/json
    - type: string (enum: realtime) (required) — The type of session to create. Always `realtime` for the Rea...
    - output_modalities: array<string (enum: text, audio)> (optional) — The set of modalities the model can respond with. It default...
    - model: object (optional) — The Realtime model used for this session.

    - instructions: string (optional) — The default system instructions (i.e. system message) prepen...
    - audio: object (2 fields) (optional) — Configuration for input and output audio.

    - include: array<string (enum: item.input_audio_transcription.logprobs)> (optional) — Additional fields to include in server outputs.

`item.input...
    - tracing: object (optional) — Realtime API can write session traces to the [Traces Dashboa...
    - tools: array<object> (optional) — Tools available to the model.
    - tool_choice: object (optional) — How the model chooses tools. Provide one of the string modes...
    - max_output_tokens: object (optional) — Maximum number of output tokens for a single assistant respo...
    - truncation: object (optional) — Controls how the realtime conversation is truncated prior to...
    - prompt: object (optional)

RESPONSES
  - 200: Call accepted successfully.

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/realtime/calls/123/accept" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /realtime/calls/{call_id}/hangup
TAGS: Realtime
SUMMARY: Hang up call
DESCRIPTION: End an active Realtime API call, whether it was initiated over SIP or
WebRTC.
AUTH: BEARER token

REQUEST
  Path params:
  - call_id (string, required)

RESPONSES
  - 200: Call hangup initiated successfully.

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/realtime/calls/123/hangup" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [POST] /realtime/calls/{call_id}/refer
TAGS: Realtime
SUMMARY: Refer call
DESCRIPTION: Transfer an active SIP call to a new destination using the SIP REFER verb.
AUTH: BEARER token

REQUEST
  Path params:
  - call_id (string, required)
  Body:
  Content-Type: application/json
    - target_uri: string (required) — URI that should appear in the SIP Refer-To header. Supports ...

RESPONSES
  - 200: Call referred successfully.

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/realtime/calls/123/refer" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /realtime/calls/{call_id}/reject
TAGS: Realtime
SUMMARY: Reject call
DESCRIPTION: Decline an incoming SIP call by returning a SIP status code to the caller.
AUTH: BEARER token

REQUEST
  Path params:
  - call_id (string, required)
  Body:
  Content-Type: application/json
    - status_code: integer (optional) — SIP response code to send back to the caller. Defaults to `6...

RESPONSES
  - 200: Call rejected successfully.

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/realtime/calls/123/reject" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /realtime/client_secrets
TAGS: Realtime
SUMMARY: Create client secret
DESCRIPTION: Create a Realtime client secret with an associated session configuration.

AUTH: BEARER token

REQUEST
  Body:
  Content-Type: application/json
    - expires_after: object (2 fields) (optional) — Configuration for the client secret expiration. Expiration r...
    - session: object (optional) — Session configuration to use for the client secret. Choose e...

RESPONSES
  - 200 (application/json): Client secret created successfully.
        - value: string (required) — The generated client secret value.
        - expires_at: integer (required) — Expiration timestamp for the client secret, in seconds since...
        - session: object (required) — The session configuration for either a realtime or transcrip...

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/realtime/client_secrets" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /realtime/sessions
TAGS: Realtime
SUMMARY: Create session
DESCRIPTION: Create an ephemeral API token for use in client-side applications with the
Realtime API. Can be configured with the same session parameters as the
`session.update` client event.

It responds with a se... (see full docs)
AUTH: BEARER token

REQUEST
  Body:
  Content-Type: application/json
    - client_secret: object (2 fields) (required) — Ephemeral key returned by the API.
    - modalities: object (optional) — The set of modalities the model can respond with. To disable...
    - instructions: string (optional) — The default system instructions (i.e. system message) prepen...
    - voice: object (optional)
    - input_audio_format: string (optional) — The format of input audio. Options are `pcm16`, `g711_ulaw`,...
    - output_audio_format: string (optional) — The format of output audio. Options are `pcm16`, `g711_ulaw`...
    - input_audio_transcription: object (1 fields) (optional) — Configuration for input audio transcription, defaults to off...
    - speed: number (optional) — The speed of the model's spoken response. 1.0 is the default...
    - tracing: object (optional) — Configuration options for tracing. Set to null to disable tr...
    - turn_detection: object (4 fields) (optional) — Configuration for turn detection. Can be set to `null` to tu...
    - tools: array<object (4 fields)> (optional) — Tools (functions) available to the model.
    - tool_choice: string (optional) — How the model chooses tools. Options are `auto`, `none`, `re...
    - temperature: number (optional) — Sampling temperature for the model, limited to [0.6, 1.2]. D...
    - max_response_output_tokens: object (optional) — Maximum number of output tokens for a single assistant respo...
    - truncation: object (optional) — Controls how the realtime conversation is truncated prior to...
    - prompt: object (optional)

RESPONSES
  - 200 (application/json): Session created successfully.
        - id: string (optional) — Unique identifier for the session that looks like `sess_1234...
        - object: string (optional) — The object type. Always `realtime.session`.
        - expires_at: integer (optional) — Expiration timestamp for the session, in seconds since epoch...
        - include: array<string (enum: item.input_audio_transcription.logprobs)> (optional) — Additional fields to include in server outputs.
- `item.inpu...
        - model: string (optional) — The Realtime model used for this session.
        - output_modalities: object (optional) — The set of modalities the model can respond with. To disable...
        - instructions: string (optional) — The default system instructions (i.e. system message) prepen...
        - audio: object (2 fields) (optional) — Configuration for input and output audio for the session.

        - tracing: object (optional) — Configuration options for tracing. Set to null to disable tr...
        - turn_detection: object (4 fields) (optional) — Configuration for turn detection. Can be set to `null` to tu...
        - tools: array<object (4 fields)> (optional) — Tools (functions) available to the model.
        - tool_choice: string (optional) — How the model chooses tools. Options are `auto`, `none`, `re...
        - max_output_tokens: object (optional) — Maximum number of output tokens for a single assistant respo...

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/realtime/sessions" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /realtime/transcription_sessions
TAGS: Realtime
SUMMARY: Create transcription session
DESCRIPTION: Create an ephemeral API token for use in client-side applications with the
Realtime API specifically for realtime transcriptions. 
Can be configured with the same session parameters as the `transcript... (see full docs)
AUTH: BEARER token

REQUEST
  Body:
  Content-Type: application/json
    - turn_detection: object (4 fields) (optional) — Configuration for turn detection. Can be set to `null` to tu...
    - input_audio_noise_reduction: object (1 fields) (optional) — Configuration for input audio noise reduction. This can be s...
    - input_audio_format: string (enum: pcm16, g711_ulaw, g711_alaw) (optional) — The format of input audio. Options are `pcm16`, `g711_ulaw`,...
    - input_audio_transcription: object (3 fields) (optional)
    - include: array<string (enum: item.input_audio_transcription.logprobs)> (optional) — The set of items to include in the transcription. Current av...

RESPONSES
  - 200 (application/json): Session created successfully.
        - client_secret: object (2 fields) (required) — Ephemeral key returned by the API. Only present when the ses...
        - modalities: object (optional) — The set of modalities the model can respond with. To disable...
        - input_audio_format: string (optional) — The format of input audio. Options are `pcm16`, `g711_ulaw`,...
        - input_audio_transcription: object (3 fields) (optional)
        - turn_detection: object (4 fields) (optional) — Configuration for turn detection. Can be set to `null` to tu...

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/realtime/transcription_sessions" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================

### Tag: Responses
================================================================================
ENDPOINT: [DELETE] /responses/{response_id}
TAGS: Responses
SUMMARY: Delete a model response
DESCRIPTION: Deletes a model response with the given ID.

AUTH: BEARER token

REQUEST
  Path params:
  - response_id (string, required)

RESPONSES
  - 200: OK
  - 404 (application/json): Not Found
        - code: object (required)
        - message: string (required)
        - param: object (required)
        - type: string (required)

EXAMPLE (curl)
curl -X DELETE \
  "https://api.openai.com/v1/responses/resp_677efb5139a88190b512bc3fef8e535d" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /responses/{response_id}
TAGS: Responses
SUMMARY: Get a model response
DESCRIPTION: Retrieves a model response with the given ID.

AUTH: BEARER token

REQUEST
  Path params:
  - response_id (string, required)
  Query params:
  - include (array<string (enum: code_interpreter_call.outputs, computer_call_output.output.image_url, file_search_call.results, message.input_image.image_url, message.output_text.logprobs...)>, optional)
  - stream (boolean, optional)
  - starting_after (integer, optional)
  - include_obfuscation (boolean, optional)

RESPONSES
  - 200 (application/json): OK
        (empty)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/responses/resp_677efb5139a88190b512bc3fef8e535d?include=example&stream=example&starting_after=example&include_obfuscation=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /responses/{response_id}/input_items
TAGS: Responses
SUMMARY: List input items
DESCRIPTION: Returns a list of input items for a given response.
AUTH: BEARER token

REQUEST
  Path params:
  - response_id (string, required)
  Query params:
  - limit (integer, optional)
  - order (string (enum: asc, desc), optional)
  - after (string, optional)
  - include (array<string (enum: code_interpreter_call.outputs, computer_call_output.output.image_url, file_search_call.results, message.input_image.image_url, message.output_text.logprobs...)>, optional)

RESPONSES
  - 200 (application/json): OK
        - object: object (required) — The type of object returned, must be `list`.
        - data: array<object> (required) — A list of items used to generate this response.
        - has_more: boolean (required) — Whether there are more items available.
        - first_id: string (required) — The ID of the first item in the list.
        - last_id: string (required) — The ID of the last item in the list.

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/responses/123/input_items?limit=example&order=example&after=example&include=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [POST] /responses
TAGS: Responses
SUMMARY: Create a model response
DESCRIPTION: Creates a model response. Provide [text](https://platform.openai.com/docs/guides/text) or
[image](https://platform.openai.com/docs/guides/images) inputs to generate [text](https://platform.openai.com/... (see full docs)
AUTH: BEARER token

REQUEST
  Body:
  Content-Type: application/json
    (empty)

RESPONSES
  - 200 (application/json): OK
        (empty)
  - 200 (text/event-stream): OK
        (empty)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/responses" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /responses/{response_id}/cancel
TAGS: Responses
SUMMARY: Cancel a response
DESCRIPTION: Cancels a model response with the given ID. Only responses created with
the `background` parameter set to `true` can be cancelled. 
[Learn more](https://platform.openai.com/docs/guides/background).

AUTH: BEARER token

REQUEST
  Path params:
  - response_id (string, required)

RESPONSES
  - 200 (application/json): OK
        (empty)
  - 404 (application/json): Not Found
        - code: object (required)
        - message: string (required)
        - param: object (required)
        - type: string (required)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/responses/resp_677efb5139a88190b512bc3fef8e535d/cancel" \
  -H "Authorization: Bearer $TOKEN"
================================================================================

### Tag: Untagged
================================================================================
ENDPOINT: [DELETE] /chatkit/threads/{thread_id}
TAGS: Untagged
SUMMARY: Delete ChatKit thread
DESCRIPTION: Delete a ChatKit thread
AUTH: BEARER token

REQUEST
  Path params:
  - thread_id (string, required)

RESPONSES
  - 200 (application/json): Success
        - id: string (required) — Identifier of the deleted thread.
        - object: string (enum: chatkit.thread.deleted) (required) — Type discriminator that is always `chatkit.thread.deleted`.
        - deleted: boolean (required) — Indicates that the thread has been deleted.

EXAMPLE (curl)
curl -X DELETE \
  "https://api.openai.com/v1/chatkit/threads/cthr_123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [DELETE] /containers/{container_id}
TAGS: Untagged
SUMMARY: Delete a container
DESCRIPTION: Delete Container
AUTH: BEARER token

REQUEST
  Path params:
  - container_id (string, required)

RESPONSES
  - 200: OK

EXAMPLE (curl)
curl -X DELETE \
  "https://api.openai.com/v1/containers/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [DELETE] /containers/{container_id}/files/{file_id}
TAGS: Untagged
SUMMARY: Delete a container file
DESCRIPTION: Delete Container File
AUTH: BEARER token

REQUEST
  Path params:
  - container_id (string, required)
  - file_id (string, required)

RESPONSES
  - 200: OK

EXAMPLE (curl)
curl -X DELETE \
  "https://api.openai.com/v1/containers/123/files/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [DELETE] /organization/admin_api_keys/{key_id}
TAGS: Untagged
SUMMARY: Delete admin API key
DESCRIPTION: Delete an organization admin API key
AUTH: BEARER token

REQUEST
  Path params:
  - key_id (string, required)

RESPONSES
  - 200 (application/json): Confirmation that the API key was deleted.
        - id: string (optional)
        - object: string (optional)
        - deleted: boolean (optional)

EXAMPLE (curl)
curl -X DELETE \
  "https://api.openai.com/v1/organization/admin_api_keys/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /chatkit/threads
TAGS: Untagged
SUMMARY: List ChatKit threads
AUTH: BEARER token

REQUEST
  Query params:
  - limit (integer, optional)
  - order (string (enum: asc, desc), optional)
  - after (string, optional)
  - before (string, optional)
  - user (string, optional)

RESPONSES
  - 200 (application/json): Success
        - object: object (required) — The type of object returned, must be `list`.
        - data: array<object (6 fields)> (required) — A list of items
        - first_id: object (required)
        - last_id: object (required)
        - has_more: boolean (required) — Whether there are more items available.

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/chatkit/threads?limit=example&order=example&after=example&before=example&user=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /chatkit/threads/{thread_id}
TAGS: Untagged
SUMMARY: Retrieve ChatKit thread
DESCRIPTION: Retrieve a ChatKit thread
AUTH: BEARER token

REQUEST
  Path params:
  - thread_id (string, required)

RESPONSES
  - 200 (application/json): Success
        - id: string (required) — Identifier of the thread.
        - object: string (enum: chatkit.thread) (required) — Type discriminator that is always `chatkit.thread`.
        - created_at: integer (required) — Unix timestamp (in seconds) for when the thread was created.
        - title: object (required)
        - status: object (required) — Current status for the thread. Defaults to `active` for newl...
        - user: string (required) — Free-form string that identifies your end user who owns the ...

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/chatkit/threads/cthr_123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /chatkit/threads/{thread_id}/items
TAGS: Untagged
SUMMARY: List ChatKit thread items
AUTH: BEARER token

REQUEST
  Path params:
  - thread_id (string, required)
  Query params:
  - limit (integer, optional)
  - order (string (enum: asc, desc), optional)
  - after (string, optional)
  - before (string, optional)

RESPONSES
  - 200 (application/json): Success
        - object: object (required) — The type of object returned, must be `list`.
        - data: array<object> (required) — A list of items
        - first_id: object (required)
        - last_id: object (required)
        - has_more: boolean (required) — Whether there are more items available.

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/chatkit/threads/cthr_123/items?limit=example&order=example&after=example&before=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /containers
TAGS: Untagged
SUMMARY: List containers
DESCRIPTION: List Containers
AUTH: BEARER token

REQUEST
  Query params:
  - limit (integer, optional)
  - order (string (enum: asc, desc), optional)
  - after (string, optional)

RESPONSES
  - 200 (application/json): Success
        - object: object (required) — The type of object returned, must be 'list'.
        - data: array<object (6 fields)> (required) — A list of containers.
        - first_id: string (required) — The ID of the first container in the list.
        - last_id: string (required) — The ID of the last container in the list.
        - has_more: boolean (required) — Whether there are more containers available.

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/containers?limit=example&order=example&after=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /containers/{container_id}
TAGS: Untagged
SUMMARY: Retrieve container
DESCRIPTION: Retrieve Container
AUTH: BEARER token

REQUEST
  Path params:
  - container_id (string, required)

RESPONSES
  - 200 (application/json): Success
        - id: string (required) — Unique identifier for the container.
        - object: string (required) — The type of this object.
        - name: string (required) — Name of the container.
        - created_at: integer (required) — Unix timestamp (in seconds) when the container was created.
        - status: string (required) — Status of the container (e.g., active, deleted).
        - expires_after: object (2 fields) (optional) — The container will expire after this time period.
The anchor...

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/containers/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /containers/{container_id}/files
TAGS: Untagged
SUMMARY: List container files
DESCRIPTION: List Container files
AUTH: BEARER token

REQUEST
  Path params:
  - container_id (string, required)
  Query params:
  - limit (integer, optional)
  - order (string (enum: asc, desc), optional)
  - after (string, optional)

RESPONSES
  - 200 (application/json): Success
        - object: object (required) — The type of object returned, must be 'list'.
        - data: array<object (7 fields)> (required) — A list of container files.
        - first_id: string (required) — The ID of the first file in the list.
        - last_id: string (required) — The ID of the last file in the list.
        - has_more: boolean (required) — Whether there are more files available.

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/containers/123/files?limit=example&order=example&after=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /containers/{container_id}/files/{file_id}
TAGS: Untagged
SUMMARY: Retrieve container file
DESCRIPTION: Retrieve Container File
AUTH: BEARER token

REQUEST
  Path params:
  - container_id (string, required)
  - file_id (string, required)

RESPONSES
  - 200 (application/json): Success
        - id: string (required) — Unique identifier for the file.
        - object: string (required) — The type of this object (`container.file`).
        - container_id: string (required) — The container this file belongs to.
        - created_at: integer (required) — Unix timestamp (in seconds) when the file was created.
        - bytes: integer (required) — Size of the file in bytes.
        - path: string (required) — Path of the file in the container.
        - source: string (required) — Source of the file (e.g., `user`, `assistant`).

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/containers/123/files/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /containers/{container_id}/files/{file_id}/content
TAGS: Untagged
SUMMARY: Retrieve container file content
DESCRIPTION: Retrieve Container File Content
AUTH: BEARER token

REQUEST
  Path params:
  - container_id (string, required)
  - file_id (string, required)

RESPONSES
  - 200: Success

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/containers/123/files/123/content" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /organization/admin_api_keys
TAGS: Untagged
SUMMARY: List all organization and project API keys.
DESCRIPTION: List organization API keys
AUTH: BEARER token

REQUEST
  Query params:
  - after (string, optional)
  - order (string (enum: asc, desc), optional)
  - limit (integer, optional)

RESPONSES
  - 200 (application/json): A list of organization API keys.
        - object: string (optional)
        - data: array<object (8 fields)> (optional)
        - has_more: boolean (optional)
        - first_id: string (optional)
        - last_id: string (optional)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/organization/admin_api_keys?after=example&order=example&limit=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /organization/admin_api_keys/{key_id}
TAGS: Untagged
SUMMARY: Retrieve admin API key
DESCRIPTION: Retrieve a single organization API key
AUTH: BEARER token

REQUEST
  Path params:
  - key_id (string, required)

RESPONSES
  - 200 (application/json): Details of the requested API key.
        - object: string (required) — The object type, which is always `organization.admin_api_key...
        - id: string (required) — The identifier, which can be referenced in API endpoints
        - name: string (required) — The name of the API key
        - redacted_value: string (required) — The redacted value of the API key
        - value: string (optional) — The value of the API key. Only shown on create.
        - created_at: integer (int64) (required) — The Unix timestamp (in seconds) of when the API key was crea...
        - last_used_at: object (required)
        - owner: object (6 fields) (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/organization/admin_api_keys/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [POST] /chatkit/files
TAGS: Untagged
SUMMARY: Upload file to ChatKit
DESCRIPTION: Upload a ChatKit file
AUTH: BEARER token

REQUEST
  Body:
  Content-Type: multipart/form-data
    - file: string (binary) (required) — Binary file contents to store with the ChatKit session. Supp...
  Content-Type: application/json
    - file: string (binary) (required) — Binary file contents to store with the ChatKit session. Supp...

RESPONSES
  - 200 (application/json): Success
        (empty)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/chatkit/files" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /chatkit/sessions
TAGS: Untagged
SUMMARY: Create ChatKit session
DESCRIPTION: Create a ChatKit session
AUTH: BEARER token

REQUEST
  Body:
  Content-Type: application/json
    - workflow: object (4 fields) (required) — Workflow reference and overrides applied to the chat session...
    - user: string (required) — A free-form string that identifies your end user; ensures th...
    - expires_after: object (2 fields) (optional) — Controls when the session expires relative to an anchor time...
    - rate_limits: object (1 fields) (optional) — Controls request rate limits for the session.
    - chatkit_configuration: object (3 fields) (optional) — Optional per-session configuration settings for ChatKit beha...

RESPONSES
  - 200 (application/json): Success
        - id: string (required) — Identifier for the ChatKit session.
        - object: string (enum: chatkit.session) (required) — Type discriminator that is always `chatkit.session`.
        - expires_at: integer (required) — Unix timestamp (in seconds) for when the session expires.
        - client_secret: string (required) — Ephemeral client secret that authenticates session requests.
        - workflow: object (4 fields) (required) — Workflow metadata and state returned for the session.
        - user: string (required) — User identifier associated with the session.
        - rate_limits: object (1 fields) (required) — Active per-minute request limit for the session.
        - max_requests_per_1_minute: integer (required) — Convenience copy of the per-minute request limit.
        - status: string (enum: active, expired, cancelled) (required)
        - chatkit_configuration: object (3 fields) (required) — ChatKit configuration for the session.

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/chatkit/sessions" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /chatkit/sessions/{session_id}/cancel
TAGS: Untagged
SUMMARY: Cancel chat session
DESCRIPTION: Cancel a ChatKit session
AUTH: BEARER token

REQUEST
  Path params:
  - session_id (string, required)

RESPONSES
  - 200 (application/json): Success
        - id: string (required) — Identifier for the ChatKit session.
        - object: string (enum: chatkit.session) (required) — Type discriminator that is always `chatkit.session`.
        - expires_at: integer (required) — Unix timestamp (in seconds) for when the session expires.
        - client_secret: string (required) — Ephemeral client secret that authenticates session requests.
        - workflow: object (4 fields) (required) — Workflow metadata and state returned for the session.
        - user: string (required) — User identifier associated with the session.
        - rate_limits: object (1 fields) (required) — Active per-minute request limit for the session.
        - max_requests_per_1_minute: integer (required) — Convenience copy of the per-minute request limit.
        - status: string (enum: active, expired, cancelled) (required)
        - chatkit_configuration: object (3 fields) (required) — ChatKit configuration for the session.

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/chatkit/sessions/cksess_123/cancel" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [POST] /containers
TAGS: Untagged
SUMMARY: Create container
DESCRIPTION: Create Container
AUTH: BEARER token

REQUEST
  Body:
  Content-Type: application/json
    - name: string (required) — Name of the container to create.
    - file_ids: array<string> (optional) — IDs of files to copy to the container.
    - expires_after: object (2 fields) (optional) — Container expiration time in seconds relative to the 'anchor...

RESPONSES
  - 200 (application/json): Success
        - id: string (required) — Unique identifier for the container.
        - object: string (required) — The type of this object.
        - name: string (required) — Name of the container.
        - created_at: integer (required) — Unix timestamp (in seconds) when the container was created.
        - status: string (required) — Status of the container (e.g., active, deleted).
        - expires_after: object (2 fields) (optional) — The container will expire after this time period.
The anchor...

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/containers" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /containers/{container_id}/files
TAGS: Untagged
SUMMARY: Create container file
DESCRIPTION: Create a Container File

You can send either a multipart/form-data request with the raw file content, or a JSON request with a file ID.

AUTH: BEARER token

REQUEST
  Path params:
  - container_id (string, required)
  Body:
  Content-Type: multipart/form-data
    - file_id: string (optional) — Name of the file to create.
    - file: string (binary) (optional) — The File object (not file name) to be uploaded.


RESPONSES
  - 200 (application/json): Success
        - id: string (required) — Unique identifier for the file.
        - object: string (required) — The type of this object (`container.file`).
        - container_id: string (required) — The container this file belongs to.
        - created_at: integer (required) — Unix timestamp (in seconds) when the file was created.
        - bytes: integer (required) — Size of the file in bytes.
        - path: string (required) — Path of the file in the container.
        - source: string (required) — Source of the file (e.g., `user`, `assistant`).

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/containers/123/files" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [POST] /organization/admin_api_keys
TAGS: Untagged
SUMMARY: Create admin API key
DESCRIPTION: Create an organization admin API key
AUTH: BEARER token

REQUEST
  Body:
  Content-Type: application/json
    - name: string (required)

RESPONSES
  - 200 (application/json): The newly created admin API key.
        - object: string (required) — The object type, which is always `organization.admin_api_key...
        - id: string (required) — The identifier, which can be referenced in API endpoints
        - name: string (required) — The name of the API key
        - redacted_value: string (required) — The redacted value of the API key
        - value: string (optional) — The value of the API key. Only shown on create.
        - created_at: integer (int64) (required) — The Unix timestamp (in seconds) of when the API key was crea...
        - last_used_at: object (required)
        - owner: object (6 fields) (required)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/organization/admin_api_keys" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================

### Tag: Uploads
================================================================================
ENDPOINT: [POST] /uploads
TAGS: Uploads
SUMMARY: Create upload
DESCRIPTION: Creates an intermediate [Upload](https://platform.openai.com/docs/api-reference/uploads/object) object
that you can add [Parts](https://platform.openai.com/docs/api-reference/uploads/part-object) to.
... (see full docs)
AUTH: BEARER token

REQUEST
  Body:
  Content-Type: application/json
    - filename: string (required) — The name of the file to upload.

    - purpose: string (enum: assistants, batch, fine-tune, vision) (required) — The intended purpose of the uploaded file.

See the [documen...
    - bytes: integer (required) — The number of bytes in the file you are uploading.

    - mime_type: string (required) — The MIME type of the file.

This must fall within the suppor...
    - expires_after: object (2 fields) (optional) — The expiration policy for a file. By default, files with `pu...

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The Upload unique identifier, which can be referenced in API...
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the Upload was crea...
        - filename: string (required) — The name of the file to be uploaded.
        - bytes: integer (required) — The intended number of bytes to be uploaded.
        - purpose: string (required) — The intended purpose of the file. [Please refer here](https:...
        - status: string (enum: pending, completed, cancelled, expired) (required) — The status of the Upload.
        - expires_at: integer (required) — The Unix timestamp (in seconds) for when the Upload will exp...
        - object: string (enum: upload) (required) — The object type, which is always "upload".
        - file: object (optional)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/uploads" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /uploads/{upload_id}/cancel
TAGS: Uploads
SUMMARY: Cancel upload
DESCRIPTION: Cancels the Upload. No Parts may be added after an Upload is cancelled.

AUTH: BEARER token

REQUEST
  Path params:
  - upload_id (string, required)

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The Upload unique identifier, which can be referenced in API...
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the Upload was crea...
        - filename: string (required) — The name of the file to be uploaded.
        - bytes: integer (required) — The intended number of bytes to be uploaded.
        - purpose: string (required) — The intended purpose of the file. [Please refer here](https:...
        - status: string (enum: pending, completed, cancelled, expired) (required) — The status of the Upload.
        - expires_at: integer (required) — The Unix timestamp (in seconds) for when the Upload will exp...
        - object: string (enum: upload) (required) — The object type, which is always "upload".
        - file: object (optional)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/uploads/upload_abc123/cancel" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [POST] /uploads/{upload_id}/complete
TAGS: Uploads
SUMMARY: Complete upload
DESCRIPTION: Completes the [Upload](https://platform.openai.com/docs/api-reference/uploads/object). 

Within the returned Upload object, there is a nested [File](https://platform.openai.com/docs/api-reference/file... (see full docs)
AUTH: BEARER token

REQUEST
  Path params:
  - upload_id (string, required)
  Body:
  Content-Type: application/json
    - part_ids: array<string> (required) — The ordered list of Part IDs.

    - md5: string (optional) — The optional md5 checksum for the file contents to verify if...

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The Upload unique identifier, which can be referenced in API...
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the Upload was crea...
        - filename: string (required) — The name of the file to be uploaded.
        - bytes: integer (required) — The intended number of bytes to be uploaded.
        - purpose: string (required) — The intended purpose of the file. [Please refer here](https:...
        - status: string (enum: pending, completed, cancelled, expired) (required) — The status of the Upload.
        - expires_at: integer (required) — The Unix timestamp (in seconds) for when the Upload will exp...
        - object: string (enum: upload) (required) — The object type, which is always "upload".
        - file: object (optional)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/uploads/upload_abc123/complete" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /uploads/{upload_id}/parts
TAGS: Uploads
SUMMARY: Add upload part
DESCRIPTION: Adds a [Part](https://platform.openai.com/docs/api-reference/uploads/part-object) to an [Upload](https://platform.openai.com/docs/api-reference/uploads/object) object. A Part represents a chunk of byt... (see full docs)
AUTH: BEARER token

REQUEST
  Path params:
  - upload_id (string, required)
  Body:
  Content-Type: multipart/form-data
    - data: string (binary) (required) — The chunk of bytes for this Part.


RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The upload Part unique identifier, which can be referenced i...
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the Part was create...
        - upload_id: string (required) — The ID of the Upload object that this Part was added to.
        - object: string (enum: upload.part) (required) — The object type, which is always `upload.part`.

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/uploads/upload_abc123/parts" \
  -H "Authorization: Bearer $TOKEN"
================================================================================

### Tag: Usage
================================================================================
ENDPOINT: [GET] /organization/costs
TAGS: Usage
SUMMARY: Costs
DESCRIPTION: Get costs details for the organization.
AUTH: BEARER token

REQUEST
  Query params:
  - start_time (integer, required)
  - end_time (integer, optional)
  - bucket_width (string (enum: 1d), optional)
  - project_ids (array<string>, optional)
  - group_by (array<string (enum: project_id, line_item)>, optional)
  - limit (integer, optional)
  - page (string, optional)

RESPONSES
  - 200 (application/json): Costs data retrieved successfully.
        - object: string (enum: page) (required)
        - data: array<object (4 fields)> (required)
        - has_more: boolean (required)
        - next_page: string (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/organization/costs?start_time=example&end_time=example&bucket_width=example&project_ids=example&group_by=example&limit=example&page=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /organization/usage/audio_speeches
TAGS: Usage
SUMMARY: Audio speeches
DESCRIPTION: Get audio speeches usage details for the organization.
AUTH: BEARER token

REQUEST
  Query params:
  - start_time (integer, required)
  - end_time (integer, optional)
  - bucket_width (string (enum: 1m, 1h, 1d), optional)
  - project_ids (array<string>, optional)
  - user_ids (array<string>, optional)
  - api_key_ids (array<string>, optional)
  - models (array<string>, optional)
  - group_by (array<string (enum: project_id, user_id, api_key_id, model)>, optional)
  - limit (integer, optional)
  - page (string, optional)

RESPONSES
  - 200 (application/json): Usage data retrieved successfully.
        - object: string (enum: page) (required)
        - data: array<object (4 fields)> (required)
        - has_more: boolean (required)
        - next_page: string (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/organization/usage/audio_speeches?start_time=example&end_time=example&bucket_width=example&project_ids=example&user_ids=example&api_key_ids=example&models=example&group_by=example&limit=example&page=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /organization/usage/audio_transcriptions
TAGS: Usage
SUMMARY: Audio transcriptions
DESCRIPTION: Get audio transcriptions usage details for the organization.
AUTH: BEARER token

REQUEST
  Query params:
  - start_time (integer, required)
  - end_time (integer, optional)
  - bucket_width (string (enum: 1m, 1h, 1d), optional)
  - project_ids (array<string>, optional)
  - user_ids (array<string>, optional)
  - api_key_ids (array<string>, optional)
  - models (array<string>, optional)
  - group_by (array<string (enum: project_id, user_id, api_key_id, model)>, optional)
  - limit (integer, optional)
  - page (string, optional)

RESPONSES
  - 200 (application/json): Usage data retrieved successfully.
        - object: string (enum: page) (required)
        - data: array<object (4 fields)> (required)
        - has_more: boolean (required)
        - next_page: string (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/organization/usage/audio_transcriptions?start_time=example&end_time=example&bucket_width=example&project_ids=example&user_ids=example&api_key_ids=example&models=example&group_by=example&limit=example&page=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /organization/usage/code_interpreter_sessions
TAGS: Usage
SUMMARY: Code interpreter sessions
DESCRIPTION: Get code interpreter sessions usage details for the organization.
AUTH: BEARER token

REQUEST
  Query params:
  - start_time (integer, required)
  - end_time (integer, optional)
  - bucket_width (string (enum: 1m, 1h, 1d), optional)
  - project_ids (array<string>, optional)
  - group_by (array<string (enum: project_id)>, optional)
  - limit (integer, optional)
  - page (string, optional)

RESPONSES
  - 200 (application/json): Usage data retrieved successfully.
        - object: string (enum: page) (required)
        - data: array<object (4 fields)> (required)
        - has_more: boolean (required)
        - next_page: string (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/organization/usage/code_interpreter_sessions?start_time=example&end_time=example&bucket_width=example&project_ids=example&group_by=example&limit=example&page=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /organization/usage/completions
TAGS: Usage
SUMMARY: Completions
DESCRIPTION: Get completions usage details for the organization.
AUTH: BEARER token

REQUEST
  Query params:
  - start_time (integer, required)
  - end_time (integer, optional)
  - bucket_width (string (enum: 1m, 1h, 1d), optional)
  - project_ids (array<string>, optional)
  - user_ids (array<string>, optional)
  - api_key_ids (array<string>, optional)
  - models (array<string>, optional)
  - batch (boolean, optional)
  - group_by (array<string (enum: project_id, user_id, api_key_id, model, batch)>, optional)
  - limit (integer, optional)
  - page (string, optional)

RESPONSES
  - 200 (application/json): Usage data retrieved successfully.
        - object: string (enum: page) (required)
        - data: array<object (4 fields)> (required)
        - has_more: boolean (required)
        - next_page: string (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/organization/usage/completions?start_time=example&end_time=example&bucket_width=example&project_ids=example&user_ids=example&api_key_ids=example&models=example&batch=example&group_by=example&limit=example&page=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /organization/usage/embeddings
TAGS: Usage
SUMMARY: Embeddings
DESCRIPTION: Get embeddings usage details for the organization.
AUTH: BEARER token

REQUEST
  Query params:
  - start_time (integer, required)
  - end_time (integer, optional)
  - bucket_width (string (enum: 1m, 1h, 1d), optional)
  - project_ids (array<string>, optional)
  - user_ids (array<string>, optional)
  - api_key_ids (array<string>, optional)
  - models (array<string>, optional)
  - group_by (array<string (enum: project_id, user_id, api_key_id, model)>, optional)
  - limit (integer, optional)
  - page (string, optional)

RESPONSES
  - 200 (application/json): Usage data retrieved successfully.
        - object: string (enum: page) (required)
        - data: array<object (4 fields)> (required)
        - has_more: boolean (required)
        - next_page: string (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/organization/usage/embeddings?start_time=example&end_time=example&bucket_width=example&project_ids=example&user_ids=example&api_key_ids=example&models=example&group_by=example&limit=example&page=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /organization/usage/images
TAGS: Usage
SUMMARY: Images
DESCRIPTION: Get images usage details for the organization.
AUTH: BEARER token

REQUEST
  Query params:
  - start_time (integer, required)
  - end_time (integer, optional)
  - bucket_width (string (enum: 1m, 1h, 1d), optional)
  - sources (array<string (enum: image.generation, image.edit, image.variation)>, optional)
  - sizes (array<string (enum: 256x256, 512x512, 1024x1024, 1792x1792, 1024x1792)>, optional)
  - project_ids (array<string>, optional)
  - user_ids (array<string>, optional)
  - api_key_ids (array<string>, optional)
  - models (array<string>, optional)
  - group_by (array<string (enum: project_id, user_id, api_key_id, model, size...)>, optional)
  - limit (integer, optional)
  - page (string, optional)

RESPONSES
  - 200 (application/json): Usage data retrieved successfully.
        - object: string (enum: page) (required)
        - data: array<object (4 fields)> (required)
        - has_more: boolean (required)
        - next_page: string (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/organization/usage/images?start_time=example&end_time=example&bucket_width=example&sources=example&sizes=example&project_ids=example&user_ids=example&api_key_ids=example&models=example&group_by=example&limit=example&page=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /organization/usage/moderations
TAGS: Usage
SUMMARY: Moderations
DESCRIPTION: Get moderations usage details for the organization.
AUTH: BEARER token

REQUEST
  Query params:
  - start_time (integer, required)
  - end_time (integer, optional)
  - bucket_width (string (enum: 1m, 1h, 1d), optional)
  - project_ids (array<string>, optional)
  - user_ids (array<string>, optional)
  - api_key_ids (array<string>, optional)
  - models (array<string>, optional)
  - group_by (array<string (enum: project_id, user_id, api_key_id, model)>, optional)
  - limit (integer, optional)
  - page (string, optional)

RESPONSES
  - 200 (application/json): Usage data retrieved successfully.
        - object: string (enum: page) (required)
        - data: array<object (4 fields)> (required)
        - has_more: boolean (required)
        - next_page: string (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/organization/usage/moderations?start_time=example&end_time=example&bucket_width=example&project_ids=example&user_ids=example&api_key_ids=example&models=example&group_by=example&limit=example&page=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /organization/usage/vector_stores
TAGS: Usage
SUMMARY: Vector stores
DESCRIPTION: Get vector stores usage details for the organization.
AUTH: BEARER token

REQUEST
  Query params:
  - start_time (integer, required)
  - end_time (integer, optional)
  - bucket_width (string (enum: 1m, 1h, 1d), optional)
  - project_ids (array<string>, optional)
  - group_by (array<string (enum: project_id)>, optional)
  - limit (integer, optional)
  - page (string, optional)

RESPONSES
  - 200 (application/json): Usage data retrieved successfully.
        - object: string (enum: page) (required)
        - data: array<object (4 fields)> (required)
        - has_more: boolean (required)
        - next_page: string (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/organization/usage/vector_stores?start_time=example&end_time=example&bucket_width=example&project_ids=example&group_by=example&limit=example&page=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================

### Tag: Users
================================================================================
ENDPOINT: [DELETE] /organization/users/{user_id}
TAGS: Users
SUMMARY: Delete user
DESCRIPTION: Deletes a user from the organization.
AUTH: BEARER token

REQUEST
  Path params:
  - user_id (string, required)

RESPONSES
  - 200 (application/json): User deleted successfully.
        - object: string (enum: organization.user.deleted) (required)
        - id: string (required)
        - deleted: boolean (required)

EXAMPLE (curl)
curl -X DELETE \
  "https://api.openai.com/v1/organization/users/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /organization/users
TAGS: Users
SUMMARY: List users
DESCRIPTION: Lists all of the users in the organization.
AUTH: BEARER token

REQUEST
  Query params:
  - limit (integer, optional)
  - after (string, optional)
  - emails (array<string>, optional)

RESPONSES
  - 200 (application/json): Users listed successfully.
        - object: string (enum: list) (required)
        - data: array<object (6 fields)> (required)
        - first_id: string (required)
        - last_id: string (required)
        - has_more: boolean (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/organization/users?limit=example&after=example&emails=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /organization/users/{user_id}
TAGS: Users
SUMMARY: Retrieve user
DESCRIPTION: Retrieves a user by their identifier.
AUTH: BEARER token

REQUEST
  Path params:
  - user_id (string, required)

RESPONSES
  - 200 (application/json): User retrieved successfully.
        - object: string (enum: organization.user) (required) — The object type, which is always `organization.user`
        - id: string (required) — The identifier, which can be referenced in API endpoints
        - name: string (required) — The name of the user
        - email: string (required) — The email address of the user
        - role: string (enum: owner, reader) (required) — `owner` or `reader`
        - added_at: integer (required) — The Unix timestamp (in seconds) of when the user was added.

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/organization/users/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [POST] /organization/users/{user_id}
TAGS: Users
SUMMARY: Modify user
DESCRIPTION: Modifies a user's role in the organization.
AUTH: BEARER token

REQUEST
  Path params:
  - user_id (string, required)
  Body:
  Content-Type: application/json
    - role: string (enum: owner, reader) (required) — `owner` or `reader`

RESPONSES
  - 200 (application/json): User role updated successfully.
        - object: string (enum: organization.user) (required) — The object type, which is always `organization.user`
        - id: string (required) — The identifier, which can be referenced in API endpoints
        - name: string (required) — The name of the user
        - email: string (required) — The email address of the user
        - role: string (enum: owner, reader) (required) — `owner` or `reader`
        - added_at: integer (required) — The Unix timestamp (in seconds) of when the user was added.

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/organization/users/123" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================

### Tag: Vector stores
================================================================================
ENDPOINT: [DELETE] /vector_stores/{vector_store_id}
TAGS: Vector stores
SUMMARY: Delete vector store
DESCRIPTION: Delete a vector store.
AUTH: BEARER token

REQUEST
  Path params:
  - vector_store_id (string, required)

RESPONSES
  - 200 (application/json): OK
        - id: string (required)
        - deleted: boolean (required)
        - object: string (enum: vector_store.deleted) (required)

EXAMPLE (curl)
curl -X DELETE \
  "https://api.openai.com/v1/vector_stores/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [DELETE] /vector_stores/{vector_store_id}/files/{file_id}
TAGS: Vector stores
SUMMARY: Delete vector store file
DESCRIPTION: Delete a vector store file. This will remove the file from the vector store but the file itself will not be deleted. To delete the file, use the [delete file](https://platform.openai.com/docs/api-refe... (see full docs)
AUTH: BEARER token

REQUEST
  Path params:
  - vector_store_id (string, required)
  - file_id (string, required)

RESPONSES
  - 200 (application/json): OK
        - id: string (required)
        - deleted: boolean (required)
        - object: string (enum: vector_store.file.deleted) (required)

EXAMPLE (curl)
curl -X DELETE \
  "https://api.openai.com/v1/vector_stores/123/files/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /vector_stores
TAGS: Vector stores
SUMMARY: List vector stores
DESCRIPTION: Returns a list of vector stores.
AUTH: BEARER token

REQUEST
  Query params:
  - limit (integer, optional)
  - order (string (enum: asc, desc), optional)
  - after (string, optional)
  - before (string, optional)

RESPONSES
  - 200 (application/json): OK
        - object: string (required)
        - data: array<object (11 fields)> (required)
        - first_id: string (required)
        - last_id: string (required)
        - has_more: boolean (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/vector_stores?limit=example&order=example&after=example&before=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /vector_stores/{vector_store_id}
TAGS: Vector stores
SUMMARY: Retrieve vector store
DESCRIPTION: Retrieves a vector store.
AUTH: BEARER token

REQUEST
  Path params:
  - vector_store_id (string, required)

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The identifier, which can be referenced in API endpoints.
        - object: string (enum: vector_store) (required) — The object type, which is always `vector_store`.
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the vector store wa...
        - name: string (required) — The name of the vector store.
        - usage_bytes: integer (required) — The total number of bytes used by the files in the vector st...
        - file_counts: object (5 fields) (required)
        - status: string (enum: expired, in_progress, completed) (required) — The status of the vector store, which can be either `expired...
        - expires_after: object (2 fields) (optional) — The expiration policy for a vector store.
        - expires_at: object (optional)
        - last_active_at: object (required)
        - metadata: object (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/vector_stores/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /vector_stores/{vector_store_id}/file_batches/{batch_id}
TAGS: Vector stores
SUMMARY: Retrieve vector store file batch
DESCRIPTION: Retrieves a vector store file batch.
AUTH: BEARER token

REQUEST
  Path params:
  - vector_store_id (string, required)
  - batch_id (string, required)

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The identifier, which can be referenced in API endpoints.
        - object: string (enum: vector_store.files_batch) (required) — The object type, which is always `vector_store.file_batch`.
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the vector store fi...
        - vector_store_id: string (required) — The ID of the [vector store](https://platform.openai.com/doc...
        - status: string (enum: in_progress, completed, cancelled, failed) (required) — The status of the vector store files batch, which can be eit...
        - file_counts: object (5 fields) (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/vector_stores/vs_abc123/file_batches/vsfb_abc123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /vector_stores/{vector_store_id}/file_batches/{batch_id}/files
TAGS: Vector stores
SUMMARY: List vector store files in a batch
DESCRIPTION: Returns a list of vector store files in a batch.
AUTH: BEARER token

REQUEST
  Path params:
  - vector_store_id (string, required)
  - batch_id (string, required)
  Query params:
  - limit (integer, optional)
  - order (string (enum: asc, desc), optional)
  - after (string, optional)
  - before (string, optional)
  - filter (string (enum: in_progress, completed, failed, cancelled), optional)

RESPONSES
  - 200 (application/json): OK
        - object: string (required)
        - data: array<object (9 fields)> (required)
        - first_id: string (required)
        - last_id: string (required)
        - has_more: boolean (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/vector_stores/123/file_batches/123/files?limit=example&order=example&after=example&before=example&filter=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /vector_stores/{vector_store_id}/files
TAGS: Vector stores
SUMMARY: List vector store files
DESCRIPTION: Returns a list of vector store files.
AUTH: BEARER token

REQUEST
  Path params:
  - vector_store_id (string, required)
  Query params:
  - limit (integer, optional)
  - order (string (enum: asc, desc), optional)
  - after (string, optional)
  - before (string, optional)
  - filter (string (enum: in_progress, completed, failed, cancelled), optional)

RESPONSES
  - 200 (application/json): OK
        - object: string (required)
        - data: array<object (9 fields)> (required)
        - first_id: string (required)
        - last_id: string (required)
        - has_more: boolean (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/vector_stores/123/files?limit=example&order=example&after=example&before=example&filter=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /vector_stores/{vector_store_id}/files/{file_id}
TAGS: Vector stores
SUMMARY: Retrieve vector store file
DESCRIPTION: Retrieves a vector store file.
AUTH: BEARER token

REQUEST
  Path params:
  - vector_store_id (string, required)
  - file_id (string, required)

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The identifier, which can be referenced in API endpoints.
        - object: string (enum: vector_store.file) (required) — The object type, which is always `vector_store.file`.
        - usage_bytes: integer (required) — The total vector store usage in bytes. Note that this may be...
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the vector store fi...
        - vector_store_id: string (required) — The ID of the [vector store](https://platform.openai.com/doc...
        - status: string (enum: in_progress, completed, cancelled, failed) (required) — The status of the vector store file, which can be either `in...
        - last_error: object (required)
        - chunking_strategy: object (optional) — The strategy used to chunk the file.
        - attributes: object (optional)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/vector_stores/vs_abc123/files/file-abc123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /vector_stores/{vector_store_id}/files/{file_id}/content
TAGS: Vector stores
SUMMARY: Retrieve vector store file content
DESCRIPTION: Retrieve the parsed contents of a vector store file.
AUTH: BEARER token

REQUEST
  Path params:
  - vector_store_id (string, required)
  - file_id (string, required)

RESPONSES
  - 200 (application/json): OK
        - object: string (enum: vector_store.file_content.page) (required) — The object type, which is always `vector_store.file_content....
        - data: array<object (2 fields)> (required) — Parsed content of the file.
        - has_more: boolean (required) — Indicates if there are more content pages to fetch.
        - next_page: object (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/vector_stores/vs_abc123/files/file-abc123/content" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [POST] /vector_stores
TAGS: Vector stores
SUMMARY: Create vector store
DESCRIPTION: Create a vector store.
AUTH: BEARER token

REQUEST
  Body:
  Content-Type: application/json
    - file_ids: array<string> (optional) — A list of [File](https://platform.openai.com/docs/api-refere...
    - name: string (optional) — The name of the vector store.
    - expires_after: object (2 fields) (optional) — The expiration policy for a vector store.
    - chunking_strategy: object (optional) — The chunking strategy used to chunk the file(s). If not set,...
    - metadata: object (optional)

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The identifier, which can be referenced in API endpoints.
        - object: string (enum: vector_store) (required) — The object type, which is always `vector_store`.
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the vector store wa...
        - name: string (required) — The name of the vector store.
        - usage_bytes: integer (required) — The total number of bytes used by the files in the vector st...
        - file_counts: object (5 fields) (required)
        - status: string (enum: expired, in_progress, completed) (required) — The status of the vector store, which can be either `expired...
        - expires_after: object (2 fields) (optional) — The expiration policy for a vector store.
        - expires_at: object (optional)
        - last_active_at: object (required)
        - metadata: object (required)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/vector_stores" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /vector_stores/{vector_store_id}
TAGS: Vector stores
SUMMARY: Modify vector store
DESCRIPTION: Modifies a vector store.
AUTH: BEARER token

REQUEST
  Path params:
  - vector_store_id (string, required)
  Body:
  Content-Type: application/json
    - name: string (optional) — The name of the vector store.
    - expires_after: object (optional)
    - metadata: object (optional)

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The identifier, which can be referenced in API endpoints.
        - object: string (enum: vector_store) (required) — The object type, which is always `vector_store`.
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the vector store wa...
        - name: string (required) — The name of the vector store.
        - usage_bytes: integer (required) — The total number of bytes used by the files in the vector st...
        - file_counts: object (5 fields) (required)
        - status: string (enum: expired, in_progress, completed) (required) — The status of the vector store, which can be either `expired...
        - expires_after: object (2 fields) (optional) — The expiration policy for a vector store.
        - expires_at: object (optional)
        - last_active_at: object (required)
        - metadata: object (required)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/vector_stores/123" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /vector_stores/{vector_store_id}/file_batches
TAGS: Vector stores
SUMMARY: Create vector store file batch
DESCRIPTION: Create a vector store file batch.
AUTH: BEARER token

REQUEST
  Path params:
  - vector_store_id (string, required)
  Body:
  Content-Type: application/json
    - file_ids: array<string> (required) — A list of [File](https://platform.openai.com/docs/api-refere...
    - chunking_strategy: object (optional) — The chunking strategy used to chunk the file(s). If not set,...
    - attributes: object (optional)

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The identifier, which can be referenced in API endpoints.
        - object: string (enum: vector_store.files_batch) (required) — The object type, which is always `vector_store.file_batch`.
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the vector store fi...
        - vector_store_id: string (required) — The ID of the [vector store](https://platform.openai.com/doc...
        - status: string (enum: in_progress, completed, cancelled, failed) (required) — The status of the vector store files batch, which can be eit...
        - file_counts: object (5 fields) (required)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/vector_stores/vs_abc123/file_batches" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /vector_stores/{vector_store_id}/file_batches/{batch_id}/cancel
TAGS: Vector stores
SUMMARY: Cancel vector store file batch
DESCRIPTION: Cancel a vector store file batch. This attempts to cancel the processing of files in this batch as soon as possible.
AUTH: BEARER token

REQUEST
  Path params:
  - vector_store_id (string, required)
  - batch_id (string, required)

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The identifier, which can be referenced in API endpoints.
        - object: string (enum: vector_store.files_batch) (required) — The object type, which is always `vector_store.file_batch`.
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the vector store fi...
        - vector_store_id: string (required) — The ID of the [vector store](https://platform.openai.com/doc...
        - status: string (enum: in_progress, completed, cancelled, failed) (required) — The status of the vector store files batch, which can be eit...
        - file_counts: object (5 fields) (required)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/vector_stores/123/file_batches/123/cancel" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [POST] /vector_stores/{vector_store_id}/files
TAGS: Vector stores
SUMMARY: Create vector store file
DESCRIPTION: Create a vector store file by attaching a [File](https://platform.openai.com/docs/api-reference/files) to a [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object).
AUTH: BEARER token

REQUEST
  Path params:
  - vector_store_id (string, required)
  Body:
  Content-Type: application/json
    - file_id: string (required) — A [File](https://platform.openai.com/docs/api-reference/file...
    - chunking_strategy: object (optional) — The chunking strategy used to chunk the file(s). If not set,...
    - attributes: object (optional)

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The identifier, which can be referenced in API endpoints.
        - object: string (enum: vector_store.file) (required) — The object type, which is always `vector_store.file`.
        - usage_bytes: integer (required) — The total vector store usage in bytes. Note that this may be...
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the vector store fi...
        - vector_store_id: string (required) — The ID of the [vector store](https://platform.openai.com/doc...
        - status: string (enum: in_progress, completed, cancelled, failed) (required) — The status of the vector store file, which can be either `in...
        - last_error: object (required)
        - chunking_strategy: object (optional) — The strategy used to chunk the file.
        - attributes: object (optional)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/vector_stores/vs_abc123/files" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /vector_stores/{vector_store_id}/files/{file_id}
TAGS: Vector stores
SUMMARY: Update vector store file attributes
DESCRIPTION: Update attributes on a vector store file.
AUTH: BEARER token

REQUEST
  Path params:
  - vector_store_id (string, required)
  - file_id (string, required)
  Body:
  Content-Type: application/json
    - attributes: object (required)

RESPONSES
  - 200 (application/json): OK
        - id: string (required) — The identifier, which can be referenced in API endpoints.
        - object: string (enum: vector_store.file) (required) — The object type, which is always `vector_store.file`.
        - usage_bytes: integer (required) — The total vector store usage in bytes. Note that this may be...
        - created_at: integer (required) — The Unix timestamp (in seconds) for when the vector store fi...
        - vector_store_id: string (required) — The ID of the [vector store](https://platform.openai.com/doc...
        - status: string (enum: in_progress, completed, cancelled, failed) (required) — The status of the vector store file, which can be either `in...
        - last_error: object (required)
        - chunking_strategy: object (optional) — The strategy used to chunk the file.
        - attributes: object (optional)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/vector_stores/vs_abc123/files/file-abc123" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /vector_stores/{vector_store_id}/search
TAGS: Vector stores
SUMMARY: Search vector store
DESCRIPTION: Search a vector store for relevant chunks based on a query and file attributes filter.
AUTH: BEARER token

REQUEST
  Path params:
  - vector_store_id (string, required)
  Body:
  Content-Type: application/json
    - query: object (required) — A query string for a search
    - rewrite_query: boolean (optional) — Whether to rewrite the natural language query for vector sea...
    - max_num_results: integer (optional) — The maximum number of results to return. This number should ...
    - filters: object (optional) — A filter to apply based on file attributes.
    - ranking_options: object (2 fields) (optional) — Ranking options for search.

RESPONSES
  - 200 (application/json): OK
        - object: string (enum: vector_store.search_results.page) (required) — The object type, which is always `vector_store.search_result...
        - search_query: array<string> (required)
        - data: array<object (5 fields)> (required) — The list of search result items.
        - has_more: boolean (required) — Indicates if there are more results to fetch.
        - next_page: object (required)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/vector_stores/vs_abc123/search" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================

### Tag: Videos
================================================================================
ENDPOINT: [DELETE] /videos/{video_id}
TAGS: Videos
SUMMARY: Delete video
DESCRIPTION: Delete a video
AUTH: BEARER token

REQUEST
  Path params:
  - video_id (string, required)

RESPONSES
  - 200 (application/json): Success
        - object: string (enum: video.deleted) (required) — The object type that signals the deletion response.
        - deleted: boolean (required) — Indicates that the video resource was deleted.
        - id: string (required) — Identifier of the deleted video.

EXAMPLE (curl)
curl -X DELETE \
  "https://api.openai.com/v1/videos/video_123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /videos
TAGS: Videos
SUMMARY: List videos
AUTH: BEARER token

REQUEST
  Query params:
  - limit (integer, optional)
  - order (string (enum: asc, desc), optional)
  - after (string, optional)

RESPONSES
  - 200 (application/json): Success
        - object: object (required) — The type of object returned, must be `list`.
        - data: array<object (12 fields)> (required) — A list of items
        - first_id: object (required)
        - last_id: object (required)
        - has_more: boolean (required) — Whether there are more items available.

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/videos?limit=example&order=example&after=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /videos/{video_id}
TAGS: Videos
SUMMARY: Retrieve video
DESCRIPTION: Retrieve a video
AUTH: BEARER token

REQUEST
  Path params:
  - video_id (string, required)

RESPONSES
  - 200 (application/json): Success
        - id: string (required) — Unique identifier for the video job.
        - object: string (enum: video) (required) — The object type, which is always `video`.
        - model: string (enum: sora-2, sora-2-pro) (required)
        - status: string (enum: queued, in_progress, completed, failed) (required)
        - progress: integer (required) — Approximate completion percentage for the generation task.
        - created_at: integer (required) — Unix timestamp (seconds) for when the job was created.
        - completed_at: object (required)
        - expires_at: object (required)
        - size: string (enum: 720x1280, 1280x720, 1024x1792, 1792x1024) (required)
        - seconds: string (enum: 4, 8, 12) (required)
        - remixed_from_video_id: object (required)
        - error: object (required)

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/videos/video_123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [GET] /videos/{video_id}/content
TAGS: Videos
SUMMARY: Retrieve video content
DESCRIPTION: Download video content
AUTH: BEARER token

REQUEST
  Path params:
  - video_id (string, required)
  Query params:
  - variant (string (enum: video, thumbnail, spritesheet), optional)

RESPONSES
  - 200 (video/mp4): The video bytes or preview asset that matches the requested variant.
        string (binary)
  - 200 (image/webp): The video bytes or preview asset that matches the requested variant.
        string (binary)
  - 200 (application/json): The video bytes or preview asset that matches the requested variant.
        string

EXAMPLE (curl)
curl -X GET \
  "https://api.openai.com/v1/videos/video_123/content?variant=example" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
================================================================================
ENDPOINT: [POST] /videos
TAGS: Videos
SUMMARY: Create video
DESCRIPTION: Create a video
AUTH: BEARER token

REQUEST
  Body:
  Content-Type: multipart/form-data
    - model: string (enum: sora-2, sora-2-pro) (optional)
    - prompt: string (required) — Text prompt that describes the video to generate.
    - input_reference: string (binary) (optional) — Optional image reference that guides generation.
    - seconds: string (enum: 4, 8, 12) (optional)
    - size: string (enum: 720x1280, 1280x720, 1024x1792, 1792x1024) (optional)
  Content-Type: application/json
    - model: string (enum: sora-2, sora-2-pro) (optional)
    - prompt: string (required) — Text prompt that describes the video to generate.
    - input_reference: string (binary) (optional) — Optional image reference that guides generation.
    - seconds: string (enum: 4, 8, 12) (optional)
    - size: string (enum: 720x1280, 1280x720, 1024x1792, 1792x1024) (optional)

RESPONSES
  - 200 (application/json): Success
        - id: string (required) — Unique identifier for the video job.
        - object: string (enum: video) (required) — The object type, which is always `video`.
        - model: string (enum: sora-2, sora-2-pro) (required)
        - status: string (enum: queued, in_progress, completed, failed) (required)
        - progress: integer (required) — Approximate completion percentage for the generation task.
        - created_at: integer (required) — Unix timestamp (seconds) for when the job was created.
        - completed_at: object (required)
        - expires_at: object (required)
        - size: string (enum: 720x1280, 1280x720, 1024x1792, 1792x1024) (required)
        - seconds: string (enum: 4, 8, 12) (required)
        - remixed_from_video_id: object (required)
        - error: object (required)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/videos" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================
================================================================================
ENDPOINT: [POST] /videos/{video_id}/remix
TAGS: Videos
SUMMARY: Remix video
DESCRIPTION: Create a video remix
AUTH: BEARER token

REQUEST
  Path params:
  - video_id (string, required)
  Body:
  Content-Type: multipart/form-data
    - prompt: string (required) — Updated text prompt that directs the remix generation.
  Content-Type: application/json
    - prompt: string (required) — Updated text prompt that directs the remix generation.

RESPONSES
  - 200 (application/json): Success
        - id: string (required) — Unique identifier for the video job.
        - object: string (enum: video) (required) — The object type, which is always `video`.
        - model: string (enum: sora-2, sora-2-pro) (required)
        - status: string (enum: queued, in_progress, completed, failed) (required)
        - progress: integer (required) — Approximate completion percentage for the generation task.
        - created_at: integer (required) — Unix timestamp (seconds) for when the job was created.
        - completed_at: object (required)
        - expires_at: object (required)
        - size: string (enum: 720x1280, 1280x720, 1024x1792, 1792x1024) (required)
        - seconds: string (enum: 4, 8, 12) (required)
        - remixed_from_video_id: object (required)
        - error: object (required)

EXAMPLE (curl)
curl -X POST \
  "https://api.openai.com/v1/videos/video_123/remix" \
  -d '{"key": "value"}' \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
================================================================================


================================================================================
## COMPONENTS APPENDIX
================================================================================

Shared schemas referenced throughout the API:

### ActiveStatus
Type: object
Description: Indicates that a thread is active.

- type: string (enum: active) (required) — Status discriminator that is always `active`.

### AddUploadPartRequest
Type: object

- data: string (binary) (required) — The chunk of bytes for this Part.


### AdminApiKey
Type: object
Description: Represents an individual Admin API key in an org.

- object: string (required) — The object type, which is always `organization.admin_api_key...
- id: string (required) — The identifier, which can be referenced in API endpoints
- name: string (required) — The name of the API key
- redacted_value: string (required) — The redacted value of the API key
- value: string (optional) — The value of the API key. Only shown on create.
- created_at: integer (int64) (required) — The Unix timestamp (in seconds) of when the API key was crea...
- last_used_at: object (required)
- owner: object (6 fields) (required)

### Annotation
Type: object

(empty)

### ApiKeyList
Type: object

- object: string (optional)
- data: array<object> (optional)
- has_more: boolean (optional)
- first_id: string (optional)
- last_id: string (optional)

### ApproximateLocation
Type: object

- type: string (enum: approximate) (required) — The type of location approximation. Always `approximate`.
- country: object (optional)
- region: object (optional)
- city: object (optional)
- timezone: object (optional)

### AssistantMessageItem
Type: object
Description: Assistant-authored message within a thread.

- id: string (required) — Identifier of the thread item.
- object: string (enum: chatkit.thread_item) (required) — Type discriminator that is always `chatkit.thread_item`.
- created_at: integer (required) — Unix timestamp (in seconds) for when the item was created.
- thread_id: string (required) — Identifier of the parent thread.
- type: string (enum: chatkit.assistant_message) (required) — Type discriminator that is always `chatkit.assistant_message...
- content: array<object> (required) — Ordered assistant response segments.

### AssistantObject
Type: object
Description: Represents an `assistant` that can call the model and use tools.

- id: string (required) — The identifier, which can be referenced in API endpoints.
- object: string (enum: assistant) (required) — The object type, which is always `assistant`.
- created_at: integer (required) — The Unix timestamp (in seconds) for when the assistant was c...
- name: object (required)
- description: object (required)
- model: string (required) — ID of the model to use. You can use the [List models](https:...
- instructions: object (required)
- tools: array<object> (required) — A list of tool enabled on the assistant. There can be a maxi...
- tool_resources: object (optional)
- metadata: object (required)
- temperature: object (optional)
- top_p: object (optional)
- response_format: object (optional)

### AssistantStreamEvent
Type: object
Description: Represents an event emitted when streaming a Run.

Each event in a server-sent events stream has an `event` and `data` property:

```
event: thread.created
data: {"id": "thread_123", "object": "thread...

(empty)

### AssistantSupportedModels
Type: string

string (enum: gpt-5, gpt-5-mini, gpt-5-nano, gpt-5-2025-08-07, gpt-5-mini-2025-08-07...)

### AssistantTool
Type: object

(empty)

### AssistantToolsCode
Type: object

- type: string (enum: code_interpreter) (required) — The type of tool being defined: `code_interpreter`

### AssistantToolsFileSearch
Type: object

- type: string (enum: file_search) (required) — The type of tool being defined: `file_search`
- file_search: object (2 fields) (optional) — Overrides for the file search tool.

### AssistantToolsFileSearchTypeOnly
Type: object

- type: string (enum: file_search) (required) — The type of tool being defined: `file_search`

### AssistantToolsFunction
Type: object

- type: string (enum: function) (required) — The type of tool being defined: `function`
- function: object (required)

### AssistantsApiResponseFormatOption
Type: object
Description: Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4),...

(empty)

### AssistantsApiToolChoiceOption
Type: object
Description: Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between ge...

(empty)

### AssistantsNamedToolChoice
Type: object
Description: Specifies a tool the model should use. Use to force the model to call a specific tool.

- type: string (enum: function, code_interpreter, file_search) (required) — The type of the tool. If type is `function`, the function na...
- function: object (1 fields) (optional)

### Attachment
Type: object
Description: Attachment metadata included on thread items.

- type: object (required) — Attachment discriminator.
- id: string (required) — Identifier for the attachment.
- name: string (required) — Original display name for the attachment.
- mime_type: string (required) — MIME type of the attachment.
- preview_url: object (required)

### AttachmentType
Type: string

string (enum: image, file)

### AudioResponseFormat
Type: string
Description: The format of the output, in one of these options: `json`, `text`, `srt`, `verbose_json`, or `vtt`. For `gpt-4o-transcribe` and `gpt-4o-mini-transcribe`, the only supported format is `json`.


string (enum: json, text, srt, verbose_json, vtt)

### AudioTranscription
Type: object

- model: string (enum: whisper-1, gpt-4o-transcribe-latest, gpt-4o-mini-transcribe, gpt-4o-transcribe) (optional) — The model to use for transcription. Current options are `whi...
- language: string (optional) — The language of the input audio. Supplying the input languag...
- prompt: string (optional) — An optional text to guide the model's style or continue a pr...

### AuditLog
Type: object
Description: A log of a user action or configuration change within this organization.

- id: string (required) — The ID of this log.
- type: object (required)
- effective_at: integer (required) — The Unix timestamp (in seconds) of the event.
- project: object (2 fields) (optional) — The project that the action was scoped to. Absent for action...
- actor: object (required)
- api_key.created: object (2 fields) (optional) — The details for events with this `type`.
- api_key.updated: object (2 fields) (optional) — The details for events with this `type`.
- api_key.deleted: object (1 fields) (optional) — The details for events with this `type`.
- checkpoint.permission.created: object (2 fields) (optional) — The project and fine-tuned model checkpoint that the checkpo...
- checkpoint.permission.deleted: object (1 fields) (optional) — The details for events with this `type`.
- external_key.registered: object (2 fields) (optional) — The details for events with this `type`.
- external_key.removed: object (1 fields) (optional) — The details for events with this `type`.
- group.created: object (2 fields) (optional) — The details for events with this `type`.
- group.updated: object (2 fields) (optional) — The details for events with this `type`.
- group.deleted: object (1 fields) (optional) — The details for events with this `type`.
- scim.enabled: object (1 fields) (optional) — The details for events with this `type`.
- scim.disabled: object (1 fields) (optional) — The details for events with this `type`.
- invite.sent: object (2 fields) (optional) — The details for events with this `type`.
- invite.accepted: object (1 fields) (optional) — The details for events with this `type`.
- invite.deleted: object (1 fields) (optional) — The details for events with this `type`.
- ip_allowlist.created: object (3 fields) (optional) — The details for events with this `type`.
- ip_allowlist.updated: object (2 fields) (optional) — The details for events with this `type`.
- ip_allowlist.deleted: object (3 fields) (optional) — The details for events with this `type`.
- ip_allowlist.config.activated: object (1 fields) (optional) — The details for events with this `type`.
- ip_allowlist.config.deactivated: object (1 fields) (optional) — The details for events with this `type`.
- login.succeeded: object (optional) — This event has no additional fields beyond the standard audi...
- login.failed: object (2 fields) (optional) — The details for events with this `type`.
- logout.succeeded: object (optional) — This event has no additional fields beyond the standard audi...
- logout.failed: object (2 fields) (optional) — The details for events with this `type`.
- organization.updated: object (2 fields) (optional) — The details for events with this `type`.
- project.created: object (2 fields) (optional) — The details for events with this `type`.
- project.updated: object (2 fields) (optional) — The details for events with this `type`.
- project.archived: object (1 fields) (optional) — The details for events with this `type`.
- project.deleted: object (1 fields) (optional) — The details for events with this `type`.
- rate_limit.updated: object (2 fields) (optional) — The details for events with this `type`.
- rate_limit.deleted: object (1 fields) (optional) — The details for events with this `type`.
- role.created: object (5 fields) (optional) — The details for events with this `type`.
- role.updated: object (2 fields) (optional) — The details for events with this `type`.
- role.deleted: object (1 fields) (optional) — The details for events with this `type`.
- role.assignment.created: object (5 fields) (optional) — The details for events with this `type`.
- role.assignment.deleted: object (5 fields) (optional) — The details for events with this `type`.
- service_account.created: object (2 fields) (optional) — The details for events with this `type`.
- service_account.updated: object (2 fields) (optional) — The details for events with this `type`.
- service_account.deleted: object (1 fields) (optional) — The details for events with this `type`.
- user.added: object (2 fields) (optional) — The details for events with this `type`.
- user.updated: object (2 fields) (optional) — The details for events with this `type`.
- user.deleted: object (1 fields) (optional) — The details for events with this `type`.
- certificate.created: object (2 fields) (optional) — The details for events with this `type`.
- certificate.updated: object (2 fields) (optional) — The details for events with this `type`.
- certificate.deleted: object (3 fields) (optional) — The details for events with this `type`.
- certificates.activated: object (1 fields) (optional) — The details for events with this `type`.
- certificates.deactivated: object (1 fields) (optional) — The details for events with this `type`.

### AuditLogActor
Type: object
Description: The actor who performed the audit logged action.

- type: string (enum: session, api_key) (optional) — The type of actor. Is either `session` or `api_key`.
- session: object (optional)
- api_key: object (optional)

### AuditLogActorApiKey
Type: object
Description: The API Key used to perform the audit logged action.

- id: string (optional) — The tracking id of the API key.
- type: string (enum: user, service_account) (optional) — The type of API key. Can be either `user` or `service_accoun...
- user: object (optional)
- service_account: object (optional)

### AuditLogActorServiceAccount
Type: object
Description: The service account that performed the audit logged action.

- id: string (optional) — The service account id.

### AuditLogActorSession
Type: object
Description: The session in which the audit logged action was performed.

- user: object (optional)
- ip_address: string (optional) — The IP address from which the action was performed.

### AuditLogActorUser
Type: object
Description: The user who performed the audit logged action.

- id: string (optional) — The user id.
- email: string (optional) — The user email.

### AuditLogEventType
Type: string
Description: The event type.

string (enum: api_key.created, api_key.updated, api_key.deleted, certificate.created, certificate.updated...)

### AutoChunkingStrategyRequestParam
Type: object
Description: The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.

- type: string (enum: auto) (required) — Always `auto`.

### AutomaticThreadTitlingParam
Type: object
Description: Controls whether ChatKit automatically generates thread titles.

- enabled: boolean (optional) — Enable automatic thread title generation. Defaults to true.

### Batch
Type: object

- id: string (required)
- object: string (enum: batch) (required) — The object type, which is always `batch`.
- endpoint: string (required) — The OpenAI API endpoint used by the batch.
- model: string (optional) — Model ID used to process the batch, like `gpt-5-2025-08-07`....
- errors: object (2 fields) (optional)
- input_file_id: string (required) — The ID of the input file for the batch.
- completion_window: string (required) — The time frame within which the batch should be processed.
- status: string (enum: validating, failed, in_progress, finalizing, completed...) (required) — The current status of the batch.
- output_file_id: string (optional) — The ID of the file containing the outputs of successfully ex...
- error_file_id: string (optional) — The ID of the file containing the outputs of requests with e...
- created_at: integer (required) — The Unix timestamp (in seconds) for when the batch was creat...
- in_progress_at: integer (optional) — The Unix timestamp (in seconds) for when the batch started p...
- expires_at: integer (optional) — The Unix timestamp (in seconds) for when the batch will expi...
- finalizing_at: integer (optional) — The Unix timestamp (in seconds) for when the batch started f...
- completed_at: integer (optional) — The Unix timestamp (in seconds) for when the batch was compl...
- failed_at: integer (optional) — The Unix timestamp (in seconds) for when the batch failed.
- expired_at: integer (optional) — The Unix timestamp (in seconds) for when the batch expired.
- cancelling_at: integer (optional) — The Unix timestamp (in seconds) for when the batch started c...
- cancelled_at: integer (optional) — The Unix timestamp (in seconds) for when the batch was cance...
- request_counts: object (optional)
- usage: object (5 fields) (optional) — Represents token usage details including input tokens, outpu...
- metadata: object (optional)

### BatchError
Type: object

- code: string (optional) — An error code identifying the error type.
- message: string (optional) — A human-readable message providing more details about the er...
- param: object (optional)
- line: object (optional)

### BatchFileExpirationAfter
Type: object
Description: The expiration policy for the output and/or error file that are generated for a batch.

- anchor: string (enum: created_at) (required) — Anchor timestamp after which the expiration policy applies. ...
- seconds: integer (required) — The number of seconds after the anchor time that the file wi...

### BatchRequestCounts
Type: object
Description: The request counts for different statuses within the batch.

- total: integer (required) — Total number of requests in the batch.
- completed: integer (required) — Number of requests that have been completed successfully.
- failed: integer (required) — Number of requests that have failed.

### BatchRequestInput
Type: object
Description: The per-line object of the batch input file

- custom_id: string (optional) — A developer-provided per-request id that will be used to mat...
- method: string (enum: POST) (optional) — The HTTP method to be used for the request. Currently only `...
- url: string (optional) — The OpenAI API relative URL to be used for the request. Curr...

### BatchRequestOutput
Type: object
Description: The per-line object of the batch output and error files

- id: string (optional)
- custom_id: string (optional) — A developer-provided per-request id that will be used to mat...
- response: object (optional)
- error: object (optional)

### Certificate
Type: object
Description: Represents an individual `certificate` uploaded to the organization.

- object: string (enum: certificate, organization.certificate, organization.project.certificate) (required) — The object type.

- If creating, updating, or getting a spec...
- id: string (required) — The identifier, which can be referenced in API endpoints
- name: string (required) — The name of the certificate.
- created_at: integer (required) — The Unix timestamp (in seconds) of when the certificate was ...
- certificate_details: object (3 fields) (required)
- active: boolean (optional) — Whether the certificate is currently active at the specified...

### ChatCompletionAllowedTools
Type: object
Description: Constrains the tools available to the model to a pre-defined set.


- mode: string (enum: auto, required) (required) — Constrains the tools available to the model to a pre-defined...
- tools: array<object> (required) — A list of tool definitions that the model should be allowed ...

### ChatCompletionAllowedToolsChoice
Type: object
Description: Constrains the tools available to the model to a pre-defined set.


- type: string (enum: allowed_tools) (required) — Allowed tool configuration type. Always `allowed_tools`.
- allowed_tools: object (required)

### ChatCompletionDeleted
Type: object

- object: string (enum: chat.completion.deleted) (required) — The type of object being deleted.
- id: string (required) — The ID of the chat completion that was deleted.
- deleted: boolean (required) — Whether the chat completion was deleted.

### ChatCompletionFunctionCallOption
Type: object
Description: Specifying a particular function via `{"name": "my_function"}` forces the model to call that function.


- name: string (required) — The name of the function to call.

### ChatCompletionFunctions
Type: object

- description: string (optional) — A description of what the function does, used by the model t...
- name: string (required) — The name of the function to be called. Must be a-z, A-Z, 0-9...
- parameters: object (optional)

### ChatCompletionList
Type: object
Description: An object representing a list of Chat Completions.


- object: string (enum: list) (required) — The type of this object. It is always set to "list".

- data: array<object> (required) — An array of chat completion objects.

- first_id: string (required) — The identifier of the first chat completion in the data arra...
- last_id: string (required) — The identifier of the last chat completion in the data array...
- has_more: boolean (required) — Indicates whether there are more Chat Completions available.

### ChatCompletionMessageCustomToolCall
Type: object
Description: A call to a custom tool created by the model.


- id: string (required) — The ID of the tool call.
- type: string (enum: custom) (required) — The type of the tool. Always `custom`.
- custom: object (2 fields) (required) — The custom tool that the model called.

### ChatCompletionMessageList
Type: object
Description: An object representing a list of chat completion messages.


- object: string (enum: list) (required) — The type of this object. It is always set to "list".

- data: array<object> (required) — An array of chat completion message objects.

- first_id: string (required) — The identifier of the first chat message in the data array.
- last_id: string (required) — The identifier of the last chat message in the data array.
- has_more: boolean (required) — Indicates whether there are more chat messages available.

### ChatCompletionMessageToolCall
Type: object
Description: A call to a function tool created by the model.


- id: string (required) — The ID of the tool call.
- type: string (enum: function) (required) — The type of the tool. Currently, only `function` is supporte...
- function: object (2 fields) (required) — The function that the model called.

### ChatCompletionMessageToolCallChunk
Type: object

- index: integer (required)
- id: string (optional) — The ID of the tool call.
- type: string (enum: function) (optional) — The type of the tool. Currently, only `function` is supporte...
- function: object (2 fields) (optional)

### ChatCompletionMessageToolCalls
Type: array
Description: The tool calls generated by the model, such as function calls.

array<object>

### ChatCompletionModalities
Type: object

(empty)

### ChatCompletionNamedToolChoice
Type: object
Description: Specifies a tool the model should use. Use to force the model to call a specific function.

- type: string (enum: function) (required) — For function calling, the type is always `function`.
- function: object (1 fields) (required)

### ChatCompletionNamedToolChoiceCustom
Type: object
Description: Specifies a tool the model should use. Use to force the model to call a specific custom tool.

- type: string (enum: custom) (required) — For custom tool calling, the type is always `custom`.
- custom: object (1 fields) (required)

### ChatCompletionRequestAssistantMessage
Type: object
Description: Messages sent by the model in response to user messages.


- content: object (optional)
- refusal: object (optional)
- role: string (enum: assistant) (required) — The role of the messages author, in this case `assistant`.
- name: string (optional) — An optional name for the participant. Provides the model inf...
- audio: object (optional)
- tool_calls: object (optional)
- function_call: object (optional)

### ChatCompletionRequestAssistantMessageContentPart
Type: object

(empty)

### ChatCompletionRequestDeveloperMessage
Type: object
Description: Developer-provided instructions that the model should follow, regardless of
messages sent by the user. With o1 models and newer, `developer` messages
replace the previous `system` messages.


- content: object (required) — The contents of the developer message.
- role: string (enum: developer) (required) — The role of the messages author, in this case `developer`.
- name: string (optional) — An optional name for the participant. Provides the model inf...

### ChatCompletionRequestFunctionMessage
Type: object

- role: string (enum: function) (required) — The role of the messages author, in this case `function`.
- content: object (required)
- name: string (required) — The name of the function to call.

### ChatCompletionRequestMessage
Type: object

(empty)

### ChatCompletionRequestMessageContentPartAudio
Type: object
Description: Learn about [audio inputs](https://platform.openai.com/docs/guides/audio).


- type: string (enum: input_audio) (required) — The type of the content part. Always `input_audio`.
- input_audio: object (2 fields) (required)

### ChatCompletionRequestMessageContentPartFile
Type: object
Description: Learn about [file inputs](https://platform.openai.com/docs/guides/text) for text generation.


- type: string (enum: file) (required) — The type of the content part. Always `file`.
- file: object (3 fields) (required)

### ChatCompletionRequestMessageContentPartImage
Type: object
Description: Learn about [image inputs](https://platform.openai.com/docs/guides/vision).


- type: string (enum: image_url) (required) — The type of the content part.
- image_url: object (2 fields) (required)

### ChatCompletionRequestMessageContentPartRefusal
Type: object

- type: string (enum: refusal) (required) — The type of the content part.
- refusal: string (required) — The refusal message generated by the model.

### ChatCompletionRequestMessageContentPartText
Type: object
Description: Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).


- type: string (enum: text) (required) — The type of the content part.
- text: string (required) — The text content.

### ChatCompletionRequestSystemMessage
Type: object
Description: Developer-provided instructions that the model should follow, regardless of
messages sent by the user. With o1 models and newer, use `developer` messages
for this purpose instead.


- content: object (required) — The contents of the system message.
- role: string (enum: system) (required) — The role of the messages author, in this case `system`.
- name: string (optional) — An optional name for the participant. Provides the model inf...

### ChatCompletionRequestSystemMessageContentPart
Type: object

(empty)

### ChatCompletionRequestToolMessage
Type: object

- role: string (enum: tool) (required) — The role of the messages author, in this case `tool`.
- content: object (required) — The contents of the tool message.
- tool_call_id: string (required) — Tool call that this message is responding to.

### ChatCompletionRequestToolMessageContentPart
Type: object

(empty)

### ChatCompletionRequestUserMessage
Type: object
Description: Messages sent by an end user, containing prompts or additional context
information.


- content: object (required) — The contents of the user message.

- role: string (enum: user) (required) — The role of the messages author, in this case `user`.
- name: string (optional) — An optional name for the participant. Provides the model inf...

### ChatCompletionRequestUserMessageContentPart
Type: object

(empty)

### ChatCompletionResponseMessage
Type: object
Description: A chat completion message generated by the model.

- content: object (required)
- refusal: object (required)
- tool_calls: object (optional)
- annotations: array<object (2 fields)> (optional) — Annotations for the message, when applicable, as when using ...
- role: string (enum: assistant) (required) — The role of the author of this message.
- function_call: object (2 fields) (optional) — Deprecated and replaced by `tool_calls`. The name and argume...
- audio: object (optional)

### ChatCompletionRole
Type: string
Description: The role of the author of a message

string (enum: developer, system, user, assistant, tool...)

### ChatCompletionStreamOptions
Type: object

(empty)

### ChatCompletionStreamResponseDelta
Type: object
Description: A chat completion delta generated by streamed model responses.

- content: object (optional)
- function_call: object (2 fields) (optional) — Deprecated and replaced by `tool_calls`. The name and argume...
- tool_calls: array<object> (optional)
- role: string (enum: developer, system, user, assistant, tool) (optional) — The role of the author of this message.
- refusal: object (optional)

### ChatCompletionTokenLogprob
Type: object

- token: string (required) — The token.
- logprob: number (required) — The log probability of this token, if it is within the top 2...
- bytes: object (required)
- top_logprobs: array<object (3 fields)> (required) — List of the most likely tokens and their log probability, at...

### ChatCompletionTool
Type: object
Description: A function tool that can be used to generate a response.


- type: string (enum: function) (required) — The type of the tool. Currently, only `function` is supporte...
- function: object (required)

### ChatCompletionToolChoiceOption
Type: object
Description: Controls which (if any) tool is called by the model.
`none` means the model will not call any tool and instead generates a message.
`auto` means the model can pick between generating a message or call...

(empty)

### ChatModel
Type: string

string (enum: gpt-5, gpt-5-mini, gpt-5-nano, gpt-5-2025-08-07, gpt-5-mini-2025-08-07...)

### ChatSessionAutomaticThreadTitling
Type: object
Description: Automatic thread title preferences for the session.

- enabled: boolean (required) — Whether automatic thread titling is enabled.

### ChatSessionChatkitConfiguration
Type: object
Description: ChatKit configuration for the session.

- automatic_thread_titling: object (required) — Automatic thread titling preferences.
- file_upload: object (required) — Upload settings for the session.
- history: object (required) — History retention configuration.

### ChatSessionFileUpload
Type: object
Description: Upload permissions and limits applied to the session.

- enabled: boolean (required) — Indicates if uploads are enabled for the session.
- max_file_size: object (required)
- max_files: object (required)

### ChatSessionHistory
Type: object
Description: History retention preferences returned for the session.

- enabled: boolean (required) — Indicates if chat history is persisted for the session.
- recent_threads: object (required)

### ChatSessionRateLimits
Type: object
Description: Active per-minute request limit for the session.

- max_requests_per_1_minute: integer (required) — Maximum allowed requests per one-minute window.

### ChatSessionResource
Type: object
Description: Represents a ChatKit session and its resolved configuration.

- id: string (required) — Identifier for the ChatKit session.
- object: string (enum: chatkit.session) (required) — Type discriminator that is always `chatkit.session`.
- expires_at: integer (required) — Unix timestamp (in seconds) for when the session expires.
- client_secret: string (required) — Ephemeral client secret that authenticates session requests.
- workflow: object (required) — Workflow metadata for the session.
- user: string (required) — User identifier associated with the session.
- rate_limits: object (required) — Resolved rate limit values.
- max_requests_per_1_minute: integer (required) — Convenience copy of the per-minute request limit.
- status: object (required) — Current lifecycle state of the session.
- chatkit_configuration: object (required) — Resolved ChatKit feature configuration for the session.

### ChatSessionStatus
Type: string

string (enum: active, expired, cancelled)

### ChatkitConfigurationParam
Type: object
Description: Optional per-session configuration settings for ChatKit behavior.

- automatic_thread_titling: object (optional) — Configuration for automatic thread titling. When omitted, au...
- file_upload: object (optional) — Configuration for upload enablement and limits. When omitted...
- history: object (optional) — Configuration for chat history retention. When omitted, hist...

### ChatkitWorkflow
Type: object
Description: Workflow metadata and state returned for the session.

- id: string (required) — Identifier of the workflow backing the session.
- version: object (required)
- state_variables: object (required)
- tracing: object (required) — Tracing settings applied to the workflow.

### ChatkitWorkflowTracing
Type: object
Description: Controls diagnostic tracing during the session.

- enabled: boolean (required) — Indicates whether tracing is enabled.

### ChunkingStrategyRequestParam
Type: object
Description: The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy. Only applicable if `file_ids` is non-empty.

(empty)

### ChunkingStrategyResponse
Type: object
Description: The strategy used to chunk the file.

(empty)

### Click
Type: object
Description: A click action.


- type: string (enum: click) (required) — Specifies the event type. For a click action, this property ...
- button: string (enum: left, right, wheel, back, forward) (required) — Indicates which mouse button was pressed during the click. O...
- x: integer (required) — The x-coordinate where the click occurred.

- y: integer (required) — The y-coordinate where the click occurred.


### ClientToolCallItem
Type: object
Description: Record of a client side tool invocation initiated by the assistant.

- id: string (required) — Identifier of the thread item.
- object: string (enum: chatkit.thread_item) (required) — Type discriminator that is always `chatkit.thread_item`.
- created_at: integer (required) — Unix timestamp (in seconds) for when the item was created.
- thread_id: string (required) — Identifier of the parent thread.
- type: string (enum: chatkit.client_tool_call) (required) — Type discriminator that is always `chatkit.client_tool_call`...
- status: object (required) — Execution status for the tool call.
- call_id: string (required) — Identifier for the client tool call.
- name: string (required) — Tool name that was invoked.
- arguments: string (required) — JSON-encoded arguments that were sent to the tool.
- output: object (required)

### ClientToolCallStatus
Type: string

string (enum: in_progress, completed)

### ClosedStatus
Type: object
Description: Indicates that a thread has been closed.

- type: string (enum: closed) (required) — Status discriminator that is always `closed`.
- reason: object (required)

### CodeInterpreterFileOutput
Type: object
Description: The output of a code interpreter tool call that is a file.


- type: string (enum: files) (required) — The type of the code interpreter file output. Always `files`...
- files: array<object (2 fields)> (required)

### CodeInterpreterOutputImage
Type: object
Description: The image output from the code interpreter.


- type: string (enum: image) (required) — The type of the output. Always 'image'.
- url: string (required) — The URL of the image output from the code interpreter.

### CodeInterpreterOutputLogs
Type: object
Description: The logs output from the code interpreter.


- type: string (enum: logs) (required) — The type of the output. Always 'logs'.
- logs: string (required) — The logs output from the code interpreter.

### CodeInterpreterTextOutput
Type: object
Description: The output of a code interpreter tool call that is text.


- type: string (enum: logs) (required) — The type of the code interpreter text output. Always `logs`....
- logs: string (required) — The logs of the code interpreter tool call.


### CodeInterpreterTool
Type: object
Description: A tool that runs Python code to help generate a response to a prompt.


- type: string (enum: code_interpreter) (required) — The type of the code interpreter tool. Always `code_interpre...
- container: object (required) — The code interpreter container. Can be a container ID or an ...

### CodeInterpreterToolAuto
Type: object
Description: Configuration for a code interpreter container. Optionally specify the IDs
of the files to run the code on.


- type: string (enum: auto) (required) — Always `auto`.
- file_ids: array<string> (optional) — An optional list of uploaded files to make available to your...

### CodeInterpreterToolCall
Type: object
Description: A tool call to run code.


- type: string (enum: code_interpreter_call) (required) — The type of the code interpreter tool call. Always `code_int...
- id: string (required) — The unique ID of the code interpreter tool call.

- status: string (enum: in_progress, completed, incomplete, interpreting, failed) (required) — The status of the code interpreter tool call. Valid values a...
- container_id: string (required) — The ID of the container used to run the code.

- code: object (required)
- outputs: object (required)

### ComparisonFilter
Type: object
Description: A filter used to compare a specified attribute key to a given value using a defined comparison operation.


- type: string (enum: eq, ne, gt, gte, lt...) (required) — Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, ...
- key: string (required) — The key to compare against the value.
- value: object (required) — The value to compare against the attribute key; supports str...

### ComparisonFilterValueItems
Type: object

(empty)

### CompleteUploadRequest
Type: object

- part_ids: array<string> (required) — The ordered list of Part IDs.

- md5: string (optional) — The optional md5 checksum for the file contents to verify if...

### CompletionUsage
Type: object
Description: Usage statistics for the completion request.

- completion_tokens: integer (required) — Number of tokens in the generated completion.
- prompt_tokens: integer (required) — Number of tokens in the prompt.
- total_tokens: integer (required) — Total number of tokens used in the request (prompt + complet...
- completion_tokens_details: object (4 fields) (optional) — Breakdown of tokens used in a completion.
- prompt_tokens_details: object (2 fields) (optional) — Breakdown of tokens used in the prompt.

### CompoundFilter
Type: object
Description: Combine multiple filters using `and` or `or`.

- type: string (enum: and, or) (required) — Type of operation: `and` or `or`.
- filters: array<object> (required) — Array of filters to combine. Items can be `ComparisonFilter`...

### ComputerAction
Type: object

(empty)

### ComputerCallOutputItemParam
Type: object
Description: The output of a computer tool call.

- id: object (optional)
- call_id: string (required) — The ID of the computer tool call that produced the output.
- type: string (enum: computer_call_output) (required) — The type of the computer tool call output. Always `computer_...
- output: object (required)
- acknowledged_safety_checks: object (optional)
- status: object (optional)

### ComputerCallSafetyCheckParam
Type: object
Description: A pending safety check for the computer call.

- id: string (required) — The ID of the pending safety check.
- code: object (optional)
- message: object (optional)

### ComputerEnvironment
Type: string

string (enum: windows, mac, linux, ubuntu, browser)

### ComputerScreenshotContent
Type: object
Description: A screenshot of a computer.

- type: string (enum: computer_screenshot) (required) — Specifies the event type. For a computer screenshot, this pr...
- image_url: object (required)
- file_id: object (required)

### ComputerScreenshotImage
Type: object
Description: A computer screenshot image used with the computer use tool.


- type: string (enum: computer_screenshot) (required) — Specifies the event type. For a computer screenshot, this pr...
- image_url: string (optional) — The URL of the screenshot image.
- file_id: string (optional) — The identifier of an uploaded file that contains the screens...

### ComputerToolCall
Type: object
Description: A tool call to a computer use tool. See the 
[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.


- type: string (enum: computer_call) (required) — The type of the computer call. Always `computer_call`.
- id: string (required) — The unique ID of the computer call.
- call_id: string (required) — An identifier used when responding to the tool call with out...
- action: object (required)
- pending_safety_checks: array<object> (required) — The pending safety checks for the computer call.

- status: string (enum: in_progress, completed, incomplete) (required) — The status of the item. One of `in_progress`, `completed`, o...

### ComputerToolCallOutput
Type: object
Description: The output of a computer tool call.


- type: string (enum: computer_call_output) (required) — The type of the computer tool call output. Always `computer_...
- id: string (optional) — The ID of the computer tool call output.

- call_id: string (required) — The ID of the computer tool call that produced the output.

- acknowledged_safety_checks: array<object> (optional) — The safety checks reported by the API that have been acknowl...
- output: object (required)
- status: string (enum: in_progress, completed, incomplete) (optional) — The status of the message input. One of `in_progress`, `comp...

### ComputerToolCallOutputResource
Type: object

(empty)

### ComputerToolCallSafetyCheck
Type: object
Description: A pending safety check for the computer call.


- id: string (required) — The ID of the pending safety check.
- code: string (required) — The type of the pending safety check.
- message: string (required) — Details about the pending safety check.

### ComputerUsePreviewTool
Type: object
Description: A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

- type: string (enum: computer_use_preview) (required) — The type of the computer use tool. Always `computer_use_prev...
- environment: object (required) — The type of computer environment to control.
- display_width: integer (required) — The width of the computer display.
- display_height: integer (required) — The height of the computer display.

### ContainerFileCitationBody
Type: object
Description: A citation for a container file used to generate a model response.

- type: string (enum: container_file_citation) (required) — The type of the container file citation. Always `container_f...
- container_id: string (required) — The ID of the container file.
- file_id: string (required) — The ID of the file.
- start_index: integer (required) — The index of the first character of the container file citat...
- end_index: integer (required) — The index of the last character of the container file citati...
- filename: string (required) — The filename of the container file cited.

### ContainerFileListResource
Type: object

- object: object (required) — The type of object returned, must be 'list'.
- data: array<object> (required) — A list of container files.
- first_id: string (required) — The ID of the first file in the list.
- last_id: string (required) — The ID of the last file in the list.
- has_more: boolean (required) — Whether there are more files available.

### ContainerFileResource
Type: object

- id: string (required) — Unique identifier for the file.
- object: string (required) — The type of this object (`container.file`).
- container_id: string (required) — The container this file belongs to.
- created_at: integer (required) — Unix timestamp (in seconds) when the file was created.
- bytes: integer (required) — Size of the file in bytes.
- path: string (required) — Path of the file in the container.
- source: string (required) — Source of the file (e.g., `user`, `assistant`).

### ContainerListResource
Type: object

- object: object (required) — The type of object returned, must be 'list'.
- data: array<object> (required) — A list of containers.
- first_id: string (required) — The ID of the first container in the list.
- last_id: string (required) — The ID of the last container in the list.
- has_more: boolean (required) — Whether there are more containers available.

### ContainerResource
Type: object

- id: string (required) — Unique identifier for the container.
- object: string (required) — The type of this object.
- name: string (required) — Name of the container.
- created_at: integer (required) — Unix timestamp (in seconds) when the container was created.
- status: string (required) — Status of the container (e.g., active, deleted).
- expires_after: object (2 fields) (optional) — The container will expire after this time period.
The anchor...

### Content
Type: object
Description: Multi-modal input and output contents.


(empty)

### Conversation
Type: object

(empty)

### Conversation-2
Type: object
Description: The conversation that this response belongs to. Input items and output items from this response are automatically added to this conversation.

- id: string (required) — The unique ID of the conversation.

### ConversationItem
Type: object
Description: A single item within a conversation. The set of possible types are the same as the `output` type of a [Response object](https://platform.openai.com/docs/api-reference/responses/object#responses/object...

(empty)

### ConversationItemList
Type: object
Description: A list of Conversation items.

- object: object (required) — The type of object returned, must be `list`.
- data: array<object> (required) — A list of conversation items.
- has_more: boolean (required) — Whether there are more items available.
- first_id: string (required) — The ID of the first item in the list.
- last_id: string (required) — The ID of the last item in the list.

### ConversationParam
Type: object
Description: The conversation that this response belongs to.

- id: string (required) — The unique ID of the conversation.

### ConversationResource
Type: object

- id: string (required) — The unique ID of the conversation.
- object: string (enum: conversation) (required) — The object type, which is always `conversation`.
- metadata: object (required) — Set of 16 key-value pairs that can be attached to an object....
- created_at: integer (required) — The time at which the conversation was created, measured in ...

### Coordinate
Type: object
Description: An x/y coordinate pair, e.g. `{ x: 100, y: 200 }`.


- x: integer (required) — The x-coordinate.

- y: integer (required) — The y-coordinate.


### CostsResult
Type: object
Description: The aggregated costs details of the specific time bucket.

- object: string (enum: organization.costs.result) (required)
- amount: object (2 fields) (optional) — The monetary value in its associated currency.
- line_item: object (optional)
- project_id: object (optional)

### CreateAssistantRequest
Type: object

- model: object (required) — ID of the model to use. You can use the [List models](https:...
- name: object (optional)
- description: object (optional)
- instructions: object (optional)
- reasoning_effort: object (optional)
- tools: array<object> (optional) — A list of tool enabled on the assistant. There can be a maxi...
- tool_resources: object (optional)
- metadata: object (optional)
- temperature: object (optional)
- top_p: object (optional)
- response_format: object (optional)

### CreateChatCompletionRequest
Type: object

(empty)

### CreateChatCompletionResponse
Type: object
Description: Represents a chat completion response returned by model, based on the provided input.

- id: string (required) — A unique identifier for the chat completion.
- choices: array<object (4 fields)> (required) — A list of chat completion choices. Can be more than one if `...
- created: integer (required) — The Unix timestamp (in seconds) of when the chat completion ...
- model: string (required) — The model used for the chat completion.
- service_tier: object (optional)
- system_fingerprint: string (optional) — This fingerprint represents the backend configuration that t...
- object: string (enum: chat.completion) (required) — The object type, which is always `chat.completion`.
- usage: object (optional)

### CreateChatCompletionStreamResponse
Type: object
Description: Represents a streamed chunk of a chat completion response returned
by the model, based on the provided input. 
[Learn more](https://platform.openai.com/docs/guides/streaming-responses).


- id: string (required) — A unique identifier for the chat completion. Each chunk has ...
- choices: array<object (4 fields)> (required) — A list of chat completion choices. Can contain more than one...
- created: integer (required) — The Unix timestamp (in seconds) of when the chat completion ...
- model: string (required) — The model to generate the completion.
- service_tier: object (optional)
- system_fingerprint: string (optional) — This fingerprint represents the backend configuration that t...
- object: string (enum: chat.completion.chunk) (required) — The object type, which is always `chat.completion.chunk`.
- usage: object (optional) — An optional field that will only be present when you set
`st...

### CreateChatSessionBody
Type: object
Description: Parameters for provisioning a new ChatKit session.

- workflow: object (required) — Workflow that powers the session.
- user: string (required) — A free-form string that identifies your end user; ensures th...
- expires_after: object (optional) — Optional override for session expiration timing in seconds f...
- rate_limits: object (optional) — Optional override for per-minute request limits. When omitte...
- chatkit_configuration: object (optional) — Optional overrides for ChatKit runtime configuration feature...

### CreateCompletionRequest
Type: object

- model: object (required) — ID of the model to use. You can use the [List models](https:...
- prompt: object (required) — The prompt(s) to generate completions for, encoded as a stri...
- best_of: integer (optional) — Generates `best_of` completions server-side and returns the ...
- echo: boolean (optional) — Echo back the prompt in addition to the completion

- frequency_penalty: number (optional) — Number between -2.0 and 2.0. Positive values penalize new to...
- logit_bias: object (optional) — Modify the likelihood of specified tokens appearing in the c...
- logprobs: integer (optional) — Include the log probabilities on the `logprobs` most likely ...
- max_tokens: integer (optional) — The maximum number of [tokens](/tokenizer) that can be gener...
- n: integer (optional) — How many completions to generate for each prompt.

**Note:**...
- presence_penalty: number (optional) — Number between -2.0 and 2.0. Positive values penalize new to...
- seed: integer (int64) (optional) — If specified, our system will make a best effort to sample d...
- stop: object (optional)
- stream: boolean (optional) — Whether to stream back partial progress. If set, tokens will...
- stream_options: object (optional)
- suffix: string (optional) — The suffix that comes after a completion of inserted text.

...
- temperature: number (optional) — What sampling temperature to use, between 0 and 2. Higher va...
- top_p: number (optional) — An alternative to sampling with temperature, called nucleus ...
- user: string (optional) — A unique identifier representing your end-user, which can he...

### CreateCompletionResponse
Type: object
Description: Represents a completion response from the API. Note: both the streamed and non-streamed response objects share the same shape (unlike the chat endpoint).


- id: string (required) — A unique identifier for the completion.
- choices: array<object (4 fields)> (required) — The list of completion choices the model generated for the i...
- created: integer (required) — The Unix timestamp (in seconds) of when the completion was c...
- model: string (required) — The model used for completion.
- system_fingerprint: string (optional) — This fingerprint represents the backend configuration that t...
- object: string (enum: text_completion) (required) — The object type, which is always "text_completion"
- usage: object (optional)

### CreateContainerBody
Type: object

- name: string (required) — Name of the container to create.
- file_ids: array<string> (optional) — IDs of files to copy to the container.
- expires_after: object (2 fields) (optional) — Container expiration time in seconds relative to the 'anchor...

### CreateContainerFileBody
Type: object

- file_id: string (optional) — Name of the file to create.
- file: string (binary) (optional) — The File object (not file name) to be uploaded.


### CreateConversationBody
Type: object

- metadata: object (optional)
- items: object (optional)

### CreateEmbeddingRequest
Type: object

- input: object (required) — Input text to embed, encoded as a string or array of tokens....
- model: object (required) — ID of the model to use. You can use the [List models](https:...
- encoding_format: string (enum: float, base64) (optional) — The format to return the embeddings in. Can be either `float...
- dimensions: integer (optional) — The number of dimensions the resulting output embeddings sho...
- user: string (optional) — A unique identifier representing your end-user, which can he...

### CreateEmbeddingResponse
Type: object

- data: array<object> (required) — The list of embeddings generated by the model.
- model: string (required) — The name of the model used to generate the embedding.
- object: string (enum: list) (required) — The object type, which is always "list".
- usage: object (2 fields) (required) — The usage information for the request.

### CreateEvalCompletionsRunDataSource
Type: object
Description: A CompletionsRunDataSource object describing a model sampling configuration.


- type: string (enum: completions) (required) — The type of run data source. Always `completions`.
- input_messages: object (optional) — Used when sampling from a model. Dictates the structure of t...
- sampling_params: object (7 fields) (optional)
- model: string (optional) — The name of the model to use for generating completions (e.g...
- source: object (required) — Determines what populates the `item` namespace in this run's...

### CreateEvalCustomDataSourceConfig
Type: object
Description: A CustomDataSourceConfig object that defines the schema for the data source used for the evaluation runs.
This schema is used to define the shape of the data that will be:
- Used to define your testin...

- type: string (enum: custom) (required) — The type of data source. Always `custom`.
- item_schema: object (required) — The json schema for each row in the data source.
- include_sample_schema: boolean (optional) — Whether the eval should expect you to populate the sample na...

### CreateEvalItem
Type: object
Description: A chat message that makes up the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

(empty)

### CreateEvalJsonlRunDataSource
Type: object
Description: A JsonlRunDataSource object with that specifies a JSONL file that matches the eval 


- type: string (enum: jsonl) (required) — The type of data source. Always `jsonl`.
- source: object (required) — Determines what populates the `item` namespace in the data s...

### CreateEvalLabelModelGrader
Type: object
Description: A LabelModelGrader object which uses a model to assign labels to each item
in the evaluation.


- type: string (enum: label_model) (required) — The object type, which is always `label_model`.
- name: string (required) — The name of the grader.
- model: string (required) — The model to use for the evaluation. Must support structured...
- input: array<object> (required) — A list of chat messages forming the prompt or context. May i...
- labels: array<string> (required) — The labels to classify to each item in the evaluation.
- passing_labels: array<string> (required) — The labels that indicate a passing result. Must be a subset ...

### CreateEvalLogsDataSourceConfig
Type: object
Description: A data source config which specifies the metadata property of your logs query.
This is usually metadata like `usecase=chatbot` or `prompt-version=v2`, etc.


- type: string (enum: logs) (required) — The type of data source. Always `logs`.
- metadata: object (optional) — Metadata filters for the logs data source.

### CreateEvalRequest
Type: object

- name: string (optional) — The name of the evaluation.
- metadata: object (optional)
- data_source_config: object (required) — The configuration for the data source used for the evaluatio...
- testing_criteria: array<object> (required) — A list of graders for all eval runs in this group. Graders c...

### CreateEvalResponsesRunDataSource
Type: object
Description: A ResponsesRunDataSource object describing a model sampling configuration.


- type: string (enum: responses) (required) — The type of run data source. Always `responses`.
- input_messages: object (optional) — Used when sampling from a model. Dictates the structure of t...
- sampling_params: object (7 fields) (optional)
- model: string (optional) — The name of the model to use for generating completions (e.g...
- source: object (required) — Determines what populates the `item` namespace in this run's...

### CreateEvalRunRequest
Type: object

- name: string (optional) — The name of the run.
- metadata: object (optional)
- data_source: object (required) — Details about the run's data source.

### CreateEvalStoredCompletionsDataSourceConfig
Type: object
Description: Deprecated in favor of LogsDataSourceConfig.


- type: string (enum: stored_completions) (required) — The type of data source. Always `stored_completions`.
- metadata: object (optional) — Metadata filters for the stored completions data source.

### CreateFileRequest
Type: object

- file: string (binary) (required) — The File object (not file name) to be uploaded.

- purpose: object (required)
- expires_after: object (optional)

### CreateFineTuningCheckpointPermissionRequest
Type: object

- project_ids: array<string> (required) — The project identifiers to grant access to.

### CreateFineTuningJobRequest
Type: object

- model: object (required) — The name of the model to fine-tune. You can select one of th...
- training_file: string (required) — The ID of an uploaded file that contains training data.

See...
- hyperparameters: object (3 fields) (optional) — The hyperparameters used for the fine-tuning job.
This value...
- suffix: string (optional) — A string of up to 64 characters that will be added to your f...
- validation_file: string (optional) — The ID of an uploaded file that contains validation data.

I...
- integrations: array<object (2 fields)> (optional) — A list of integrations to enable for your fine-tuning job.
- seed: integer (optional) — The seed controls the reproducibility of the job. Passing in...
- method: object (optional)
- metadata: object (optional)

### CreateImageEditRequest
Type: object

- image: object (required) — The image(s) to edit. Must be a supported image file or an a...
- prompt: string (required) — A text description of the desired image(s). The maximum leng...
- mask: string (binary) (optional) — An additional image whose fully transparent areas (e.g. wher...
- background: string (enum: transparent, opaque, auto) (optional) — Allows to set transparency for the background of the generat...
- model: object (optional) — The model to use for image generation. Only `dall-e-2` and `...
- n: integer (optional) — The number of images to generate. Must be between 1 and 10.
- size: string (enum: 256x256, 512x512, 1024x1024, 1536x1024, 1024x1536...) (optional) — The size of the generated images. Must be one of `1024x1024`...
- response_format: string (enum: url, b64_json) (optional) — The format in which the generated images are returned. Must ...
- output_format: string (enum: png, jpeg, webp) (optional) — The format in which the generated images are returned. This ...
- output_compression: integer (optional) — The compression level (0-100%) for the generated images. Thi...
- user: string (optional) — A unique identifier representing your end-user, which can he...
- input_fidelity: object (optional)
- stream: boolean (optional) — Edit the image in streaming mode. Defaults to `false`. See t...
- partial_images: object (optional)
- quality: string (enum: standard, low, medium, high, auto) (optional) — The quality of the image that will be generated. `high`, `me...

### CreateImageRequest
Type: object

- prompt: string (required) — A text description of the desired image(s). The maximum leng...
- model: object (optional) — The model to use for image generation. One of `dall-e-2`, `d...
- n: integer (optional) — The number of images to generate. Must be between 1 and 10. ...
- quality: string (enum: standard, hd, low, medium, high...) (optional) — The quality of the image that will be generated.

- `auto` (...
- response_format: string (enum: url, b64_json) (optional) — The format in which generated images with `dall-e-2` and `da...
- output_format: string (enum: png, jpeg, webp) (optional) — The format in which the generated images are returned. This ...
- output_compression: integer (optional) — The compression level (0-100%) for the generated images. Thi...
- stream: boolean (optional) — Generate the image in streaming mode. Defaults to `false`. S...
- partial_images: object (optional)
- size: string (enum: auto, 1024x1024, 1536x1024, 1024x1536, 256x256...) (optional) — The size of the generated images. Must be one of `1024x1024`...
- moderation: string (enum: low, auto) (optional) — Control the content-moderation level for images generated by...
- background: string (enum: transparent, opaque, auto) (optional) — Allows to set transparency for the background of the generat...
- style: string (enum: vivid, natural) (optional) — The style of the generated images. This parameter is only su...
- user: string (optional) — A unique identifier representing your end-user, which can he...

### CreateImageVariationRequest
Type: object

- image: string (binary) (required) — The image to use as the basis for the variation(s). Must be ...
- model: object (optional) — The model to use for image generation. Only `dall-e-2` is su...
- n: integer (optional) — The number of images to generate. Must be between 1 and 10.
- response_format: string (enum: url, b64_json) (optional) — The format in which the generated images are returned. Must ...
- size: string (enum: 256x256, 512x512, 1024x1024) (optional) — The size of the generated images. Must be one of `256x256`, ...
- user: string (optional) — A unique identifier representing your end-user, which can he...

### CreateMessageRequest
Type: object

- role: string (enum: user, assistant) (required) — The role of the entity that is creating the message. Allowed...
- content: object (required)
- attachments: object (optional)
- metadata: object (optional)

### CreateModelResponseProperties
Type: object

(empty)

### CreateModerationRequest
Type: object

- input: object (required) — Input (or inputs) to classify. Can be a single string, an ar...
- model: object (optional) — The content moderation model you would like to use. Learn mo...

### CreateModerationResponse
Type: object
Description: Represents if a given text input is potentially harmful.

- id: string (required) — The unique identifier for the moderation request.
- model: string (required) — The model used to generate the moderation results.
- results: array<object (4 fields)> (required) — A list of moderation objects.

### CreateResponse
Type: object

(empty)

### CreateRunRequest
Type: object

- assistant_id: string (required) — The ID of the [assistant](https://platform.openai.com/docs/a...
- model: object (optional) — The ID of the [Model](https://platform.openai.com/docs/api-r...
- reasoning_effort: object (optional)
- instructions: string (optional) — Overrides the [instructions](https://platform.openai.com/doc...
- additional_instructions: string (optional) — Appends additional instructions at the end of the instructio...
- additional_messages: array<object> (optional) — Adds additional messages to the thread before creating the r...
- tools: array<object> (optional) — Override the tools the assistant can use for this run. This ...
- metadata: object (optional)
- temperature: number (optional) — What sampling temperature to use, between 0 and 2. Higher va...
- top_p: number (optional) — An alternative to sampling with temperature, called nucleus ...
- stream: boolean (optional) — If `true`, returns a stream of events that happen during the...
- max_prompt_tokens: integer (optional) — The maximum number of prompt tokens that may be used over th...
- max_completion_tokens: integer (optional) — The maximum number of completion tokens that may be used ove...
- truncation_strategy: object (optional)
- tool_choice: object (optional)
- parallel_tool_calls: object (optional)
- response_format: object (optional)

### CreateRunRequestWithoutStream
Type: object

- assistant_id: string (required) — The ID of the [assistant](https://platform.openai.com/docs/a...
- model: object (optional) — The ID of the [Model](https://platform.openai.com/docs/api-r...
- reasoning_effort: object (optional)
- instructions: string (optional) — Overrides the [instructions](https://platform.openai.com/doc...
- additional_instructions: string (optional) — Appends additional instructions at the end of the instructio...
- additional_messages: array<object> (optional) — Adds additional messages to the thread before creating the r...
- tools: array<object> (optional) — Override the tools the assistant can use for this run. This ...
- metadata: object (optional)
- temperature: number (optional) — What sampling temperature to use, between 0 and 2. Higher va...
- top_p: number (optional) — An alternative to sampling with temperature, called nucleus ...
- max_prompt_tokens: integer (optional) — The maximum number of prompt tokens that may be used over th...
- max_completion_tokens: integer (optional) — The maximum number of completion tokens that may be used ove...
- truncation_strategy: object (optional)
- tool_choice: object (optional)
- parallel_tool_calls: object (optional)
- response_format: object (optional)

### CreateSpeechRequest
Type: object

- model: object (required) — One of the available [TTS models](https://platform.openai.co...
- input: string (required) — The text to generate audio for. The maximum length is 4096 c...
- instructions: string (optional) — Control the voice of your generated audio with additional in...
- voice: object (required) — The voice to use when generating the audio. Supported voices...
- response_format: string (enum: mp3, opus, aac, flac, wav...) (optional) — The format to audio in. Supported formats are `mp3`, `opus`,...
- speed: number (optional) — The speed of the generated audio. Select a value from `0.25`...
- stream_format: string (enum: sse, audio) (optional) — The format to stream the audio in. Supported formats are `ss...

### CreateSpeechResponseStreamEvent
Type: object

(empty)

### CreateThreadAndRunRequest
Type: object

- assistant_id: string (required) — The ID of the [assistant](https://platform.openai.com/docs/a...
- thread: object (optional)
- model: object (optional) — The ID of the [Model](https://platform.openai.com/docs/api-r...
- instructions: string (optional) — Override the default system message of the assistant. This i...
- tools: array<object> (optional) — Override the tools the assistant can use for this run. This ...
- tool_resources: object (2 fields) (optional) — A set of resources that are used by the assistant's tools. T...
- metadata: object (optional)
- temperature: number (optional) — What sampling temperature to use, between 0 and 2. Higher va...
- top_p: number (optional) — An alternative to sampling with temperature, called nucleus ...
- stream: boolean (optional) — If `true`, returns a stream of events that happen during the...
- max_prompt_tokens: integer (optional) — The maximum number of prompt tokens that may be used over th...
- max_completion_tokens: integer (optional) — The maximum number of completion tokens that may be used ove...
- truncation_strategy: object (optional)
- tool_choice: object (optional)
- parallel_tool_calls: object (optional)
- response_format: object (optional)

### CreateThreadAndRunRequestWithoutStream
Type: object

- assistant_id: string (required) — The ID of the [assistant](https://platform.openai.com/docs/a...
- thread: object (optional)
- model: object (optional) — The ID of the [Model](https://platform.openai.com/docs/api-r...
- instructions: string (optional) — Override the default system message of the assistant. This i...
- tools: array<object> (optional) — Override the tools the assistant can use for this run. This ...
- tool_resources: object (2 fields) (optional) — A set of resources that are used by the assistant's tools. T...
- metadata: object (optional)
- temperature: number (optional) — What sampling temperature to use, between 0 and 2. Higher va...
- top_p: number (optional) — An alternative to sampling with temperature, called nucleus ...
- max_prompt_tokens: integer (optional) — The maximum number of prompt tokens that may be used over th...
- max_completion_tokens: integer (optional) — The maximum number of completion tokens that may be used ove...
- truncation_strategy: object (optional)
- tool_choice: object (optional)
- parallel_tool_calls: object (optional)
- response_format: object (optional)

### CreateThreadRequest
Type: object
Description: Options to create a new thread. If no thread is provided when running a
request, an empty thread will be created.


- messages: array<object> (optional) — A list of [messages](https://platform.openai.com/docs/api-re...
- tool_resources: object (optional)
- metadata: object (optional)

### CreateTranscriptionRequest
Type: object

- file: string (binary) (required) — The audio file object (not file name) to transcribe, in one ...
- model: object (required) — ID of the model to use. The options are `gpt-4o-transcribe`,...
- language: string (optional) — The language of the input audio. Supplying the input languag...
- prompt: string (optional) — An optional text to guide the model's style or continue a pr...
- response_format: object (optional)
- temperature: number (optional) — The sampling temperature, between 0 and 1. Higher values lik...
- stream: object (optional)
- chunking_strategy: object (optional)
- timestamp_granularities: array<string (enum: word, segment)> (optional) — The timestamp granularities to populate for this transcripti...
- include: array<object> (optional) — Additional information to include in the transcription respo...

### CreateTranscriptionResponseJson
Type: object
Description: Represents a transcription response returned by model, based on the provided input.

- text: string (required) — The transcribed text.
- logprobs: array<object (3 fields)> (optional) — The log probabilities of the tokens in the transcription. On...
- usage: object (optional) — Token usage statistics for the request.

### CreateTranscriptionResponseStreamEvent
Type: object

(empty)

### CreateTranscriptionResponseVerboseJson
Type: object
Description: Represents a verbose json transcription response returned by model, based on the provided input.

- language: string (required) — The language of the input audio.
- duration: number (required) — The duration of the input audio.
- text: string (required) — The transcribed text.
- words: array<object> (optional) — Extracted words and their corresponding timestamps.
- segments: array<object> (optional) — Segments of the transcribed text and their corresponding det...
- usage: object (optional)

### CreateTranslationRequest
Type: object

- file: string (binary) (required) — The audio file object (not file name) translate, in one of t...
- model: object (required) — ID of the model to use. Only `whisper-1` (which is powered b...
- prompt: string (optional) — An optional text to guide the model's style or continue a pr...
- response_format: string (enum: json, text, srt, verbose_json, vtt) (optional) — The format of the output, in one of these options: `json`, `...
- temperature: number (optional) — The sampling temperature, between 0 and 1. Higher values lik...

### CreateTranslationResponseJson
Type: object

- text: string (required)

### CreateTranslationResponseVerboseJson
Type: object

- language: string (required) — The language of the output translation (always `english`).
- duration: number (required) — The duration of the input audio.
- text: string (required) — The translated text.
- segments: array<object> (optional) — Segments of the translated text and their corresponding deta...

### CreateUploadRequest
Type: object

- filename: string (required) — The name of the file to upload.

- purpose: string (enum: assistants, batch, fine-tune, vision) (required) — The intended purpose of the uploaded file.

See the [documen...
- bytes: integer (required) — The number of bytes in the file you are uploading.

- mime_type: string (required) — The MIME type of the file.

This must fall within the suppor...
- expires_after: object (optional)

### CreateVectorStoreFileBatchRequest
Type: object

- file_ids: array<string> (required) — A list of [File](https://platform.openai.com/docs/api-refere...
- chunking_strategy: object (optional)
- attributes: object (optional)

### CreateVectorStoreFileRequest
Type: object

- file_id: string (required) — A [File](https://platform.openai.com/docs/api-reference/file...
- chunking_strategy: object (optional)
- attributes: object (optional)

### CreateVectorStoreRequest
Type: object

- file_ids: array<string> (optional) — A list of [File](https://platform.openai.com/docs/api-refere...
- name: string (optional) — The name of the vector store.
- expires_after: object (optional)
- chunking_strategy: object (optional)
- metadata: object (optional)

### CreateVideoBody
Type: object
Description: Parameters for creating a new video generation job.

- model: object (optional) — The video generation model to use. Defaults to `sora-2`.
- prompt: string (required) — Text prompt that describes the video to generate.
- input_reference: string (binary) (optional) — Optional image reference that guides generation.
- seconds: object (optional) — Clip duration in seconds. Defaults to 4 seconds.
- size: object (optional) — Output resolution formatted as width x height. Defaults to 7...

### CreateVideoRemixBody
Type: object
Description: Parameters for remixing an existing generated video.

- prompt: string (required) — Updated text prompt that directs the remix generation.

### CustomTool
Type: object
Description: A custom tool that processes input using a specified format. Learn more about
[custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools).


- type: string (enum: custom) (required) — The type of the custom tool. Always `custom`.
- name: string (required) — The name of the custom tool, used to identify it in tool cal...
- description: string (optional) — Optional description of the custom tool, used to provide mor...
- format: object (optional) — The input format for the custom tool. Default is unconstrain...

### CustomToolCall
Type: object
Description: A call to a custom tool created by the model.


- type: string (enum: custom_tool_call) (required) — The type of the custom tool call. Always `custom_tool_call`....
- id: string (optional) — The unique ID of the custom tool call in the OpenAI platform...
- call_id: string (required) — An identifier used to map this custom tool call to a tool ca...
- name: string (required) — The name of the custom tool being called.

- input: string (required) — The input for the custom tool call generated by the model.


### CustomToolCallOutput
Type: object
Description: The output of a custom tool call from your code, being sent back to the model.


- type: string (enum: custom_tool_call_output) (required) — The type of the custom tool call output. Always `custom_tool...
- id: string (optional) — The unique ID of the custom tool call output in the OpenAI p...
- call_id: string (required) — The call ID, used to map this custom tool call output to a c...
- output: object (required) — The output from the custom tool call generated by your code....

### CustomToolChatCompletions
Type: object
Description: A custom tool that processes input using a specified format.


- type: string (enum: custom) (required) — The type of the custom tool. Always `custom`.
- custom: object (3 fields) (required) — Properties of the custom tool.


### DeleteAssistantResponse
Type: object

- id: string (required)
- deleted: boolean (required)
- object: string (enum: assistant.deleted) (required)

### DeleteCertificateResponse
Type: object

- object: object (required) — The object type, must be `certificate.deleted`.
- id: string (required) — The ID of the certificate that was deleted.

### DeleteFileResponse
Type: object

- id: string (required)
- object: string (enum: file) (required)
- deleted: boolean (required)

### DeleteFineTuningCheckpointPermissionResponse
Type: object

- id: string (required) — The ID of the fine-tuned model checkpoint permission that wa...
- object: string (enum: checkpoint.permission) (required) — The object type, which is always "checkpoint.permission".
- deleted: boolean (required) — Whether the fine-tuned model checkpoint permission was succe...

### DeleteMessageResponse
Type: object

- id: string (required)
- deleted: boolean (required)
- object: string (enum: thread.message.deleted) (required)

### DeleteModelResponse
Type: object

- id: string (required)
- deleted: boolean (required)
- object: string (required)

### DeleteThreadResponse
Type: object

- id: string (required)
- deleted: boolean (required)
- object: string (enum: thread.deleted) (required)

### DeleteVectorStoreFileResponse
Type: object

- id: string (required)
- deleted: boolean (required)
- object: string (enum: vector_store.file.deleted) (required)

### DeleteVectorStoreResponse
Type: object

- id: string (required)
- deleted: boolean (required)
- object: string (enum: vector_store.deleted) (required)

### DeletedConversation
Type: object

(empty)

### DeletedConversationResource
Type: object

- object: string (enum: conversation.deleted) (required)
- deleted: boolean (required)
- id: string (required)

### DeletedThreadResource
Type: object
Description: Confirmation payload returned after deleting a thread.

- id: string (required) — Identifier of the deleted thread.
- object: string (enum: chatkit.thread.deleted) (required) — Type discriminator that is always `chatkit.thread.deleted`.
- deleted: boolean (required) — Indicates that the thread has been deleted.

### DeletedVideoResource
Type: object
Description: Confirmation payload returned after deleting a video.

- object: string (enum: video.deleted) (required) — The object type that signals the deletion response.
- deleted: boolean (required) — Indicates that the video resource was deleted.
- id: string (required) — Identifier of the deleted video.

### DetailEnum
Type: string

string (enum: low, high, auto)

### DoneEvent
Type: object
Description: Occurs when a stream ends.

- event: string (enum: done) (required)
- data: string (enum: [DONE]) (required)

### DoubleClick
Type: object
Description: A double click action.


- type: string (enum: double_click) (required) — Specifies the event type. For a double click action, this pr...
- x: integer (required) — The x-coordinate where the double click occurred.

- y: integer (required) — The y-coordinate where the double click occurred.


### Drag
Type: object
Description: A drag action.


- type: string (enum: drag) (required) — Specifies the event type. For a drag action, this property i...
- path: array<object> (required) — An array of coordinates representing the path of the drag ac...

### EasyInputMessage
Type: object
Description: A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` ro...

- role: string (enum: user, assistant, system, developer) (required) — The role of the message input. One of `user`, `assistant`, `...
- content: object (required) — Text, image, or audio input to the model, used to generate a...
- type: string (enum: message) (optional) — The type of the message input. Always `message`.


### Embedding
Type: object
Description: Represents an embedding vector returned by embedding endpoint.


- index: integer (required) — The index of the embedding in the list of embeddings.
- embedding: array<number (float)> (required) — The embedding vector, which is a list of floats. The length ...
- object: string (enum: embedding) (required) — The object type, which is always "embedding".

### Error
Type: object

- code: object (required)
- message: string (required)
- param: object (required)
- type: string (required)

### Error-2
Type: object

- code: string (required)
- message: string (required)

### ErrorEvent
Type: object
Description: Occurs when an [error](https://platform.openai.com/docs/guides/error-codes#api-errors) occurs. This can happen due to an internal server error or a timeout.

- event: string (enum: error) (required)
- data: object (required)

### ErrorResponse
Type: object

- error: object (required)

### Eval
Type: object
Description: An Eval object with a data source config and testing criteria.
An Eval represents a task to be done for your LLM integration.
Like:
 - Improve the quality of my chatbot
 - See how well my chatbot hand...

- object: string (enum: eval) (required) — The object type.
- id: string (required) — Unique identifier for the evaluation.
- name: string (required) — The name of the evaluation.
- data_source_config: object (required) — Configuration of data sources used in runs of the evaluation...
- testing_criteria: array<object> (required) — A list of testing criteria.
- created_at: integer (required) — The Unix timestamp (in seconds) for when the eval was create...
- metadata: object (required)

### EvalApiError
Type: object
Description: An object representing an error response from the Eval API.


- code: string (required) — The error code.
- message: string (required) — The error message.

### EvalCustomDataSourceConfig
Type: object
Description: A CustomDataSourceConfig which specifies the schema of your `item` and optionally `sample` namespaces.
The response schema defines the shape of the data that will be:
- Used to define your testing cri...

- type: string (enum: custom) (required) — The type of data source. Always `custom`.
- schema: object (required) — The json schema for the run data source items.
Learn how to ...

### EvalGraderLabelModel
Type: object

(empty)

### EvalGraderPython
Type: object

(empty)

### EvalGraderScoreModel
Type: object

(empty)

### EvalGraderStringCheck
Type: object

(empty)

### EvalGraderTextSimilarity
Type: object

(empty)

### EvalItem
Type: object
Description: A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` ro...

- role: string (enum: user, assistant, system, developer) (required) — The role of the message input. One of `user`, `assistant`, `...
- content: object (required) — Inputs to the model - can contain template strings.

- type: string (enum: message) (optional) — The type of the message input. Always `message`.


### EvalJsonlFileContentSource
Type: object

- type: string (enum: file_content) (required) — The type of jsonl source. Always `file_content`.
- content: array<object (2 fields)> (required) — The content of the jsonl file.

### EvalJsonlFileIdSource
Type: object

- type: string (enum: file_id) (required) — The type of jsonl source. Always `file_id`.
- id: string (required) — The identifier of the file.

### EvalList
Type: object
Description: An object representing a list of evals.


- object: string (enum: list) (required) — The type of this object. It is always set to "list".

- data: array<object> (required) — An array of eval objects.

- first_id: string (required) — The identifier of the first eval in the data array.
- last_id: string (required) — The identifier of the last eval in the data array.
- has_more: boolean (required) — Indicates whether there are more evals available.

### EvalLogsDataSourceConfig
Type: object
Description: A LogsDataSourceConfig which specifies the metadata property of your logs query.
This is usually metadata like `usecase=chatbot` or `prompt-version=v2`, etc.
The schema returned by this data source co...

- type: string (enum: logs) (required) — The type of data source. Always `logs`.
- metadata: object (optional)
- schema: object (required) — The json schema for the run data source items.
Learn how to ...

### EvalResponsesSource
Type: object
Description: A EvalResponsesSource object describing a run data source configuration.


- type: string (enum: responses) (required) — The type of run data source. Always `responses`.
- metadata: object (optional)
- model: object (optional)
- instructions_search: object (optional)
- created_after: object (optional)
- created_before: object (optional)
- reasoning_effort: object (optional)
- temperature: object (optional)
- top_p: object (optional)
- users: object (optional)
- tools: object (optional)

### EvalRun
Type: object
Description: A schema representing an evaluation run.


- object: string (enum: eval.run) (required) — The type of the object. Always "eval.run".
- id: string (required) — Unique identifier for the evaluation run.
- eval_id: string (required) — The identifier of the associated evaluation.
- status: string (required) — The status of the evaluation run.
- model: string (required) — The model that is evaluated, if applicable.
- name: string (required) — The name of the evaluation run.
- created_at: integer (required) — Unix timestamp (in seconds) when the evaluation run was crea...
- report_url: string (required) — The URL to the rendered evaluation run report on the UI dash...
- result_counts: object (4 fields) (required) — Counters summarizing the outcomes of the evaluation run.
- per_model_usage: array<object (6 fields)> (required) — Usage statistics for each model during the evaluation run.
- per_testing_criteria_results: array<object (3 fields)> (required) — Results per testing criteria applied during the evaluation r...
- data_source: object (required) — Information about the run's data source.
- metadata: object (required)
- error: object (required)

### EvalRunList
Type: object
Description: An object representing a list of runs for an evaluation.


- object: string (enum: list) (required) — The type of this object. It is always set to "list".

- data: array<object> (required) — An array of eval run objects.

- first_id: string (required) — The identifier of the first eval run in the data array.
- last_id: string (required) — The identifier of the last eval run in the data array.
- has_more: boolean (required) — Indicates whether there are more evals available.

### EvalRunOutputItem
Type: object
Description: A schema representing an evaluation run output item.


- object: string (enum: eval.run.output_item) (required) — The type of the object. Always "eval.run.output_item".
- id: string (required) — Unique identifier for the evaluation run output item.
- run_id: string (required) — The identifier of the evaluation run associated with this ou...
- eval_id: string (required) — The identifier of the evaluation group.
- created_at: integer (required) — Unix timestamp (in seconds) when the evaluation run was crea...
- status: string (required) — The status of the evaluation run.
- datasource_item_id: integer (required) — The identifier for the data source item.
- datasource_item: object (required) — Details of the input data source item.
- results: array<object> (required) — A list of grader results for this output item.
- sample: object (10 fields) (required) — A sample containing the input and output of the evaluation r...

### EvalRunOutputItemList
Type: object
Description: An object representing a list of output items for an evaluation run.


- object: string (enum: list) (required) — The type of this object. It is always set to "list".

- data: array<object> (required) — An array of eval run output item objects.

- first_id: string (required) — The identifier of the first eval run output item in the data...
- last_id: string (required) — The identifier of the last eval run output item in the data ...
- has_more: boolean (required) — Indicates whether there are more eval run output items avail...

### EvalRunOutputItemResult
Type: object
Description: A single grader result for an evaluation run output item.


- name: string (required) — The name of the grader.
- type: string (optional) — The grader type (for example, "string-check-grader").
- score: number (required) — The numeric score produced by the grader.
- passed: boolean (required) — Whether the grader considered the output a pass.
- sample: object (optional) — Optional sample or intermediate data produced by the grader.

### EvalStoredCompletionsDataSourceConfig
Type: object
Description: Deprecated in favor of LogsDataSourceConfig.


- type: string (enum: stored_completions) (required) — The type of data source. Always `stored_completions`.
- metadata: object (optional)
- schema: object (required) — The json schema for the run data source items.
Learn how to ...

### EvalStoredCompletionsSource
Type: object
Description: A StoredCompletionsRunDataSource configuration describing a set of filters


- type: string (enum: stored_completions) (required) — The type of source. Always `stored_completions`.
- metadata: object (optional)
- model: object (optional)
- created_after: object (optional)
- created_before: object (optional)
- limit: object (optional)

### ExpiresAfterParam
Type: object
Description: Controls when the session expires relative to an anchor timestamp.

- anchor: string (enum: created_at) (required) — Base timestamp used to calculate expiration. Currently fixed...
- seconds: integer (required) — Number of seconds after the anchor when the session expires.

### FileAnnotation
Type: object
Description: Annotation that references an uploaded file.

- type: string (enum: file) (required) — Type discriminator that is always `file` for this annotation...
- source: object (required) — File attachment referenced by the annotation.

### FileAnnotationSource
Type: object
Description: Attachment source referenced by an annotation.

- type: string (enum: file) (required) — Type discriminator that is always `file`.
- filename: string (required) — Filename referenced by the annotation.

### FileCitationBody
Type: object
Description: A citation to a file.

- type: string (enum: file_citation) (required) — The type of the file citation. Always `file_citation`.
- file_id: string (required) — The ID of the file.
- index: integer (required) — The index of the file in the list of files.
- filename: string (required) — The filename of the file cited.

### FileExpirationAfter
Type: object
Description: The expiration policy for a file. By default, files with `purpose=batch` expire after 30 days and all other files are persisted until they are manually deleted.

- anchor: string (enum: created_at) (required) — Anchor timestamp after which the expiration policy applies. ...
- seconds: integer (required) — The number of seconds after the anchor time that the file wi...

### FilePartResource
Type: object
Description: Metadata for a non-image file uploaded through ChatKit.

- id: string (required) — Unique identifier for the uploaded file.
- type: string (enum: file) (required) — Type discriminator that is always `file`.
- name: object (required)
- mime_type: object (required)
- upload_url: object (required)

### FilePath
Type: object
Description: A path to a file.


- type: string (enum: file_path) (required) — The type of the file path. Always `file_path`.

- file_id: string (required) — The ID of the file.

- index: integer (required) — The index of the file in the list of files.


### FilePurpose
Type: string
Description: The intended purpose of the uploaded file. One of: - `assistants`: Used in the Assistants API - `batch`: Used in the Batch API - `fine-tune`: Used for fine-tuning - `vision`: Images used for vision fi...

string (enum: assistants, batch, fine-tune, vision, user_data...)

### FileSearchRanker
Type: string
Description: The ranker to use for the file search. If not specified will use the `auto` ranker.

string (enum: auto, default_2024_08_21)

### FileSearchRankingOptions
Type: object
Description: The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

See the [file search tool documentation](https://platform.openai...

- ranker: object (optional)
- score_threshold: number (required) — The score threshold for the file search. All values must be ...

### FileSearchTool
Type: object
Description: A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

- type: string (enum: file_search) (required) — The type of the file search tool. Always `file_search`.
- vector_store_ids: array<string> (required) — The IDs of the vector stores to search.
- max_num_results: integer (optional) — The maximum number of results to return. This number should ...
- ranking_options: object (optional) — Ranking options for search.
- filters: object (optional)

### FileSearchToolCall
Type: object
Description: The results of a file search tool call. See the
[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.


- id: string (required) — The unique ID of the file search tool call.

- type: string (enum: file_search_call) (required) — The type of the file search tool call. Always `file_search_c...
- status: string (enum: in_progress, searching, completed, incomplete, failed) (required) — The status of the file search tool call. One of `in_progress...
- queries: array<string> (required) — The queries used to search for files.

- results: object (optional)

### FileUploadParam
Type: object
Description: Controls whether users can upload files.

- enabled: boolean (optional) — Enable uploads for this session. Defaults to false.
- max_file_size: integer (optional) — Maximum size in megabytes for each uploaded file. Defaults t...
- max_files: integer (optional) — Maximum number of files that can be uploaded to the session....

### Filters
Type: object

(empty)

### FineTuneChatCompletionRequestAssistantMessage
Type: object

(empty)

### FineTuneChatRequestInput
Type: object
Description: The per-line training example of a fine-tuning input file for chat models using the supervised method.
Input messages may contain text or image content only. Audio and file input messages
are not curr...

- messages: array<object> (optional)
- tools: array<object> (optional) — A list of tools the model may generate JSON inputs for.
- parallel_tool_calls: object (optional)
- functions: array<object> (optional) — A list of functions the model may generate JSON inputs for.

### FineTuneDPOHyperparameters
Type: object
Description: The hyperparameters used for the DPO fine-tuning job.

- beta: object (optional) — The beta value for the DPO method. A higher beta value will ...
- batch_size: object (optional) — Number of examples in each batch. A larger batch size means ...
- learning_rate_multiplier: object (optional) — Scaling factor for the learning rate. A smaller learning rat...
- n_epochs: object (optional) — The number of epochs to train the model for. An epoch refers...

### FineTuneDPOMethod
Type: object
Description: Configuration for the DPO fine-tuning method.

- hyperparameters: object (optional)

### FineTuneMethod
Type: object
Description: The method used for fine-tuning.

- type: string (enum: supervised, dpo, reinforcement) (required) — The type of method. Is either `supervised`, `dpo`, or `reinf...
- supervised: object (optional)
- dpo: object (optional)
- reinforcement: object (optional)

### FineTunePreferenceRequestInput
Type: object
Description: The per-line training example of a fine-tuning input file for chat models using the dpo method.
Input messages may contain text or image content only. Audio and file input messages
are not currently s...

- input: object (3 fields) (optional)
- preferred_output: array<object> (optional) — The preferred completion message for the output.
- non_preferred_output: array<object> (optional) — The non-preferred completion message for the output.

### FineTuneReinforcementHyperparameters
Type: object
Description: The hyperparameters used for the reinforcement fine-tuning job.

- batch_size: object (optional) — Number of examples in each batch. A larger batch size means ...
- learning_rate_multiplier: object (optional) — Scaling factor for the learning rate. A smaller learning rat...
- n_epochs: object (optional) — The number of epochs to train the model for. An epoch refers...
- reasoning_effort: string (enum: default, low, medium, high) (optional) — Level of reasoning effort.

- compute_multiplier: object (optional) — Multiplier on amount of compute used for exploring search sp...
- eval_interval: object (optional) — The number of training steps between evaluation runs.

- eval_samples: object (optional) — Number of evaluation samples to generate per training step.


### FineTuneReinforcementMethod
Type: object
Description: Configuration for the reinforcement fine-tuning method.

- grader: object (required) — The grader used for the fine-tuning job.
- hyperparameters: object (optional)

### FineTuneReinforcementRequestInput
Type: object
Description: Per-line training example for reinforcement fine-tuning. Note that `messages` and `tools` are the only reserved keywords.
Any other arbitrary key-value data can be included on training datapoints and ...

- messages: array<object> (required)
- tools: array<object> (optional) — A list of tools the model may generate JSON inputs for.

### FineTuneSupervisedHyperparameters
Type: object
Description: The hyperparameters used for the fine-tuning job.

- batch_size: object (optional) — Number of examples in each batch. A larger batch size means ...
- learning_rate_multiplier: object (optional) — Scaling factor for the learning rate. A smaller learning rat...
- n_epochs: object (optional) — The number of epochs to train the model for. An epoch refers...

### FineTuneSupervisedMethod
Type: object
Description: Configuration for the supervised fine-tuning method.

- hyperparameters: object (optional)

### FineTuningCheckpointPermission
Type: object
Description: The `checkpoint.permission` object represents a permission for a fine-tuned model checkpoint.


- id: string (required) — The permission identifier, which can be referenced in the AP...
- created_at: integer (required) — The Unix timestamp (in seconds) for when the permission was ...
- project_id: string (required) — The project identifier that the permission is for.
- object: string (enum: checkpoint.permission) (required) — The object type, which is always "checkpoint.permission".

### FineTuningIntegration
Type: object

- type: string (enum: wandb) (required) — The type of the integration being enabled for the fine-tunin...
- wandb: object (4 fields) (required) — The settings for your integration with Weights and Biases. T...

### FineTuningJob
Type: object
Description: The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.


- id: string (required) — The object identifier, which can be referenced in the API en...
- created_at: integer (required) — The Unix timestamp (in seconds) for when the fine-tuning job...
- error: object (required)
- fine_tuned_model: object (required)
- finished_at: object (required)
- hyperparameters: object (3 fields) (required) — The hyperparameters used for the fine-tuning job. This value...
- model: string (required) — The base model that is being fine-tuned.
- object: string (enum: fine_tuning.job) (required) — The object type, which is always "fine_tuning.job".
- organization_id: string (required) — The organization that owns the fine-tuning job.
- result_files: array<string> (required) — The compiled results file ID(s) for the fine-tuning job. You...
- status: string (enum: validating_files, queued, running, succeeded, failed...) (required) — The current status of the fine-tuning job, which can be eith...
- trained_tokens: object (required)
- training_file: string (required) — The file ID used for training. You can retrieve the training...
- validation_file: object (required)
- integrations: object (optional)
- seed: integer (required) — The seed used for the fine-tuning job.
- estimated_finish: object (optional)
- method: object (optional)
- metadata: object (optional)

### FineTuningJobCheckpoint
Type: object
Description: The `fine_tuning.job.checkpoint` object represents a model checkpoint for a fine-tuning job that is ready to use.


- id: string (required) — The checkpoint identifier, which can be referenced in the AP...
- created_at: integer (required) — The Unix timestamp (in seconds) for when the checkpoint was ...
- fine_tuned_model_checkpoint: string (required) — The name of the fine-tuned checkpoint model that is created.
- step_number: integer (required) — The step number that the checkpoint was created at.
- metrics: object (7 fields) (required) — Metrics at the step number during the fine-tuning job.
- fine_tuning_job_id: string (required) — The name of the fine-tuning job that this checkpoint was cre...
- object: string (enum: fine_tuning.job.checkpoint) (required) — The object type, which is always "fine_tuning.job.checkpoint...

### FineTuningJobEvent
Type: object
Description: Fine-tuning job event object

- object: string (enum: fine_tuning.job.event) (required) — The object type, which is always "fine_tuning.job.event".
- id: string (required) — The object identifier.
- created_at: integer (required) — The Unix timestamp (in seconds) for when the fine-tuning job...
- level: string (enum: info, warn, error) (required) — The log level of the event.
- message: string (required) — The message of the event.
- type: string (enum: message, metrics) (optional) — The type of event.
- data: object (optional) — The data associated with the event.

### FunctionAndCustomToolCallOutput
Type: object

(empty)

### FunctionCallItemStatus
Type: string

string (enum: in_progress, completed, incomplete)

### FunctionCallOutputItemParam
Type: object
Description: The output of a function tool call.

- id: object (optional)
- call_id: string (required) — The unique ID of the function tool call generated by the mod...
- type: string (enum: function_call_output) (required) — The type of the function tool call output. Always `function_...
- output: object (required) — Text, image, or file output of the function tool call.
- status: object (optional)

### FunctionObject
Type: object

- description: string (optional) — A description of what the function does, used by the model t...
- name: string (required) — The name of the function to be called. Must be a-z, A-Z, 0-9...
- parameters: object (optional)
- strict: object (optional)

### FunctionParameters
Type: object
Description: The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https:/...

(empty)

### FunctionTool
Type: object
Description: Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

- type: string (enum: function) (required) — The type of the function tool. Always `function`.
- name: string (required) — The name of the function to call.
- description: object (optional)
- parameters: object (required)
- strict: object (required)

### FunctionToolCall
Type: object
Description: A tool call to run a function. See the 
[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.


- id: string (optional) — The unique ID of the function tool call.

- type: string (enum: function_call) (required) — The type of the function tool call. Always `function_call`.

- call_id: string (required) — The unique ID of the function tool call generated by the mod...
- name: string (required) — The name of the function to run.

- arguments: string (required) — A JSON string of the arguments to pass to the function.

- status: string (enum: in_progress, completed, incomplete) (optional) — The status of the item. One of `in_progress`, `completed`, o...

### FunctionToolCallOutput
Type: object
Description: The output of a function tool call.


- id: string (optional) — The unique ID of the function tool call output. Populated wh...
- type: string (enum: function_call_output) (required) — The type of the function tool call output. Always `function_...
- call_id: string (required) — The unique ID of the function tool call generated by the mod...
- output: object (required) — The output from the function call generated by your code.
Ca...
- status: string (enum: in_progress, completed, incomplete) (optional) — The status of the item. One of `in_progress`, `completed`, o...

### FunctionToolCallOutputResource
Type: object

(empty)

### FunctionToolCallResource
Type: object

(empty)

### GraderLabelModel
Type: object
Description: A LabelModelGrader object which uses a model to assign labels to each item
in the evaluation.


- type: string (enum: label_model) (required) — The object type, which is always `label_model`.
- name: string (required) — The name of the grader.
- model: string (required) — The model to use for the evaluation. Must support structured...
- input: array<object> (required)
- labels: array<string> (required) — The labels to assign to each item in the evaluation.
- passing_labels: array<string> (required) — The labels that indicate a passing result. Must be a subset ...

### GraderMulti
Type: object
Description: A MultiGrader object combines the output of multiple graders to produce a single score.

- type: string (enum: multi) (required) — The object type, which is always `multi`.
- name: string (required) — The name of the grader.
- graders: object (required)
- calculate_output: string (required) — A formula to calculate the output based on grader results.

### GraderPython
Type: object
Description: A PythonGrader object that runs a python script on the input.


- type: string (enum: python) (required) — The object type, which is always `python`.
- name: string (required) — The name of the grader.
- source: string (required) — The source code of the python script.
- image_tag: string (optional) — The image tag to use for the python script.

### GraderScoreModel
Type: object
Description: A ScoreModelGrader object that uses a model to assign a score to the input.


- type: string (enum: score_model) (required) — The object type, which is always `score_model`.
- name: string (required) — The name of the grader.
- model: string (required) — The model to use for the evaluation.
- sampling_params: object (5 fields) (optional) — The sampling parameters for the model.
- input: array<object> (required) — The input text. This may include template strings.
- range: array<number> (optional) — The range of the score. Defaults to `[0, 1]`.

### GraderStringCheck
Type: object
Description: A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.


- type: string (enum: string_check) (required) — The object type, which is always `string_check`.
- name: string (required) — The name of the grader.
- input: string (required) — The input text. This may include template strings.
- reference: string (required) — The reference text. This may include template strings.
- operation: string (enum: eq, ne, like, ilike) (required) — The string check operation to perform. One of `eq`, `ne`, `l...

### GraderTextSimilarity
Type: object
Description: A TextSimilarityGrader object which grades text based on similarity metrics.


- type: string (enum: text_similarity) (required) — The type of grader.
- name: string (required) — The name of the grader.
- input: string (required) — The text being graded.
- reference: string (required) — The text being graded against.
- evaluation_metric: string (enum: cosine, fuzzy_match, bleu, gleu, meteor...) (required) — The evaluation metric to use. One of `cosine`, `fuzzy_match`...

### HistoryParam
Type: object
Description: Controls how much historical context is retained for the session.

- enabled: boolean (optional) — Enables chat users to access previous ChatKit threads. Defau...
- recent_threads: integer (optional) — Number of recent ChatKit threads users have access to. Defau...

### Image
Type: object
Description: Represents the content or the URL of an image generated by the OpenAI API.

- b64_json: string (optional) — The base64-encoded JSON of the generated image. Default valu...
- url: string (optional) — When using `dall-e-2` or `dall-e-3`, the URL of the generate...
- revised_prompt: string (optional) — For `dall-e-3` only, the revised prompt that was used to gen...

### ImageDetail
Type: string

string (enum: low, high, auto)

### ImageEditCompletedEvent
Type: object
Description: Emitted when image editing has completed and the final image is available.


- type: string (enum: image_edit.completed) (required) — The type of the event. Always `image_edit.completed`.

- b64_json: string (required) — Base64-encoded final edited image data, suitable for renderi...
- created_at: integer (required) — The Unix timestamp when the event was created.

- size: string (enum: 1024x1024, 1024x1536, 1536x1024, auto) (required) — The size of the edited image.

- quality: string (enum: low, medium, high, auto) (required) — The quality setting for the edited image.

- background: string (enum: transparent, opaque, auto) (required) — The background setting for the edited image.

- output_format: string (enum: png, webp, jpeg) (required) — The output format for the edited image.

- usage: object (required)

### ImageEditPartialImageEvent
Type: object
Description: Emitted when a partial image is available during image editing streaming.


- type: string (enum: image_edit.partial_image) (required) — The type of the event. Always `image_edit.partial_image`.

- b64_json: string (required) — Base64-encoded partial image data, suitable for rendering as...
- created_at: integer (required) — The Unix timestamp when the event was created.

- size: string (enum: 1024x1024, 1024x1536, 1536x1024, auto) (required) — The size of the requested edited image.

- quality: string (enum: low, medium, high, auto) (required) — The quality setting for the requested edited image.

- background: string (enum: transparent, opaque, auto) (required) — The background setting for the requested edited image.

- output_format: string (enum: png, webp, jpeg) (required) — The output format for the requested edited image.

- partial_image_index: integer (required) — 0-based index for the partial image (streaming).


### ImageEditStreamEvent
Type: object

(empty)

### ImageGenCompletedEvent
Type: object
Description: Emitted when image generation has completed and the final image is available.


- type: string (enum: image_generation.completed) (required) — The type of the event. Always `image_generation.completed`.

- b64_json: string (required) — Base64-encoded image data, suitable for rendering as an imag...
- created_at: integer (required) — The Unix timestamp when the event was created.

- size: string (enum: 1024x1024, 1024x1536, 1536x1024, auto) (required) — The size of the generated image.

- quality: string (enum: low, medium, high, auto) (required) — The quality setting for the generated image.

- background: string (enum: transparent, opaque, auto) (required) — The background setting for the generated image.

- output_format: string (enum: png, webp, jpeg) (required) — The output format for the generated image.

- usage: object (required)

### ImageGenInputUsageDetails
Type: object
Description: The input tokens detailed information for the image generation.

- text_tokens: integer (required) — The number of text tokens in the input prompt.
- image_tokens: integer (required) — The number of image tokens in the input prompt.

### ImageGenPartialImageEvent
Type: object
Description: Emitted when a partial image is available during image generation streaming.


- type: string (enum: image_generation.partial_image) (required) — The type of the event. Always `image_generation.partial_imag...
- b64_json: string (required) — Base64-encoded partial image data, suitable for rendering as...
- created_at: integer (required) — The Unix timestamp when the event was created.

- size: string (enum: 1024x1024, 1024x1536, 1536x1024, auto) (required) — The size of the requested image.

- quality: string (enum: low, medium, high, auto) (required) — The quality setting for the requested image.

- background: string (enum: transparent, opaque, auto) (required) — The background setting for the requested image.

- output_format: string (enum: png, webp, jpeg) (required) — The output format for the requested image.

- partial_image_index: integer (required) — 0-based index for the partial image (streaming).


### ImageGenStreamEvent
Type: object

(empty)

### ImageGenTool
Type: object
Description: A tool that generates images using a model like `gpt-image-1`.


- type: string (enum: image_generation) (required) — The type of the image generation tool. Always `image_generat...
- model: string (enum: gpt-image-1, gpt-image-1-mini) (optional) — The image generation model to use. Default: `gpt-image-1`.

- quality: string (enum: low, medium, high, auto) (optional) — The quality of the generated image. One of `low`, `medium`, ...
- size: string (enum: 1024x1024, 1024x1536, 1536x1024, auto) (optional) — The size of the generated image. One of `1024x1024`, `1024x1...
- output_format: string (enum: png, webp, jpeg) (optional) — The output format of the generated image. One of `png`, `web...
- output_compression: integer (optional) — Compression level for the output image. Default: 100.

- moderation: string (enum: auto, low) (optional) — Moderation level for the generated image. Default: `auto`.

- background: string (enum: transparent, opaque, auto) (optional) — Background type for the generated image. One of `transparent...
- input_fidelity: object (optional)
- input_image_mask: object (2 fields) (optional) — Optional mask for inpainting. Contains `image_url`
(string, ...
- partial_images: integer (optional) — Number of partial images to generate in streaming mode, from...

### ImageGenToolCall
Type: object
Description: An image generation request made by the model.


- type: string (enum: image_generation_call) (required) — The type of the image generation call. Always `image_generat...
- id: string (required) — The unique ID of the image generation call.

- status: string (enum: in_progress, completed, generating, failed) (required) — The status of the image generation call.

- result: object (required)

### ImageGenUsage
Type: object
Description: For `gpt-image-1` only, the token usage information for the image generation.

- input_tokens: integer (required) — The number of tokens (images and text) in the input prompt.
- total_tokens: integer (required) — The total number of tokens (images and text) used for the im...
- output_tokens: integer (required) — The number of output tokens generated by the model.
- input_tokens_details: object (required)

### ImageInputFidelity
Type: object

(empty)

### ImagePartResource
Type: object
Description: Metadata for an image uploaded through ChatKit.

- id: string (required) — Unique identifier for the uploaded image.
- type: string (enum: image) (required) — Type discriminator that is always `image`.
- mime_type: string (required) — MIME type of the uploaded image.
- name: object (required)
- preview_url: string (required) — Preview URL that can be rendered inline for the image.
- upload_url: object (required)

### ImagesResponse
Type: object
Description: The response from the image generation endpoint.

- created: integer (required) — The Unix timestamp (in seconds) of when the image was create...
- data: array<object> (optional) — The list of generated images.
- background: string (enum: transparent, opaque) (optional) — The background parameter used for the image generation. Eith...
- output_format: string (enum: png, webp, jpeg) (optional) — The output format of the image generation. Either `png`, `we...
- size: string (enum: 1024x1024, 1024x1536, 1536x1024) (optional) — The size of the image generated. Either `1024x1024`, `1024x1...
- quality: string (enum: low, medium, high) (optional) — The quality of the image generated. Either `low`, `medium`, ...
- usage: object (optional)

### ImagesUsage
Type: object
Description: For `gpt-image-1` only, the token usage information for the image generation.


- total_tokens: integer (required) — The total number of tokens (images and text) used for the im...
- input_tokens: integer (required) — The number of tokens (images and text) in the input prompt.
- output_tokens: integer (required) — The number of image tokens in the output image.
- input_tokens_details: object (2 fields) (required) — The input tokens detailed information for the image generati...

### Includable
Type: string
Description: Specify additional output data to include in the model response. Currently
supported values are:
- `web_search_call.action.sources`: Include the sources of the web search tool call.
- `code_interprete...

string (enum: code_interpreter_call.outputs, computer_call_output.output.image_url, file_search_call.results, message.input_image.image_url, message.output_text.logprobs...)

### InferenceOptions
Type: object
Description: Model and tool overrides applied when generating the assistant response.

- tool_choice: object (required)
- model: object (required)

### InputAudio
Type: object
Description: An audio input to the model.


- type: string (enum: input_audio) (required) — The type of the input item. Always `input_audio`.

- input_audio: object (2 fields) (required)

### InputContent
Type: object

(empty)

### InputFileContent
Type: object
Description: A file input to the model.

- type: string (enum: input_file) (required) — The type of the input item. Always `input_file`.
- file_id: object (optional)
- filename: string (optional) — The name of the file to be sent to the model.
- file_url: string (optional) — The URL of the file to be sent to the model.
- file_data: string (optional) — The content of the file to be sent to the model.


### InputFileContentParam
Type: object
Description: A file input to the model.

- type: string (enum: input_file) (required) — The type of the input item. Always `input_file`.
- file_id: object (optional)
- filename: object (optional)
- file_data: object (optional)
- file_url: object (optional)

### InputImageContent
Type: object
Description: An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

- type: string (enum: input_image) (required) — The type of the input item. Always `input_image`.
- image_url: object (optional)
- file_id: object (optional)
- detail: object (required) — The detail level of the image to be sent to the model. One o...

### InputImageContentParamAutoParam
Type: object
Description: An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

- type: string (enum: input_image) (required) — The type of the input item. Always `input_image`.
- image_url: object (optional)
- file_id: object (optional)
- detail: object (optional)

### InputItem
Type: object

(empty)

### InputMessage
Type: object
Description: A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` ro...

- type: string (enum: message) (optional) — The type of the message input. Always set to `message`.

- role: string (enum: user, system, developer) (required) — The role of the message input. One of `user`, `system`, or `...
- status: string (enum: in_progress, completed, incomplete) (optional) — The status of item. One of `in_progress`, `completed`, or
`i...
- content: object (required)

### InputMessageContentList
Type: array
Description: A list of one or many input items to the model, containing different content 
types.


array<object>

### InputMessageResource
Type: object

(empty)

### InputTextContent
Type: object
Description: A text input to the model.

- type: string (enum: input_text) (required) — The type of the input item. Always `input_text`.
- text: string (required) — The text input to the model.

### InputTextContentParam
Type: object
Description: A text input to the model.

- type: string (enum: input_text) (required) — The type of the input item. Always `input_text`.
- text: string (required) — The text input to the model.

### Invite
Type: object
Description: Represents an individual `invite` to the organization.

- object: string (enum: organization.invite) (required) — The object type, which is always `organization.invite`
- id: string (required) — The identifier, which can be referenced in API endpoints
- email: string (required) — The email address of the individual to whom the invite was s...
- role: string (enum: owner, reader) (required) — `owner` or `reader`
- status: string (enum: accepted, expired, pending) (required) — `accepted`,`expired`, or `pending`
- invited_at: integer (required) — The Unix timestamp (in seconds) of when the invite was sent.
- expires_at: integer (required) — The Unix timestamp (in seconds) of when the invite expires.
- accepted_at: integer (optional) — The Unix timestamp (in seconds) of when the invite was accep...
- projects: array<object (2 fields)> (optional) — The projects that were granted membership upon acceptance of...

### InviteDeleteResponse
Type: object

- object: string (enum: organization.invite.deleted) (required) — The object type, which is always `organization.invite.delete...
- id: string (required)
- deleted: boolean (required)

### InviteListResponse
Type: object

- object: string (enum: list) (required) — The object type, which is always `list`
- data: array<object> (required)
- first_id: string (optional) — The first `invite_id` in the retrieved `list`
- last_id: string (optional) — The last `invite_id` in the retrieved `list`
- has_more: boolean (optional) — The `has_more` property is used for pagination to indicate t...

### InviteRequest
Type: object

- email: string (required) — Send an email to this address
- role: string (enum: reader, owner) (required) — `owner` or `reader`
- projects: array<object (2 fields)> (optional) — An array of projects to which membership is granted at the s...

### Item
Type: object
Description: Content item used to generate a response.


(empty)

### ItemReferenceParam
Type: object
Description: An internal identifier for an item to reference.

- type: object (optional)
- id: string (required) — The ID of the item to reference.

### ItemResource
Type: object
Description: Content item used to generate a response.


(empty)

### KeyPress
Type: object
Description: A collection of keypresses the model would like to perform.


- type: string (enum: keypress) (required) — Specifies the event type. For a keypress action, this proper...
- keys: array<string> (required) — The combination of keys the model is requesting to be presse...

### ListAssistantsResponse
Type: object

- object: string (required)
- data: array<object> (required)
- first_id: string (required)
- last_id: string (required)
- has_more: boolean (required)

### ListAuditLogsResponse
Type: object

- object: string (enum: list) (required)
- data: array<object> (required)
- first_id: string (required)
- last_id: string (required)
- has_more: boolean (required)

### ListBatchesResponse
Type: object

- data: array<object> (required)
- first_id: string (optional)
- last_id: string (optional)
- has_more: boolean (required)
- object: string (enum: list) (required)

### ListCertificatesResponse
Type: object

- data: array<object> (required)
- first_id: string (optional)
- last_id: string (optional)
- has_more: boolean (required)
- object: string (enum: list) (required)

### ListFilesResponse
Type: object

- object: string (required)
- data: array<object> (required)
- first_id: string (required)
- last_id: string (required)
- has_more: boolean (required)

### ListFineTuningCheckpointPermissionResponse
Type: object

- data: array<object> (required)
- object: string (enum: list) (required)
- first_id: object (optional)
- last_id: object (optional)
- has_more: boolean (required)

### ListFineTuningJobCheckpointsResponse
Type: object

- data: array<object> (required)
- object: string (enum: list) (required)
- first_id: object (optional)
- last_id: object (optional)
- has_more: boolean (required)

### ListFineTuningJobEventsResponse
Type: object

- data: array<object> (required)
- object: string (enum: list) (required)
- has_more: boolean (required)

### ListMessagesResponse
Type: object

- object: string (required)
- data: array<object> (required)
- first_id: string (required)
- last_id: string (required)
- has_more: boolean (required)

### ListModelsResponse
Type: object

- object: string (enum: list) (required)
- data: array<object> (required)

### ListPaginatedFineTuningJobsResponse
Type: object

- data: array<object> (required)
- has_more: boolean (required)
- object: string (enum: list) (required)

### ListRunStepsResponse
Type: object

- object: string (required)
- data: array<object> (required)
- first_id: string (required)
- last_id: string (required)
- has_more: boolean (required)

### ListRunsResponse
Type: object

- object: string (required)
- data: array<object> (required)
- first_id: string (required)
- last_id: string (required)
- has_more: boolean (required)

### ListVectorStoreFilesResponse
Type: object

- object: string (required)
- data: array<object> (required)
- first_id: string (required)
- last_id: string (required)
- has_more: boolean (required)

### ListVectorStoresResponse
Type: object

- object: string (required)
- data: array<object> (required)
- first_id: string (required)
- last_id: string (required)
- has_more: boolean (required)

### LocalShellExecAction
Type: object
Description: Execute a shell command on the server.


- type: string (enum: exec) (required) — The type of the local shell action. Always `exec`.

- command: array<string> (required) — The command to run.

- timeout_ms: object (optional)
- working_directory: object (optional)
- env: object (required) — Environment variables to set for the command.

- user: object (optional)

### LocalShellTool
Type: object
Description: A tool that allows the model to execute shell commands in a local environment.


- type: string (enum: local_shell) (required) — The type of the local shell tool. Always `local_shell`.

### LocalShellToolCall
Type: object
Description: A tool call to run a command on the local shell.


- type: string (enum: local_shell_call) (required) — The type of the local shell call. Always `local_shell_call`....
- id: string (required) — The unique ID of the local shell call.

- call_id: string (required) — The unique ID of the local shell tool call generated by the ...
- action: object (required)
- status: string (enum: in_progress, completed, incomplete) (required) — The status of the local shell call.


### LocalShellToolCallOutput
Type: object
Description: The output of a local shell tool call.


- type: string (enum: local_shell_call_output) (required) — The type of the local shell tool call output. Always `local_...
- id: string (required) — The unique ID of the local shell tool call generated by the ...
- output: string (required) — A JSON string of the output of the local shell tool call.

- status: object (optional)

### LockedStatus
Type: object
Description: Indicates that a thread is locked and cannot accept new input.

- type: string (enum: locked) (required) — Status discriminator that is always `locked`.
- reason: object (required)

### LogProb
Type: object
Description: The log probability of a token.

- token: string (required)
- logprob: number (required)
- bytes: array<integer> (required)
- top_logprobs: array<object> (required)

### LogProbProperties
Type: object
Description: A log probability object.


- token: string (required) — The token that was used to generate the log probability.

- logprob: number (required) — The log probability of the token.

- bytes: array<integer> (required) — The bytes that were used to generate the log probability.


### MCPApprovalRequest
Type: object
Description: A request for human approval of a tool invocation.


- type: string (enum: mcp_approval_request) (required) — The type of the item. Always `mcp_approval_request`.

- id: string (required) — The unique ID of the approval request.

- server_label: string (required) — The label of the MCP server making the request.

- name: string (required) — The name of the tool to run.

- arguments: string (required) — A JSON string of arguments for the tool.


### MCPApprovalResponse
Type: object
Description: A response to an MCP approval request.


- type: string (enum: mcp_approval_response) (required) — The type of the item. Always `mcp_approval_response`.

- id: object (optional)
- approval_request_id: string (required) — The ID of the approval request being answered.

- approve: boolean (required) — Whether the request was approved.

- reason: object (optional)

### MCPApprovalResponseResource
Type: object
Description: A response to an MCP approval request.


- type: string (enum: mcp_approval_response) (required) — The type of the item. Always `mcp_approval_response`.

- id: string (required) — The unique ID of the approval response

- approval_request_id: string (required) — The ID of the approval request being answered.

- approve: boolean (required) — Whether the request was approved.

- reason: object (optional)

### MCPListTools
Type: object
Description: A list of tools available on an MCP server.


- type: string (enum: mcp_list_tools) (required) — The type of the item. Always `mcp_list_tools`.

- id: string (required) — The unique ID of the list.

- server_label: string (required) — The label of the MCP server.

- tools: array<object> (required) — The tools available on the server.

- error: object (optional)

### MCPListToolsTool
Type: object
Description: A tool available on an MCP server.


- name: string (required) — The name of the tool.

- description: object (optional)
- input_schema: object (required) — The JSON schema describing the tool's input.

- annotations: object (optional)

### MCPTool
Type: object
Description: Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).


- type: string (enum: mcp) (required) — The type of the MCP tool. Always `mcp`.
- server_label: string (required) — A label for this MCP server, used to identify it in tool cal...
- server_url: string (optional) — The URL for the MCP server. One of `server_url` or `connecto...
- connector_id: string (enum: connector_dropbox, connector_gmail, connector_googlecalendar, connector_googledrive, connector_microsoftteams...) (optional) — Identifier for service connectors, like those available in C...
- authorization: string (optional) — An OAuth access token that can be used with a remote MCP ser...
- server_description: string (optional) — Optional description of the MCP server, used to provide more...
- headers: object (optional)
- allowed_tools: object (optional)
- require_approval: object (optional)

### MCPToolCall
Type: object
Description: An invocation of a tool on an MCP server.


- type: string (enum: mcp_call) (required) — The type of the item. Always `mcp_call`.

- id: string (required) — The unique ID of the tool call.

- server_label: string (required) — The label of the MCP server running the tool.

- name: string (required) — The name of the tool that was run.

- arguments: string (required) — A JSON string of the arguments passed to the tool.

- output: object (optional)
- error: object (optional)
- status: object (optional) — The status of the tool call. One of `in_progress`, `complete...
- approval_request_id: object (optional)

### MCPToolCallStatus
Type: string

string (enum: in_progress, completed, incomplete, calling, failed)

### MCPToolFilter
Type: object
Description: A filter object to specify which tools are allowed.


- tool_names: array<string> (optional) — List of allowed tool names.
- read_only: boolean (optional) — Indicates whether or not a tool modifies data or is read-onl...

### Message
Type: object
Description: A message to or from the model.

- type: string (enum: message) (required) — The type of the message. Always set to `message`.
- id: string (required) — The unique ID of the message.
- status: object (required) — The status of item. One of `in_progress`, `completed`, or `i...
- role: object (required) — The role of the message. One of `unknown`, `user`, `assistan...
- content: array<object> (required) — The content of the message

### MessageContent
Type: object

(empty)

### MessageContentDelta
Type: object

(empty)

### MessageContentImageFileObject
Type: object
Description: References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

- type: string (enum: image_file) (required) — Always `image_file`.
- image_file: object (2 fields) (required)

### MessageContentImageUrlObject
Type: object
Description: References an image URL in the content of a message.

- type: string (enum: image_url) (required) — The type of the content part.
- image_url: object (2 fields) (required)

### MessageContentRefusalObject
Type: object
Description: The refusal content generated by the assistant.

- type: string (enum: refusal) (required) — Always `refusal`.
- refusal: string (required)

### MessageContentTextAnnotationsFileCitationObject
Type: object
Description: A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file_search" tool to search file...

- type: string (enum: file_citation) (required) — Always `file_citation`.
- text: string (required) — The text in the message content that needs to be replaced.
- file_citation: object (1 fields) (required)
- start_index: integer (required)
- end_index: integer (required)

### MessageContentTextAnnotationsFilePathObject
Type: object
Description: A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.

- type: string (enum: file_path) (required) — Always `file_path`.
- text: string (required) — The text in the message content that needs to be replaced.
- file_path: object (1 fields) (required)
- start_index: integer (required)
- end_index: integer (required)

### MessageContentTextObject
Type: object
Description: The text content that is part of a message.

- type: string (enum: text) (required) — Always `text`.
- text: object (2 fields) (required)

### MessageDeltaContentImageFileObject
Type: object
Description: References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

- index: integer (required) — The index of the content part in the message.
- type: string (enum: image_file) (required) — Always `image_file`.
- image_file: object (2 fields) (optional)

### MessageDeltaContentImageUrlObject
Type: object
Description: References an image URL in the content of a message.

- index: integer (required) — The index of the content part in the message.
- type: string (enum: image_url) (required) — Always `image_url`.
- image_url: object (2 fields) (optional)

### MessageDeltaContentRefusalObject
Type: object
Description: The refusal content that is part of a message.

- index: integer (required) — The index of the refusal part in the message.
- type: string (enum: refusal) (required) — Always `refusal`.
- refusal: string (optional)

### MessageDeltaContentTextAnnotationsFileCitationObject
Type: object
Description: A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file_search" tool to search file...

- index: integer (required) — The index of the annotation in the text content part.
- type: string (enum: file_citation) (required) — Always `file_citation`.
- text: string (optional) — The text in the message content that needs to be replaced.
- file_citation: object (2 fields) (optional)
- start_index: integer (optional)
- end_index: integer (optional)

### MessageDeltaContentTextAnnotationsFilePathObject
Type: object
Description: A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.

- index: integer (required) — The index of the annotation in the text content part.
- type: string (enum: file_path) (required) — Always `file_path`.
- text: string (optional) — The text in the message content that needs to be replaced.
- file_path: object (1 fields) (optional)
- start_index: integer (optional)
- end_index: integer (optional)

### MessageDeltaContentTextObject
Type: object
Description: The text content that is part of a message.

- index: integer (required) — The index of the content part in the message.
- type: string (enum: text) (required) — Always `text`.
- text: object (2 fields) (optional)

### MessageDeltaObject
Type: object
Description: Represents a message delta i.e. any changed fields on a message during streaming.


- id: string (required) — The identifier of the message, which can be referenced in AP...
- object: string (enum: thread.message.delta) (required) — The object type, which is always `thread.message.delta`.
- delta: object (2 fields) (required) — The delta containing the fields that have changed on the Mes...

### MessageObject
Type: object
Description: Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

- id: string (required) — The identifier, which can be referenced in API endpoints.
- object: string (enum: thread.message) (required) — The object type, which is always `thread.message`.
- created_at: integer (required) — The Unix timestamp (in seconds) for when the message was cre...
- thread_id: string (required) — The [thread](https://platform.openai.com/docs/api-reference/...
- status: string (enum: in_progress, incomplete, completed) (required) — The status of the message, which can be either `in_progress`...
- incomplete_details: object (required)
- completed_at: object (required)
- incomplete_at: object (required)
- role: string (enum: user, assistant) (required) — The entity that produced the message. One of `user` or `assi...
- content: array<object> (required) — The content of the message in array of text and/or images.
- assistant_id: object (required)
- run_id: object (required)
- attachments: object (required)
- metadata: object (required)

### MessageRequestContentTextObject
Type: object
Description: The text content that is part of a message.

- type: string (enum: text) (required) — Always `text`.
- text: string (required) — Text content to be sent to the model

### MessageRole
Type: string

string (enum: unknown, user, assistant, system, critic...)

### MessageStatus
Type: string

string (enum: in_progress, completed, incomplete)

### MessageStreamEvent
Type: object

(empty)

### Metadata
Type: object

(empty)

### Model
Type: object
Description: Describes an OpenAI model offering that can be used with the API.

- id: string (required) — The model identifier, which can be referenced in the API end...
- created: integer (required) — The Unix timestamp (in seconds) when the model was created.
- object: string (enum: model) (required) — The object type, which is always "model".
- owned_by: string (required) — The organization that owns the model.

### ModelIds
Type: object

(empty)

### ModelIdsResponses
Type: object

(empty)

### ModelIdsShared
Type: object

(empty)

### ModelResponseProperties
Type: object

- metadata: object (optional)
- top_logprobs: object (optional)
- temperature: object (optional)
- top_p: object (optional)
- user: string (optional) — This field is being replaced by `safety_identifier` and `pro...
- safety_identifier: string (optional) — A stable identifier used to help detect users of your applic...
- prompt_cache_key: string (optional) — Used by OpenAI to cache responses for similar requests to op...
- service_tier: object (optional)

### ModerationImageURLInput
Type: object
Description: An object describing an image to classify.

- type: string (enum: image_url) (required) — Always `image_url`.
- image_url: object (1 fields) (required) — Contains either an image URL or a data URL for a base64 enco...

### ModerationTextInput
Type: object
Description: An object describing text to classify.

- type: string (enum: text) (required) — Always `text`.
- text: string (required) — A string of text to classify.

### ModifyAssistantRequest
Type: object

- model: object (optional) — ID of the model to use. You can use the [List models](https:...
- reasoning_effort: object (optional)
- name: object (optional)
- description: object (optional)
- instructions: object (optional)
- tools: array<object> (optional) — A list of tool enabled on the assistant. There can be a maxi...
- tool_resources: object (optional)
- metadata: object (optional)
- temperature: object (optional)
- top_p: object (optional)
- response_format: object (optional)

### ModifyCertificateRequest
Type: object

- name: string (required) — The updated name for the certificate

### ModifyMessageRequest
Type: object

- metadata: object (optional)

### ModifyRunRequest
Type: object

- metadata: object (optional)

### ModifyThreadRequest
Type: object

- tool_resources: object (optional)
- metadata: object (optional)

### Move
Type: object
Description: A mouse move action.


- type: string (enum: move) (required) — Specifies the event type. For a move action, this property i...
- x: integer (required) — The x-coordinate to move to.

- y: integer (required) — The y-coordinate to move to.


### NoiseReductionType
Type: string
Description: Type of noise reduction. `near_field` is for close-talking microphones such as headphones, `far_field` is for far-field microphones such as laptop or conference room microphones.


string (enum: near_field, far_field)

### OpenAIFile
Type: object
Description: The `File` object represents a document that has been uploaded to OpenAI.

- id: string (required) — The file identifier, which can be referenced in the API endp...
- bytes: integer (required) — The size of the file, in bytes.
- created_at: integer (required) — The Unix timestamp (in seconds) for when the file was create...
- expires_at: integer (optional) — The Unix timestamp (in seconds) for when the file will expir...
- filename: string (required) — The name of the file.
- object: string (enum: file) (required) — The object type, which is always `file`.
- purpose: string (enum: assistants, assistants_output, batch, batch_output, fine-tune...) (required) — The intended purpose of the file. Supported values are `assi...
- status: string (enum: uploaded, processed, error) (required) — Deprecated. The current status of the file, which can be eit...
- status_details: string (optional) — Deprecated. For details on why a fine-tuning training file f...

### OrderEnum
Type: string

string (enum: asc, desc)

### OtherChunkingStrategyResponseParam
Type: object
Description: This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

- type: string (enum: other) (required) — Always `other`.

### OutputAudio
Type: object
Description: An audio output from the model.


- type: string (enum: output_audio) (required) — The type of the output audio. Always `output_audio`.

- data: string (required) — Base64-encoded audio data from the model.

- transcript: string (required) — The transcript of the audio data from the model.


### OutputContent
Type: object

(empty)

### OutputItem
Type: object

(empty)

### OutputMessage
Type: object
Description: An output message from the model.


- id: string (required) — The unique ID of the output message.

- type: string (enum: message) (required) — The type of the output message. Always `message`.

- role: string (enum: assistant) (required) — The role of the output message. Always `assistant`.

- content: array<object> (required) — The content of the output message.

- status: string (enum: in_progress, completed, incomplete) (required) — The status of the message input. One of `in_progress`, `comp...

### OutputMessageContent
Type: object

(empty)

### OutputTextContent
Type: object
Description: A text output from the model.

- type: string (enum: output_text) (required) — The type of the output text. Always `output_text`.
- text: string (required) — The text output from the model.
- annotations: array<object> (required) — The annotations of the text output.
- logprobs: array<object> (optional)

### ParallelToolCalls
Type: boolean
Description: Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

boolean

### PartialImages
Type: object

(empty)

### PredictionContent
Type: object
Description: Static predicted output content, such as the content of a text file that is
being regenerated.


- type: string (enum: content) (required) — The type of the predicted content you want to provide. This ...
- content: object (required) — The content that should be matched when generating a model r...

### Project
Type: object
Description: Represents an individual project.

- id: string (required) — The identifier, which can be referenced in API endpoints
- object: string (enum: organization.project) (required) — The object type, which is always `organization.project`
- name: string (required) — The name of the project. This appears in reporting.
- created_at: integer (required) — The Unix timestamp (in seconds) of when the project was crea...
- archived_at: object (optional)
- status: string (enum: active, archived) (required) — `active` or `archived`

### ProjectApiKey
Type: object
Description: Represents an individual API key in a project.

- object: string (enum: organization.project.api_key) (required) — The object type, which is always `organization.project.api_k...
- redacted_value: string (required) — The redacted value of the API key
- name: string (required) — The name of the API key
- created_at: integer (required) — The Unix timestamp (in seconds) of when the API key was crea...
- last_used_at: integer (required) — The Unix timestamp (in seconds) of when the API key was last...
- id: string (required) — The identifier, which can be referenced in API endpoints
- owner: object (3 fields) (required)

### ProjectApiKeyDeleteResponse
Type: object

- object: string (enum: organization.project.api_key.deleted) (required)
- id: string (required)
- deleted: boolean (required)

### ProjectApiKeyListResponse
Type: object

- object: string (enum: list) (required)
- data: array<object> (required)
- first_id: string (required)
- last_id: string (required)
- has_more: boolean (required)

### ProjectCreateRequest
Type: object

- name: string (required) — The friendly name of the project, this name appears in repor...
- geography: string (enum: US, EU, JP, IN, KR...) (optional) — Create the project with the specified data residency region....

### ProjectListResponse
Type: object

- object: string (enum: list) (required)
- data: array<object> (required)
- first_id: string (required)
- last_id: string (required)
- has_more: boolean (required)

### ProjectRateLimit
Type: object
Description: Represents a project rate limit config.

- object: string (enum: project.rate_limit) (required) — The object type, which is always `project.rate_limit`
- id: string (required) — The identifier, which can be referenced in API endpoints.
- model: string (required) — The model this rate limit applies to.
- max_requests_per_1_minute: integer (required) — The maximum requests per minute.
- max_tokens_per_1_minute: integer (required) — The maximum tokens per minute.
- max_images_per_1_minute: integer (optional) — The maximum images per minute. Only present for relevant mod...
- max_audio_megabytes_per_1_minute: integer (optional) — The maximum audio megabytes per minute. Only present for rel...
- max_requests_per_1_day: integer (optional) — The maximum requests per day. Only present for relevant mode...
- batch_1_day_max_input_tokens: integer (optional) — The maximum batch input tokens per day. Only present for rel...

### ProjectRateLimitListResponse
Type: object

- object: string (enum: list) (required)
- data: array<object> (required)
- first_id: string (required)
- last_id: string (required)
- has_more: boolean (required)

### ProjectRateLimitUpdateRequest
Type: object

- max_requests_per_1_minute: integer (optional) — The maximum requests per minute.
- max_tokens_per_1_minute: integer (optional) — The maximum tokens per minute.
- max_images_per_1_minute: integer (optional) — The maximum images per minute. Only relevant for certain mod...
- max_audio_megabytes_per_1_minute: integer (optional) — The maximum audio megabytes per minute. Only relevant for ce...
- max_requests_per_1_day: integer (optional) — The maximum requests per day. Only relevant for certain mode...
- batch_1_day_max_input_tokens: integer (optional) — The maximum batch input tokens per day. Only relevant for ce...

### ProjectServiceAccount
Type: object
Description: Represents an individual service account in a project.

- object: string (enum: organization.project.service_account) (required) — The object type, which is always `organization.project.servi...
- id: string (required) — The identifier, which can be referenced in API endpoints
- name: string (required) — The name of the service account
- role: string (enum: owner, member) (required) — `owner` or `member`
- created_at: integer (required) — The Unix timestamp (in seconds) of when the service account ...

### ProjectServiceAccountApiKey
Type: object

- object: string (enum: organization.project.service_account.api_key) (required) — The object type, which is always `organization.project.servi...
- value: string (required)
- name: string (required)
- created_at: integer (required)
- id: string (required)

### ProjectServiceAccountCreateRequest
Type: object

- name: string (required) — The name of the service account being created.

### ProjectServiceAccountCreateResponse
Type: object

- object: string (enum: organization.project.service_account) (required)
- id: string (required)
- name: string (required)
- role: string (enum: member) (required) — Service accounts can only have one role of type `member`
- created_at: integer (required)
- api_key: object (required)

### ProjectServiceAccountDeleteResponse
Type: object

- object: string (enum: organization.project.service_account.deleted) (required)
- id: string (required)
- deleted: boolean (required)

### ProjectServiceAccountListResponse
Type: object

- object: string (enum: list) (required)
- data: array<object> (required)
- first_id: string (required)
- last_id: string (required)
- has_more: boolean (required)

### ProjectUpdateRequest
Type: object

- name: string (required) — The updated name of the project, this name appears in report...

### ProjectUser
Type: object
Description: Represents an individual user in a project.

- object: string (enum: organization.project.user) (required) — The object type, which is always `organization.project.user`
- id: string (required) — The identifier, which can be referenced in API endpoints
- name: string (required) — The name of the user
- email: string (required) — The email address of the user
- role: string (enum: owner, member) (required) — `owner` or `member`
- added_at: integer (required) — The Unix timestamp (in seconds) of when the project was adde...

### ProjectUserCreateRequest
Type: object

- user_id: string (required) — The ID of the user.
- role: string (enum: owner, member) (required) — `owner` or `member`

### ProjectUserDeleteResponse
Type: object

- object: string (enum: organization.project.user.deleted) (required)
- id: string (required)
- deleted: boolean (required)

### ProjectUserListResponse
Type: object

- object: string (required)
- data: array<object> (required)
- first_id: string (required)
- last_id: string (required)
- has_more: boolean (required)

### ProjectUserUpdateRequest
Type: object

- role: string (enum: owner, member) (required) — `owner` or `member`

### Prompt
Type: object

(empty)

### RankerVersionType
Type: string

string (enum: auto, default-2024-11-15)

### RankingOptions
Type: object

- ranker: object (optional) — The ranker to use for the file search.
- score_threshold: number (optional) — The score threshold for the file search, a number between 0 ...

### RateLimitsParam
Type: object
Description: Controls request rate limits for the session.

- max_requests_per_1_minute: integer (optional) — Maximum number of requests allowed per minute for the sessio...

### RealtimeAudioFormats
Type: object

(empty)

### RealtimeBetaClientEventConversationItemCreate
Type: object
Description: Add a new Item to the Conversation's context, including messages, function 
calls, and function call responses. This event can be used both to populate a 
"history" of the conversation and to add new ...

- event_id: string (optional) — Optional client-generated ID used to identify this event.
- type: object (required) — The event type, must be `conversation.item.create`.
- previous_item_id: string (optional) — The ID of the preceding item after which the new item will b...
- item: object (required)

### RealtimeBetaClientEventConversationItemDelete
Type: object
Description: Send this event when you want to remove any item from the conversation 
history. The server will respond with a `conversation.item.deleted` event, 
unless the item does not exist in the conversation h...

- event_id: string (optional) — Optional client-generated ID used to identify this event.
- type: object (required) — The event type, must be `conversation.item.delete`.
- item_id: string (required) — The ID of the item to delete.

### RealtimeBetaClientEventConversationItemRetrieve
Type: object
Description: Send this event when you want to retrieve the server's representation of a specific item in the conversation history. This is useful, for example, to inspect user audio after noise cancellation and VA...

- event_id: string (optional) — Optional client-generated ID used to identify this event.
- type: object (required) — The event type, must be `conversation.item.retrieve`.
- item_id: string (required) — The ID of the item to retrieve.

### RealtimeBetaClientEventConversationItemTruncate
Type: object
Description: Send this event to truncate a previous assistant message’s audio. The server 
will produce audio faster than realtime, so this event is useful when the user 
interrupts to truncate audio that has alre...

- event_id: string (optional) — Optional client-generated ID used to identify this event.
- type: object (required) — The event type, must be `conversation.item.truncate`.
- item_id: string (required) — The ID of the assistant message item to truncate. Only assis...
- content_index: integer (required) — The index of the content part to truncate. Set this to 0.
- audio_end_ms: integer (required) — Inclusive duration up to which audio is truncated, in millis...

### RealtimeBetaClientEventInputAudioBufferAppend
Type: object
Description: Send this event to append audio bytes to the input audio buffer. The audio 
buffer is temporary storage you can write to and later commit. In Server VAD 
mode, the audio buffer is used to detect speec...

- event_id: string (optional) — Optional client-generated ID used to identify this event.
- type: object (required) — The event type, must be `input_audio_buffer.append`.
- audio: string (required) — Base64-encoded audio bytes. This must be in the format speci...

### RealtimeBetaClientEventInputAudioBufferClear
Type: object
Description: Send this event to clear the audio bytes in the buffer. The server will 
respond with an `input_audio_buffer.cleared` event.


- event_id: string (optional) — Optional client-generated ID used to identify this event.
- type: object (required) — The event type, must be `input_audio_buffer.clear`.

### RealtimeBetaClientEventInputAudioBufferCommit
Type: object
Description: Send this event to commit the user input audio buffer, which will create a 
new user message item in the conversation. This event will produce an error 
if the input audio buffer is empty. When in Ser...

- event_id: string (optional) — Optional client-generated ID used to identify this event.
- type: object (required) — The event type, must be `input_audio_buffer.commit`.

### RealtimeBetaClientEventOutputAudioBufferClear
Type: object
Description: **WebRTC Only:** Emit to cut off the current audio response. This will trigger the server to
stop generating audio and emit a `output_audio_buffer.cleared` event. This 
event should be preceded by a `...

- event_id: string (optional) — The unique ID of the client event used for error handling.
- type: object (required) — The event type, must be `output_audio_buffer.clear`.

### RealtimeBetaClientEventResponseCancel
Type: object
Description: Send this event to cancel an in-progress response. The server will respond 
with a `response.done` event with a status of `response.status=cancelled`. If 
there is no response to cancel, the server wi...

- event_id: string (optional) — Optional client-generated ID used to identify this event.
- type: object (required) — The event type, must be `response.cancel`.
- response_id: string (optional) — A specific response ID to cancel - if not provided, will can...

### RealtimeBetaClientEventResponseCreate
Type: object
Description: This event instructs the server to create a Response, which means triggering 
model inference. When in Server VAD mode, the server will create Responses 
automatically.

A Response will include at lea...

- event_id: string (optional) — Optional client-generated ID used to identify this event.
- type: object (required) — The event type, must be `response.create`.
- response: object (optional)

### RealtimeBetaClientEventSessionUpdate
Type: object
Description: Send this event to update the session’s default configuration.
The client may send this event at any time to update any field,
except for `voice`. However, note that once a session has been
initialize...

- event_id: string (optional) — Optional client-generated ID used to identify this event.
- type: object (required) — The event type, must be `session.update`.
- session: object (required)

### RealtimeBetaClientEventTranscriptionSessionUpdate
Type: object
Description: Send this event to update a transcription session.


- event_id: string (optional) — Optional client-generated ID used to identify this event.
- type: object (required) — The event type, must be `transcription_session.update`.
- session: object (required)

### RealtimeBetaResponse
Type: object
Description: The response resource.

- id: string (optional) — The unique ID of the response.
- object: object (optional) — The object type, must be `realtime.response`.
- status: string (enum: completed, cancelled, failed, incomplete, in_progress) (optional) — The final status of the response (`completed`, `cancelled`, ...
- status_details: object (3 fields) (optional) — Additional details about the status.
- output: array<object> (optional) — The list of output items generated by the response.
- metadata: object (optional)
- usage: object (5 fields) (optional) — Usage statistics for the Response, this will correspond to b...
- conversation_id: string (optional) — Which conversation the response is added to, determined by t...
- voice: object (optional) — The voice the model used to respond.
Current voice options a...
- modalities: array<string (enum: text, audio)> (optional) — The set of modalities the model used to respond. If there ar...
- output_audio_format: string (enum: pcm16, g711_ulaw, g711_alaw) (optional) — The format of output audio. Options are `pcm16`, `g711_ulaw`...
- temperature: number (optional) — Sampling temperature for the model, limited to [0.6, 1.2]. D...
- max_output_tokens: object (optional) — Maximum number of output tokens for a single assistant respo...

### RealtimeBetaResponseCreateParams
Type: object
Description: Create a new Realtime response with these parameters

- modalities: array<string (enum: text, audio)> (optional) — The set of modalities the model can respond with. To disable...
- instructions: string (optional) — The default system instructions (i.e. system message) prepen...
- voice: object (optional) — The voice the model uses to respond. Voice cannot be changed...
- output_audio_format: string (enum: pcm16, g711_ulaw, g711_alaw) (optional) — The format of output audio. Options are `pcm16`, `g711_ulaw`...
- tools: array<object (4 fields)> (optional) — Tools (functions) available to the model.
- tool_choice: object (optional) — How the model chooses tools. Provide one of the string modes...
- temperature: number (optional) — Sampling temperature for the model, limited to [0.6, 1.2]. D...
- max_output_tokens: object (optional) — Maximum number of output tokens for a single assistant respo...
- conversation: object (optional) — Controls which conversation the response is added to. Curren...
- metadata: object (optional)
- prompt: object (optional)
- input: array<object> (optional) — Input items to include in the prompt for the model. Using th...

### RealtimeBetaServerEventConversationItemCreated
Type: object
Description: Returned when a conversation item is created. There are several scenarios that produce this event:
  - The server is generating a Response, which if successful will produce
    either one or two Items...

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `conversation.item.created`.
- previous_item_id: object (optional)
- item: object (required)

### RealtimeBetaServerEventConversationItemDeleted
Type: object
Description: Returned when an item in the conversation is deleted by the client with a 
`conversation.item.delete` event. This event is used to synchronize the 
server's understanding of the conversation history w...

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `conversation.item.deleted`.
- item_id: string (required) — The ID of the item that was deleted.

### RealtimeBetaServerEventConversationItemInputAudioTranscriptionCompleted
Type: object
Description: This event is the output of audio transcription for user audio written to the
user audio buffer. Transcription begins when the input audio buffer is
committed by the client or server (in `server_vad` ...

- event_id: string (required) — The unique ID of the server event.
- type: string (enum: conversation.item.input_audio_transcription.completed) (required) — The event type, must be
`conversation.item.input_audio_trans...
- item_id: string (required) — The ID of the user message item containing the audio.
- content_index: integer (required) — The index of the content part containing the audio.
- transcript: string (required) — The transcribed text.
- logprobs: object (optional)
- usage: object (required) — Usage statistics for the transcription.

### RealtimeBetaServerEventConversationItemInputAudioTranscriptionDelta
Type: object
Description: Returned when the text value of an input audio transcription content part is updated.


- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `conversation.item.input_audio_trans...
- item_id: string (required) — The ID of the item.
- content_index: integer (optional) — The index of the content part in the item's content array.
- delta: string (optional) — The text delta.
- logprobs: object (optional)

### RealtimeBetaServerEventConversationItemInputAudioTranscriptionFailed
Type: object
Description: Returned when input audio transcription is configured, and a transcription 
request for a user message failed. These events are separate from other 
`error` events so that the client can identify the ...

- event_id: string (required) — The unique ID of the server event.
- type: string (enum: conversation.item.input_audio_transcription.failed) (required) — The event type, must be
`conversation.item.input_audio_trans...
- item_id: string (required) — The ID of the user message item.
- content_index: integer (required) — The index of the content part containing the audio.
- error: object (4 fields) (required) — Details of the transcription error.

### RealtimeBetaServerEventConversationItemInputAudioTranscriptionSegment
Type: object
Description: Returned when an input audio transcription segment is identified for an item.

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `conversation.item.input_audio_trans...
- item_id: string (required) — The ID of the item containing the input audio content.
- content_index: integer (required) — The index of the input audio content part within the item.
- text: string (required) — The text for this segment.
- id: string (required) — The segment identifier.
- speaker: string (required) — The detected speaker label for this segment.
- start: number (float) (required) — Start time of the segment in seconds.
- end: number (float) (required) — End time of the segment in seconds.

### RealtimeBetaServerEventConversationItemRetrieved
Type: object
Description: Returned when a conversation item is retrieved with `conversation.item.retrieve`.


- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `conversation.item.retrieved`.
- item: object (required)

### RealtimeBetaServerEventConversationItemTruncated
Type: object
Description: Returned when an earlier assistant audio message item is truncated by the 
client with a `conversation.item.truncate` event. This event is used to 
synchronize the server's understanding of the audio ...

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `conversation.item.truncated`.
- item_id: string (required) — The ID of the assistant message item that was truncated.
- content_index: integer (required) — The index of the content part that was truncated.
- audio_end_ms: integer (required) — The duration up to which the audio was truncated, in millise...

### RealtimeBetaServerEventError
Type: object
Description: Returned when an error occurs, which could be a client problem or a server
problem. Most errors are recoverable and the session will stay open, we
recommend to implementors to monitor and log error me...

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `error`.
- error: object (5 fields) (required) — Details of the error.

### RealtimeBetaServerEventInputAudioBufferCleared
Type: object
Description: Returned when the input audio buffer is cleared by the client with a 
`input_audio_buffer.clear` event.


- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `input_audio_buffer.cleared`.

### RealtimeBetaServerEventInputAudioBufferCommitted
Type: object
Description: Returned when an input audio buffer is committed, either by the client or
automatically in server VAD mode. The `item_id` property is the ID of the user
message item that will be created, thus a `conv...

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `input_audio_buffer.committed`.
- previous_item_id: object (optional)
- item_id: string (required) — The ID of the user message item that will be created.

### RealtimeBetaServerEventInputAudioBufferSpeechStarted
Type: object
Description: Sent by the server when in `server_vad` mode to indicate that speech has been 
detected in the audio buffer. This can happen any time audio is added to the 
buffer (unless speech is already detected)....

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `input_audio_buffer.speech_started`.
- audio_start_ms: integer (required) — Milliseconds from the start of all audio written to the buff...
- item_id: string (required) — The ID of the user message item that will be created when sp...

### RealtimeBetaServerEventInputAudioBufferSpeechStopped
Type: object
Description: Returned in `server_vad` mode when the server detects the end of speech in 
the audio buffer. The server will also send an `conversation.item.created` 
event with the user message item that is created...

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `input_audio_buffer.speech_stopped`.
- audio_end_ms: integer (required) — Milliseconds since the session started when speech stopped. ...
- item_id: string (required) — The ID of the user message item that will be created.

### RealtimeBetaServerEventMCPListToolsCompleted
Type: object
Description: Returned when listing MCP tools has completed for an item.

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `mcp_list_tools.completed`.
- item_id: string (required) — The ID of the MCP list tools item.

### RealtimeBetaServerEventMCPListToolsFailed
Type: object
Description: Returned when listing MCP tools has failed for an item.

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `mcp_list_tools.failed`.
- item_id: string (required) — The ID of the MCP list tools item.

### RealtimeBetaServerEventMCPListToolsInProgress
Type: object
Description: Returned when listing MCP tools is in progress for an item.

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `mcp_list_tools.in_progress`.
- item_id: string (required) — The ID of the MCP list tools item.

### RealtimeBetaServerEventRateLimitsUpdated
Type: object
Description: Emitted at the beginning of a Response to indicate the updated rate limits. 
When a Response is created some tokens will be "reserved" for the output 
tokens, the rate limits shown here reflect that r...

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `rate_limits.updated`.
- rate_limits: array<object (4 fields)> (required) — List of rate limit information.

### RealtimeBetaServerEventResponseAudioDelta
Type: object
Description: Returned when the model-generated audio is updated.

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.output_audio.delta`.
- response_id: string (required) — The ID of the response.
- item_id: string (required) — The ID of the item.
- output_index: integer (required) — The index of the output item in the response.
- content_index: integer (required) — The index of the content part in the item's content array.
- delta: string (required) — Base64-encoded audio data delta.

### RealtimeBetaServerEventResponseAudioDone
Type: object
Description: Returned when the model-generated audio is done. Also emitted when a Response
is interrupted, incomplete, or cancelled.


- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.output_audio.done`.
- response_id: string (required) — The ID of the response.
- item_id: string (required) — The ID of the item.
- output_index: integer (required) — The index of the output item in the response.
- content_index: integer (required) — The index of the content part in the item's content array.

### RealtimeBetaServerEventResponseAudioTranscriptDelta
Type: object
Description: Returned when the model-generated transcription of audio output is updated.


- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.output_audio_transcript.de...
- response_id: string (required) — The ID of the response.
- item_id: string (required) — The ID of the item.
- output_index: integer (required) — The index of the output item in the response.
- content_index: integer (required) — The index of the content part in the item's content array.
- delta: string (required) — The transcript delta.

### RealtimeBetaServerEventResponseAudioTranscriptDone
Type: object
Description: Returned when the model-generated transcription of audio output is done
streaming. Also emitted when a Response is interrupted, incomplete, or
cancelled.


- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.output_audio_transcript.do...
- response_id: string (required) — The ID of the response.
- item_id: string (required) — The ID of the item.
- output_index: integer (required) — The index of the output item in the response.
- content_index: integer (required) — The index of the content part in the item's content array.
- transcript: string (required) — The final transcript of the audio.

### RealtimeBetaServerEventResponseContentPartAdded
Type: object
Description: Returned when a new content part is added to an assistant message item during
response generation.


- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.content_part.added`.
- response_id: string (required) — The ID of the response.
- item_id: string (required) — The ID of the item to which the content part was added.
- output_index: integer (required) — The index of the output item in the response.
- content_index: integer (required) — The index of the content part in the item's content array.
- part: object (4 fields) (required) — The content part that was added.

### RealtimeBetaServerEventResponseContentPartDone
Type: object
Description: Returned when a content part is done streaming in an assistant message item.
Also emitted when a Response is interrupted, incomplete, or cancelled.


- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.content_part.done`.
- response_id: string (required) — The ID of the response.
- item_id: string (required) — The ID of the item.
- output_index: integer (required) — The index of the output item in the response.
- content_index: integer (required) — The index of the content part in the item's content array.
- part: object (4 fields) (required) — The content part that is done.

### RealtimeBetaServerEventResponseCreated
Type: object
Description: Returned when a new Response is created. The first event of response creation,
where the response is in an initial state of `in_progress`.


- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.created`.
- response: object (required)

### RealtimeBetaServerEventResponseDone
Type: object
Description: Returned when a Response is done streaming. Always emitted, no matter the 
final state. The Response object included in the `response.done` event will 
include all output Items in the Response but wil...

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.done`.
- response: object (required)

### RealtimeBetaServerEventResponseFunctionCallArgumentsDelta
Type: object
Description: Returned when the model-generated function call arguments are updated.


- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.function_call_arguments.de...
- response_id: string (required) — The ID of the response.
- item_id: string (required) — The ID of the function call item.
- output_index: integer (required) — The index of the output item in the response.
- call_id: string (required) — The ID of the function call.
- delta: string (required) — The arguments delta as a JSON string.

### RealtimeBetaServerEventResponseFunctionCallArgumentsDone
Type: object
Description: Returned when the model-generated function call arguments are done streaming.
Also emitted when a Response is interrupted, incomplete, or cancelled.


- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.function_call_arguments.do...
- response_id: string (required) — The ID of the response.
- item_id: string (required) — The ID of the function call item.
- output_index: integer (required) — The index of the output item in the response.
- call_id: string (required) — The ID of the function call.
- arguments: string (required) — The final arguments as a JSON string.

### RealtimeBetaServerEventResponseMCPCallArgumentsDelta
Type: object
Description: Returned when MCP tool call arguments are updated during response generation.

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.mcp_call_arguments.delta`.
- response_id: string (required) — The ID of the response.
- item_id: string (required) — The ID of the MCP tool call item.
- output_index: integer (required) — The index of the output item in the response.
- delta: string (required) — The JSON-encoded arguments delta.
- obfuscation: object (optional)

### RealtimeBetaServerEventResponseMCPCallArgumentsDone
Type: object
Description: Returned when MCP tool call arguments are finalized during response generation.

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.mcp_call_arguments.done`.
- response_id: string (required) — The ID of the response.
- item_id: string (required) — The ID of the MCP tool call item.
- output_index: integer (required) — The index of the output item in the response.
- arguments: string (required) — The final JSON-encoded arguments string.

### RealtimeBetaServerEventResponseMCPCallCompleted
Type: object
Description: Returned when an MCP tool call has completed successfully.

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.mcp_call.completed`.
- output_index: integer (required) — The index of the output item in the response.
- item_id: string (required) — The ID of the MCP tool call item.

### RealtimeBetaServerEventResponseMCPCallFailed
Type: object
Description: Returned when an MCP tool call has failed.

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.mcp_call.failed`.
- output_index: integer (required) — The index of the output item in the response.
- item_id: string (required) — The ID of the MCP tool call item.

### RealtimeBetaServerEventResponseMCPCallInProgress
Type: object
Description: Returned when an MCP tool call has started and is in progress.

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.mcp_call.in_progress`.
- output_index: integer (required) — The index of the output item in the response.
- item_id: string (required) — The ID of the MCP tool call item.

### RealtimeBetaServerEventResponseOutputItemAdded
Type: object
Description: Returned when a new Item is created during Response generation.

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.output_item.added`.
- response_id: string (required) — The ID of the Response to which the item belongs.
- output_index: integer (required) — The index of the output item in the Response.
- item: object (required)

### RealtimeBetaServerEventResponseOutputItemDone
Type: object
Description: Returned when an Item is done streaming. Also emitted when a Response is 
interrupted, incomplete, or cancelled.


- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.output_item.done`.
- response_id: string (required) — The ID of the Response to which the item belongs.
- output_index: integer (required) — The index of the output item in the Response.
- item: object (required)

### RealtimeBetaServerEventResponseTextDelta
Type: object
Description: Returned when the text value of an "output_text" content part is updated.

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.output_text.delta`.
- response_id: string (required) — The ID of the response.
- item_id: string (required) — The ID of the item.
- output_index: integer (required) — The index of the output item in the response.
- content_index: integer (required) — The index of the content part in the item's content array.
- delta: string (required) — The text delta.

### RealtimeBetaServerEventResponseTextDone
Type: object
Description: Returned when the text value of an "output_text" content part is done streaming. Also
emitted when a Response is interrupted, incomplete, or cancelled.


- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.output_text.done`.
- response_id: string (required) — The ID of the response.
- item_id: string (required) — The ID of the item.
- output_index: integer (required) — The index of the output item in the response.
- content_index: integer (required) — The index of the content part in the item's content array.
- text: string (required) — The final text content.

### RealtimeBetaServerEventSessionCreated
Type: object
Description: Returned when a Session is created. Emitted automatically when a new 
connection is established as the first server event. This event will contain 
the default Session configuration.


- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `session.created`.
- session: object (required)

### RealtimeBetaServerEventSessionUpdated
Type: object
Description: Returned when a session is updated with a `session.update` event, unless
there is an error.


- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `session.updated`.
- session: object (required)

### RealtimeBetaServerEventTranscriptionSessionCreated
Type: object
Description: Returned when a transcription session is created.


- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `transcription_session.created`.
- session: object (required)

### RealtimeBetaServerEventTranscriptionSessionUpdated
Type: object
Description: Returned when a transcription session is updated with a `transcription_session.update` event, unless 
there is an error.


- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `transcription_session.updated`.
- session: object (required)

### RealtimeCallCreateRequest
Type: object
Description: Parameters required to initiate a realtime call and receive the SDP answer
needed to complete a WebRTC peer connection. Provide an SDP offer generated
by your client and optionally configure the sessi...

- sdp: string (required) — WebRTC Session Description Protocol (SDP) offer generated by...
- session: object (optional) — Optional session configuration to apply before the realtime ...

### RealtimeCallReferRequest
Type: object
Description: Parameters required to transfer a SIP call to a new destination using the
Realtime API.

- target_uri: string (required) — URI that should appear in the SIP Refer-To header. Supports ...

### RealtimeCallRejectRequest
Type: object
Description: Parameters used to decline an incoming SIP call handled by the Realtime API.

- status_code: integer (optional) — SIP response code to send back to the caller. Defaults to `6...

### RealtimeClientEvent
Type: object
Description: A realtime client event.


(empty)

### RealtimeClientEventConversationItemCreate
Type: object
Description: Add a new Item to the Conversation's context, including messages, function 
calls, and function call responses. This event can be used both to populate a 
"history" of the conversation and to add new ...

- event_id: string (optional) — Optional client-generated ID used to identify this event.
- type: object (required) — The event type, must be `conversation.item.create`.
- previous_item_id: string (optional) — The ID of the preceding item after which the new item will b...
- item: object (required)

### RealtimeClientEventConversationItemDelete
Type: object
Description: Send this event when you want to remove any item from the conversation 
history. The server will respond with a `conversation.item.deleted` event, 
unless the item does not exist in the conversation h...

- event_id: string (optional) — Optional client-generated ID used to identify this event.
- type: object (required) — The event type, must be `conversation.item.delete`.
- item_id: string (required) — The ID of the item to delete.

### RealtimeClientEventConversationItemRetrieve
Type: object
Description: Send this event when you want to retrieve the server's representation of a specific item in the conversation history. This is useful, for example, to inspect user audio after noise cancellation and VA...

- event_id: string (optional) — Optional client-generated ID used to identify this event.
- type: object (required) — The event type, must be `conversation.item.retrieve`.
- item_id: string (required) — The ID of the item to retrieve.

### RealtimeClientEventConversationItemTruncate
Type: object
Description: Send this event to truncate a previous assistant message’s audio. The server 
will produce audio faster than realtime, so this event is useful when the user 
interrupts to truncate audio that has alre...

- event_id: string (optional) — Optional client-generated ID used to identify this event.
- type: object (required) — The event type, must be `conversation.item.truncate`.
- item_id: string (required) — The ID of the assistant message item to truncate. Only assis...
- content_index: integer (required) — The index of the content part to truncate. Set this to `0`.
- audio_end_ms: integer (required) — Inclusive duration up to which audio is truncated, in millis...

### RealtimeClientEventInputAudioBufferAppend
Type: object
Description: Send this event to append audio bytes to the input audio buffer. The audio 
buffer is temporary storage you can write to and later commit. A "commit" will create a new
user message item in the convers...

- event_id: string (optional) — Optional client-generated ID used to identify this event.
- type: object (required) — The event type, must be `input_audio_buffer.append`.
- audio: string (required) — Base64-encoded audio bytes. This must be in the format speci...

### RealtimeClientEventInputAudioBufferClear
Type: object
Description: Send this event to clear the audio bytes in the buffer. The server will 
respond with an `input_audio_buffer.cleared` event.


- event_id: string (optional) — Optional client-generated ID used to identify this event.
- type: object (required) — The event type, must be `input_audio_buffer.clear`.

### RealtimeClientEventInputAudioBufferCommit
Type: object
Description: Send this event to commit the user input audio buffer, which will create a  new user message item in the conversation. This event will produce an error  if the input audio buffer is empty. When in Ser...

- event_id: string (optional) — Optional client-generated ID used to identify this event.
- type: object (required) — The event type, must be `input_audio_buffer.commit`.

### RealtimeClientEventOutputAudioBufferClear
Type: object
Description: **WebRTC Only:** Emit to cut off the current audio response. This will trigger the server to
stop generating audio and emit a `output_audio_buffer.cleared` event. This 
event should be preceded by a `...

- event_id: string (optional) — The unique ID of the client event used for error handling.
- type: object (required) — The event type, must be `output_audio_buffer.clear`.

### RealtimeClientEventResponseCancel
Type: object
Description: Send this event to cancel an in-progress response. The server will respond 
with a `response.done` event with a status of `response.status=cancelled`. If 
there is no response to cancel, the server wi...

- event_id: string (optional) — Optional client-generated ID used to identify this event.
- type: object (required) — The event type, must be `response.cancel`.
- response_id: string (optional) — A specific response ID to cancel - if not provided, will can...

### RealtimeClientEventResponseCreate
Type: object
Description: This event instructs the server to create a Response, which means triggering 
model inference. When in Server VAD mode, the server will create Responses 
automatically.

A Response will include at lea...

- event_id: string (optional) — Optional client-generated ID used to identify this event.
- type: object (required) — The event type, must be `response.create`.
- response: object (optional)

### RealtimeClientEventSessionUpdate
Type: object
Description: Send this event to update the session’s configuration.
The client may send this event at any time to update any field
except for `voice` and `model`. `voice` can be updated only if there have been no ...

- event_id: string (optional) — Optional client-generated ID used to identify this event. Th...
- type: object (required) — The event type, must be `session.update`.
- session: object (required) — Update the Realtime session. Choose either a realtime
sessio...

### RealtimeClientEventTranscriptionSessionUpdate
Type: object
Description: Send this event to update a transcription session.


- event_id: string (optional) — Optional client-generated ID used to identify this event.
- type: object (required) — The event type, must be `transcription_session.update`.
- session: object (required)

### RealtimeConnectParams
Type: object

- model: string (optional)
- call_id: string (optional)

### RealtimeConversationItem
Type: object
Description: A single item within a Realtime conversation.

(empty)

### RealtimeConversationItemFunctionCall
Type: object
Description: A function call item in a Realtime conversation.

- id: string (optional) — The unique ID of the item. This may be provided by the clien...
- object: string (enum: realtime.item) (optional) — Identifier for the API object being returned - always `realt...
- type: string (enum: function_call) (required) — The type of the item. Always `function_call`.
- status: string (enum: completed, incomplete, in_progress) (optional) — The status of the item. Has no effect on the conversation.
- call_id: string (optional) — The ID of the function call.
- name: string (required) — The name of the function being called.
- arguments: string (required) — The arguments of the function call. This is a JSON-encoded s...

### RealtimeConversationItemFunctionCallOutput
Type: object
Description: A function call output item in a Realtime conversation.

- id: string (optional) — The unique ID of the item. This may be provided by the clien...
- object: string (enum: realtime.item) (optional) — Identifier for the API object being returned - always `realt...
- type: string (enum: function_call_output) (required) — The type of the item. Always `function_call_output`.
- status: string (enum: completed, incomplete, in_progress) (optional) — The status of the item. Has no effect on the conversation.
- call_id: string (required) — The ID of the function call this output is for.
- output: string (required) — The output of the function call, this is free text and can c...

### RealtimeConversationItemMessageAssistant
Type: object
Description: An assistant message item in a Realtime conversation.

- id: string (optional) — The unique ID of the item. This may be provided by the clien...
- object: string (enum: realtime.item) (optional) — Identifier for the API object being returned - always `realt...
- type: string (enum: message) (required) — The type of the item. Always `message`.
- status: string (enum: completed, incomplete, in_progress) (optional) — The status of the item. Has no effect on the conversation.
- role: string (enum: assistant) (required) — The role of the message sender. Always `assistant`.
- content: array<object (4 fields)> (required) — The content of the message.

### RealtimeConversationItemMessageSystem
Type: object
Description: A system message in a Realtime conversation can be used to provide additional context or instructions to the model. This is similar but distinct from the instruction prompt provided at the start of a ...

- id: string (optional) — The unique ID of the item. This may be provided by the clien...
- object: string (enum: realtime.item) (optional) — Identifier for the API object being returned - always `realt...
- type: string (enum: message) (required) — The type of the item. Always `message`.
- status: string (enum: completed, incomplete, in_progress) (optional) — The status of the item. Has no effect on the conversation.
- role: string (enum: system) (required) — The role of the message sender. Always `system`.
- content: array<object (2 fields)> (required) — The content of the message.

### RealtimeConversationItemMessageUser
Type: object
Description: A user message item in a Realtime conversation.

- id: string (optional) — The unique ID of the item. This may be provided by the clien...
- object: string (enum: realtime.item) (optional) — Identifier for the API object being returned - always `realt...
- type: string (enum: message) (required) — The type of the item. Always `message`.
- status: string (enum: completed, incomplete, in_progress) (optional) — The status of the item. Has no effect on the conversation.
- role: string (enum: user) (required) — The role of the message sender. Always `user`.
- content: array<object (6 fields)> (required) — The content of the message.

### RealtimeConversationItemWithReference
Type: object
Description: The item to add to the conversation.

- id: string (optional) — For an item of type (`message` | `function_call` | `function...
- type: string (enum: message, function_call, function_call_output, item_reference) (optional) — The type of the item (`message`, `function_call`, `function_...
- object: string (enum: realtime.item) (optional) — Identifier for the API object being returned - always `realt...
- status: string (enum: completed, incomplete, in_progress) (optional) — The status of the item (`completed`, `incomplete`, `in_progr...
- role: string (enum: user, assistant, system) (optional) — The role of the message sender (`user`, `assistant`, `system...
- content: array<object (5 fields)> (optional) — The content of the message, applicable for `message` items. ...
- call_id: string (optional) — The ID of the function call (for `function_call` and 
`funct...
- name: string (optional) — The name of the function being called (for `function_call` i...
- arguments: string (optional) — The arguments of the function call (for `function_call` item...
- output: string (optional) — The output of the function call (for `function_call_output` ...

### RealtimeCreateClientSecretRequest
Type: object
Description: Create a session and client secret for the Realtime API. The request can specify
either a realtime or a transcription session configuration.
[Learn more about the Realtime API](https://platform.openai...

- expires_after: object (2 fields) (optional) — Configuration for the client secret expiration. Expiration r...
- session: object (optional) — Session configuration to use for the client secret. Choose e...

### RealtimeCreateClientSecretResponse
Type: object
Description: Response from creating a session and client secret for the Realtime API.


- value: string (required) — The generated client secret value.
- expires_at: integer (required) — Expiration timestamp for the client secret, in seconds since...
- session: object (required) — The session configuration for either a realtime or transcrip...

### RealtimeFunctionTool
Type: object

- type: string (enum: function) (optional) — The type of the tool, i.e. `function`.
- name: string (optional) — The name of the function.
- description: string (optional) — The description of the function, including guidance on when ...
- parameters: object (optional) — Parameters of the function in JSON Schema.

### RealtimeMCPApprovalRequest
Type: object
Description: A Realtime item requesting human approval of a tool invocation.


- type: string (enum: mcp_approval_request) (required) — The type of the item. Always `mcp_approval_request`.
- id: string (required) — The unique ID of the approval request.
- server_label: string (required) — The label of the MCP server making the request.
- name: string (required) — The name of the tool to run.
- arguments: string (required) — A JSON string of arguments for the tool.

### RealtimeMCPApprovalResponse
Type: object
Description: A Realtime item responding to an MCP approval request.


- type: string (enum: mcp_approval_response) (required) — The type of the item. Always `mcp_approval_response`.
- id: string (required) — The unique ID of the approval response.
- approval_request_id: string (required) — The ID of the approval request being answered.
- approve: boolean (required) — Whether the request was approved.
- reason: object (optional)

### RealtimeMCPHTTPError
Type: object

- type: string (enum: http_error) (required)
- code: integer (required)
- message: string (required)

### RealtimeMCPListTools
Type: object
Description: A Realtime item listing tools available on an MCP server.


- type: string (enum: mcp_list_tools) (required) — The type of the item. Always `mcp_list_tools`.
- id: string (optional) — The unique ID of the list.
- server_label: string (required) — The label of the MCP server.
- tools: array<object> (required) — The tools available on the server.

### RealtimeMCPProtocolError
Type: object

- type: string (enum: protocol_error) (required)
- code: integer (required)
- message: string (required)

### RealtimeMCPToolCall
Type: object
Description: A Realtime item representing an invocation of a tool on an MCP server.


- type: string (enum: mcp_call) (required) — The type of the item. Always `mcp_call`.
- id: string (required) — The unique ID of the tool call.
- server_label: string (required) — The label of the MCP server running the tool.
- name: string (required) — The name of the tool that was run.
- arguments: string (required) — A JSON string of the arguments passed to the tool.
- approval_request_id: object (optional)
- output: object (optional)
- error: object (optional)

### RealtimeMCPToolExecutionError
Type: object

- type: string (enum: tool_execution_error) (required)
- message: string (required)

### RealtimeResponse
Type: object
Description: The response resource.

- id: string (optional) — The unique ID of the response, will look like `resp_1234`.
- object: object (optional) — The object type, must be `realtime.response`.
- status: string (enum: completed, cancelled, failed, incomplete, in_progress) (optional) — The final status of the response (`completed`, `cancelled`, ...
- status_details: object (3 fields) (optional) — Additional details about the status.
- output: array<object> (optional) — The list of output items generated by the response.
- metadata: object (optional)
- audio: object (1 fields) (optional) — Configuration for audio output.
- usage: object (5 fields) (optional) — Usage statistics for the Response, this will correspond to b...
- conversation_id: string (optional) — Which conversation the response is added to, determined by t...
- output_modalities: array<string (enum: text, audio)> (optional) — The set of modalities the model used to respond, currently t...
- max_output_tokens: object (optional) — Maximum number of output tokens for a single assistant respo...

### RealtimeResponseCreateParams
Type: object
Description: Create a new Realtime response with these parameters

- output_modalities: array<string (enum: text, audio)> (optional) — The set of modalities the model used to respond, currently t...
- instructions: string (optional) — The default system instructions (i.e. system message) prepen...
- audio: object (1 fields) (optional) — Configuration for audio input and output.
- tools: array<object> (optional) — Tools available to the model.
- tool_choice: object (optional) — How the model chooses tools. Provide one of the string modes...
- max_output_tokens: object (optional) — Maximum number of output tokens for a single assistant respo...
- conversation: object (optional) — Controls which conversation the response is added to. Curren...
- metadata: object (optional)
- prompt: object (optional)
- input: array<object> (optional) — Input items to include in the prompt for the model. Using th...

### RealtimeServerEvent
Type: object
Description: A realtime server event.


(empty)

### RealtimeServerEventConversationCreated
Type: object
Description: Returned when a conversation is created. Emitted right after session creation.


- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `conversation.created`.
- conversation: object (2 fields) (required) — The conversation resource.

### RealtimeServerEventConversationItemAdded
Type: object
Description: Sent by the server when an Item is added to the default Conversation. This can happen in several cases:
- When the client sends a `conversation.item.create` event.
- When the input audio buffer is com...

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `conversation.item.added`.
- previous_item_id: object (optional)
- item: object (required)

### RealtimeServerEventConversationItemCreated
Type: object
Description: Returned when a conversation item is created. There are several scenarios that produce this event:
  - The server is generating a Response, which if successful will produce
    either one or two Items...

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `conversation.item.created`.
- previous_item_id: object (optional)
- item: object (required)

### RealtimeServerEventConversationItemDeleted
Type: object
Description: Returned when an item in the conversation is deleted by the client with a 
`conversation.item.delete` event. This event is used to synchronize the 
server's understanding of the conversation history w...

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `conversation.item.deleted`.
- item_id: string (required) — The ID of the item that was deleted.

### RealtimeServerEventConversationItemDone
Type: object
Description: Returned when a conversation item is finalized.

The event will include the full content of the Item except for audio data, which can be retrieved separately with a `conversation.item.retrieve` event ...

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `conversation.item.done`.
- previous_item_id: object (optional)
- item: object (required)

### RealtimeServerEventConversationItemInputAudioTranscriptionCompleted
Type: object
Description: This event is the output of audio transcription for user audio written to the
user audio buffer. Transcription begins when the input audio buffer is
committed by the client or server (when VAD is enab...

- event_id: string (required) — The unique ID of the server event.
- type: string (enum: conversation.item.input_audio_transcription.completed) (required) — The event type, must be
`conversation.item.input_audio_trans...
- item_id: string (required) — The ID of the item containing the audio that is being transc...
- content_index: integer (required) — The index of the content part containing the audio.
- transcript: string (required) — The transcribed text.
- logprobs: object (optional)
- usage: object (required) — Usage statistics for the transcription, this is billed accor...

### RealtimeServerEventConversationItemInputAudioTranscriptionDelta
Type: object
Description: Returned when the text value of an input audio transcription content part is updated with incremental transcription results.


- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `conversation.item.input_audio_trans...
- item_id: string (required) — The ID of the item containing the audio that is being transc...
- content_index: integer (optional) — The index of the content part in the item's content array.
- delta: string (optional) — The text delta.
- logprobs: object (optional)

### RealtimeServerEventConversationItemInputAudioTranscriptionFailed
Type: object
Description: Returned when input audio transcription is configured, and a transcription 
request for a user message failed. These events are separate from other 
`error` events so that the client can identify the ...

- event_id: string (required) — The unique ID of the server event.
- type: string (enum: conversation.item.input_audio_transcription.failed) (required) — The event type, must be
`conversation.item.input_audio_trans...
- item_id: string (required) — The ID of the user message item.
- content_index: integer (required) — The index of the content part containing the audio.
- error: object (4 fields) (required) — Details of the transcription error.

### RealtimeServerEventConversationItemInputAudioTranscriptionSegment
Type: object
Description: Returned when an input audio transcription segment is identified for an item.

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `conversation.item.input_audio_trans...
- item_id: string (required) — The ID of the item containing the input audio content.
- content_index: integer (required) — The index of the input audio content part within the item.
- text: string (required) — The text for this segment.
- id: string (required) — The segment identifier.
- speaker: string (required) — The detected speaker label for this segment.
- start: number (float) (required) — Start time of the segment in seconds.
- end: number (float) (required) — End time of the segment in seconds.

### RealtimeServerEventConversationItemRetrieved
Type: object
Description: Returned when a conversation item is retrieved with `conversation.item.retrieve`. This is provided as a way to fetch the server's representation of an item, for example to get access to the post-proce...

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `conversation.item.retrieved`.
- item: object (required)

### RealtimeServerEventConversationItemTruncated
Type: object
Description: Returned when an earlier assistant audio message item is truncated by the 
client with a `conversation.item.truncate` event. This event is used to 
synchronize the server's understanding of the audio ...

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `conversation.item.truncated`.
- item_id: string (required) — The ID of the assistant message item that was truncated.
- content_index: integer (required) — The index of the content part that was truncated.
- audio_end_ms: integer (required) — The duration up to which the audio was truncated, in millise...

### RealtimeServerEventError
Type: object
Description: Returned when an error occurs, which could be a client problem or a server
problem. Most errors are recoverable and the session will stay open, we
recommend to implementors to monitor and log error me...

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `error`.
- error: object (5 fields) (required) — Details of the error.

### RealtimeServerEventInputAudioBufferCleared
Type: object
Description: Returned when the input audio buffer is cleared by the client with a 
`input_audio_buffer.clear` event.


- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `input_audio_buffer.cleared`.

### RealtimeServerEventInputAudioBufferCommitted
Type: object
Description: Returned when an input audio buffer is committed, either by the client or
automatically in server VAD mode. The `item_id` property is the ID of the user
message item that will be created, thus a `conv...

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `input_audio_buffer.committed`.
- previous_item_id: object (optional)
- item_id: string (required) — The ID of the user message item that will be created.

### RealtimeServerEventInputAudioBufferSpeechStarted
Type: object
Description: Sent by the server when in `server_vad` mode to indicate that speech has been 
detected in the audio buffer. This can happen any time audio is added to the 
buffer (unless speech is already detected)....

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `input_audio_buffer.speech_started`.
- audio_start_ms: integer (required) — Milliseconds from the start of all audio written to the buff...
- item_id: string (required) — The ID of the user message item that will be created when sp...

### RealtimeServerEventInputAudioBufferSpeechStopped
Type: object
Description: Returned in `server_vad` mode when the server detects the end of speech in 
the audio buffer. The server will also send an `conversation.item.created` 
event with the user message item that is created...

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `input_audio_buffer.speech_stopped`.
- audio_end_ms: integer (required) — Milliseconds since the session started when speech stopped. ...
- item_id: string (required) — The ID of the user message item that will be created.

### RealtimeServerEventInputAudioBufferTimeoutTriggered
Type: object
Description: Returned when the Server VAD timeout is triggered for the input audio buffer. This is configured
with `idle_timeout_ms` in the `turn_detection` settings of the session, and it indicates that
there has...

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `input_audio_buffer.timeout_triggere...
- audio_start_ms: integer (required) — Millisecond offset of audio written to the input audio buffe...
- audio_end_ms: integer (required) — Millisecond offset of audio written to the input audio buffe...
- item_id: string (required) — The ID of the item associated with this segment.

### RealtimeServerEventMCPListToolsCompleted
Type: object
Description: Returned when listing MCP tools has completed for an item.

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `mcp_list_tools.completed`.
- item_id: string (required) — The ID of the MCP list tools item.

### RealtimeServerEventMCPListToolsFailed
Type: object
Description: Returned when listing MCP tools has failed for an item.

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `mcp_list_tools.failed`.
- item_id: string (required) — The ID of the MCP list tools item.

### RealtimeServerEventMCPListToolsInProgress
Type: object
Description: Returned when listing MCP tools is in progress for an item.

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `mcp_list_tools.in_progress`.
- item_id: string (required) — The ID of the MCP list tools item.

### RealtimeServerEventOutputAudioBufferCleared
Type: object
Description: **WebRTC Only:** Emitted when the output audio buffer is cleared. This happens either in VAD
mode when the user has interrupted (`input_audio_buffer.speech_started`),
or when the client has emitted th...

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `output_audio_buffer.cleared`.
- response_id: string (required) — The unique ID of the response that produced the audio.

### RealtimeServerEventOutputAudioBufferStarted
Type: object
Description: **WebRTC Only:** Emitted when the server begins streaming audio to the client. This event is
emitted after an audio content part has been added (`response.content_part.added`)
to the response.
[Learn ...

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `output_audio_buffer.started`.
- response_id: string (required) — The unique ID of the response that produced the audio.

### RealtimeServerEventOutputAudioBufferStopped
Type: object
Description: **WebRTC Only:** Emitted when the output audio buffer has been completely drained on the server,
and no more audio is forthcoming. This event is emitted after the full response
data has been sent to t...

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `output_audio_buffer.stopped`.
- response_id: string (required) — The unique ID of the response that produced the audio.

### RealtimeServerEventRateLimitsUpdated
Type: object
Description: Emitted at the beginning of a Response to indicate the updated rate limits. 
When a Response is created some tokens will be "reserved" for the output 
tokens, the rate limits shown here reflect that r...

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `rate_limits.updated`.
- rate_limits: array<object (4 fields)> (required) — List of rate limit information.

### RealtimeServerEventResponseAudioDelta
Type: object
Description: Returned when the model-generated audio is updated.

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.output_audio.delta`.
- response_id: string (required) — The ID of the response.
- item_id: string (required) — The ID of the item.
- output_index: integer (required) — The index of the output item in the response.
- content_index: integer (required) — The index of the content part in the item's content array.
- delta: string (required) — Base64-encoded audio data delta.

### RealtimeServerEventResponseAudioDone
Type: object
Description: Returned when the model-generated audio is done. Also emitted when a Response
is interrupted, incomplete, or cancelled.


- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.output_audio.done`.
- response_id: string (required) — The ID of the response.
- item_id: string (required) — The ID of the item.
- output_index: integer (required) — The index of the output item in the response.
- content_index: integer (required) — The index of the content part in the item's content array.

### RealtimeServerEventResponseAudioTranscriptDelta
Type: object
Description: Returned when the model-generated transcription of audio output is updated.


- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.output_audio_transcript.de...
- response_id: string (required) — The ID of the response.
- item_id: string (required) — The ID of the item.
- output_index: integer (required) — The index of the output item in the response.
- content_index: integer (required) — The index of the content part in the item's content array.
- delta: string (required) — The transcript delta.

### RealtimeServerEventResponseAudioTranscriptDone
Type: object
Description: Returned when the model-generated transcription of audio output is done
streaming. Also emitted when a Response is interrupted, incomplete, or
cancelled.


- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.output_audio_transcript.do...
- response_id: string (required) — The ID of the response.
- item_id: string (required) — The ID of the item.
- output_index: integer (required) — The index of the output item in the response.
- content_index: integer (required) — The index of the content part in the item's content array.
- transcript: string (required) — The final transcript of the audio.

### RealtimeServerEventResponseContentPartAdded
Type: object
Description: Returned when a new content part is added to an assistant message item during
response generation.


- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.content_part.added`.
- response_id: string (required) — The ID of the response.
- item_id: string (required) — The ID of the item to which the content part was added.
- output_index: integer (required) — The index of the output item in the response.
- content_index: integer (required) — The index of the content part in the item's content array.
- part: object (4 fields) (required) — The content part that was added.

### RealtimeServerEventResponseContentPartDone
Type: object
Description: Returned when a content part is done streaming in an assistant message item.
Also emitted when a Response is interrupted, incomplete, or cancelled.


- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.content_part.done`.
- response_id: string (required) — The ID of the response.
- item_id: string (required) — The ID of the item.
- output_index: integer (required) — The index of the output item in the response.
- content_index: integer (required) — The index of the content part in the item's content array.
- part: object (4 fields) (required) — The content part that is done.

### RealtimeServerEventResponseCreated
Type: object
Description: Returned when a new Response is created. The first event of response creation,
where the response is in an initial state of `in_progress`.


- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.created`.
- response: object (required)

### RealtimeServerEventResponseDone
Type: object
Description: Returned when a Response is done streaming. Always emitted, no matter the 
final state. The Response object included in the `response.done` event will 
include all output Items in the Response but wil...

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.done`.
- response: object (required)

### RealtimeServerEventResponseFunctionCallArgumentsDelta
Type: object
Description: Returned when the model-generated function call arguments are updated.


- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.function_call_arguments.de...
- response_id: string (required) — The ID of the response.
- item_id: string (required) — The ID of the function call item.
- output_index: integer (required) — The index of the output item in the response.
- call_id: string (required) — The ID of the function call.
- delta: string (required) — The arguments delta as a JSON string.

### RealtimeServerEventResponseFunctionCallArgumentsDone
Type: object
Description: Returned when the model-generated function call arguments are done streaming.
Also emitted when a Response is interrupted, incomplete, or cancelled.


- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.function_call_arguments.do...
- response_id: string (required) — The ID of the response.
- item_id: string (required) — The ID of the function call item.
- output_index: integer (required) — The index of the output item in the response.
- call_id: string (required) — The ID of the function call.
- arguments: string (required) — The final arguments as a JSON string.

### RealtimeServerEventResponseMCPCallArgumentsDelta
Type: object
Description: Returned when MCP tool call arguments are updated during response generation.

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.mcp_call_arguments.delta`.
- response_id: string (required) — The ID of the response.
- item_id: string (required) — The ID of the MCP tool call item.
- output_index: integer (required) — The index of the output item in the response.
- delta: string (required) — The JSON-encoded arguments delta.
- obfuscation: object (optional)

### RealtimeServerEventResponseMCPCallArgumentsDone
Type: object
Description: Returned when MCP tool call arguments are finalized during response generation.

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.mcp_call_arguments.done`.
- response_id: string (required) — The ID of the response.
- item_id: string (required) — The ID of the MCP tool call item.
- output_index: integer (required) — The index of the output item in the response.
- arguments: string (required) — The final JSON-encoded arguments string.

### RealtimeServerEventResponseMCPCallCompleted
Type: object
Description: Returned when an MCP tool call has completed successfully.

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.mcp_call.completed`.
- output_index: integer (required) — The index of the output item in the response.
- item_id: string (required) — The ID of the MCP tool call item.

### RealtimeServerEventResponseMCPCallFailed
Type: object
Description: Returned when an MCP tool call has failed.

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.mcp_call.failed`.
- output_index: integer (required) — The index of the output item in the response.
- item_id: string (required) — The ID of the MCP tool call item.

### RealtimeServerEventResponseMCPCallInProgress
Type: object
Description: Returned when an MCP tool call has started and is in progress.

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.mcp_call.in_progress`.
- output_index: integer (required) — The index of the output item in the response.
- item_id: string (required) — The ID of the MCP tool call item.

### RealtimeServerEventResponseOutputItemAdded
Type: object
Description: Returned when a new Item is created during Response generation.

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.output_item.added`.
- response_id: string (required) — The ID of the Response to which the item belongs.
- output_index: integer (required) — The index of the output item in the Response.
- item: object (required)

### RealtimeServerEventResponseOutputItemDone
Type: object
Description: Returned when an Item is done streaming. Also emitted when a Response is 
interrupted, incomplete, or cancelled.


- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.output_item.done`.
- response_id: string (required) — The ID of the Response to which the item belongs.
- output_index: integer (required) — The index of the output item in the Response.
- item: object (required)

### RealtimeServerEventResponseTextDelta
Type: object
Description: Returned when the text value of an "output_text" content part is updated.

- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.output_text.delta`.
- response_id: string (required) — The ID of the response.
- item_id: string (required) — The ID of the item.
- output_index: integer (required) — The index of the output item in the response.
- content_index: integer (required) — The index of the content part in the item's content array.
- delta: string (required) — The text delta.

### RealtimeServerEventResponseTextDone
Type: object
Description: Returned when the text value of an "output_text" content part is done streaming. Also
emitted when a Response is interrupted, incomplete, or cancelled.


- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `response.output_text.done`.
- response_id: string (required) — The ID of the response.
- item_id: string (required) — The ID of the item.
- output_index: integer (required) — The index of the output item in the response.
- content_index: integer (required) — The index of the content part in the item's content array.
- text: string (required) — The final text content.

### RealtimeServerEventSessionCreated
Type: object
Description: Returned when a Session is created. Emitted automatically when a new
connection is established as the first server event. This event will contain
the default Session configuration.


- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `session.created`.
- session: object (required) — The session configuration.

### RealtimeServerEventSessionUpdated
Type: object
Description: Returned when a session is updated with a `session.update` event, unless
there is an error.


- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `session.updated`.
- session: object (required) — The session configuration.

### RealtimeServerEventTranscriptionSessionUpdated
Type: object
Description: Returned when a transcription session is updated with a `transcription_session.update` event, unless 
there is an error.


- event_id: string (required) — The unique ID of the server event.
- type: object (required) — The event type, must be `transcription_session.updated`.
- session: object (required)

### RealtimeSession
Type: object
Description: Realtime session object for the beta interface.

- id: string (optional) — Unique identifier for the session that looks like `sess_1234...
- object: string (enum: realtime.session) (optional) — The object type. Always `realtime.session`.
- modalities: object (optional) — The set of modalities the model can respond with. To disable...
- model: string (enum: gpt-realtime, gpt-realtime-2025-08-28, gpt-4o-realtime-preview, gpt-4o-realtime-preview-2024-10-01, gpt-4o-realtime-preview-2024-12-17...) (optional) — The Realtime model used for this session.

- instructions: string (optional) — The default system instructions (i.e. system message) prepen...
- voice: object (optional) — The voice the model uses to respond. Voice cannot be changed...
- input_audio_format: string (enum: pcm16, g711_ulaw, g711_alaw) (optional) — The format of input audio. Options are `pcm16`, `g711_ulaw`,...
- output_audio_format: string (enum: pcm16, g711_ulaw, g711_alaw) (optional) — The format of output audio. Options are `pcm16`, `g711_ulaw`...
- input_audio_transcription: object (optional)
- turn_detection: object (optional)
- input_audio_noise_reduction: object (1 fields) (optional) — Configuration for input audio noise reduction. This can be s...
- speed: number (optional) — The speed of the model's spoken response. 1.0 is the default...
- tracing: object (optional)
- tools: array<object> (optional) — Tools (functions) available to the model.
- tool_choice: string (optional) — How the model chooses tools. Options are `auto`, `none`, `re...
- temperature: number (optional) — Sampling temperature for the model, limited to [0.6, 1.2]. F...
- max_response_output_tokens: object (optional) — Maximum number of output tokens for a single assistant respo...
- expires_at: integer (optional) — Expiration timestamp for the session, in seconds since epoch...
- prompt: object (optional)
- include: object (optional)

### RealtimeSessionCreateRequest
Type: object
Description: A new Realtime session configuration, with an ephemeral key. Default TTL
for keys is one minute.


- client_secret: object (2 fields) (required) — Ephemeral key returned by the API.
- modalities: object (optional) — The set of modalities the model can respond with. To disable...
- instructions: string (optional) — The default system instructions (i.e. system message) prepen...
- voice: object (optional) — The voice the model uses to respond. Voice cannot be changed...
- input_audio_format: string (optional) — The format of input audio. Options are `pcm16`, `g711_ulaw`,...
- output_audio_format: string (optional) — The format of output audio. Options are `pcm16`, `g711_ulaw`...
- input_audio_transcription: object (1 fields) (optional) — Configuration for input audio transcription, defaults to off...
- speed: number (optional) — The speed of the model's spoken response. 1.0 is the default...
- tracing: object (optional) — Configuration options for tracing. Set to null to disable tr...
- turn_detection: object (4 fields) (optional) — Configuration for turn detection. Can be set to `null` to tu...
- tools: array<object (4 fields)> (optional) — Tools (functions) available to the model.
- tool_choice: string (optional) — How the model chooses tools. Options are `auto`, `none`, `re...
- temperature: number (optional) — Sampling temperature for the model, limited to [0.6, 1.2]. D...
- max_response_output_tokens: object (optional) — Maximum number of output tokens for a single assistant respo...
- truncation: object (optional)
- prompt: object (optional)

### RealtimeSessionCreateRequestGA
Type: object
Description: Realtime session object configuration.

- type: string (enum: realtime) (required) — The type of session to create. Always `realtime` for the Rea...
- output_modalities: array<string (enum: text, audio)> (optional) — The set of modalities the model can respond with. It default...
- model: object (optional) — The Realtime model used for this session.

- instructions: string (optional) — The default system instructions (i.e. system message) prepen...
- audio: object (2 fields) (optional) — Configuration for input and output audio.

- include: array<string (enum: item.input_audio_transcription.logprobs)> (optional) — Additional fields to include in server outputs.

`item.input...
- tracing: object (optional) — Realtime API can write session traces to the [Traces Dashboa...
- tools: array<object> (optional) — Tools available to the model.
- tool_choice: object (optional) — How the model chooses tools. Provide one of the string modes...
- max_output_tokens: object (optional) — Maximum number of output tokens for a single assistant respo...
- truncation: object (optional)
- prompt: object (optional)

### RealtimeSessionCreateResponse
Type: object
Description: A Realtime session configuration object.


- id: string (optional) — Unique identifier for the session that looks like `sess_1234...
- object: string (optional) — The object type. Always `realtime.session`.
- expires_at: integer (optional) — Expiration timestamp for the session, in seconds since epoch...
- include: array<string (enum: item.input_audio_transcription.logprobs)> (optional) — Additional fields to include in server outputs.
- `item.inpu...
- model: string (optional) — The Realtime model used for this session.
- output_modalities: object (optional) — The set of modalities the model can respond with. To disable...
- instructions: string (optional) — The default system instructions (i.e. system message) prepen...
- audio: object (2 fields) (optional) — Configuration for input and output audio for the session.

- tracing: object (optional) — Configuration options for tracing. Set to null to disable tr...
- turn_detection: object (4 fields) (optional) — Configuration for turn detection. Can be set to `null` to tu...
- tools: array<object> (optional) — Tools (functions) available to the model.
- tool_choice: string (optional) — How the model chooses tools. Options are `auto`, `none`, `re...
- max_output_tokens: object (optional) — Maximum number of output tokens for a single assistant respo...

### RealtimeSessionCreateResponseGA
Type: object
Description: A new Realtime session configuration, with an ephemeral key. Default TTL
for keys is one minute.


- client_secret: object (2 fields) (required) — Ephemeral key returned by the API.
- type: string (enum: realtime) (required) — The type of session to create. Always `realtime` for the Rea...
- output_modalities: array<string (enum: text, audio)> (optional) — The set of modalities the model can respond with. It default...
- model: object (optional) — The Realtime model used for this session.

- instructions: string (optional) — The default system instructions (i.e. system message) prepen...
- audio: object (2 fields) (optional) — Configuration for input and output audio.

- include: array<string (enum: item.input_audio_transcription.logprobs)> (optional) — Additional fields to include in server outputs.

`item.input...
- tracing: object (optional)
- tools: array<object> (optional) — Tools available to the model.
- tool_choice: object (optional) — How the model chooses tools. Provide one of the string modes...
- max_output_tokens: object (optional) — Maximum number of output tokens for a single assistant respo...
- truncation: object (optional)
- prompt: object (optional)

### RealtimeTranscriptionSessionCreateRequest
Type: object
Description: Realtime transcription session object configuration.

- turn_detection: object (4 fields) (optional) — Configuration for turn detection. Can be set to `null` to tu...
- input_audio_noise_reduction: object (1 fields) (optional) — Configuration for input audio noise reduction. This can be s...
- input_audio_format: string (enum: pcm16, g711_ulaw, g711_alaw) (optional) — The format of input audio. Options are `pcm16`, `g711_ulaw`,...
- input_audio_transcription: object (optional) — Configuration for input audio transcription. The client can ...
- include: array<string (enum: item.input_audio_transcription.logprobs)> (optional) — The set of items to include in the transcription. Current av...

### RealtimeTranscriptionSessionCreateRequestGA
Type: object
Description: Realtime transcription session object configuration.

- type: string (enum: transcription) (required) — The type of session to create. Always `transcription` for tr...
- audio: object (1 fields) (optional) — Configuration for input and output audio.

- include: array<string (enum: item.input_audio_transcription.logprobs)> (optional) — Additional fields to include in server outputs.

`item.input...

### RealtimeTranscriptionSessionCreateResponse
Type: object
Description: A new Realtime transcription session configuration.

When a session is created on the server via REST API, the session object
also contains an ephemeral key. Default TTL for keys is 10 minutes. This
p...

- client_secret: object (2 fields) (required) — Ephemeral key returned by the API. Only present when the ses...
- modalities: object (optional) — The set of modalities the model can respond with. To disable...
- input_audio_format: string (optional) — The format of input audio. Options are `pcm16`, `g711_ulaw`,...
- input_audio_transcription: object (optional) — Configuration of the transcription model.

- turn_detection: object (4 fields) (optional) — Configuration for turn detection. Can be set to `null` to tu...

### RealtimeTranscriptionSessionCreateResponseGA
Type: object
Description: A Realtime transcription session configuration object.


- type: string (enum: transcription) (required) — The type of session. Always `transcription` for transcriptio...
- id: string (required) — Unique identifier for the session that looks like `sess_1234...
- object: string (required) — The object type. Always `realtime.transcription_session`.
- expires_at: integer (optional) — Expiration timestamp for the session, in seconds since epoch...
- include: array<string (enum: item.input_audio_transcription.logprobs)> (optional) — Additional fields to include in server outputs.
- `item.inpu...
- audio: object (1 fields) (optional) — Configuration for input audio for the session.


### RealtimeTruncation
Type: object
Description: Controls how the realtime conversation is truncated prior to model inference.
The default is `auto`.


(empty)

### RealtimeTurnDetection
Type: object

(empty)

### Reasoning
Type: object
Description: **gpt-5 and o-series models only**

Configuration options for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).


- effort: object (optional)
- summary: object (optional)
- generate_summary: object (optional)

### ReasoningEffort
Type: object

(empty)

### ReasoningItem
Type: object
Description: A description of the chain of thought used by a reasoning model while generating
a response. Be sure to include these items in your `input` to the Responses API
for subsequent turns of a conversation ...

- type: string (enum: reasoning) (required) — The type of the object. Always `reasoning`.

- id: string (required) — The unique identifier of the reasoning content.

- encrypted_content: object (optional)
- summary: array<object> (required) — Reasoning summary content.

- content: array<object> (optional) — Reasoning text content.

- status: string (enum: in_progress, completed, incomplete) (optional) — The status of the item. One of `in_progress`, `completed`, o...

### ReasoningTextContent
Type: object
Description: Reasoning text from the model.

- type: string (enum: reasoning_text) (required) — The type of the reasoning text. Always `reasoning_text`.
- text: string (required) — The reasoning text from the model.

### RefusalContent
Type: object
Description: A refusal from the model.

- type: string (enum: refusal) (required) — The type of the refusal. Always `refusal`.
- refusal: string (required) — The refusal explanation from the model.

### Response
Type: object

(empty)

### ResponseAudioDeltaEvent
Type: object
Description: Emitted when there is a partial audio response.

- type: string (enum: response.audio.delta) (required) — The type of the event. Always `response.audio.delta`.

- sequence_number: integer (required) — A sequence number for this chunk of the stream response.

- delta: string (required) — A chunk of Base64 encoded response audio bytes.


### ResponseAudioDoneEvent
Type: object
Description: Emitted when the audio response is complete.

- type: string (enum: response.audio.done) (required) — The type of the event. Always `response.audio.done`.

- sequence_number: integer (required) — The sequence number of the delta.


### ResponseAudioTranscriptDeltaEvent
Type: object
Description: Emitted when there is a partial transcript of audio.

- type: string (enum: response.audio.transcript.delta) (required) — The type of the event. Always `response.audio.transcript.del...
- delta: string (required) — The partial transcript of the audio response.

- sequence_number: integer (required) — The sequence number of this event.

### ResponseAudioTranscriptDoneEvent
Type: object
Description: Emitted when the full audio transcript is completed.

- type: string (enum: response.audio.transcript.done) (required) — The type of the event. Always `response.audio.transcript.don...
- sequence_number: integer (required) — The sequence number of this event.

### ResponseCodeInterpreterCallCodeDeltaEvent
Type: object
Description: Emitted when a partial code snippet is streamed by the code interpreter.

- type: string (enum: response.code_interpreter_call_code.delta) (required) — The type of the event. Always `response.code_interpreter_cal...
- output_index: integer (required) — The index of the output item in the response for which the c...
- item_id: string (required) — The unique identifier of the code interpreter tool call item...
- delta: string (required) — The partial code snippet being streamed by the code interpre...
- sequence_number: integer (required) — The sequence number of this event, used to order streaming e...

### ResponseCodeInterpreterCallCodeDoneEvent
Type: object
Description: Emitted when the code snippet is finalized by the code interpreter.

- type: string (enum: response.code_interpreter_call_code.done) (required) — The type of the event. Always `response.code_interpreter_cal...
- output_index: integer (required) — The index of the output item in the response for which the c...
- item_id: string (required) — The unique identifier of the code interpreter tool call item...
- code: string (required) — The final code snippet output by the code interpreter.
- sequence_number: integer (required) — The sequence number of this event, used to order streaming e...

### ResponseCodeInterpreterCallCompletedEvent
Type: object
Description: Emitted when the code interpreter call is completed.

- type: string (enum: response.code_interpreter_call.completed) (required) — The type of the event. Always `response.code_interpreter_cal...
- output_index: integer (required) — The index of the output item in the response for which the c...
- item_id: string (required) — The unique identifier of the code interpreter tool call item...
- sequence_number: integer (required) — The sequence number of this event, used to order streaming e...

### ResponseCodeInterpreterCallInProgressEvent
Type: object
Description: Emitted when a code interpreter call is in progress.

- type: string (enum: response.code_interpreter_call.in_progress) (required) — The type of the event. Always `response.code_interpreter_cal...
- output_index: integer (required) — The index of the output item in the response for which the c...
- item_id: string (required) — The unique identifier of the code interpreter tool call item...
- sequence_number: integer (required) — The sequence number of this event, used to order streaming e...

### ResponseCodeInterpreterCallInterpretingEvent
Type: object
Description: Emitted when the code interpreter is actively interpreting the code snippet.

- type: string (enum: response.code_interpreter_call.interpreting) (required) — The type of the event. Always `response.code_interpreter_cal...
- output_index: integer (required) — The index of the output item in the response for which the c...
- item_id: string (required) — The unique identifier of the code interpreter tool call item...
- sequence_number: integer (required) — The sequence number of this event, used to order streaming e...

### ResponseCompletedEvent
Type: object
Description: Emitted when the model response is complete.

- type: string (enum: response.completed) (required) — The type of the event. Always `response.completed`.

- response: object (required) — Properties of the completed response.

- sequence_number: integer (required) — The sequence number for this event.

### ResponseContentPartAddedEvent
Type: object
Description: Emitted when a new content part is added.

- type: string (enum: response.content_part.added) (required) — The type of the event. Always `response.content_part.added`....
- item_id: string (required) — The ID of the output item that the content part was added to...
- output_index: integer (required) — The index of the output item that the content part was added...
- content_index: integer (required) — The index of the content part that was added.

- part: object (required) — The content part that was added.

- sequence_number: integer (required) — The sequence number of this event.

### ResponseContentPartDoneEvent
Type: object
Description: Emitted when a content part is done.

- type: string (enum: response.content_part.done) (required) — The type of the event. Always `response.content_part.done`.

- item_id: string (required) — The ID of the output item that the content part was added to...
- output_index: integer (required) — The index of the output item that the content part was added...
- content_index: integer (required) — The index of the content part that is done.

- sequence_number: integer (required) — The sequence number of this event.
- part: object (required) — The content part that is done.


### ResponseCreatedEvent
Type: object
Description: An event that is emitted when a response is created.


- type: string (enum: response.created) (required) — The type of the event. Always `response.created`.

- response: object (required) — The response that was created.

- sequence_number: integer (required) — The sequence number for this event.

### ResponseCustomToolCallInputDeltaEvent
Type: object
Description: Event representing a delta (partial update) to the input of a custom tool call.


- type: string (enum: response.custom_tool_call_input.delta) (required) — The event type identifier.
- sequence_number: integer (required) — The sequence number of this event.
- output_index: integer (required) — The index of the output this delta applies to.
- item_id: string (required) — Unique identifier for the API item associated with this even...
- delta: string (required) — The incremental input data (delta) for the custom tool call.

### ResponseCustomToolCallInputDoneEvent
Type: object
Description: Event indicating that input for a custom tool call is complete.


- type: string (enum: response.custom_tool_call_input.done) (required) — The event type identifier.
- sequence_number: integer (required) — The sequence number of this event.
- output_index: integer (required) — The index of the output this event applies to.
- item_id: string (required) — Unique identifier for the API item associated with this even...
- input: string (required) — The complete input data for the custom tool call.

### ResponseError
Type: object

(empty)

### ResponseErrorCode
Type: string
Description: The error code for the response.


string (enum: server_error, rate_limit_exceeded, invalid_prompt, vector_store_timeout, invalid_image...)

### ResponseErrorEvent
Type: object
Description: Emitted when an error occurs.

- type: string (enum: error) (required) — The type of the event. Always `error`.

- code: object (required)
- message: string (required) — The error message.

- param: object (required)
- sequence_number: integer (required) — The sequence number of this event.

### ResponseFailedEvent
Type: object
Description: An event that is emitted when a response fails.


- type: string (enum: response.failed) (required) — The type of the event. Always `response.failed`.

- sequence_number: integer (required) — The sequence number of this event.
- response: object (required) — The response that failed.


### ResponseFileSearchCallCompletedEvent
Type: object
Description: Emitted when a file search call is completed (results found).

- type: string (enum: response.file_search_call.completed) (required) — The type of the event. Always `response.file_search_call.com...
- output_index: integer (required) — The index of the output item that the file search call is in...
- item_id: string (required) — The ID of the output item that the file search call is initi...
- sequence_number: integer (required) — The sequence number of this event.

### ResponseFileSearchCallInProgressEvent
Type: object
Description: Emitted when a file search call is initiated.

- type: string (enum: response.file_search_call.in_progress) (required) — The type of the event. Always `response.file_search_call.in_...
- output_index: integer (required) — The index of the output item that the file search call is in...
- item_id: string (required) — The ID of the output item that the file search call is initi...
- sequence_number: integer (required) — The sequence number of this event.

### ResponseFileSearchCallSearchingEvent
Type: object
Description: Emitted when a file search is currently searching.

- type: string (enum: response.file_search_call.searching) (required) — The type of the event. Always `response.file_search_call.sea...
- output_index: integer (required) — The index of the output item that the file search call is se...
- item_id: string (required) — The ID of the output item that the file search call is initi...
- sequence_number: integer (required) — The sequence number of this event.

### ResponseFormatJsonObject
Type: object
Description: JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or...

- type: string (enum: json_object) (required) — The type of response format being defined. Always `json_obje...

### ResponseFormatJsonSchema
Type: object
Description: JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).


- type: string (enum: json_schema) (required) — The type of response format being defined. Always `json_sche...
- json_schema: object (4 fields) (required) — Structured Outputs configuration options, including a JSON S...

### ResponseFormatJsonSchemaSchema
Type: object
Description: The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).


(empty)

### ResponseFormatText
Type: object
Description: Default response format. Used to generate text responses.


- type: string (enum: text) (required) — The type of response format being defined. Always `text`.

### ResponseFormatTextGrammar
Type: object
Description: A custom grammar for the model to follow when generating text.
Learn more in the [custom grammars guide](https://platform.openai.com/docs/guides/custom-grammars).


- type: string (enum: grammar) (required) — The type of response format being defined. Always `grammar`.
- grammar: string (required) — The custom grammar for the model to follow.

### ResponseFormatTextPython
Type: object
Description: Configure the model to generate valid Python code. See the
[custom grammars guide](https://platform.openai.com/docs/guides/custom-grammars) for more details.


- type: string (enum: python) (required) — The type of response format being defined. Always `python`.

### ResponseFunctionCallArgumentsDeltaEvent
Type: object
Description: Emitted when there is a partial function-call arguments delta.

- type: string (enum: response.function_call_arguments.delta) (required) — The type of the event. Always `response.function_call_argume...
- item_id: string (required) — The ID of the output item that the function-call arguments d...
- output_index: integer (required) — The index of the output item that the function-call argument...
- sequence_number: integer (required) — The sequence number of this event.
- delta: string (required) — The function-call arguments delta that is added.


### ResponseFunctionCallArgumentsDoneEvent
Type: object
Description: Emitted when function-call arguments are finalized.

- type: string (enum: response.function_call_arguments.done) (required)
- item_id: string (required) — The ID of the item.
- name: string (required) — The name of the function that was called.
- output_index: integer (required) — The index of the output item.
- sequence_number: integer (required) — The sequence number of this event.
- arguments: string (required) — The function-call arguments.

### ResponseImageGenCallCompletedEvent
Type: object
Description: Emitted when an image generation tool call has completed and the final image is available.


- type: string (enum: response.image_generation_call.completed) (required) — The type of the event. Always 'response.image_generation_cal...
- output_index: integer (required) — The index of the output item in the response's output array.
- sequence_number: integer (required) — The sequence number of this event.
- item_id: string (required) — The unique identifier of the image generation item being pro...

### ResponseImageGenCallGeneratingEvent
Type: object
Description: Emitted when an image generation tool call is actively generating an image (intermediate state).


- type: string (enum: response.image_generation_call.generating) (required) — The type of the event. Always 'response.image_generation_cal...
- output_index: integer (required) — The index of the output item in the response's output array.
- item_id: string (required) — The unique identifier of the image generation item being pro...
- sequence_number: integer (required) — The sequence number of the image generation item being proce...

### ResponseImageGenCallInProgressEvent
Type: object
Description: Emitted when an image generation tool call is in progress.


- type: string (enum: response.image_generation_call.in_progress) (required) — The type of the event. Always 'response.image_generation_cal...
- output_index: integer (required) — The index of the output item in the response's output array.
- item_id: string (required) — The unique identifier of the image generation item being pro...
- sequence_number: integer (required) — The sequence number of the image generation item being proce...

### ResponseImageGenCallPartialImageEvent
Type: object
Description: Emitted when a partial image is available during image generation streaming.


- type: string (enum: response.image_generation_call.partial_image) (required) — The type of the event. Always 'response.image_generation_cal...
- output_index: integer (required) — The index of the output item in the response's output array.
- item_id: string (required) — The unique identifier of the image generation item being pro...
- sequence_number: integer (required) — The sequence number of the image generation item being proce...
- partial_image_index: integer (required) — 0-based index for the partial image (backend is 1-based, but...
- partial_image_b64: string (required) — Base64-encoded partial image data, suitable for rendering as...

### ResponseInProgressEvent
Type: object
Description: Emitted when the response is in progress.

- type: string (enum: response.in_progress) (required) — The type of the event. Always `response.in_progress`.

- response: object (required) — The response that is in progress.

- sequence_number: integer (required) — The sequence number of this event.

### ResponseIncompleteEvent
Type: object
Description: An event that is emitted when a response finishes as incomplete.


- type: string (enum: response.incomplete) (required) — The type of the event. Always `response.incomplete`.

- response: object (required) — The response that was incomplete.

- sequence_number: integer (required) — The sequence number of this event.

### ResponseItemList
Type: object
Description: A list of Response items.

- object: object (required) — The type of object returned, must be `list`.
- data: array<object> (required) — A list of items used to generate this response.
- has_more: boolean (required) — Whether there are more items available.
- first_id: string (required) — The ID of the first item in the list.
- last_id: string (required) — The ID of the last item in the list.

### ResponseLogProb
Type: object
Description: A logprob is the logarithmic probability that the model assigns to producing 
a particular token at a given position in the sequence. Less-negative (higher) 
logprob values indicate greater model conf...

- token: string (required) — A possible text token.
- logprob: number (required) — The log probability of this token.

- top_logprobs: array<object (2 fields)> (optional) — The log probability of the top 20 most likely tokens.


### ResponseMCPCallArgumentsDeltaEvent
Type: object
Description: Emitted when there is a delta (partial update) to the arguments of an MCP tool call.


- type: string (enum: response.mcp_call_arguments.delta) (required) — The type of the event. Always 'response.mcp_call_arguments.d...
- output_index: integer (required) — The index of the output item in the response's output array.
- item_id: string (required) — The unique identifier of the MCP tool call item being proces...
- delta: string (required) — A JSON string containing the partial update to the arguments...
- sequence_number: integer (required) — The sequence number of this event.

### ResponseMCPCallArgumentsDoneEvent
Type: object
Description: Emitted when the arguments for an MCP tool call are finalized.


- type: string (enum: response.mcp_call_arguments.done) (required) — The type of the event. Always 'response.mcp_call_arguments.d...
- output_index: integer (required) — The index of the output item in the response's output array.
- item_id: string (required) — The unique identifier of the MCP tool call item being proces...
- arguments: string (required) — A JSON string containing the finalized arguments for the MCP...
- sequence_number: integer (required) — The sequence number of this event.

### ResponseMCPCallCompletedEvent
Type: object
Description: Emitted when an MCP  tool call has completed successfully.


- type: string (enum: response.mcp_call.completed) (required) — The type of the event. Always 'response.mcp_call.completed'.
- item_id: string (required) — The ID of the MCP tool call item that completed.
- output_index: integer (required) — The index of the output item that completed.
- sequence_number: integer (required) — The sequence number of this event.

### ResponseMCPCallFailedEvent
Type: object
Description: Emitted when an MCP  tool call has failed.


- type: string (enum: response.mcp_call.failed) (required) — The type of the event. Always 'response.mcp_call.failed'.
- item_id: string (required) — The ID of the MCP tool call item that failed.
- output_index: integer (required) — The index of the output item that failed.
- sequence_number: integer (required) — The sequence number of this event.

### ResponseMCPCallInProgressEvent
Type: object
Description: Emitted when an MCP  tool call is in progress.


- type: string (enum: response.mcp_call.in_progress) (required) — The type of the event. Always 'response.mcp_call.in_progress...
- sequence_number: integer (required) — The sequence number of this event.
- output_index: integer (required) — The index of the output item in the response's output array.
- item_id: string (required) — The unique identifier of the MCP tool call item being proces...

### ResponseMCPListToolsCompletedEvent
Type: object
Description: Emitted when the list of available MCP tools has been successfully retrieved.


- type: string (enum: response.mcp_list_tools.completed) (required) — The type of the event. Always 'response.mcp_list_tools.compl...
- item_id: string (required) — The ID of the MCP tool call item that produced this output.
- output_index: integer (required) — The index of the output item that was processed.
- sequence_number: integer (required) — The sequence number of this event.

### ResponseMCPListToolsFailedEvent
Type: object
Description: Emitted when the attempt to list available MCP tools has failed.


- type: string (enum: response.mcp_list_tools.failed) (required) — The type of the event. Always 'response.mcp_list_tools.faile...
- item_id: string (required) — The ID of the MCP tool call item that failed.
- output_index: integer (required) — The index of the output item that failed.
- sequence_number: integer (required) — The sequence number of this event.

### ResponseMCPListToolsInProgressEvent
Type: object
Description: Emitted when the system is in the process of retrieving the list of available MCP tools.


- type: string (enum: response.mcp_list_tools.in_progress) (required) — The type of the event. Always 'response.mcp_list_tools.in_pr...
- item_id: string (required) — The ID of the MCP tool call item that is being processed.
- output_index: integer (required) — The index of the output item that is being processed.
- sequence_number: integer (required) — The sequence number of this event.

### ResponseModalities
Type: object

(empty)

### ResponseOutputItemAddedEvent
Type: object
Description: Emitted when a new output item is added.

- type: string (enum: response.output_item.added) (required) — The type of the event. Always `response.output_item.added`.

- output_index: integer (required) — The index of the output item that was added.

- sequence_number: integer (required) — The sequence number of this event.

- item: object (required) — The output item that was added.


### ResponseOutputItemDoneEvent
Type: object
Description: Emitted when an output item is marked done.

- type: string (enum: response.output_item.done) (required) — The type of the event. Always `response.output_item.done`.

- output_index: integer (required) — The index of the output item that was marked done.

- sequence_number: integer (required) — The sequence number of this event.

- item: object (required) — The output item that was marked done.


### ResponseOutputText
Type: object
Description: Assistant response text accompanied by optional annotations.

- type: string (enum: output_text) (required) — Type discriminator that is always `output_text`.
- text: string (required) — Assistant generated text.
- annotations: array<object> (required) — Ordered list of annotations attached to the response text.

### ResponseOutputTextAnnotationAddedEvent
Type: object
Description: Emitted when an annotation is added to output text content.


- type: string (enum: response.output_text.annotation.added) (required) — The type of the event. Always 'response.output_text.annotati...
- item_id: string (required) — The unique identifier of the item to which the annotation is...
- output_index: integer (required) — The index of the output item in the response's output array.
- content_index: integer (required) — The index of the content part within the output item.
- annotation_index: integer (required) — The index of the annotation within the content part.
- sequence_number: integer (required) — The sequence number of this event.
- annotation: object (required) — The annotation object being added. (See annotation schema fo...

### ResponsePromptVariables
Type: object

(empty)

### ResponseProperties
Type: object

- previous_response_id: object (optional)
- model: object (optional) — Model ID used to generate the response, like `gpt-4o` or `o3...
- reasoning: object (optional)
- background: object (optional)
- max_output_tokens: object (optional)
- max_tool_calls: object (optional)
- text: object (2 fields) (optional) — Configuration options for a text response from the model. Ca...
- tools: array<object> (optional) — An array of tools the model may call while generating a resp...
- tool_choice: object (optional) — How the model should select which tool (or tools) to use whe...
- prompt: object (optional)
- truncation: object (optional)

### ResponseQueuedEvent
Type: object
Description: Emitted when a response is queued and waiting to be processed.


- type: string (enum: response.queued) (required) — The type of the event. Always 'response.queued'.
- response: object (required) — The full response object that is queued.
- sequence_number: integer (required) — The sequence number for this event.

### ResponseReasoningSummaryPartAddedEvent
Type: object
Description: Emitted when a new reasoning summary part is added.

- type: string (enum: response.reasoning_summary_part.added) (required) — The type of the event. Always `response.reasoning_summary_pa...
- item_id: string (required) — The ID of the item this summary part is associated with.

- output_index: integer (required) — The index of the output item this summary part is associated...
- summary_index: integer (required) — The index of the summary part within the reasoning summary.

- sequence_number: integer (required) — The sequence number of this event.

- part: object (2 fields) (required) — The summary part that was added.


### ResponseReasoningSummaryPartDoneEvent
Type: object
Description: Emitted when a reasoning summary part is completed.

- type: string (enum: response.reasoning_summary_part.done) (required) — The type of the event. Always `response.reasoning_summary_pa...
- item_id: string (required) — The ID of the item this summary part is associated with.

- output_index: integer (required) — The index of the output item this summary part is associated...
- summary_index: integer (required) — The index of the summary part within the reasoning summary.

- sequence_number: integer (required) — The sequence number of this event.

- part: object (2 fields) (required) — The completed summary part.


### ResponseReasoningSummaryTextDeltaEvent
Type: object
Description: Emitted when a delta is added to a reasoning summary text.

- type: string (enum: response.reasoning_summary_text.delta) (required) — The type of the event. Always `response.reasoning_summary_te...
- item_id: string (required) — The ID of the item this summary text delta is associated wit...
- output_index: integer (required) — The index of the output item this summary text delta is asso...
- summary_index: integer (required) — The index of the summary part within the reasoning summary.

- delta: string (required) — The text delta that was added to the summary.

- sequence_number: integer (required) — The sequence number of this event.


### ResponseReasoningSummaryTextDoneEvent
Type: object
Description: Emitted when a reasoning summary text is completed.

- type: string (enum: response.reasoning_summary_text.done) (required) — The type of the event. Always `response.reasoning_summary_te...
- item_id: string (required) — The ID of the item this summary text is associated with.

- output_index: integer (required) — The index of the output item this summary text is associated...
- summary_index: integer (required) — The index of the summary part within the reasoning summary.

- text: string (required) — The full text of the completed reasoning summary.

- sequence_number: integer (required) — The sequence number of this event.


### ResponseReasoningTextDeltaEvent
Type: object
Description: Emitted when a delta is added to a reasoning text.

- type: string (enum: response.reasoning_text.delta) (required) — The type of the event. Always `response.reasoning_text.delta...
- item_id: string (required) — The ID of the item this reasoning text delta is associated w...
- output_index: integer (required) — The index of the output item this reasoning text delta is as...
- content_index: integer (required) — The index of the reasoning content part this delta is associ...
- delta: string (required) — The text delta that was added to the reasoning content.

- sequence_number: integer (required) — The sequence number of this event.


### ResponseReasoningTextDoneEvent
Type: object
Description: Emitted when a reasoning text is completed.

- type: string (enum: response.reasoning_text.done) (required) — The type of the event. Always `response.reasoning_text.done`...
- item_id: string (required) — The ID of the item this reasoning text is associated with.

- output_index: integer (required) — The index of the output item this reasoning text is associat...
- content_index: integer (required) — The index of the reasoning content part.

- text: string (required) — The full text of the completed reasoning content.

- sequence_number: integer (required) — The sequence number of this event.


### ResponseRefusalDeltaEvent
Type: object
Description: Emitted when there is a partial refusal text.

- type: string (enum: response.refusal.delta) (required) — The type of the event. Always `response.refusal.delta`.

- item_id: string (required) — The ID of the output item that the refusal text is added to....
- output_index: integer (required) — The index of the output item that the refusal text is added ...
- content_index: integer (required) — The index of the content part that the refusal text is added...
- delta: string (required) — The refusal text that is added.

- sequence_number: integer (required) — The sequence number of this event.


### ResponseRefusalDoneEvent
Type: object
Description: Emitted when refusal text is finalized.

- type: string (enum: response.refusal.done) (required) — The type of the event. Always `response.refusal.done`.

- item_id: string (required) — The ID of the output item that the refusal text is finalized...
- output_index: integer (required) — The index of the output item that the refusal text is finali...
- content_index: integer (required) — The index of the content part that the refusal text is final...
- refusal: string (required) — The refusal text that is finalized.

- sequence_number: integer (required) — The sequence number of this event.


### ResponseStreamEvent
Type: object

(empty)

### ResponseStreamOptions
Type: object

(empty)

### ResponseTextDeltaEvent
Type: object
Description: Emitted when there is an additional text delta.

- type: string (enum: response.output_text.delta) (required) — The type of the event. Always `response.output_text.delta`.

- item_id: string (required) — The ID of the output item that the text delta was added to.

- output_index: integer (required) — The index of the output item that the text delta was added t...
- content_index: integer (required) — The index of the content part that the text delta was added ...
- delta: string (required) — The text delta that was added.

- sequence_number: integer (required) — The sequence number for this event.
- logprobs: array<object> (required) — The log probabilities of the tokens in the delta.


### ResponseTextDoneEvent
Type: object
Description: Emitted when text content is finalized.

- type: string (enum: response.output_text.done) (required) — The type of the event. Always `response.output_text.done`.

- item_id: string (required) — The ID of the output item that the text content is finalized...
- output_index: integer (required) — The index of the output item that the text content is finali...
- content_index: integer (required) — The index of the content part that the text content is final...
- text: string (required) — The text content that is finalized.

- sequence_number: integer (required) — The sequence number for this event.
- logprobs: array<object> (required) — The log probabilities of the tokens in the delta.


### ResponseUsage
Type: object
Description: Represents token usage details including input tokens, output tokens,
a breakdown of output tokens, and the total tokens used.


- input_tokens: integer (required) — The number of input tokens.
- input_tokens_details: object (1 fields) (required) — A detailed breakdown of the input tokens.
- output_tokens: integer (required) — The number of output tokens.
- output_tokens_details: object (1 fields) (required) — A detailed breakdown of the output tokens.
- total_tokens: integer (required) — The total number of tokens used.

### ResponseWebSearchCallCompletedEvent
Type: object
Description: Emitted when a web search call is completed.

- type: string (enum: response.web_search_call.completed) (required) — The type of the event. Always `response.web_search_call.comp...
- output_index: integer (required) — The index of the output item that the web search call is ass...
- item_id: string (required) — Unique ID for the output item associated with the web search...
- sequence_number: integer (required) — The sequence number of the web search call being processed.

### ResponseWebSearchCallInProgressEvent
Type: object
Description: Emitted when a web search call is initiated.

- type: string (enum: response.web_search_call.in_progress) (required) — The type of the event. Always `response.web_search_call.in_p...
- output_index: integer (required) — The index of the output item that the web search call is ass...
- item_id: string (required) — Unique ID for the output item associated with the web search...
- sequence_number: integer (required) — The sequence number of the web search call being processed.

### ResponseWebSearchCallSearchingEvent
Type: object
Description: Emitted when a web search call is executing.

- type: string (enum: response.web_search_call.searching) (required) — The type of the event. Always `response.web_search_call.sear...
- output_index: integer (required) — The index of the output item that the web search call is ass...
- item_id: string (required) — Unique ID for the output item associated with the web search...
- sequence_number: integer (required) — The sequence number of the web search call being processed.

### RunCompletionUsage
Type: object

(empty)

### RunGraderRequest
Type: object

- grader: object (required) — The grader used for the fine-tuning job.
- item: object (optional) — The dataset item provided to the grader. This will be used t...
- model_sample: string (required) — The model sample to be evaluated. This value will be used to...

### RunGraderResponse
Type: object

- reward: number (required)
- metadata: object (7 fields) (required)
- sub_rewards: object (required)
- model_grader_token_usage_per_model: object (required)

### RunObject
Type: object
Description: Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

- id: string (required) — The identifier, which can be referenced in API endpoints.
- object: string (enum: thread.run) (required) — The object type, which is always `thread.run`.
- created_at: integer (required) — The Unix timestamp (in seconds) for when the run was created...
- thread_id: string (required) — The ID of the [thread](https://platform.openai.com/docs/api-...
- assistant_id: string (required) — The ID of the [assistant](https://platform.openai.com/docs/a...
- status: object (required)
- required_action: object (2 fields) (required) — Details on the action required to continue the run. Will be ...
- last_error: object (2 fields) (required) — The last error associated with this run. Will be `null` if t...
- expires_at: integer (required) — The Unix timestamp (in seconds) for when the run will expire...
- started_at: integer (required) — The Unix timestamp (in seconds) for when the run was started...
- cancelled_at: integer (required) — The Unix timestamp (in seconds) for when the run was cancell...
- failed_at: integer (required) — The Unix timestamp (in seconds) for when the run failed.
- completed_at: integer (required) — The Unix timestamp (in seconds) for when the run was complet...
- incomplete_details: object (1 fields) (required) — Details on why the run is incomplete. Will be `null` if the ...
- model: string (required) — The model that the [assistant](https://platform.openai.com/d...
- instructions: string (required) — The instructions that the [assistant](https://platform.opena...
- tools: array<object> (required) — The list of tools that the [assistant](https://platform.open...
- metadata: object (required)
- usage: object (required)
- temperature: number (optional) — The sampling temperature used for this run. If not set, defa...
- top_p: number (optional) — The nucleus sampling value used for this run. If not set, de...
- max_prompt_tokens: integer (required) — The maximum number of prompt tokens specified to have been u...
- max_completion_tokens: integer (required) — The maximum number of completion tokens specified to have be...
- truncation_strategy: object (required)
- tool_choice: object (required)
- parallel_tool_calls: object (required)
- response_format: object (required)

### RunStatus
Type: string
Description: The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

string (enum: queued, in_progress, requires_action, cancelling, cancelled...)

### RunStepCompletionUsage
Type: object

(empty)

### RunStepDeltaObject
Type: object
Description: Represents a run step delta i.e. any changed fields on a run step during streaming.


- id: string (required) — The identifier of the run step, which can be referenced in A...
- object: string (enum: thread.run.step.delta) (required) — The object type, which is always `thread.run.step.delta`.
- delta: object (required)

### RunStepDeltaObjectDelta
Type: object
Description: The delta containing the fields that have changed on the run step.

- step_details: object (optional) — The details of the run step.

### RunStepDeltaStepDetailsMessageCreationObject
Type: object
Description: Details of the message creation by the run step.

- type: string (enum: message_creation) (required) — Always `message_creation`.
- message_creation: object (1 fields) (optional)

### RunStepDeltaStepDetailsToolCall
Type: object

(empty)

### RunStepDeltaStepDetailsToolCallsCodeObject
Type: object
Description: Details of the Code Interpreter tool call the run step was involved in.

- index: integer (required) — The index of the tool call in the tool calls array.
- id: string (optional) — The ID of the tool call.
- type: string (enum: code_interpreter) (required) — The type of tool call. This is always going to be `code_inte...
- code_interpreter: object (2 fields) (optional) — The Code Interpreter tool call definition.

### RunStepDeltaStepDetailsToolCallsCodeOutputImageObject
Type: object

- index: integer (required) — The index of the output in the outputs array.
- type: string (enum: image) (required) — Always `image`.
- image: object (1 fields) (optional)

### RunStepDeltaStepDetailsToolCallsCodeOutputLogsObject
Type: object
Description: Text output from the Code Interpreter tool call as part of a run step.

- index: integer (required) — The index of the output in the outputs array.
- type: string (enum: logs) (required) — Always `logs`.
- logs: string (optional) — The text output from the Code Interpreter tool call.

### RunStepDeltaStepDetailsToolCallsFileSearchObject
Type: object

- index: integer (required) — The index of the tool call in the tool calls array.
- id: string (optional) — The ID of the tool call object.
- type: string (enum: file_search) (required) — The type of tool call. This is always going to be `file_sear...
- file_search: object (required) — For now, this is always going to be an empty object.

### RunStepDeltaStepDetailsToolCallsFunctionObject
Type: object

- index: integer (required) — The index of the tool call in the tool calls array.
- id: string (optional) — The ID of the tool call object.
- type: string (enum: function) (required) — The type of tool call. This is always going to be `function`...
- function: object (3 fields) (optional) — The definition of the function that was called.

### RunStepDeltaStepDetailsToolCallsObject
Type: object
Description: Details of the tool call.

- type: string (enum: tool_calls) (required) — Always `tool_calls`.
- tool_calls: array<object> (optional) — An array of tool calls the run step was involved in. These c...

### RunStepDetailsMessageCreationObject
Type: object
Description: Details of the message creation by the run step.

- type: string (enum: message_creation) (required) — Always `message_creation`.
- message_creation: object (1 fields) (required)

### RunStepDetailsToolCall
Type: object

(empty)

### RunStepDetailsToolCallsCodeObject
Type: object
Description: Details of the Code Interpreter tool call the run step was involved in.

- id: string (required) — The ID of the tool call.
- type: string (enum: code_interpreter) (required) — The type of tool call. This is always going to be `code_inte...
- code_interpreter: object (2 fields) (required) — The Code Interpreter tool call definition.

### RunStepDetailsToolCallsCodeOutputImageObject
Type: object

- type: string (enum: image) (required) — Always `image`.
- image: object (1 fields) (required)

### RunStepDetailsToolCallsCodeOutputLogsObject
Type: object
Description: Text output from the Code Interpreter tool call as part of a run step.

- type: string (enum: logs) (required) — Always `logs`.
- logs: string (required) — The text output from the Code Interpreter tool call.

### RunStepDetailsToolCallsFileSearchObject
Type: object

- id: string (required) — The ID of the tool call object.
- type: string (enum: file_search) (required) — The type of tool call. This is always going to be `file_sear...
- file_search: object (2 fields) (required) — For now, this is always going to be an empty object.

### RunStepDetailsToolCallsFileSearchRankingOptionsObject
Type: object
Description: The ranking options for the file search.

- ranker: object (required)
- score_threshold: number (required) — The score threshold for the file search. All values must be ...

### RunStepDetailsToolCallsFileSearchResultObject
Type: object
Description: A result instance of the file search.

- file_id: string (required) — The ID of the file that result was found in.
- file_name: string (required) — The name of the file that result was found in.
- score: number (required) — The score of the result. All values must be a floating point...
- content: array<object (2 fields)> (optional) — The content of the result that was found. The content is onl...

### RunStepDetailsToolCallsFunctionObject
Type: object

- id: string (required) — The ID of the tool call object.
- type: string (enum: function) (required) — The type of tool call. This is always going to be `function`...
- function: object (3 fields) (required) — The definition of the function that was called.

### RunStepDetailsToolCallsObject
Type: object
Description: Details of the tool call.

- type: string (enum: tool_calls) (required) — Always `tool_calls`.
- tool_calls: array<object> (required) — An array of tool calls the run step was involved in. These c...

### RunStepObject
Type: object
Description: Represents a step in execution of a run.


- id: string (required) — The identifier of the run step, which can be referenced in A...
- object: string (enum: thread.run.step) (required) — The object type, which is always `thread.run.step`.
- created_at: integer (required) — The Unix timestamp (in seconds) for when the run step was cr...
- assistant_id: string (required) — The ID of the [assistant](https://platform.openai.com/docs/a...
- thread_id: string (required) — The ID of the [thread](https://platform.openai.com/docs/api-...
- run_id: string (required) — The ID of the [run](https://platform.openai.com/docs/api-ref...
- type: string (enum: message_creation, tool_calls) (required) — The type of run step, which can be either `message_creation`...
- status: string (enum: in_progress, cancelled, failed, completed, expired) (required) — The status of the run step, which can be either `in_progress...
- step_details: object (required) — The details of the run step.
- last_error: object (required)
- expired_at: object (required)
- cancelled_at: object (required)
- failed_at: object (required)
- completed_at: object (required)
- metadata: object (required)
- usage: object (required)

### RunStepStreamEvent
Type: object

(empty)

### RunStreamEvent
Type: object

(empty)

### RunToolCallObject
Type: object
Description: Tool call objects

- id: string (required) — The ID of the tool call. This ID must be referenced when you...
- type: string (enum: function) (required) — The type of tool call the output is required for. For now, t...
- function: object (2 fields) (required) — The function definition.

### Screenshot
Type: object
Description: A screenshot action.


- type: string (enum: screenshot) (required) — Specifies the event type. For a screenshot action, this prop...

### Scroll
Type: object
Description: A scroll action.


- type: string (enum: scroll) (required) — Specifies the event type. For a scroll action, this property...
- x: integer (required) — The x-coordinate where the scroll occurred.

- y: integer (required) — The y-coordinate where the scroll occurred.

- scroll_x: integer (required) — The horizontal scroll distance.

- scroll_y: integer (required) — The vertical scroll distance.


### SearchContextSize
Type: string

string (enum: low, medium, high)

### ServiceTier
Type: object

(empty)

### SpeechAudioDeltaEvent
Type: object
Description: Emitted for each chunk of audio data generated during speech synthesis.

- type: string (enum: speech.audio.delta) (required) — The type of the event. Always `speech.audio.delta`.

- audio: string (required) — A chunk of Base64-encoded audio data.


### SpeechAudioDoneEvent
Type: object
Description: Emitted when the speech synthesis is complete and all audio has been streamed.

- type: string (enum: speech.audio.done) (required) — The type of the event. Always `speech.audio.done`.

- usage: object (3 fields) (required) — Token usage statistics for the request.


### StaticChunkingStrategy
Type: object

- max_chunk_size_tokens: integer (required) — The maximum number of tokens in each chunk. The default valu...
- chunk_overlap_tokens: integer (required) — The number of tokens that overlap between chunks. The defaul...

### StaticChunkingStrategyRequestParam
Type: object
Description: Customize your own chunking strategy by setting chunk size and chunk overlap.

- type: string (enum: static) (required) — Always `static`.
- static: object (required)

### StaticChunkingStrategyResponseParam
Type: object

- type: string (enum: static) (required) — Always `static`.
- static: object (required)

### StopConfiguration
Type: object
Description: Not supported with latest reasoning models `o3` and `o4-mini`.

Up to 4 sequences where the API will stop generating further tokens. The
returned text will not contain the stop sequence.


(empty)

### SubmitToolOutputsRunRequest
Type: object

- tool_outputs: array<object (2 fields)> (required) — A list of tools for which the outputs are being submitted.
- stream: object (optional)

### SubmitToolOutputsRunRequestWithoutStream
Type: object

- tool_outputs: array<object (2 fields)> (required) — A list of tools for which the outputs are being submitted.

### Summary
Type: object
Description: A summary text from the model.

- type: string (enum: summary_text) (required) — The type of the object. Always `summary_text`.
- text: string (required) — A summary of the reasoning output from the model so far.

### SummaryTextContent
Type: object
Description: A summary text from the model.

- type: string (enum: summary_text) (required) — The type of the object. Always `summary_text`.
- text: string (required) — A summary of the reasoning output from the model so far.

### TaskGroupItem
Type: object
Description: Collection of workflow tasks grouped together in the thread.

- id: string (required) — Identifier of the thread item.
- object: string (enum: chatkit.thread_item) (required) — Type discriminator that is always `chatkit.thread_item`.
- created_at: integer (required) — Unix timestamp (in seconds) for when the item was created.
- thread_id: string (required) — Identifier of the parent thread.
- type: string (enum: chatkit.task_group) (required) — Type discriminator that is always `chatkit.task_group`.
- tasks: array<object> (required) — Tasks included in the group.

### TaskGroupTask
Type: object
Description: Task entry that appears within a TaskGroup.

- type: object (required) — Subtype for the grouped task.
- heading: object (required)
- summary: object (required)

### TaskItem
Type: object
Description: Task emitted by the workflow to show progress and status updates.

- id: string (required) — Identifier of the thread item.
- object: string (enum: chatkit.thread_item) (required) — Type discriminator that is always `chatkit.thread_item`.
- created_at: integer (required) — Unix timestamp (in seconds) for when the item was created.
- thread_id: string (required) — Identifier of the parent thread.
- type: string (enum: chatkit.task) (required) — Type discriminator that is always `chatkit.task`.
- task_type: object (required) — Subtype for the task.
- heading: object (required)
- summary: object (required)

### TaskType
Type: string

string (enum: custom, thought)

### TextAnnotation
Type: object

(empty)

### TextAnnotationDelta
Type: object

(empty)

### TextContent
Type: object
Description: A text content.

- type: string (enum: text) (required)
- text: string (required)

### TextResponseFormatConfiguration
Type: object
Description: An object specifying the format that the model must output.

Configuring `{ "type": "json_schema" }` enables Structured Outputs, 
which ensures the model will match your supplied JSON schema. Learn mo...

(empty)

### TextResponseFormatJsonSchema
Type: object
Description: JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).


- type: string (enum: json_schema) (required) — The type of response format being defined. Always `json_sche...
- description: string (optional) — A description of what the response format is for, used by th...
- name: string (required) — The name of the response format. Must be a-z, A-Z, 0-9, or c...
- schema: object (required)
- strict: object (optional)

### ThreadItem
Type: object

(empty)

### ThreadItemListResource
Type: object
Description: A paginated list of thread items rendered for the ChatKit API.

- object: object (required) — The type of object returned, must be `list`.
- data: array<object> (required) — A list of items
- first_id: object (required)
- last_id: object (required)
- has_more: boolean (required) — Whether there are more items available.

### ThreadListResource
Type: object
Description: A paginated list of ChatKit threads.

- object: object (required) — The type of object returned, must be `list`.
- data: array<object> (required) — A list of items
- first_id: object (required)
- last_id: object (required)
- has_more: boolean (required) — Whether there are more items available.

### ThreadObject
Type: object
Description: Represents a thread that contains [messages](https://platform.openai.com/docs/api-reference/messages).

- id: string (required) — The identifier, which can be referenced in API endpoints.
- object: string (enum: thread) (required) — The object type, which is always `thread`.
- created_at: integer (required) — The Unix timestamp (in seconds) for when the thread was crea...
- tool_resources: object (required)
- metadata: object (required)

### ThreadResource
Type: object
Description: Represents a ChatKit thread and its current status.

- id: string (required) — Identifier of the thread.
- object: string (enum: chatkit.thread) (required) — Type discriminator that is always `chatkit.thread`.
- created_at: integer (required) — Unix timestamp (in seconds) for when the thread was created.
- title: object (required)
- status: object (required) — Current status for the thread. Defaults to `active` for newl...
- user: string (required) — Free-form string that identifies your end user who owns the ...

### ThreadStreamEvent
Type: object

(empty)

### ToggleCertificatesRequest
Type: object

- certificate_ids: array<string> (required)

### Tool
Type: object
Description: A tool that can be used to generate a response.


(empty)

### ToolChoice
Type: object
Description: Tool selection that the assistant should honor when executing the item.

- id: string (required) — Identifier of the requested tool.

### ToolChoiceAllowed
Type: object
Description: Constrains the tools available to the model to a pre-defined set.


- type: string (enum: allowed_tools) (required) — Allowed tool configuration type. Always `allowed_tools`.
- mode: string (enum: auto, required) (required) — Constrains the tools available to the model to a pre-defined...
- tools: array<object> (required) — A list of tool definitions that the model should be allowed ...

### ToolChoiceCustom
Type: object
Description: Use this option to force the model to call a specific custom tool.


- type: string (enum: custom) (required) — For custom tool calling, the type is always `custom`.
- name: string (required) — The name of the custom tool to call.

### ToolChoiceFunction
Type: object
Description: Use this option to force the model to call a specific function.


- type: string (enum: function) (required) — For function calling, the type is always `function`.
- name: string (required) — The name of the function to call.

### ToolChoiceMCP
Type: object
Description: Use this option to force the model to call a specific tool on a remote MCP server.


- type: string (enum: mcp) (required) — For MCP tools, the type is always `mcp`.
- server_label: string (required) — The label of the MCP server to use.

- name: object (optional)

### ToolChoiceOptions
Type: string
Description: Controls which (if any) tool is called by the model.

`none` means the model will not call any tool and instead generates a message.

`auto` means the model can pick between generating a message or ca...

string (enum: none, auto, required)

### ToolChoiceTypes
Type: object
Description: Indicates that the model should use a built-in tool to generate a response.
[Learn more about built-in tools](https://platform.openai.com/docs/guides/tools).


- type: string (enum: file_search, web_search_preview, computer_use_preview, web_search_preview_2025_03_11, image_generation...) (required) — The type of hosted tool the model should to use. Learn more ...

### TopLogProb
Type: object
Description: The top log probability of a token.

- token: string (required)
- logprob: number (required)
- bytes: array<integer> (required)

### TranscriptTextDeltaEvent
Type: object
Description: Emitted when there is an additional text delta. This is also the first event emitted when the transcription starts. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-...

- type: string (enum: transcript.text.delta) (required) — The type of the event. Always `transcript.text.delta`.

- delta: string (required) — The text delta that was additionally transcribed.

- logprobs: array<object (3 fields)> (optional) — The log probabilities of the delta. Only included if you [cr...

### TranscriptTextDoneEvent
Type: object
Description: Emitted when the transcription is complete. Contains the complete transcription text. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcr...

- type: string (enum: transcript.text.done) (required) — The type of the event. Always `transcript.text.done`.

- text: string (required) — The text that was transcribed.

- logprobs: array<object (3 fields)> (optional) — The log probabilities of the individual tokens in the transc...
- usage: object (optional)

### TranscriptTextUsageDuration
Type: object
Description: Usage statistics for models billed by audio input duration.

- type: string (enum: duration) (required) — The type of the usage object. Always `duration` for this var...
- seconds: number (required) — Duration of the input audio in seconds.

### TranscriptTextUsageTokens
Type: object
Description: Usage statistics for models billed by token usage.

- type: string (enum: tokens) (required) — The type of the usage object. Always `tokens` for this varia...
- input_tokens: integer (required) — Number of input tokens billed for this request.
- input_token_details: object (2 fields) (optional) — Details about the input tokens billed for this request.
- output_tokens: integer (required) — Number of output tokens generated.
- total_tokens: integer (required) — Total number of tokens used (input + output).

### TranscriptionChunkingStrategy
Type: object

(empty)

### TranscriptionInclude
Type: string

string (enum: logprobs)

### TranscriptionSegment
Type: object

- id: integer (required) — Unique identifier of the segment.
- seek: integer (required) — Seek offset of the segment.
- start: number (float) (required) — Start time of the segment in seconds.
- end: number (float) (required) — End time of the segment in seconds.
- text: string (required) — Text content of the segment.
- tokens: array<integer> (required) — Array of token IDs for the text content.
- temperature: number (float) (required) — Temperature parameter used for generating the segment.
- avg_logprob: number (float) (required) — Average logprob of the segment. If the value is lower than -...
- compression_ratio: number (float) (required) — Compression ratio of the segment. If the value is greater th...
- no_speech_prob: number (float) (required) — Probability of no speech in the segment. If the value is hig...

### TranscriptionWord
Type: object

- word: string (required) — The text content of the word.
- start: number (float) (required) — Start time of the word in seconds.
- end: number (float) (required) — End time of the word in seconds.

### TruncationObject
Type: object
Description: Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

- type: string (enum: auto, last_messages) (required) — The truncation strategy to use for the thread. The default i...
- last_messages: object (optional)

### Type
Type: object
Description: An action to type in text.


- type: string (enum: type) (required) — Specifies the event type. For a type action, this property i...
- text: string (required) — The text to type.


### UpdateConversationBody
Type: object

- metadata: object (required) — Set of 16 key-value pairs that can be attached to an object....

### UpdateVectorStoreFileAttributesRequest
Type: object

- attributes: object (required)

### UpdateVectorStoreRequest
Type: object

- name: string (optional) — The name of the vector store.
- expires_after: object (optional)
- metadata: object (optional)

### Upload
Type: object
Description: The Upload object can accept byte chunks in the form of Parts.


- id: string (required) — The Upload unique identifier, which can be referenced in API...
- created_at: integer (required) — The Unix timestamp (in seconds) for when the Upload was crea...
- filename: string (required) — The name of the file to be uploaded.
- bytes: integer (required) — The intended number of bytes to be uploaded.
- purpose: string (required) — The intended purpose of the file. [Please refer here](https:...
- status: string (enum: pending, completed, cancelled, expired) (required) — The status of the Upload.
- expires_at: integer (required) — The Unix timestamp (in seconds) for when the Upload will exp...
- object: string (enum: upload) (required) — The object type, which is always "upload".
- file: object (optional)

### UploadCertificateRequest
Type: object

- name: string (optional) — An optional name for the certificate
- content: string (required) — The certificate content in PEM format

### UploadFileBody
Type: object
Description: Parameters for uploading an attachment to the active ChatKit session.

- file: string (binary) (required) — Binary file contents to store with the ChatKit session. Supp...

### UploadPart
Type: object
Description: The upload Part represents a chunk of bytes we can add to an Upload object.


- id: string (required) — The upload Part unique identifier, which can be referenced i...
- created_at: integer (required) — The Unix timestamp (in seconds) for when the Part was create...
- upload_id: string (required) — The ID of the Upload object that this Part was added to.
- object: string (enum: upload.part) (required) — The object type, which is always `upload.part`.

### UrlAnnotation
Type: object
Description: Annotation that references a URL.

- type: string (enum: url) (required) — Type discriminator that is always `url` for this annotation.
- source: object (required) — URL referenced by the annotation.

### UrlAnnotationSource
Type: object
Description: URL backing an annotation entry.

- type: string (enum: url) (required) — Type discriminator that is always `url`.
- url: string (required) — URL referenced by the annotation.

### UrlCitationBody
Type: object
Description: A citation for a web resource used to generate a model response.

- type: string (enum: url_citation) (required) — The type of the URL citation. Always `url_citation`.
- url: string (required) — The URL of the web resource.
- start_index: integer (required) — The index of the first character of the URL citation in the ...
- end_index: integer (required) — The index of the last character of the URL citation in the m...
- title: string (required) — The title of the web resource.

### UsageAudioSpeechesResult
Type: object
Description: The aggregated audio speeches usage details of the specific time bucket.

- object: string (enum: organization.usage.audio_speeches.result) (required)
- characters: integer (required) — The number of characters processed.
- num_model_requests: integer (required) — The count of requests made to the model.
- project_id: object (optional)
- user_id: object (optional)
- api_key_id: object (optional)
- model: object (optional)

### UsageAudioTranscriptionsResult
Type: object
Description: The aggregated audio transcriptions usage details of the specific time bucket.

- object: string (enum: organization.usage.audio_transcriptions.result) (required)
- seconds: integer (required) — The number of seconds processed.
- num_model_requests: integer (required) — The count of requests made to the model.
- project_id: object (optional)
- user_id: object (optional)
- api_key_id: object (optional)
- model: object (optional)

### UsageCodeInterpreterSessionsResult
Type: object
Description: The aggregated code interpreter sessions usage details of the specific time bucket.

- object: string (enum: organization.usage.code_interpreter_sessions.result) (required)
- num_sessions: integer (optional) — The number of code interpreter sessions.
- project_id: object (optional)

### UsageCompletionsResult
Type: object
Description: The aggregated completions usage details of the specific time bucket.

- object: string (enum: organization.usage.completions.result) (required)
- input_tokens: integer (required) — The aggregated number of text input tokens used, including c...
- input_cached_tokens: integer (optional) — The aggregated number of text input tokens that has been cac...
- output_tokens: integer (required) — The aggregated number of text output tokens used. For custom...
- input_audio_tokens: integer (optional) — The aggregated number of audio input tokens used, including ...
- output_audio_tokens: integer (optional) — The aggregated number of audio output tokens used.
- num_model_requests: integer (required) — The count of requests made to the model.
- project_id: object (optional)
- user_id: object (optional)
- api_key_id: object (optional)
- model: object (optional)
- batch: object (optional)

### UsageEmbeddingsResult
Type: object
Description: The aggregated embeddings usage details of the specific time bucket.

- object: string (enum: organization.usage.embeddings.result) (required)
- input_tokens: integer (required) — The aggregated number of input tokens used.
- num_model_requests: integer (required) — The count of requests made to the model.
- project_id: object (optional)
- user_id: object (optional)
- api_key_id: object (optional)
- model: object (optional)

### UsageImagesResult
Type: object
Description: The aggregated images usage details of the specific time bucket.

- object: string (enum: organization.usage.images.result) (required)
- images: integer (required) — The number of images processed.
- num_model_requests: integer (required) — The count of requests made to the model.
- source: object (optional)
- size: object (optional)
- project_id: object (optional)
- user_id: object (optional)
- api_key_id: object (optional)
- model: object (optional)

### UsageModerationsResult
Type: object
Description: The aggregated moderations usage details of the specific time bucket.

- object: string (enum: organization.usage.moderations.result) (required)
- input_tokens: integer (required) — The aggregated number of input tokens used.
- num_model_requests: integer (required) — The count of requests made to the model.
- project_id: object (optional)
- user_id: object (optional)
- api_key_id: object (optional)
- model: object (optional)

### UsageResponse
Type: object

- object: string (enum: page) (required)
- data: array<object> (required)
- has_more: boolean (required)
- next_page: string (required)

### UsageTimeBucket
Type: object

- object: string (enum: bucket) (required)
- start_time: integer (required)
- end_time: integer (required)
- result: array<object> (required)

### UsageVectorStoresResult
Type: object
Description: The aggregated vector stores usage details of the specific time bucket.

- object: string (enum: organization.usage.vector_stores.result) (required)
- usage_bytes: integer (required) — The vector stores usage in bytes.
- project_id: object (optional)

### User
Type: object
Description: Represents an individual `user` within an organization.

- object: string (enum: organization.user) (required) — The object type, which is always `organization.user`
- id: string (required) — The identifier, which can be referenced in API endpoints
- name: string (required) — The name of the user
- email: string (required) — The email address of the user
- role: string (enum: owner, reader) (required) — `owner` or `reader`
- added_at: integer (required) — The Unix timestamp (in seconds) of when the user was added.

### UserDeleteResponse
Type: object

- object: string (enum: organization.user.deleted) (required)
- id: string (required)
- deleted: boolean (required)

### UserListResponse
Type: object

- object: string (enum: list) (required)
- data: array<object> (required)
- first_id: string (required)
- last_id: string (required)
- has_more: boolean (required)

### UserMessageInputText
Type: object
Description: Text block that a user contributed to the thread.

- type: string (enum: input_text) (required) — Type discriminator that is always `input_text`.
- text: string (required) — Plain-text content supplied by the user.

### UserMessageItem
Type: object
Description: User-authored messages within a thread.

- id: string (required) — Identifier of the thread item.
- object: string (enum: chatkit.thread_item) (required) — Type discriminator that is always `chatkit.thread_item`.
- created_at: integer (required) — Unix timestamp (in seconds) for when the item was created.
- thread_id: string (required) — Identifier of the parent thread.
- type: string (enum: chatkit.user_message) (required)
- content: array<object> (required) — Ordered content elements supplied by the user.
- attachments: array<object> (required) — Attachments associated with the user message. Defaults to an...
- inference_options: object (required)

### UserMessageQuotedText
Type: object
Description: Quoted snippet that the user referenced in their message.

- type: string (enum: quoted_text) (required) — Type discriminator that is always `quoted_text`.
- text: string (required) — Quoted text content.

### UserRoleUpdateRequest
Type: object

- role: string (enum: owner, reader) (required) — `owner` or `reader`

### VadConfig
Type: object

- type: string (enum: server_vad) (required) — Must be set to `server_vad` to enable manual chunking using ...
- prefix_padding_ms: integer (optional) — Amount of audio to include before the VAD detected speech (i...
- silence_duration_ms: integer (optional) — Duration of silence to detect speech stop (in milliseconds)....
- threshold: number (optional) — Sensitivity threshold (0.0 to 1.0) for voice activity detect...

### ValidateGraderRequest
Type: object

- grader: object (required) — The grader used for the fine-tuning job.

### ValidateGraderResponse
Type: object

- grader: object (optional) — The grader used for the fine-tuning job.

### VectorStoreExpirationAfter
Type: object
Description: The expiration policy for a vector store.

- anchor: string (enum: last_active_at) (required) — Anchor timestamp after which the expiration policy applies. ...
- days: integer (required) — The number of days after the anchor time that the vector sto...

### VectorStoreFileAttributes
Type: object

(empty)

### VectorStoreFileBatchObject
Type: object
Description: A batch of files attached to a vector store.

- id: string (required) — The identifier, which can be referenced in API endpoints.
- object: string (enum: vector_store.files_batch) (required) — The object type, which is always `vector_store.file_batch`.
- created_at: integer (required) — The Unix timestamp (in seconds) for when the vector store fi...
- vector_store_id: string (required) — The ID of the [vector store](https://platform.openai.com/doc...
- status: string (enum: in_progress, completed, cancelled, failed) (required) — The status of the vector store files batch, which can be eit...
- file_counts: object (5 fields) (required)

### VectorStoreFileContentResponse
Type: object
Description: Represents the parsed content of a vector store file.

- object: string (enum: vector_store.file_content.page) (required) — The object type, which is always `vector_store.file_content....
- data: array<object (2 fields)> (required) — Parsed content of the file.
- has_more: boolean (required) — Indicates if there are more content pages to fetch.
- next_page: object (required)

### VectorStoreFileObject
Type: object
Description: A list of files attached to a vector store.

- id: string (required) — The identifier, which can be referenced in API endpoints.
- object: string (enum: vector_store.file) (required) — The object type, which is always `vector_store.file`.
- usage_bytes: integer (required) — The total vector store usage in bytes. Note that this may be...
- created_at: integer (required) — The Unix timestamp (in seconds) for when the vector store fi...
- vector_store_id: string (required) — The ID of the [vector store](https://platform.openai.com/doc...
- status: string (enum: in_progress, completed, cancelled, failed) (required) — The status of the vector store file, which can be either `in...
- last_error: object (required)
- chunking_strategy: object (optional)
- attributes: object (optional)

### VectorStoreObject
Type: object
Description: A vector store is a collection of processed files can be used by the `file_search` tool.

- id: string (required) — The identifier, which can be referenced in API endpoints.
- object: string (enum: vector_store) (required) — The object type, which is always `vector_store`.
- created_at: integer (required) — The Unix timestamp (in seconds) for when the vector store wa...
- name: string (required) — The name of the vector store.
- usage_bytes: integer (required) — The total number of bytes used by the files in the vector st...
- file_counts: object (5 fields) (required)
- status: string (enum: expired, in_progress, completed) (required) — The status of the vector store, which can be either `expired...
- expires_after: object (optional)
- expires_at: object (optional)
- last_active_at: object (required)
- metadata: object (required)

### VectorStoreSearchRequest
Type: object

- query: object (required) — A query string for a search
- rewrite_query: boolean (optional) — Whether to rewrite the natural language query for vector sea...
- max_num_results: integer (optional) — The maximum number of results to return. This number should ...
- filters: object (optional) — A filter to apply based on file attributes.
- ranking_options: object (2 fields) (optional) — Ranking options for search.

### VectorStoreSearchResultContentObject
Type: object

- type: string (enum: text) (required) — The type of content.
- text: string (required) — The text content returned from search.

### VectorStoreSearchResultItem
Type: object

- file_id: string (required) — The ID of the vector store file.
- filename: string (required) — The name of the vector store file.
- score: number (required) — The similarity score for the result.
- attributes: object (required)
- content: array<object> (required) — Content chunks from the file.

### VectorStoreSearchResultsPage
Type: object

- object: string (enum: vector_store.search_results.page) (required) — The object type, which is always `vector_store.search_result...
- search_query: array<string> (required)
- data: array<object> (required) — The list of search result items.
- has_more: boolean (required) — Indicates if there are more results to fetch.
- next_page: object (required)

### Verbosity
Type: object

(empty)

### VideoContentVariant
Type: string

string (enum: video, thumbnail, spritesheet)

### VideoListResource
Type: object

- object: object (required) — The type of object returned, must be `list`.
- data: array<object> (required) — A list of items
- first_id: object (required)
- last_id: object (required)
- has_more: boolean (required) — Whether there are more items available.

### VideoModel
Type: string

string (enum: sora-2, sora-2-pro)

### VideoResource
Type: object
Description: Structured information describing a generated video job.

- id: string (required) — Unique identifier for the video job.
- object: string (enum: video) (required) — The object type, which is always `video`.
- model: object (required) — The video generation model that produced the job.
- status: object (required) — Current lifecycle status of the video job.
- progress: integer (required) — Approximate completion percentage for the generation task.
- created_at: integer (required) — Unix timestamp (seconds) for when the job was created.
- completed_at: object (required)
- expires_at: object (required)
- size: object (required) — The resolution of the generated video.
- seconds: object (required) — Duration of the generated clip in seconds.
- remixed_from_video_id: object (required)
- error: object (required)

### VideoSeconds
Type: string

string (enum: 4, 8, 12)

### VideoSize
Type: string

string (enum: 720x1280, 1280x720, 1024x1792, 1792x1024)

### VideoStatus
Type: string

string (enum: queued, in_progress, completed, failed)

### VoiceIdsShared
Type: object

(empty)

### Wait
Type: object
Description: A wait action.


- type: string (enum: wait) (required) — Specifies the event type. For a wait action, this property i...

### WebSearchActionFind
Type: object
Description: Action type "find": Searches for a pattern within a loaded page.


- type: string (enum: find) (required) — The action type.

- url: string (uri) (required) — The URL of the page searched for the pattern.

- pattern: string (required) — The pattern or text to search for within the page.


### WebSearchActionOpenPage
Type: object
Description: Action type "open_page" - Opens a specific URL from search results.


- type: string (enum: open_page) (required) — The action type.

- url: string (uri) (required) — The URL opened by the model.


### WebSearchActionSearch
Type: object
Description: Action type "search" - Performs a web search query.


- type: string (enum: search) (required) — The action type.

- query: string (required) — The search query.

- sources: array<object (2 fields)> (optional) — The sources used in the search.


### WebSearchApproximateLocation
Type: object

(empty)

### WebSearchContextSize
Type: string
Description: High level guidance for the amount of context window space to use for the 
search. One of `low`, `medium`, or `high`. `medium` is the default.


string (enum: low, medium, high)

### WebSearchLocation
Type: object
Description: Approximate location parameters for the search.

- country: string (optional) — The two-letter 
[ISO country code](https://en.wikipedia.org/...
- region: string (optional) — Free text input for the region of the user, e.g. `California...
- city: string (optional) — Free text input for the city of the user, e.g. `San Francisc...
- timezone: string (optional) — The [IANA timezone](https://timeapi.io/documentation/iana-ti...

### WebSearchPreviewTool
Type: object
Description: This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

- type: string (enum: web_search_preview, web_search_preview_2025_03_11) (required) — The type of the web search tool. One of `web_search_preview`...
- user_location: object (optional)
- search_context_size: object (optional) — High level guidance for the amount of context window space t...

### WebSearchTool
Type: object
Description: Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).


- type: string (enum: web_search, web_search_2025_08_26) (required) — The type of the web search tool. One of `web_search` or `web...
- filters: object (optional)
- user_location: object (optional)
- search_context_size: string (enum: low, medium, high) (optional) — High level guidance for the amount of context window space t...

### WebSearchToolCall
Type: object
Description: The results of a web search tool call. See the 
[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.


- id: string (required) — The unique ID of the web search tool call.

- type: string (enum: web_search_call) (required) — The type of the web search tool call. Always `web_search_cal...
- status: string (enum: in_progress, searching, completed, failed) (required) — The status of the web search tool call.

- action: object (required) — An object describing the specific action taken in this web s...

### WebhookBatchCancelled
Type: object
Description: Sent when a batch API request has been cancelled.


- created_at: integer (required) — The Unix timestamp (in seconds) of when the batch API reques...
- id: string (required) — The unique ID of the event.

- data: object (1 fields) (required) — Event data payload.

- object: string (enum: event) (optional) — The object of the event. Always `event`.

- type: string (enum: batch.cancelled) (required) — The type of the event. Always `batch.cancelled`.


### WebhookBatchCompleted
Type: object
Description: Sent when a batch API request has been completed.


- created_at: integer (required) — The Unix timestamp (in seconds) of when the batch API reques...
- id: string (required) — The unique ID of the event.

- data: object (1 fields) (required) — Event data payload.

- object: string (enum: event) (optional) — The object of the event. Always `event`.

- type: string (enum: batch.completed) (required) — The type of the event. Always `batch.completed`.


### WebhookBatchExpired
Type: object
Description: Sent when a batch API request has expired.


- created_at: integer (required) — The Unix timestamp (in seconds) of when the batch API reques...
- id: string (required) — The unique ID of the event.

- data: object (1 fields) (required) — Event data payload.

- object: string (enum: event) (optional) — The object of the event. Always `event`.

- type: string (enum: batch.expired) (required) — The type of the event. Always `batch.expired`.


### WebhookBatchFailed
Type: object
Description: Sent when a batch API request has failed.


- created_at: integer (required) — The Unix timestamp (in seconds) of when the batch API reques...
- id: string (required) — The unique ID of the event.

- data: object (1 fields) (required) — Event data payload.

- object: string (enum: event) (optional) — The object of the event. Always `event`.

- type: string (enum: batch.failed) (required) — The type of the event. Always `batch.failed`.


### WebhookEvalRunCanceled
Type: object
Description: Sent when an eval run has been canceled.


- created_at: integer (required) — The Unix timestamp (in seconds) of when the eval run was can...
- id: string (required) — The unique ID of the event.

- data: object (1 fields) (required) — Event data payload.

- object: string (enum: event) (optional) — The object of the event. Always `event`.

- type: string (enum: eval.run.canceled) (required) — The type of the event. Always `eval.run.canceled`.


### WebhookEvalRunFailed
Type: object
Description: Sent when an eval run has failed.


- created_at: integer (required) — The Unix timestamp (in seconds) of when the eval run failed....
- id: string (required) — The unique ID of the event.

- data: object (1 fields) (required) — Event data payload.

- object: string (enum: event) (optional) — The object of the event. Always `event`.

- type: string (enum: eval.run.failed) (required) — The type of the event. Always `eval.run.failed`.


### WebhookEvalRunSucceeded
Type: object
Description: Sent when an eval run has succeeded.


- created_at: integer (required) — The Unix timestamp (in seconds) of when the eval run succeed...
- id: string (required) — The unique ID of the event.

- data: object (1 fields) (required) — Event data payload.

- object: string (enum: event) (optional) — The object of the event. Always `event`.

- type: string (enum: eval.run.succeeded) (required) — The type of the event. Always `eval.run.succeeded`.


### WebhookFineTuningJobCancelled
Type: object
Description: Sent when a fine-tuning job has been cancelled.


- created_at: integer (required) — The Unix timestamp (in seconds) of when the fine-tuning job ...
- id: string (required) — The unique ID of the event.

- data: object (1 fields) (required) — Event data payload.

- object: string (enum: event) (optional) — The object of the event. Always `event`.

- type: string (enum: fine_tuning.job.cancelled) (required) — The type of the event. Always `fine_tuning.job.cancelled`.


### WebhookFineTuningJobFailed
Type: object
Description: Sent when a fine-tuning job has failed.


- created_at: integer (required) — The Unix timestamp (in seconds) of when the fine-tuning job ...
- id: string (required) — The unique ID of the event.

- data: object (1 fields) (required) — Event data payload.

- object: string (enum: event) (optional) — The object of the event. Always `event`.

- type: string (enum: fine_tuning.job.failed) (required) — The type of the event. Always `fine_tuning.job.failed`.


### WebhookFineTuningJobSucceeded
Type: object
Description: Sent when a fine-tuning job has succeeded.


- created_at: integer (required) — The Unix timestamp (in seconds) of when the fine-tuning job ...
- id: string (required) — The unique ID of the event.

- data: object (1 fields) (required) — Event data payload.

- object: string (enum: event) (optional) — The object of the event. Always `event`.

- type: string (enum: fine_tuning.job.succeeded) (required) — The type of the event. Always `fine_tuning.job.succeeded`.


### WebhookRealtimeCallIncoming
Type: object
Description: Sent when Realtime API Receives a incoming SIP call.


- created_at: integer (required) — The Unix timestamp (in seconds) of when the model response w...
- id: string (required) — The unique ID of the event.

- data: object (2 fields) (required) — Event data payload.

- object: string (enum: event) (optional) — The object of the event. Always `event`.

- type: string (enum: realtime.call.incoming) (required) — The type of the event. Always `realtime.call.incoming`.


### WebhookResponseCancelled
Type: object
Description: Sent when a background response has been cancelled.


- created_at: integer (required) — The Unix timestamp (in seconds) of when the model response w...
- id: string (required) — The unique ID of the event.

- data: object (1 fields) (required) — Event data payload.

- object: string (enum: event) (optional) — The object of the event. Always `event`.

- type: string (enum: response.cancelled) (required) — The type of the event. Always `response.cancelled`.


### WebhookResponseCompleted
Type: object
Description: Sent when a background response has been completed.


- created_at: integer (required) — The Unix timestamp (in seconds) of when the model response w...
- id: string (required) — The unique ID of the event.

- data: object (1 fields) (required) — Event data payload.

- object: string (enum: event) (optional) — The object of the event. Always `event`.

- type: string (enum: response.completed) (required) — The type of the event. Always `response.completed`.


### WebhookResponseFailed
Type: object
Description: Sent when a background response has failed.


- created_at: integer (required) — The Unix timestamp (in seconds) of when the model response f...
- id: string (required) — The unique ID of the event.

- data: object (1 fields) (required) — Event data payload.

- object: string (enum: event) (optional) — The object of the event. Always `event`.

- type: string (enum: response.failed) (required) — The type of the event. Always `response.failed`.


### WebhookResponseIncomplete
Type: object
Description: Sent when a background response has been interrupted.


- created_at: integer (required) — The Unix timestamp (in seconds) of when the model response w...
- id: string (required) — The unique ID of the event.

- data: object (1 fields) (required) — Event data payload.

- object: string (enum: event) (optional) — The object of the event. Always `event`.

- type: string (enum: response.incomplete) (required) — The type of the event. Always `response.incomplete`.


### WidgetMessageItem
Type: object
Description: Thread item that renders a widget payload.

- id: string (required) — Identifier of the thread item.
- object: string (enum: chatkit.thread_item) (required) — Type discriminator that is always `chatkit.thread_item`.
- created_at: integer (required) — Unix timestamp (in seconds) for when the item was created.
- thread_id: string (required) — Identifier of the parent thread.
- type: string (enum: chatkit.widget) (required) — Type discriminator that is always `chatkit.widget`.
- widget: string (required) — Serialized widget payload rendered in the UI.

### WorkflowParam
Type: object
Description: Workflow reference and overrides applied to the chat session.

- id: string (required) — Identifier for the workflow invoked by the session.
- version: string (optional) — Specific workflow version to run. Defaults to the latest dep...
- state_variables: object (optional) — State variables forwarded to the workflow. Keys may be up to...
- tracing: object (optional) — Optional tracing overrides for the workflow invocation. When...

### WorkflowTracingParam
Type: object
Description: Controls diagnostic tracing during the session.

- enabled: boolean (optional) — Whether tracing is enabled during the session. Defaults to t...

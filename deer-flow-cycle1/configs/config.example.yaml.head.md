# First 200 lines of config.example.yaml

```yaml
# Configuration for the DeerFlow application
#
# Guidelines:
# - Copy this file to `config.yaml` and customize it for your environment
# - The default path of this configuration file is `config.yaml` in the project root.
#   You can set `DEER_FLOW_PROJECT_ROOT` to define that root explicitly, or use
#   `DEER_FLOW_CONFIG_PATH` to point at a specific config file.
# - Runtime state defaults to `.deer-flow` under the project root. Override it
#   with `DEER_FLOW_HOME` when you need a different writable data directory.
# - Set `DEER_FLOW_DATE_TIMEZONE` to an IANA timezone name (e.g. `Asia/Shanghai`)
#   when the conversation date injected into agents should follow a zone other
#   than the server's local timezone. It is read at runtime by the date-context
#   middlewares (not a config-schema field), so it can be set on a container
#   without mounting a `config.yaml`.
# - Environment variables are available for all field values. Example: `api_key: $OPENAI_API_KEY`
# - The `use` path is a string that looks like "package_name.sub_package_name.module_name:class_name/variable_name".

# ============================================================================
# Config Version (used to detect outdated config files)
# ============================================================================
# Bump this number when the config schema changes.
# Run `make config-upgrade` to merge new fields into your local config.yaml.
config_version: 58

# Optional operator-owned literal prompt extensions (see CONFIGURATION.md):
# lead_prompt_overlay:
#   prepend: "Apply our organization-wide writing conventions."
#   append: "End reports with a concise decision summary."
# Subagents: subagents.agents.<name>.prompt_overlay.{prepend,append}
# DeerMem: memory.backend_config.{prompt_prepend,prompt_append}

# Optional per-model request pacing (inside a models[] entry):
# request_admission:
#   requests_per_minute: 60
#   group: shared-provider-account  # optional; defaults to the model config name
#   max_wait_seconds: 300
#   max_queue_size: 256
# Off unless configured. Shared groups require identical settings; restart after
# changes. Process-local RPM only, not TPM or a cluster-wide quota. See the
# "Model request admission" section in backend/docs/CONFIGURATION.md.

# ============================================================================
# Logging
# ============================================================================
# Log level for deerflow modules (debug/info/warning/error)
log_level: info

# Trace ids are always issued and always returned in the `X-Trace-Id` response
# header; this block controls log output only — whether records carry a
# `trace_id` field, and in which format. Off by default because enabling it
# changes the log format. Restart required (see reload_boundary.py).
logging:
  enhance:
    enabled: false
    format: text

# ============================================================================
# Agent Extensions
# ============================================================================
# Optional AgentMiddleware classes loaded into the lead and subagent runtime
# middleware chains after built-in runtime middlewares, but before the
# safety/clarification tail. Missing packages, invalid classes, and broken
# modules fail at agent creation with an actionable import error; constructor
# errors fail at agent creation with the underlying exception.
# The same list applies to both lead and subagent runtimes; lead-only vs
# subagent-only configuration is not expressible yet. Each entry is a class
# path or `{class, kwargs}` for constructor arguments. kwargs values must be
# JSON types (object, array, string, number, boolean, or null); YAML dates
# and timestamps are coerced to ISO strings so they match JSON. Treat these
# files as trusted operator config because middleware classes execute code.
# Uncomment this block to define middlewares in config.yaml. Leaving it commented
# lets extensions_config.json remain the source of truth for this fixed-slot
# (not deprecated) middleware list. Packaged plugins use the `plugins:` block below.
# extensions:
#   middlewares:
#     - my_company.deerflow_middlewares:DomainGuardMiddleware
#     - class: my_company.deerflow_middlewares:LatencyStampingMiddleware
#       kwargs:
#         header: X-DeerFlow-Latency

# ============================================================================
# Tracing / Observability (Monocle)
# ============================================================================
# Optional agent tracing via Monocle. Configured through environment variables
# (MONOCLE_TRACING, MONOCLE_EXPORTERS, OKAHU_API_KEY — like LangSmith/Langfuse),
# not config.yaml keys, and OFF by default. See README.md → "Monocle Tracing"
# for setup, what each exporter captures, and where the trace data goes.

# ============================================================================
# Token Usage
# ============================================================================
# Enable token usage collection and display.
# When enabled, DeerFlow records input/output/total tokens per model call
# and shows usage metadata in the workspace UI when providers return it.
token_usage:
  enabled: true

# ============================================================================
# Token Budget — Per-run token limits
# ============================================================================
# Prevents runaway API costs by enforcing hard token limits per run.
# When warn_threshold is crossed, the agent receives an in-context warning.
# When hard_stop_threshold is crossed, tool_calls are stripped and the agent
# is forced to produce a final answer immediately.
token_budget:
  enabled: false                # Set to true to activate budget enforcement
  max_tokens: 200000            # Total token limit (input + output) per run
  max_input_tokens: null        # Optional separate input-only limit
  max_output_tokens: null       # Optional separate output-only limit
  warn_threshold: 0.8           # Warn at 80% of the budget
  hard_stop_threshold: 1.0      # Force stop at 100% of the budget

# ============================================================================
# Recursion Limits
# ============================================================================
# A run's recursion_limit caps the number of LangGraph super-steps (each is at
# least one LLM call). Clients may override the default per request; invalid or
# non-positive client values fall back to this configured default.
recursion_limit: 100

# The Gateway never trusts a configured or client-supplied value above this
# ceiling, preventing runaway API cost / DoS. Raise it only if you legitimately
# run very deeply nested subagent graphs.
max_recursion_limit: 1000


# ============================================================================
# Models Configuration
# ============================================================================
# Configure available LLM models for the agent to use.
#
# Two token fields look similar but mean different things:
# - `max_tokens` is the per-call OUTPUT cap passed to the provider.
# - `context_window` is a positive integer for the total context capacity
#   (prompt + completion). It drives the real-time "% context used" indicator
#   in the chat UI and feeds the model's langchain profile, which fraction-based
#   summarization triggers (`summarization.trigger: [{type: fraction, ...}]`)
#   resolve their thresholds from. Third-party OpenAI-compatible models carry no
#   built-in profile, so without `context_window` a fraction trigger degrades
#   (dropped with a warning) instead of crashing the agent build.
# Leave `context_window` unset if the provider limit is unknown; the percentage
# will not render. Verify configured values against the provider's model docs.
#
# Optional per-model pricing (powers the real-cost display on the workspace
# console). Add a `pricing` block to any model entry; use ONE currency across
# all models. Mixed currencies disable cost reporting to prevent invalid sums.
# Prices are per one million tokens.
#
#   pricing:
#     currency: CNY                    # ISO code shown in the console (CNY, USD, ...)
#     input_per_million: 8.0           # price per 1M input tokens (cache miss)
#     output_per_million: 32.0         # price per 1M output tokens
#     input_cache_hit_per_million: 0.8 # price per 1M cache-hit input tokens
#                                      # (optional; omit → hits billed at miss price)

models:
  # Example: Volcengine (Doubao) model
  # - name: doubao-seed-1.8
  #   display_name: Doubao-Seed-1.8
  #   use: deerflow.models.patched_deepseek:PatchedChatDeepSeek
  #   model: doubao-seed-1-8-251228
  #   api_base: https://ark.cn-beijing.volces.com/api/v3
  #   api_key: $VOLCENGINE_API_KEY
  #   timeout: 600.0
  #   max_retries: 2
  #   context_window: 262144     # Total prompt + completion capacity
  #   supports_thinking: true
  #   supports_vision: true
  #   supports_reasoning_effort: true
  #   when_thinking_enabled:
  #     extra_body:
  #       thinking:
  #         type: enabled
  #   when_thinking_disabled:
  #     extra_body:
  #       thinking:
  #         type: disabled

  # Example: Volcengine Coding Plan (one key, multi-vendor gateway)
  # The Coding Plan endpoint (/api/coding/v3) lets you access models from
  # Doubao, GLM, DeepSeek, Kimi, and MiniMax with a single API key.
  # Each model may differ in thinking/vision support - configure per-model.
  #
  # - name: glm-5.2-cp
  #   display_name: GLM-5.2 (Coding Plan)
  #   use: deerflow.models.patched_deepseek:PatchedChatDeepSeek
  #   model: glm-5.2
  #   api_base: https://ark.cn-beijing.volces.com/api/coding/v3
  #   api_key: $VOLCENGINE_API_KEY
  #   timeout: 600.0
  #   max_retries: 2
  #   supports_thinking: true
  #   supports_vision: false
  #   supports_reasoning_effort: true
  #   when_thinking_enabled:
  #     extra_body:
  #       thinking:
  #         type: enabled
  #   when_thinking_disabled:
  #     extra_body:
```

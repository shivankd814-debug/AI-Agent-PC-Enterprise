# Enterprise hardening roadmap

## Phase 1 — Core (this starter)
- API control plane, task records, approval records, audit events
- Local SQLite development database
- Safe tool registry and opt-in adapters

## Phase 2 — Production foundation
- PostgreSQL + Alembic migrations
- Redis + durable queue (Celery, Dramatiq or Temporal)
- OIDC/SSO, MFA, role-based and tenant-scoped authorization
- Vault/KMS-backed secrets, encryption at rest and in transit
- Structured logs, OpenTelemetry traces, metrics and alerting
- Backups, restore drills, rate limiting and request quotas

## Phase 3 — Agent runtime
- Planner/executor/verifier state machine
- Provider abstraction and model routing
- Retrieval-augmented memory with per-tenant access controls
- Sandboxed code execution and artifact scanning
- Human approval policies per tool and risk tier

## Phase 4 — Enterprise operations
- Admin console, team management, billing and usage metering
- Workflow versioning, retries, idempotency and dead-letter queues
- Red-team testing, threat model, penetration test and compliance review
- High availability, disaster recovery and load testing

## Non-negotiable controls
- No silent payments, publishing, messaging or destructive file operations.
- Require approval for externally visible or irreversible actions.
- Keep a complete audit trail and emergency stop.

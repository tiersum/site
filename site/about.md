# About TierSum

## Product Overview

TierSum is a **Hierarchical Summary Knowledge Base** — a RAG-free document retrieval system that preserves document structure through multi-layer abstraction and hot/cold document tiering, all at chapter granularity.

## Why TierSum

Most retrieval systems chop documents into small overlapping chunks and rely on similarity search, blurring structure and losing context. TierSum keeps a **clear hierarchy** — document overview, chapter-level summaries, and full source — plus a **tag and topic layer** so you navigate knowledge the way humans organize it, not the way embeddings shard it.

Hot and cold paths both respect chapter boundaries, not fixed-size fragments. Every retrieval returns **meaningful, complete sections**.

## What You Can Do

- **Search** — Natural language progressive query narrows *tags → documents → chapters*, like skimming an outline before opening the right section
- **Documents** — Ingest Markdown content. Hot docs get full LLM analysis per chapter; cold docs are indexed and retrieved the same way, at chapter granularity
- **Topics & Tags** — Browse auto-generated tags grouped into LLM-curated topics, keeping navigation meaningful as the library grows
- **Integrate** — Full REST API plus MCP protocol for AI agents and automation

## Who It Is For

Teams that live in Markdown: internal runbooks, architecture notes, support playbooks, research memos, and agent-facing knowledge. The same instance exposes a browser UI and programmatic access so humans and automation share one source of truth.

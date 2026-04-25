# About TierSum

## Product Overview

TierSum is a **Hierarchical Summary Knowledge Base** — a RAG-free document retrieval system powered by multi-layer abstraction and hot/cold document tiering.

## Why TierSum

Many retrieval systems split text into small overlapping chunks and rely mainly on similarity search. That can blur structure and lose context. TierSum keeps a **clear hierarchy**: document overview, chapter-level summaries, and original Markdown — plus a **tag and topic layer** so you navigate knowledge the way humans organize it, not the way embeddings shard it.

On the **hot path**, AI work runs **when documents are ingested**: LLM semantic chapter extraction produces tags, a document synopsis, and chapter-level summaries — the **pre-shaped layer** that **progressive query** reuses, narrowing *tags → documents → chapters* with LLM scoring at each hop, like skimming an outline before opening the right section. **Cold** documents use **Markdown syntax chapter extraction**: content is split by headings into natural chapters (not blind fixed-size fragments), indexed with BM25 inverted index + HNSW vector hybrid search, and returned **by whole chapters**. Both tiers share chapter-level granularity preserving semantic integrity. Ones that see heavy use can **promote** to hot when you want the full pre-shaped experience.

> **Chapter-first, hot or cold.** For *both* paths, TierSum treats **Markdown sections (chapters)** as the working unit — aligned with headings and document structure — instead of blind fixed-size fragments. Summaries, progressive narrowing, and cold search all respect those boundaries so **meaning stays intact end-to-end**.

## What You Can Do

- **Search** — Ask in natural language. **Progressive query** walks *tags → documents → chapters* the way a reader would skim an outline before opening a section: each step uses LLM relevance on top of **pre-built summaries and tags** where available, then can synthesize an answer with citations when configured.
- **Documents** — Ingest Markdown (and more over time). Hot docs get LLM summaries and tags per **chapter**; cold docs are indexed and retrieved the same way — **by chapter** — so every tier keeps coherent sections, not shredded text.
- **Topics & Tags** — Browse a shared catalog of tags grouped into *topics* (themes). Regroup refreshes those themes from your catalog so navigation stays meaningful as the library grows.

## Hot vs Cold (Plain Language)

The difference is *how much LLM work runs on ingest* — not the grain of your knowledge. **Hot and cold both stay chapter-centric:** retrieval, ranking, and what you read back are built on **whole markdown chapters**, preserving semantic integrity whether the doc is fully analyzed or cost-optimized.

- **Hot** documents use **LLM semantic chapter extraction**: chapter-level summaries and tags form the pre-shaped layer progressive query uses — narrowing *tags → documents → chapters* with LLM scoring at each hop.
- **Cold** documents use **Markdown syntax chapter extraction**: content is split by Markdown headings into natural chapters (not fixed-size chunks), indexed with BM25 inverted index + HNSW vector hybrid search. No LLM calls on ingest. Both tiers share chapter-level granularity preserving semantic integrity. Frequently used cold docs can be promoted toward hot automatically or manually.

## Who It Is For

Teams that live in Markdown: internal runbooks, architecture notes, support playbooks, research memos, and agent-facing knowledge. The same instance exposes a browser UI and programmatic access (REST and MCP) so humans and automation share one source of truth.

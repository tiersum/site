# TierSum

<div class="text-center mb-8">
  <p class="text-xl text-slate-400 mb-4">Your Knowledge, <strong class="text-slate-100">Hierarchically Organized</strong></p>
  <p class="text-slate-500 mb-6">TierSum is a RAG-free document retrieval system that preserves document structure through multi-layer abstraction. Hot documents get LLM semantic chapter extraction for progressive query; cold documents use Markdown syntax chapter extraction indexed with BM25 inverted + vector hybrid search. All at chapter granularity — not arbitrary chunks.</p>
  <div class="flex justify-center gap-4">
    <a href="/site/documentation" class="btn btn-primary">Get Started</a>
    <a href="/site/about" class="btn btn-outline border-slate-600">Learn More</a>
  </div>
</div>

---

## Why TierSum

Many retrieval systems split text into small overlapping chunks and rely mainly on similarity search. That can blur structure and lose context. TierSum keeps a **clear hierarchy**: document overview, chapter-level summaries, and original Markdown — plus a **tag and topic layer** so you navigate knowledge the way humans organize it, not the way embeddings shard it.

On the **hot path**, AI work runs **when documents are ingested**: LLM semantic chapter extraction produces tags, a document synopsis, and chapter-level summaries — the **pre-shaped layer** that **progressive query** reuses, narrowing *tags → documents → chapters* with LLM scoring at each hop, like skimming an outline before opening the right section. **Cold** documents use **Markdown syntax chapter extraction**: content is split by headings into natural chapters (not blind fixed-size fragments), indexed with BM25 inverted index + HNSW vector hybrid search, and returned **by whole chapters**. Both tiers share chapter-level granularity preserving semantic integrity. Ones that see heavy use can **promote** to hot when you want the full pre-shaped experience.

> **Chapter-first, hot or cold.** For *both* paths, TierSum treats **Markdown sections (chapters)** as the working unit — aligned with headings and document structure — instead of blind fixed-size fragments. Summaries, progressive narrowing, and cold search all respect those boundaries so **meaning stays intact end-to-end**.

---

## Features

### Chapter-First Document Processing

Traditional RAG systems split documents into arbitrary chunks, destroying structure and context. TierSum parses Markdown by headings, creating a natural chapter hierarchy that mirrors how humans write and read.

- Heading-aware splitting preserves document structure
- Configurable token budgets per chapter
- Sliding stride for long sections
- Stable path identifiers for every section

### Hot / Cold Tiering

Choose the right ingest path for each document, balancing query quality against cost. Both paths use **chapter-level granularity** — not fixed-size chunks — preserving semantic integrity end-to-end.

- **Hot**: LLM semantic chapter extraction — full LLM analysis producing summaries, tags, and chapter analysis that powers progressive query's multi-stage ranking (tags → documents → chapters)
- **Cold**: Markdown syntax chapter extraction — heading-based split into natural chapters, indexed with BM25 inverted index + HNSW vector hybrid search. No LLM calls on ingest
- Auto-promotion from cold to hot on frequent queries; also supports manual promotion

### Progressive Query

Instead of a single vector similarity search, TierSum uses a multi-stage pipeline that mimics how humans search: narrow by topic, then document, then section.

1. **Tag Filter** — Find relevant catalog tags from the query
2. **Document Rank** — Score matching documents with LLM relevance
3. **Chapter Select** — Pick top chapters from ranked documents
4. **Optional**: Synthesize answer with citations

### Topics & Tags

Auto-generated catalog tags grouped into LLM-curated topics. Navigate your knowledge the way humans organize it.

### Dual-Track Authentication

Separate authentication paths for humans and programs. Humans use browser sessions with passkey support. Programs use scoped API keys.

- Role-based access: viewer, user, admin
- API key scopes: read, write, admin
- Device tokens for persistent sessions
- Rate limiting and brute-force protection

### REST + MCP

Full REST API for integrations. MCP (Model Context Protocol) support for AI agents and automation workflows.

---

## How It Works

### 01 — Ingest

Upload Markdown documents. Choose hot (full LLM analysis) or cold (index-only) ingest mode.

### 02 — Index

Hot docs get chapter-level summaries and tags. Cold docs are split into chapters and indexed with BM25 + HNSW vector search. All preserve heading structure.

### 03 — Query

Ask in natural language. Progressive query walks tags → docs → chapters. Get synthesized answers with citations, or browse raw chapter hits.

---

## Tech Stack

| Technology | Purpose |
|-----------|---------|
| Go 1.23+ | Backend |
| Vue 3 | Frontend |
| SQLite / PostgreSQL | Database |
| Bleve + HNSW | Search |
| OpenAI / Claude / Ollama | LLM |
| Prometheus | Metrics |
| MCP | Protocol |
| Docker | Deploy |

---

## Quick Start

### 1. Prerequisites

- Go 1.23 or later
- Make
- OpenAI API key (or Anthropic, or local Ollama)

### 2. Installation

```bash
# Clone the repository
git clone https://github.com/tiersum/tiersum.git
cd tiersum

# Copy and edit configuration
cp configs/config.example.yaml configs/config.yaml
# Edit configs/config.yaml and set your LLM API key

# Build
make build

# Run
make run
```

### 3. Bootstrap

Open http://localhost:8080 in your browser. Complete the bootstrap wizard to create the first admin user.

> The bootstrap endpoint is only accessible from localhost by default for security.

### 4. First Document

Navigate to the Library page and click "Add Document". Paste Markdown content and choose an ingest mode:

- **Hot** — LLM semantic chapter extraction (full analysis with summaries, tags, progressive query support)
- **Cold** — Markdown syntax chapter extraction (heading-based split, BM25 + vector hybrid search; both at chapter granularity)

---

## License

Open Source under MIT License
# Agent Instructions — tiersum-site

## Project Type
Pure static site. No build step, no package manager, no test framework.

## Local Development
```bash
python3 -m http.server 8000
# Open http://localhost:8000
```

## Architecture
- `index.html` — Single-page Vue 3 app (CDN-loaded), serves as the site shell
- `site/*.md` — Content pages loaded dynamically via `fetch()`
- `site/*.zh.md` — Chinese variants (auto-selected by `navigator.language`)
- `deploy/nginx-tiersum.conf` — Production Nginx config

## Critical Rules

### 1. Navigation is Hard-Coded
Adding a new `site/*.md` file **requires** updating the `navItems` array in `index.html` (~line 217). There is no auto-discovery.

### 2. Nginx Location Order Matters
In `nginx-tiersum.conf`, the `.md$` location **must** come before the `[^/]+$` location. Otherwise Markdown files are misrouted to the SPA fallback.

```nginx
# CORRECT
location ~ ^/site/.+\.md$ { ... }
location ~ ^/site/[^/]+$ { ... }
```

### 3. No Restart Needed on Deploy
Static files are read from disk per-request. After `git pull`, changes are live immediately. Only reload Nginx if the `.conf` itself changes.

## Adding Content
1. Create `site/<page>.md` and `site/<page>.zh.md`
2. Add entry to `navItems` in `index.html`
3. Commit both files together

## Management UI
Links to `/ui/*` route to the separate **tiersum** Go backend (not this repo). This repo only handles the public marketing/docs site.

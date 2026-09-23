# Graph Report - bot-telegram  (2026-09-22)

## Corpus Check
- 11 files · ~1,985 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 87 nodes · 149 edges · 9 communities (7 shown, 2 thin omitted)
- Extraction: 85% EXTRACTED · 15% INFERRED · 0% AMBIGUOUS · INFERRED: 22 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `8e3ac871`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]

## God Nodes (most connected - your core abstractions)
1. `BotApp` - 19 edges
2. `Moderator` - 17 edges
3. `EventLogger` - 14 edges
4. `Update` - 12 edges
5. `DEFAULT_TYPE` - 11 edges
6. `Announcements` - 10 edges
7. `FaqHandler` - 10 edges
8. `nullforge — Telegram Moderator + FAQ Bot` - 10 edges
9. `TestModeration` - 9 edges
10. `match_faq()` - 7 edges

## Surprising Connections (you probably didn't know these)
- `_NullLogger` --uses--> `Moderator`  [INFERRED]
  tests/test_moderation.py → src/moderation.py
- `TestModeration` --uses--> `Moderator`  [INFERRED]
  tests/test_moderation.py → src/moderation.py
- `TestLogger` --uses--> `Moderator`  [INFERRED]
  tests/test_moderation.py → src/moderation.py
- `_NullLogger` --uses--> `EventLogger`  [INFERRED]
  tests/test_moderation.py → src/log.py
- `TestModeration` --uses--> `EventLogger`  [INFERRED]
  tests/test_moderation.py → src/log.py

## Communities (9 total, 2 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.13
Nodes (14): Arquitectura, code:bash (python -m venv .venv), code:bash (BOT_TOKEN=TU_TOKEN_AQUI python run.py), code:bash (PYTHONPATH=. .venv/Scripts/python.exe -m unittest discover -), code:block4 (run.py                 # entry point: carga config, lanza po), Comandos, Configuración, Contacto (+6 more)

### Community 1 - "Community 1"
Cohesion: 0.26
Nodes (5): load_config(), main(), DEFAULT_TYPE, BotApp, Update

### Community 3 - "Community 3"
Cohesion: 0.17
Nodes (5): bool, EventLogger, _NullLogger, TestLogger, TestModeration

### Community 7 - "Community 7"
Cohesion: 0.24
Nodes (3): _extract_domains(), Moderator, RateLimiter

### Community 8 - "Community 8"
Cohesion: 0.40
Nodes (4): Guion de video-demo (screen recording, sin voz, ~2 min), Post, Preparación (una sola vez, requiere dueño), Toma única (seguir en orden, ~2 min)

## Knowledge Gaps
- **12 isolated node(s):** `Funcionalidades`, `Stack`, `code:bash (python -m venv .venv)`, `code:bash (BOT_TOKEN=TU_TOKEN_AQUI python run.py)`, `code:bash (PYTHONPATH=. .venv/Scripts/python.exe -m unittest discover -)` (+7 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Moderator` connect `Community 7` to `Community 1`, `Community 2`, `Community 3`?**
  _High betweenness centrality (0.196) - this node is a cross-community bridge._
- **Why does `BotApp` connect `Community 1` to `Community 2`, `Community 3`, `Community 7`?**
  _High betweenness centrality (0.151) - this node is a cross-community bridge._
- **Why does `EventLogger` connect `Community 3` to `Community 1`, `Community 2`?**
  _High betweenness centrality (0.109) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `BotApp` (e.g. with `Announcements` and `FaqHandler`) actually correct?**
  _`BotApp` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `Moderator` (e.g. with `BotApp` and `Update`) actually correct?**
  _`Moderator` has 7 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `EventLogger` (e.g. with `BotApp` and `Update`) actually correct?**
  _`EventLogger` has 7 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `Update` (e.g. with `Announcements` and `FaqHandler`) actually correct?**
  _`Update` has 4 INFERRED edges - model-reasoned connections that need verification._
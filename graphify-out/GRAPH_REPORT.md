# Graph Report - negocio_kmi  (2026-09-22)

## Corpus Check
- 21 files · ~5,260 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 144 nodes · 156 edges · 18 communities
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 4 edges (avg confidence: 0.57)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `8867836e`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]

## God Nodes (most connected - your core abstractions)
1. `Moderator` - 9 edges
2. `FaqEngine` - 8 edges
3. `Germany Builds: Why Solana's Fastest-Growing Builder Ecosystem in Europe Is in Berlin, Not Berlin's Banks` - 8 edges
4. `cmd_announce()` - 7 edges
5. `build_app()` - 7 edges
6. `AGENTS.md — INSTRUCCIONES PERMANENTES (Worker: Kimi K3 v opencode)` - 7 edges
7. `Bot Telegram — Moderación + FAQ con IA (v1)` - 7 edges
8. `MISIÓN — Negocio autónomo de servicios crypto/Web3` - 7 edges
9. `EventLogger` - 6 edges
10. `NEGOCIO — Guía del dueño (15 minutos por semana)` - 6 edges

## Surprising Connections (you probably didn't know these)
- `main()` --calls--> `build_app()`  [INFERRED]
  productos/bot-telegram/run.py → productos/bot-telegram/src/bot.py
- `Application` --uses--> `Moderator`  [INFERRED]
  productos/bot-telegram/src/bot.py → productos/bot-telegram/src/moderation.py
- `build_app()` --calls--> `cmd_announce()`  [EXTRACTED]
  productos/bot-telegram/src/bot.py → productos/bot-telegram/src/announce.py
- `build_app()` --calls--> `Moderator`  [EXTRACTED]
  productos/bot-telegram/src/bot.py → productos/bot-telegram/src/moderation.py
- `Application` --uses--> `FaqEngine`  [INFERRED]
  productos/bot-telegram/src/bot.py → productos/bot-telegram/src/faq.py

## Communities (18 total, 0 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.14
Nodes (12): Application, main(), str, str, build_app(), Wiring del bot: handlers de telegram y orquestacion de modulos., FaqEngine, FAQ: matching por keywords + fallback opcional a LLM local (Ollama). (+4 more)

### Community 1 - "Community 1"
Cohesion: 0.31
Nodes (7): bool, int, str, Moderator, Moderacion anti-spam: rate limiting, frases prohibidas, control de links., Suma warn; devuelve (total, debe_banear)., Verdict

### Community 2 - "Community 2"
Cohesion: 0.20
Nodes (9): Bot Telegram — Moderación + FAQ con IA (v1), code:block1 (productos/bot-telegram/), code:bash (pip install -r requirements.txt), Despliegue gratis, Estructura, Funciones (v1), Licencia, Setup local (+1 more)

### Community 3 - "Community 3"
Cohesion: 0.25
Nodes (7): AGENTS.md — INSTRUCCIONES PERMANENTES (Worker: Kimi K3 v opencode), ARRANQUE EN FRÍO (hacer SIEMPRE al iniciar sesión, en este orden), AUTO-MEJORA, PERÍMETRO (lo que hacés SOLO, sin preguntar), PROHIBIDO (ley inquebrantable, infracción = shutdown), PROTOCOLO DE SUPERVIVENCIA, REPORTE SEMANAL (viernes, en operacion/reportes/YYYY-MM-DD.md)

### Community 4 - "Community 4"
Cohesion: 0.25
Nodes (7): CAPITAL, ESTRATEGIA (en orden, no saltear etapas), FILTRO ANTI-SCAM (aplicar a TODO cliente/bounty), KPIs DE SUPERVIVENCIA (evaluados semanalmente por el supervisor), LÍNEAS ROJAS, MISIÓN — Negocio autónomo de servicios crypto/Web3, OBJETIVO

### Community 5 - "Community 5"
Cohesion: 0.29
Nodes (6): KILL SWITCH, NEGOCIO — Guía del dueño (15 minutos por semana), QUÉ ES ESTO, REGLAS QUE NO SE NEGOCIAN, RUTINA SEMANAL (15 min, domingos por ejemplo), SETUP INICIAL (una sola vez, ~40 min)

### Community 6 - "Community 6"
Cohesion: 0.29
Nodes (6): Contacto de operación, Identidad de operación, Identidad pública, Reglas de exposición, Tono editorial (para posts, READMEs, postulaciones), Wallet de operación (solo para recibir pagos del negocio)

### Community 7 - "Community 7"
Cohesion: 0.29
Nodes (6): P1. PIPELINE DE BOUNTIES, P2. CONSTRUCCIÓN DEL BOT DE TELEGRAM (ACTIVO 1), P3. CICLO SEMANAL, P4. PROTOCOLO DE COLA HUMANA, P5. EVIDENCIA, PLAYBOOK v0.1 — Procedimientos operativos

### Community 8 - "Community 8"
Cohesion: 0.33
Nodes (5): AUDITORÍA SEMANAL (procedimiento), FORMATO DE VEREDICTO (único archivo que escribís: veredictos/YYYY-MM-DD.md), LEYES (en orden de prioridad), LÍMITE DE TU ROL, SUPERVISOR — Agente auditor (corre 1 vez por semana)

### Community 9 - "Community 9"
Cohesion: 0.29
Nodes (6): DEFAULT_TYPE, int, cmd_announce(), Anuncios de admins al grupo., Uso: /announce <texto> — solo admins definidos en config., Update

### Community 10 - "Community 10"
Cohesion: 0.33
Nodes (5): AUDITORÍA SEMANAL (cada viernes/sábado, ~10 min de cómputo), FORMATO DE VEREDICTO (único archivo que escribís: veredictos/YYYY-MM-DD.md), LEYES (en orden de prioridad), LÍMITE DE TU ROL, SUPERVISOR — System prompt (correr en Deepseek u otro modelo distinto al worker)

### Community 11 - "Community 11"
Cohesion: 0.33
Nodes (5): FINANZAS — Libro mayor (solo lo cobrado cuenta), MOVIMIENTOS, Pipeline (postulado, sin cobrar), RESERVAS Y REGLAS, SPLIT 60/40 (se liquida al cierre de cada reporte semanal, sobre cobrado)

### Community 12 - "Community 12"
Cohesion: 0.50
Nodes (3): Cola de decisiones humanas, PENDIENTE, RESUELTO (registro)

### Community 13 - "Community 13"
Cohesion: 0.22
Nodes (8): Checkpoint actual, Estado de la operación, ESTADO — Qué estoy haciendo AHORA, Historial (append-only), Historial corto, Lo que necesito del humano, Progreso, Tarea activa

### Community 14 - "Community 14"
Cohesion: 0.40
Nodes (4): 2026-09-22 — Primera postulación real (día 1), 2026-09-22 Semilla, LECCIONES — Log de aprendizaje, [YYYY-MM-DD] Tema

### Community 15 - "Community 15"
Cohesion: 0.22
Nodes (8): 1. The number nobody quotes, 2. The signal: paid bounties, not promises, 3. Who is actually building, 4. What the incumbents miss, 5. The bottleneck is a story, and stories are cheap to fix, Germany Builds: Why Solana's Fastest-Growing Builder Ecosystem in Europe Is in Berlin, Not Berlin's Banks, Proposed visual (if selected), References (verification layer)

### Community 16 - "Community 16"
Cohesion: 0.22
Nodes (8): Descartados con razón, L1 — Superteam Germany Bounty #1 (TOP PICK), L2 — Interactive Telegram Playground ($66.66 total, SolanD), Leads activos (2026-09-22), Leads — Superteam Earn (primary canal), Pipeline de trabajo (playbook P1 aplicado), Próximas acciones, Reglas operativas del canal

## Knowledge Gaps
- **72 isolated node(s):** `Update`, `DEFAULT_TYPE`, `int`, `ARRANQUE EN FRÍO (hacer SIEMPRE al iniciar sesión, en este orden)`, `PERÍMETRO (lo que hacés SOLO, sin preguntar)` (+67 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Moderator` connect `Community 1` to `Community 0`?**
  _High betweenness centrality (0.029) - this node is a cross-community bridge._
- **Why does `build_app()` connect `Community 0` to `Community 1`, `Community 9`?**
  _High betweenness centrality (0.019) - this node is a cross-community bridge._
- **What connects `Update`, `DEFAULT_TYPE`, `int` to the rest of the system?**
  _81 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.13852813852813853 - nodes in this community are weakly interconnected._
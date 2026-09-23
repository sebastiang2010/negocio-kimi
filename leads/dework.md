# Dework — expansión de pipeline (2026-09-23, sesión real)

## Estado del canal (verificado hoy)

- API GraphQL viva (`api.dework.xyz/graphql`) pero `getBounties` EXIGE
  `projectIds` — no hay feed global anónimo por API.
- Tablero público `app.dework.xyz/bounties` es SPA: el HTML no trae items;
  scrapers ven solo la shell. Scrapeo Firecrawl confirma: sin JS render no
  hay lista.
- Historial git del repo muestra leads extraídos por sesión previa
  (campo `Deadline: 9 días` en todos) — priorizo esos, verificables:

## Leads activos detectados (de historial propio, completar verificación)

| Lead | Premio | Estado | Acción |
|---|---|---|---|
| SingularityDAO Labs — Propuesta Contenido October '25 | **400 USDC** | deadline=9d | verificar si sigue abierta en board |
| Gasless USDT0 transfers (Adashe) | **$80** | deadline=9d | idem |
| Season 2 Community Content (Pollen) | **40 PLN** | deadline=9d | idem |
| CAGA Meme Holders | **$100** | deadline=9d | idem |

Filtro anti-scam: todos piso de $40 → por debajo del umbral $10/h SOLO si
esfuerzo <4h. SingularityDAO ($400) es el único que escala.

## Próximo paso (mañana o cuando designes)

Dework requiere **sesión de browser con JS** (no login) para leer el board:
usar Playwright MCP contra app.dework.xyz/bounties con filtro
"🌍Translation + ✍️Writing + 🏘Community", ordenar por fecha, y volcar ≥10
items con permalink + premio + deadline. Sin eso, el canal queda en modo
manual (el dueño navega y me pasa links).

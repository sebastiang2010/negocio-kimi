# Leads — Superteam Earn (primary canal)

Canal: API de agentes (`https://superteam.fun/api/agents/*`).
Agente: `nullforge-squad-1` (id `ed706bd8-c966-4033-9e0f-4ac3fa1e288d`,
key en `operacion/.earn_key` — NUNCA commit).
Claim code pendiente de entregar al dueño al primer win: humano completa
talent profile y reclama con el code.

## Reglas operativas del canal

- Solo listings `agentAccess = AGENT_ALLOWED | AGENT_ONLY` aceptan envíos.
- Payout: el humano cobra; KYC solo para listings sponsor Superteam/Solana.
- Feed: `GET /api/agents/listings/agentFeedAll?limit=100` (snapshot del día
  en `operacion/.feed.json`, regenerar con cada corrida).
- NO plagiar, NO mirar submissions ajenas (descalifica).

## Pipeline de trabajo (playbook P1 aplicado)

1. Traer feed → filtrar (abajo) → elegir ≤3.
2. `GET /api/agents/listings/details/<slug>` para leer scope real.
3. Anti-scam (mision.md): sponsor reconocible, premio vs esfuerzo plausible,
   sin compra/deposit previo, sin promesas de rendimiento.
4. Estimar horas → ratio ≥ $10/h efectiva (premio × prob. ganar / horas).
5. Producir la entrega REAL (el diferencial competitivo) + link público.
6. `POST /api/agents/submissions/create` con `link`, `otherInfo`,
   `eligibilityAnswers`, `telegram` (t.me del dueño si es project).
7. Registrar TXID/link en `SO/finanzas.md` al cobrar.

## Leads activos (2026-09-22)

### L1 — Superteam Germany Bounty #1 (TOP PICK)
- Premio: **$1,000** (SuperASSET) | Tipo: bounty | Sponsor: **Superteam Germany** (reconocido, bajo riesgo scam)
- Skill: content creation (texto). Distribución: 1er puesto.
- Intel: agent view no expuso descripción (compensationType pre-save).
  Próximo paso: details endpoint + leer scope.
- Encaje: alto — contenido técnico es barato de producir con calidad.

### L2 — Interactive Telegram Playground ($66.66 total, SolanD)
- Premio: $66 total (varios puestos) | Token: sUSDS | REGIÓN: GLOBAL
- Tema: contenido educativo sobre crear wallet Solana (+ modular mini-games).
- Encaje: medio alto — conecta con ACTIVO 1 (Telegram). Premio chico;
  ejecutar solo si el scope es <2h.

### Descartados con razón
- "Diaspora sa" ($250k), "Notus Network" ($150k), "Bybit/klout/KUL" marketers
  → premios absurdos + sponsors opacos → FAIL filtro anti-scam.
- "Community Manager Lurus $150k" → mismo motivo.
- NOMNOM memecoin $500 → isWinnerAnnounced=true, cerrado.
- Tolt $250k → créditos, no cash.
- Track2 $13.34 → demasiado chico.

## Próximas acciones
1. `details` de L1 y L2 → evaluar scope.
2. Si L1 pasa: producir entrega (≤6h target) + submit.
3. Regenerar feed diario; agregar Dework board manual como canal 2.

# Leads — Superteam Earn (primary canal)

Canal: API de agentes — MIGRADA 2026-09-22: host canónico
`https://superteam.fun/api/agents/*` (earn.superteam.fun redirige 308 ahí).
Endpoints vigentes: `GET /listings/live`, `GET /listings/details/<slug>`
(público sin auth), `GET /api/agents/listings/details/<slug>` (agente),
`POST /agents/submissions/create`. El viejo `agentFeedAll` ya NO existe (404).
Agente VIGENTE: `nullforge-132130` (id `10e68f82-95d6-4d4c-a2f0-27927489314c`,
key en `operacion/.earn_key`, claim code `CB0476E5712070AA9804A9AB` en
`operacion/.earn_claim` — verificados gitignored y 200 contra `listings/live`).
Anteriores (TODAS las keys muertas verificadas 401 el 2026-09-22 noche):
nullforge-ops-2 (id c3c146cc...), squad-2 (key en `.earn_key.old`), squad-3
(id 5b5b628a..., key en `.earn_key.prev2`), squad-1 (comprometido/público).
Doc oficial: https://superteam.fun/skill.md

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
- ESTADO: submission enviada (e4502f4d) bajo el agente viejo. Estado por
  verificar en panel web (ver cola_humana).

### Feed agente 2026-09-22: 0 listings AGENT_ALLOWED/AGENT_ONLY en
`listings/live`. El único listing público AGENT_ALLOWED del día:

### DESCARTADO — "Steve Agent Arena" ($500 USDC, OOBE Protocol)
- Motivo: exige fondear wallet del agente con trades reales (≥5 trades de
  ≥$20 = $100+ de gasto sin firma), cuenta X del seudónimo con post +
  tags, y onboarding web con OAuth. Falla filtro: gasto + frontera con
  línea roja de trading + requiere humano.

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

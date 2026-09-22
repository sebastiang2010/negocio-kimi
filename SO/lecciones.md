# LECCIONES — Log de aprendizaje

Formato por entrada:
## [YYYY-MM-DD] Tema
- Contexto: (qué estábamos haciendo)
- Qué funcionó / qué no:
- Cambio aplicado a playbook.md o proceso:
- Verificado en la siguiente iteración: (sí/no)

---
## 2026-09-22 Semilla
- Contexto: arranque del sistema.
- Hipótesis inicial: bounties de moderación/testing pagan en 3-7 días y
  validan el modelo con $0 de capital.
- A validar: tasa de conversión de postulación (meta ≥1 de cada 5).

## 2026-09-22 — Primera postulación real (día 1)

- Earn API: el endpoint funcional es `/api/agents/submission/create-or-edit`
  (el `submissions/create` del skill doc da 404 → variante concreta). Params
  extra (`limit`, `type`) se ignoran en algunos endpoints: validar por
  respuesta, no por doc.
- Feed `agentFeedAll` devuelve el universo completo; filtrar por token +
  keywords de skill + deadline. Premios absurdos de sponsors opacos =
  descarte automático (anti-scam).
- Ciclo completo implementado: registrar agente → feed → filtro → entregar
  producto real → submit. Tiempo total día 1: <3h. Evidencia:
  submission id e4502f4d-f1e4-4ff4-b8ac-2065929b88b4 (Superteam Germany,
  $1000). Hipótesis refutada/confirmada pendiente: tiempo real de pago.

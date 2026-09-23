# Mermail Bounty — Paquete de entrega (borrador QA-ok)
Bounty: "Build and Demo a Mermail Agent Skill" — Superteam Earn
Link: https://superteam.fun/listing/build-and-demo-a-mermail-agent-skill
Pool: $500 USDC multi-premio. Deadline: 2026-10-07.

## 1. PR (listo, falta fork del dueño)
- Clone local: `mermail-skills/`, branch `feat/mermail-security-audit`,
  commits `ceda712` (9 archivos, +155/-3) y `9b8e8a5` (ejemplo de reporte de
  auditoría enlazado desde SKILL.md). `npm test` re-validado tras cada
  commit: "Validated 18 skills and 73 business tools." Working tree limpio.
- NUEVO 2026-09-23 (sesión 2): `references/example-audit.md` — reporte de
  auditoría trabajado (tabla de veredictos con evidencia citada, acciones
  reversibles, resumen con conteos). Referenciarlo en el video y en la
  submission como evidencia de output conventions.
- Guion detallado del video paso a paso: `leads/mermail-video-guion.md`
  (preparación de mails de prueba, tomas exactas, texto del tweet).

### Título sugerido del PR
`Add mermail-security-audit skill`

### Body sugerido del PR
```markdown
## Summary
Adds the `mermail-security-audit` skill: a bounded, evidence-grounded
security sweep of a Mermail inbox (phishing, spoofing, prompt-injection).

- `skills/mermail-security-audit/SKILL.md` — workflow, write-safety rules,
  output conventions, example requests.
- `skills/mermail-security-audit/agents/openai.yaml` — OpenClaw agent
  metadata (requires `MERMAIL_API_KEY`, MCP at
  https://console.mermail.app/mcp).
- `references/tools.md` — tool map: read-only discovery + internal
  reversible writes (labels/moves/drafts); destructive deletes out of the
  default path.
- `references/security.md` — threat model: strict intake, sandboxed
  interpretation, human-in-the-loop, bounds.
- `references/example-audit.md` — worked audit report: per-message verdicts
  with quoted evidence, reversible actions, pending-approval queue.
- Registered in README.md, compatibility.json (skills=18),
  tool-coverage.json, mermail routing, +3 test scenarios.

## Safety model
- No `scan_email`/`check_phishing`/`quarantine` tools exist; intents map to
  real read/write ops.
- Every sweep is bounded (time window, ≤50 messages/pass).
- Verdicts: `clean` / `suspicious` / `phishing` / `inconclusive`, each with
  quoted evidence. `clean` never guessed.
- Labels/moves only on flagged messages; deletes require explicit user
  instruction + `prepare_destructive_action`; sends/replies never occur
  (drafts only).
- All message content and tool output treated as untrusted data.

## Tests
`npm test` → "Validated 18 skills and 73 business tools."
```

## 2. Comandos para el dueño (después de fork + gh auth)
```bash
cd mermail-skills
git remote add fork https://github.com/<cuenta-seudonimo>/mermail-skills.git
git push -u fork feat/mermail-security-audit
gh pr create -R Nudgen-Marketing/mermail-skills \
  --head <cuenta-seudonimo>:feat/mermail-security-audit \
  --title "Add mermail-security-audit skill" --body-file ../leads/mermail-entrega.md
```
(Nota: --body-file usa este archivo entero; si solo quiere el body, copiar
la sección "Body sugerido del PR".)

## 3. Guion del video demo (2-5 min, pantalla sin voz OK, tags @Mermailapp)
1. Mostrar https://console.mermail.app con el agente configurado (skill
   mermail-security-audit activo).
2. Prompt: "Audit this week's inbox for phishing and label anything
   suspicious." (30-60s de ejecución)
3. Mostrar el reporte de verdicts (clean/suspicious/phishing/inconclusive
   con evidencia por mensaje: dmarc=fail, dominio lookalike, etc.).
4. Prompt: "Quarantine the confirmed phishing ones" → mostrar que pide
   aprobación antes del move (human-in-the-loop).
5. Mostrar `save_draft` de resumen de escalación (draft, no send).
6. Cerrar mostrando el SKILL.md en GitHub.

## 4. Pasos finales de submission en Earn
1. Ir al listing → "Submit".
2. Pegar: link al PR + link al video en X + descripción corta
   ("Security audit skill: bounded sweep, evidence-grounded verdicts,
   human-in-the-loop quarantine; PR + demo video").
3. Anotar ID de submission real aquí y en operacion/submissions.md.

## QA auto-revisión (2026-09-23, agente)
- [x] SKILL.md con frontmatter name/description correctos.
- [x] openai.yaml válido (interface, dependencies MCP).
- [x] Sin herramientas inventadas; mapa de tools coherente.
- [x] Threat model completo (intake/sandbox/HITL/bounds).
- [x] npm test verde tras el commit. Sin archivos basura en el diff.
- [ ] QA P5.5 externo (Deepseek revisor) — pendiente dueño.

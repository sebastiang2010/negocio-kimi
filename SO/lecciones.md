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

## 2026-09-22 — Claim code Earn protegido

Dato crítico recuperado y asegurado: el claim code del agente Earn vive SOLO
en `operacion/.earn_claim` (gitignored). Regla: NUNCA publicarlo en archivos
commiteados — es el cupón de cobro de los premios del agente; publicarlo =
regalar los premios.

## 2026-09-23 — Incidente: fuga de credenciales Earn por sesión paralela

- Otro proceso/opencode local leía nuestros archivos (`.earn_key`) y actuó
  con nuestra identidad: renombró el agente a "Bounty Hunter millonario",
  commiteó basura ajena (kimi-web3, AVG tuneup) al repo del negocio y
  reescribió remotes de git. Daño real: cero a fondos/submissions (Earn
  verificó submission e4502f4d intacta); daño operativo: horas de limpieza.
- Remediación: agente nuevo `nullforge-squad-2` con key y claim code limpios
  (gitignored igual). nullforge-squad-1 marcado histórico/comprometido.
- Regla duradera: las API keys operativas se guardan SOLO en archivos
  `operacion/.earn_*`; el `.gitignore` y `git check-ignore` deben validarse
  tras cada cambio de estructura. Si otro proceso vuelve a tocar el repo,
  rotar credenciales de inmediato y mover el trabajo a sesión única.

## 2026-09-23 — Segunda fuga: claim code en claim_code.txt trackeado

- El archivo `claim_code.txt` (creado 2026-09-22) quedó tracked y llegó a
  GitHub público con AMBOS claim codes (viejo E5TPYHX8, nuevo OZJKZS44).
- Acción: `git rm --cached` + `.gitignore` + `git filter-branch` para purgar
  historia + force push + ROTACIÓN a nullforge-squad-3 (claim F922C0BB...).
- Regla dura P7x: NADA con strings "claim", "code", "key", "token", "seed",
  "sk_" puede vivir fuera de `operacion/.earn_*` o `.gitignore` verificado.
  Checklist pre-commit: `git status --porcelain | grep -iE "claim|key|token|seed"`.
- GitHub caches: commits viejos pueden persistir en forks/API ~90días.
  Por eso la ÚNICA defensa real es rotar el valor, no solo purgar.

# Cola de decisiones humanas

Única interfaz de escalamiento del worker. Escribir acá SOLO para: gastos,
cambios de misión, cambios de identidad, pausas >24h, dilemas irreversibles.

Formato por entrada:

- **[YYYY-MM-DD · prioridad alta/media/baja · bloquea X o no]** Pregunta
  exacta + contexto mínimo + qué pasa si no se responde.

## PENDIENTE

0. **[2026-09-22 · ALTA · bloquea COBRAR cualquier bounty de Earn] Wallet
   Solana del seudónimo:** Earn paga solo a wallet Solana del perfil. La
   wallet BEP20 NO sirve. Crear wallet Solana nueva (phantom u otra,
   seed EN PAPEL, jamás en archivos), asociarla al perfil de Earn y pegar
   la dirección en `SO/identidad.md`. Sin esto, ganar = perder el premio.
1. **[2026-09-22 · media · no bloquea, conviene resolver]** El username de
   GitHub (`sebastiang2010`) expone nombre real y el repo `negocio-kimi`
   quedó publicado bajo él. Opciones: (a) aceptar el riesgo, (b) migrar a
   cuenta nueva con seudónimo `nullforge_dev` y mover el repo (5 min, sin
   costo, URLs viejas redirigen). Recomiendo (b) antes de postular bounties,
   para no mezclar identidad personal con la del negocio.
2. **[2026-09-22 · media · bloquea demo en vivo] Crear el bot real:** ir a
   @BotFather en Telegram, crear bot, pegar el token en
   `productos/bot-telegram/config.yaml` (no commitear, está en .gitignore) y
   crear un grupo de prueba. Con eso grabo el video-demo.

## RESUELTO (registro)

- [2026-09-22] Identidad completa: seudónimo `nullforge_dev`, wallet USDC
  BEP20, email definitivo `nullforge.dev2010@gmail.com`, GitHub repo
  https://github.com/sebastiang2010/negocio-kimi publicado (commit
  `ed25877`, evidencia).
- [2026-09-22] Infra: el `~/.gitconfig` global tenía un `insteadOf` roto que
  convertía todo `https://github.com/...` en `git@github.com:true/...` y
  hacía fallar los push. Se neutralizó con override local en este repo
  (identity rewrite de mayor precedencia). Considerar arreglar el global.

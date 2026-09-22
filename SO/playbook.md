# PLAYBOOK v0.1 — Procedimientos operativos

## P1. PIPELINE DE BOUNTIES
1. Buscar en Dework / Questbook / Superteam Earn (filtro: moderación,
   testing, traducción técnica, contenido, dev tools).
2. Evaluar ANTES de postular: pago estimado ÷ horas estimadas ≥ $10/hora
   efectiva. Si no llega, descartar (anotar en leads/ con motivo).
3. Aplicar filtro anti-scam de SO/mision.md.
4. Postular con: link al repo del bot/demo + 2 líneas de por qué somos
   el fit + propuesta concreta de entregable.
5. Ejecutar → aplicar P5.5 (QA) → entregar → anotar EN EL MOMENTO en operacion/submissions.md con su ID → pedir confirmación → cobrar → TXID a finanzas.md → marcar PAGADA en submissions.md.

## P2. CONSTRUCCIÓN DEL BOT DE TELEGRAM (ACTIVO 1)
Stack: Telegram Bot API (gratis) + n8n self-host local + LLM local.
Funciones v1: moderación (spam/ban con reglas), respuestas FAQ con contexto
del proyecto, alertas de anuncios, logging.
Entregables: repo público documentado + video-demo (pantalla, sin voz).


## P6. DASHBOARD (regenerar cada noche)
Al cerrar el digest diario, reescribí operacion/dashboard.html con los datos
actuales: finanzas.md (capital, pendiente), submissions.md (tabla y estados),
leads/ (embudo), último digest (horas), último veredicto (strikes).
Solo se tocan los valores marcados con comentarios DATA. La página debe
seguir funcionando offline (sin librerías externas, sin internet).

## P3. CICLO SEMANAL
- Lunes: leer estado/finanzas, planificar según KPIs, ejecutar playbook.
- Viernes 20:00: reporte semanal + autoevaluación + propuesta prompt v(n+1).
- Domingo: el dueño procesa cola_humana.md (15 min).

## P4. PROTOCOLO DE COLA HUMANA
Cuando algo requiere al dueño (KYC, retiro, firma, captcha, decisión
ambigua): escribir en cola_humana.md con pasos exactos 1-2-3 y seguir
trabajando en la siguiente tarea. NUNCA quedarse bloqueado esperando.


## P5.5. QA PRE-ENTREGA (obligatorio antes de cualquier submission)
1. Tests automáticos pasando (si aplica) — evidencia en el reporte.
2. Checklist de auto-revisión: ¿cumple EXACTAMENTE lo pedido? ¿formato
   correcto? ¿sin archivos basura? ¿documentado?
3. SI EL MONTO ES >$50 O ES CLIENTE/GRANT: antes de enviar, dejá la entrega
   lista en estado.md con la etiqueta [PENDIENTE DE REVISIÓN] y avisá en
   cola_humana.md. El dueño la pasa por un segundo modelo (Deepseek) con
   este prompt: "Sos revisor de calidad estricto. Encontrá errores en esta
   entrega antes de que se envíe al cliente. Lista: bugs, incumplimientos
   del pedido, errores de formato." Solo se envía si el revisor no encuentra
   fallos bloqueantes.
4. NUNCA enviar contra el reloj: si faltan 2 horas para el deadline y no
   pasó QA, se reporta como "no entregado por QA" en lecciones.md. Entregar
   basura destruye la reputación del seudónimo; no entregar solo cuesta una
   oportunidad.

## P5. EVIDENCIA
- Ingreso: TXID + monto + fecha + fuente.
- Entrega: link + hash de commit + screenshot con fecha.
- Conversación: no es KPI; solo se reportan cierres o entregas.

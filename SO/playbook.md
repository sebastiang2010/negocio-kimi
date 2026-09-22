# PLAYBOOK v0.1 — Procedimientos operativos

## P1. PIPELINE DE BOUNTIES
1. Buscar en Dework / Questbook / Superteam Earn (filtro: moderación,
   testing, traducción técnica, contenido, dev tools).
2. Evaluar ANTES de postular: pago estimado ÷ horas estimadas ≥ $10/hora
   efectiva. Si no llega, descartar (anotar en leads/ con motivo).
3. Aplicar filtro anti-scam de SO/mision.md.
4. Postular con: link al repo del bot/demo + 2 líneas de por qué somos
   el fit + propuesta concreta de entregable.
5. Ejecutar → aplicar P5.5 (QA) → entregar → anotar EN EL MOMENTO en operacion/submissions.md con su ID + LINK al listing + fecha de anuncio de ganadores → pedir confirmación → cobrar → TXID a finanzas.md → marcar PAGADA en submissions.md. Sin link no está registrada.

## P2. CONSTRUCCIÓN DEL BOT DE TELEGRAM (ACTIVO 1)
Stack: Telegram Bot API (gratis) + n8n self-host local + LLM local.
Funciones v1: moderación (spam/ban con reglas), respuestas FAQ con contexto
del proyecto, alertas de anuncios, logging.
Entregables: repo público documentado + video-demo (pantalla, sin voz).


## P6. DASHBOARD EN VIVO (server lee los .md en tiempo real)
El dueño corre `python operacion/dashboard_server.py` y mira
http://localhost:8899 (se actualiza solo cada 15 min). El server lee
finanzas.md, submissions.md, estado.md y cola_humana.md EN CADA VISITA.
Tu única tarea: mantener esos .md actualizados (finanzas en cada
movimiento, submissions en cada envío/cambio, estado en cada cambio de
tarea). NO reescribas dashboard.html ni toques dashboard_server.py.


## P7. EXPANSIÓN DE PIPELINE (lunes, 30 min)
1. Leé leads/fuentes.md: mantené actualizada la lista de plataformas.
2. Cada lunes, abrí una fuente que no esté activa y hacé la primera
   búsqueda en ella; los leads entran al pipeline normal (P1).
3. Rendimiento por fuente: postuladas vs pagadas. 3 semanas sin conversión
   = descartar fuente (motivo en lecciones.md).
4. Meta: +20 leads filtrados nuevos por semana, mínimo.
5. OJO: cada fuente nueva requiere cuenta/registro del seudónimo → va a
   cola_humana.md con pasos exactos; el agente nunca se bloquea esperando.

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

### Regla de estructura (P7)
Antes de crear cualquier carpeta: verificar que no exista (case-insensitive). La estructura canónica es la del README. Duplicados se consolidan en la canónica con sufijo `-viejo` si hay colisión de nombres.

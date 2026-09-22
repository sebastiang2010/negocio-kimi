# SUBMISSIONS — Registro de entregas (la base de datos de la operación)

REGLA: cada postulación se anota acá EN EL MOMENTO de enviarla, con su ID.
Cada cambio de estado se actualiza en esta tabla el mismo día. Si no está
en esta tabla, no existió. El supervisor coteja esta tabla contra los
reportes semanales: una submission declarada en un reporte que no aparece
acá = strike.

| ID | Fecha envío | Plataforma | Bounty / Cliente | Tipo de tarea | Monto | Estado | Fecha cambio | Pago (TXID) | Notas |
|---|---|---|---|---|---|---|---|---|---|
| e4502f4d | 2026-09-22 | Superteam Earn (Germany) | Superteam Germany | Artículo de datos/análisis | $1.000 | 🟡 ENVIADA | 2026-09-22 | — | Envío previo a regla P5.5 (QA cruzado). Verificar red de pago: wallet registrada es BEP20, Earn paga en Solana → crear wallet SPL si aplica |

## ESTADOS permitidos
🔵 BORRADOR (en construcción) | 🟡 ENVIADA (esperando revisión) |
🟢 ACEPTADA (aprobada, esperando pago) | 💰 PAGADA (TXID en finanzas.md) |
🔴 RECHAZADA (con motivo) | ⚪ CADUCADA (deadline pasó sin enviar)

## REGLAS DE USO
1. ENVIAR = anotar acá en la misma sesión. Nunca después.
2. Cambio de estado = actualizar FECHA CAMBIO el mismo día.
3. PAGADA = solo con TXID real, que también va a finanzas.md.
4. RECHAZADA = anotar el motivo en Notas + una línea en lecciones.md
   (qué falló del QA para que no se repita).
5. El supervisor verifica estados contra la plataforma cada viernes.

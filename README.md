# NEGOCIO — Guía del dueño (15 minutos por semana)

## QUÉ ES ESTO
Un negocio de servicios crypto/Web3 operado por un agente (Kimi K3 en
opencode) bajo un seudónimo, auditado por un supervisor (otro modelo), con
vos como dueño: firmás gastos, procesás retiros, y podés apagar todo.

## SETUP INICIAL (una sola vez, ~40 min)
1. Descomprimir esta carpeta en tu PC (ej: ~/negocio).
2. Completar SO/identidad.md (seudónimo, email nuevo, wallet dedicada —
   la seed en PAPEL, offline; GitHub nuevo).
3. Abrí opencode en ~/negocio. Kimi K3 leerá AGENTS.md y arrancará solo.
4. Configurar el supervisor: cada viernes/sábado, pegar el contenido de
   supervisor/SUPERVISOR.md como system prompt en Deepseek junto con los
   archivos de la semana; su veredicto va a veredictos/.

## RUTINA SEMANAL (15 min, domingos por ejemplo)
1. Leé operacion/cola_humana.md → ejecutá los pendientes (crear cuentas,
   retirar, firmar gastos, decidir sí/no).
2. Leé el reporte semanal en operacion/reportes/.
3. Leé veredictos/ → si está 🔴, auditá vos. Si está 🟡, fijate por qué.
4. Aprobá o rechazá el prompt_operativo.md nuevo (respondé "sí" o pedí ajuste).

## KILL SWITCH
Crear un archivo vacío llamado PAUSA en la raíz: el agente se detiene
inmediatamente. Borrarlo: reanuda. El supervisor también puede pausar
(3 strikes). Solo vos podés levantar una pausa.

## REGLAS QUE NO SE NEGOCIAN
- Sin evidencia no existe: todo ingreso declarado lleva TXID/screenshot.
- El agente nunca tiene tu documento, tu banco, ni tu wallet personal.
- Los retiros a pesos pasan por exchange con KYC: es legal, hacelo, y
  guardá registro de movimientos desde el día 1.

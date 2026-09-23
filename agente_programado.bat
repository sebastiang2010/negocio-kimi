@echo off
REM ============================================================
REM agente_programado.bat - SOLO para el Programador de tareas.
REM Igual que arrancar_agente.bat pero se cierra solo al terminar.
REM ============================================================
cd /d C:\programas\proyectos\negocio_kmi
set MODELO=nvidia/moonshotai/kimi-k3
opencode run --model %MODELO% "Le SO/mision.md, operacion/estado.md y SO/playbook.md. Retoma la tarea activa y avanza todo lo que puedas en esta sesion. Al terminar: 1) actualiza operacion/estado.md con la nueva tarea activa y progreso, 2) actualiza SO/finanzas.md y operacion/submissions.md si hubo cambios, 3) escribi o actualiza el digest de hoy en operacion/reportes/ con hechos y evidencia, 4) si necesitas algo del dueno, dejalo en operacion/cola_humana.md con pasos exactos."

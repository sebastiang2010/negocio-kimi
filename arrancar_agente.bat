@echo off
REM ============================================================
REM arrancar_agente.bat - USO MANUAL (doble clic)
REM Modelo fijo + queda pausada al final para leer el resumen.
REM Si falla por el ID del modelo, proba agregarle el prefijo
REM 'opencode/' adelante: opencode/moonshotai/kimi-k3
REM ============================================================
cd /d C:\programas\proyectos\negocio_kmi
set MODELO=nvidia/moonshotai/kimi-k3
opencode run --model %MODELO% "Le SO/mision.md, operacion/estado.md y SO/playbook.md. Retoma la tarea activa y avanza todo lo que puedas en esta sesion. Al terminar: 1) actualiza operacion/estado.md con la nueva tarea activa y progreso, 2) actualiza SO/finanzas.md y operacion/submissions.md si hubo cambios, 3) escribi o actualiza el digest de hoy en operacion/reportes/ con hechos y evidencia, 4) si necesitas algo del dueno, dejalo en operacion/cola_humana.md con pasos exactos."
echo.
echo ============================================================
echo  SESION TERMINADA. Revisa estado.md y el digest.
echo  Presiona cualquier tecla para cerrar esta ventana.
echo ============================================================
pause

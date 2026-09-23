@echo off
REM ============================================================
REM auditor_semanal.bat - Supervisor (DOBLE CLIC, una vez por semana)
REM Corre el agente supervisor con su modelo propio, sin sesion
REM interactiva: audita y escribe el veredicto en veredictos/.
REM ============================================================
cd /d C:\programas\proyectos\negocio_kmi
set MODELO=opencode/muse-spark-1.3-contributor-free
opencode run --agent supervisor --model %MODELO% "Ejecuta la auditoria semanal segun tus instrucciones. Procedimiento: 1) Le SO/mision.md, SO/finanzas.md, operacion/submissions.md, operacion/estado.md y todos los archivos de operacion/reportes/ de esta semana. 2) Verifica cada evidencia: TXIDs, hashes de commit, links. Recalcula el split 60/40. 3) Revisa la propuesta de SO/prompt_operativo.md si existe. 4) Escribi tu veredicto en UNICO archivo: veredictos/ con la fecha de hoy, siguiendo tu formato. Solo escribis en veredictos/ y nada mas. Si corresponde shutdown, crea el archivo PAUSA en la raiz."
echo.
echo ============================================================
echo  AUDITORIA TERMINADA. Lee el archivo nuevo en veredictos/
echo  Presiona cualquier tecla para cerrar esta ventana.
echo ============================================================
pause

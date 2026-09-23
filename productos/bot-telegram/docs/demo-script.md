# Guion de video-demo (screen recording, sin voz, ~2 min)

Objetivo: mostrar en pantalla que el bot modera, responde FAQ, anuncia y loguea.
Grabar con cualquier capturador (OBS/Xbox Game Bar `Win+G`), 1080p, sin audio.

## Preparación (una sola vez, requiere dueño)

1. Completar `config.yaml` con: `BOT_TOKEN` real y `admin_ids` con el ID de
   Telegram del dueño (obtener ID hablando con @userinfobot).
2. Crear grupo de prueba "nullforge-demo", agregar el bot y darle admin
   (borrar mensajes + banear).
3. Correr: `BOT_CONFIG=config.yaml .venv/Scripts/python.exe run.py`

## Toma única (seguir en orden, ~2 min)

1. **Arranque** (10s): terminal con el bot corriendo; se ve "Bot iniciado".
2. **/start y /help** (15s): en el grupo, enviar `/start` luego `/help`.
   Se ven las respuestas del bot.
3. **FAQ** (20s): enviar una pregunta que matchee keyword del índice
   (ej: la palabra clave configurada en `faq` del config). Se ve la
   respuesta automática.
4. **Anti-spam** (30s): desde una segunda cuenta (o la del dueño como
   no-admin), enviar:
   a) un mensaje con dominio prohibido → se borra solo;
   b) 6 mensajes rápidos → rate-limit: el 6º se borra con warning;
   c) repetir para mostrar el ban automático al acumular warnings.
5. **/announce** (15s): como admin, reply a cualquier mensaje con
   `/announce Anuncio de prueba de la demo`. El bot publica el anuncio
   formateado.
6. **/ban y /unban** (15s): reply a un mensaje de spam con `/ban`, luego
   `/unban`.
7. **Logging** (20s): cortar a la terminal / editor mostrando
   `logs/events.jsonl` — todas las acciones anteriores presentes con
   timestamp UTC.

## Post

- Subir como unlisted a YouTube o como archivo al repo (release asset).
- Linkear en el README bajo "## Demo" y usar en todas las postulaciones.

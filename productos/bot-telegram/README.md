# nullforge — Telegram Moderator + FAQ Bot

Bot de moderación para comunidades de Telegram con anti-spam, FAQ contextual y logging de eventos. Construido sobre `python-telegram-bot` v21, con LLM local opcional.

## Funcionalidades

- **Moderación anti-spam**: detección de frases prohibidas, dominios no permitidos y rate-limit por usuario (ventana deslizante). Acción configurable: `delete_and_warn` (elimina mensaje + warning, ban automático al superar el umbral).
- **FAQ**: responde preguntas frecuentes por palabras clave. LLM local (Ollama) opcional para respuestas fuera del índice.
- **Anuncios**: comando `/announce` solo para admins.
- **Logging**: todos los eventos (mensajes, bans, warnings, FAQ) en `logs/events.jsonl` (JSON Lines con timestamp UTC).

## Stack

- Python 3.13 · `python-telegram-bot>=21.0` · `PyYAML` · `httpx`
- LLM local opcional vía Ollama (`http://localhost:11434`)

## Instalación

```bash
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r requirements.txt   # Windows
# .venv/bin/pip install -r requirements.txt                    # Linux/macOS
```

## Configuración

Copiá `config.example.yaml` a `config.yaml`. El token se puede pasar por config o por variable de entorno:

```bash
BOT_TOKEN=TU_TOKEN_AQUI python run.py
# o alternativamente setearlo en config.yaml
```

> `config.yaml` está en `.gitignore` — nunca subas el token real al repo. Usá `config.example.yaml` como plantilla pública.

## Uso

```bash
PYTHONPATH=. .venv/Scripts/python.exe -m unittest discover -s tests -p "test_*.py"   # tests
BOT_CONFIG=config.yaml .venv/Scripts/python.exe run.py                               # correr el bot
```

## Comandos

| Comando | Acceso | Función |
|---|---|---|
| `/start`, `/help` | todos | Bienvenida y ayuda |
| `/announce <texto>` | admin | Publica anuncio |
| `/ban` (reply a msj) | admin | Banea al usuario |
| `/unban` (reply a msj) | admin | Des-banea al usuario |
| `/stats` | admin | Estadísticas básicas |

## Arquitectura

```
run.py                 # entry point: carga config, lanza polling
src/
  bot.py               # BotApp: enruta mensajes (moderación, FAQ, comandos)
  moderation.py        # RateLimiter + Moderator (frases, dominios, bans)
  faq.py               # FaqHandler: match por keywords + LLM opcional
  announce.py          # Announcements: anuncios solo para admins
  log.py               # EventLogger: JSONL en logs/events.jsonl
  config.example.yaml  # plantilla pública de config
tests/                 # tests unitarios (moderación, FAQ, logging)
```

## Roadmap

- Refuerzo con n8n self-host para automatizaciones externas.
- FAQ con LLM local activado por defecto.
- Multi-idioma (ES/EN).

## Contacto

nullforge — tooling open-source para comunidades web3.
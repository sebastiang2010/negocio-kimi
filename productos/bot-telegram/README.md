# Bot Telegram — Moderación + FAQ con IA (v1)

Bot de moderación para grupos de Telegram orientado a comunidades crypto/Web3.
Stack 100% gratuito y self-hosteable.

## Funciones (v1)

- **Moderación anti-spam**: rate limiting por usuario, filtros por palabras/frases,
  detección de links no permitidos, acciones configurables (warn / mute / ban).
- **FAQ inteligente**: responde preguntas frecuentes usando una base de conocimiento
  del proyecto (YAML). Matching por similitud; opcionalmente LLM local (Ollama)
  para respuestas con contexto.
- **Alertas y anuncios**: los admins pueden programar/enviar anuncios al grupo.
- **Logging**: todos los eventos (join, delete, warn, ban, faq) a JSONL para
  auditoría y métricas.

## Stack

- Telegram Bot API vía [`python-telegram-bot`](https://python-telegram-bot.org) v21
- Config en YAML, sin base de datos (JSONL para logs)
- (Opcional) Ollama local para FAQ con LLM — funciona sin LLM con matching por claves

## Estructura

```
productos/bot-telegram/
├── README.md
├── requirements.txt
├── config.example.yaml      # copiar a config.yaml y completar
├── .gitignore
├── run.py                   # entrypoint
└── src/
    ├── bot.py               # wiring de handlers
    ├── moderation.py        # anti-spam, filtros, acciones
    ├── faq.py               # FAQ con matching (+ hook LLM opcional)
    ├── announce.py          # anuncios de admins
    └── log.py               # logging estructurado JSONL
```

## Setup local

```bash
pip install -r requirements.txt
cp config.example.yaml config.yaml   # completar token + admins + faqs
python run.py
```

1. Crear bot con [@BotFather](https://t.me/BotFather) → obtener `BOT_TOKEN`.
2. Agregar el bot al grupo como **administrador** (permisos: delete, restrict, ban).
3. Completar `config.yaml` (admis por user_id numérico).

## Despliegue gratis

- Cualquier VPS free tier / Raspberry Pi / PC local con `python run.py`.
- Python 3.11+.

## Licencia

MIT — pensado como portfolio público.

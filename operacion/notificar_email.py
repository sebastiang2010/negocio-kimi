"""Notificador del worker al dueño por email directo (SMTP Gmail).
Uso: python operacion/notificar_email.py "texto del aviso"
Config: operacion/.mail_config (GITIGNORED — nunca commit)
  smtp_user = casilla emisora
  smtp_pass = app password de Gmail (16 letras)
  destinatario = mail real del dueño
Regla (AGENTS.md): max 1 mail por evento; solo P0 bloqueado, digest listo,
veredicto supervisor, resultado de bounty, credencial rotada.
"""
import sys, smtplib, ssl
from email.message import EmailMessage
from pathlib import Path

CFG = Path(__file__).parent / ".mail_config"

def load_config():
    cfg = {}
    for line in CFG.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        cfg[k.strip()] = v.strip()
    for req in ("smtp_user", "smtp_pass", "destinatario"):
        if req not in cfg:
            sys.exit(f"ERROR: falta '{req}' en {CFG}")
    return cfg

def main():
    texto = " ".join(sys.argv[1:]).strip() or "(sin texto)"
    cfg = load_config()
    msg = EmailMessage()
    msg["From"] = cfg["smtp_user"]
    msg["To"] = cfg["destinatario"]
    msg["Subject"] = "[negocio_kmi] aviso del worker"
    msg.set_content(texto + "\n")
    ctx = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ctx) as s:
        s.login(cfg["smtp_user"], cfg["smtp_pass"].replace(" ", ""))
        s.send_message(msg)
    print("EMAIL ENVIADO OK ->", cfg["destinatario"])

if __name__ == "__main__":
    if not CFG.exists():
        sys.exit(f"ERROR: no existe {CFG} (crearlo con smtp_user/smtp_pass/destinatario)")
    main()

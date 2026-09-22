#!/usr/bin/env python3
# dashboard_server.py — Tablero en vivo de la operación
#
# CÓMO USARLO (una sola vez por sesión de trabajo):
#   python operacion/dashboard_server.py
#   (si 'python' no funciona en Windows: py operacion/dashboard_server.py)
# Después abrí en tu navegador: http://localhost:8899
# La página se actualiza sola cada 15 minutos. Podés recargar con F5 cuando quieras.
# Para apagarlo: Ctrl+C en la terminal.
#
# No instala nada: usa solo la librería estándar de Python.
# Lee en vivo: SO/finanzas.md, operacion/submissions.md, operacion/estado.md,
# operacion/cola_humana.md y leads/. Si el agente actualiza los .md, el
# tablero lo muestra en el próximo refresh. El agente NO toca este archivo.

import http.server
from pathlib import Path
from datetime import datetime

BASE = Path(__file__).resolve().parent.parent  # raíz del proyecto
PORT = 8899
REFRESH_SEGUNDOS = 900  # 15 minutos


def leer(ruta):
    p = BASE / ruta
    try:
        return p.read_text(encoding="utf-8")
    except Exception:
        return ""


def tabla(lineas):
    """Devuelve las filas de datos de una tabla markdown."""
    filas = []
    for line in lineas:
        s = line.strip()
        if not s.startswith("|") or "---" in s:
            continue
        cols = [c.strip() for c in s.strip("|").split("|")]
        if cols and not any(h.lower() in ("id", "fecha") for h in cols[:1]):
            filas.append(cols)
    return filas


def datos():
    fin = leer("SO/finanzas.md")
    balance = "$0"
    for f in tabla(fin.splitlines()):
        if len(f) >= 6 and f[0].count("-") >= 2:  # filas con fecha
            balance = f[5]

    subs = []
    for f in tabla(leer("operacion/submissions.md").splitlines()):
        if len(f) >= 9 and len(f[0]) >= 6:
            subs.append({
                "id": f[0], "bounty": f[3], "link": f[4].strip("[]"),
                "monto": f[6], "anuncio": f[7], "estado": f[8], "notas": f[10] if len(f) > 10 else "",
            })

    leads_dir = BASE / "leads"
    n_leads = len([x for x in leads_dir.glob("*") if x.is_file() and x.name not in (".gitkeep", "fuentes.md")]) if leads_dir.exists() else 0

    estado = ""
    for line in leer("operacion/estado.md").splitlines():
        if "Tarea activa" in line:
            estado = line.split(":", 1)[-1].strip().strip("[]")
            break

    cola = leer("operacion/cola_humana.md").count("- [ ]")

    cobrado = balance
    en_juego = sum(float(s["monto"].replace("$", "").replace(".", "") or 0) for s in subs if "ENVIADA" in s["estado"].upper() or "ACEPTADA" in s["estado"].upper())
    return {"cobrado": cobrado, "en_juego": f"${en_juego:,.0f}".replace(",", "."),
            "subs": subs, "n_leads": n_leads, "estado": estado or "—", "cola": cola,
            "hora": datetime.now().strftime("%H:%M")}


def color_estado(e):
    e = e.upper()
    if "PAGADA" in e: return "#3fb950"
    if "ACEPTADA" in e: return "#3fb950"
    if "RECHAZADA" in e: return "#f85149"
    if "CADUCADA" in e: return "#8b949e"
    return "#d29922"


def render():
    d = datos()
    filas = "".join(
        f"<tr><td><a href='{s['link']}' target='_blank'>{s['bounty']}</a></td>"
        f"<td style='text-align:right'>{s['monto']}</td>"
        f"<td style='color:{color_estado(s['estado'])};font-weight:600'>{s['estado']}</td>"
        f"<td>{s['anuncio']}</td></tr>"
        for s in d["subs"]
    ) or "<tr><td colspan='4'>Sin submissions registradas todavía</td></tr>"

    return f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8">
<meta http-equiv="refresh" content="{REFRESH_SEGUNDOS}">
<title>Dashboard — nullforge_dev</title>
<style>
* {{ margin:0; padding:0; box-sizing:border-box; font-family:'Segoe UI',Arial,sans-serif; }}
body {{ background:#0d1117; color:#e6edf3; padding:24px; max-width:900px; margin:0 auto; }}
h1 {{ font-size:20px; }} .sub {{ color:#8b949e; font-size:13px; margin:4px 0 16px; }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(160px,1fr)); gap:10px; margin-bottom:18px; }}
.card {{ background:#161b22; border:1px solid #30363d; border-radius:8px; padding:12px 14px; }}
.label {{ font-size:11px; color:#8b949e; text-transform:uppercase; letter-spacing:.5px; }}
.value {{ font-size:26px; font-weight:bold; margin-top:4px; }}
.green {{ color:#3fb950; }} .yellow {{ color:#d29922; }} .blue {{ color:#58a6ff; }}
h2 {{ font-size:13px; color:#8b949e; margin:18px 0 8px; text-transform:uppercase; letter-spacing:.5px; }}
table {{ width:100%; border-collapse:collapse; font-size:13px; }}
th,td {{ padding:8px 10px; text-align:left; border-bottom:1px solid #21262d; }}
th {{ color:#8b949e; font-weight:normal; }} a {{ color:#58a6ff; text-decoration:none; }}
.nota {{ background:#161b22; border-left:3px solid #d29922; padding:10px 14px; font-size:13px; margin-top:14px; }}
</style></head><body>
<h1>Operación nullforge_dev</h1>
<div class="sub">En vivo · {d['hora']} hs · se actualiza solo cada 15 min · F5 para recargar ya</div>
<div class="grid">
  <div class="card"><div class="label">Cobrado (real)</div><div class="value green">{d['cobrado']}</div></div>
  <div class="card"><div class="label">En juego</div><div class="value yellow">{d['en_juego']}</div></div>
  <div class="card"><div class="label">MRR</div><div class="value blue">$0/mes</div></div>
  <div class="card"><div class="label">En vuelo</div><div class="value">{len(d['subs'])}</div></div>
  <div class="card"><div class="label">Leads en carpeta</div><div class="value">{d['n_leads']}</div></div>
</div>
<h2>Qué está haciendo el agente ahora</h2>
<div class="card" style="font-size:14px;">{d['estado']}</div>
<h2>Submissions</h2>
<table><tr><th>Bounty</th><th style="text-align:right">Monto</th><th>Estado</th><th>Anuncio</th></tr>{filas}</table>
<h2>Cola humana</h2>
<div class="card" style="font-size:14px;">{d['cola']} pendiente(s) de tu decisión → mirá operacion/cola_humana.md</div>
</body></html>"""


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        body = render().encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    print(f"Dashboard en vivo → http://localhost:{PORT}  (Ctrl+C para apagar)")
    http.server.HTTPServer(("127.0.0.1", PORT), Handler).serve_forever()

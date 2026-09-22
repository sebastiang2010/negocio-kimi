"""Entrypoint del bot."""

from pathlib import Path

import yaml

from src.bot import build_app


def main() -> None:
    cfg_path = Path(__file__).parent / "config.yaml"
    if not cfg_path.exists():
        raise SystemExit(
            "Falta config.yaml — copiá config.example.yaml y completá el token."
        )
    cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8"))
    app = build_app(cfg)
    print("Bot corriendo (Ctrl+C para frenar)...")
    app.run_polling()


if __name__ == "__main__":
    main()

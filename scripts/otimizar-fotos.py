#!/usr/bin/env python3
"""Converte as fotos de assets/ para WebP (máx. 1600px de largura).

Uso:  python3 scripts/otimizar-fotos.py
Lê   assets/gustavo-retrato.jpg (ou .jpeg/.png) e assets/gustavo-trabalhando.jpg
Gera assets/gustavo-retrato.webp e assets/gustavo-trabalhando.webp
Se "gustavo-trabalhando" não existir, usa o retrato também ali.
"""
from pathlib import Path
from PIL import Image, ImageOps

ASSETS = Path(__file__).resolve().parent.parent / "assets"
LARGURA_MAX = 1600
NOMES = ["gustavo-retrato", "gustavo-trabalhando"]
EXTS = [".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG"]


def origem(nome):
    for ext in EXTS:
        p = ASSETS / f"{nome}{ext}"
        if p.exists():
            return p
    return None


def converter(src, dst):
    img = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    if img.width > LARGURA_MAX:
        img = img.resize((LARGURA_MAX, round(img.height * LARGURA_MAX / img.width)), Image.LANCZOS)
    img.save(dst, "WEBP", quality=82, method=6)
    print(f"{src.name} -> {dst.name} ({img.width}x{img.height}, {dst.stat().st_size // 1024} KB)")


def main():
    retrato = origem("gustavo-retrato")
    if not retrato:
        raise SystemExit("Coloque assets/gustavo-retrato.jpg na pasta assets/ e rode de novo.")
    converter(retrato, ASSETS / "gustavo-retrato.webp")
    trabalhando = origem("gustavo-trabalhando") or retrato
    converter(trabalhando, ASSETS / "gustavo-trabalhando.webp")


if __name__ == "__main__":
    main()

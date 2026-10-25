#!/usr/bin/env python3
"""Zgradi igro tako, da fotografije vdela neposredno v HTML.

  index.html          samostojna stran, ki se odpre kar z diska
  dist/artifact.html  vsebina za objavo kot Claude artifact (brez lastnega <head>)

Zaženi:  python3 build.py
"""
import base64
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
PHOTOS = {
    '__IMG1__': 'lucky-roka.webp',
    '__IMG2__': 'lucky-nasmeh.webp',
    '__IMG3__': 'lucky-sprehod.webp',
}


def data_uri(name):
    return 'data:image/webp;base64,' + base64.b64encode((ROOT / 'slike' / name).read_bytes()).decode()


page = (ROOT / 'src' / 'lucky.html').read_text(encoding='utf-8')
for marker, name in PHOTOS.items():
    page = page.replace(marker, data_uri(name))

(ROOT / 'dist').mkdir(exist_ok=True)
(ROOT / 'dist' / 'artifact.html').write_text(page, encoding='utf-8')

head = (
    '<!doctype html>\n<html lang="sl">\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
)
(ROOT / 'index.html').write_text(head + page + '\n</html>\n', encoding='utf-8')
print('Zgrajeno: index.html in dist/artifact.html')

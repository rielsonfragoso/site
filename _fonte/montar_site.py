"""Gera a pasta 'dist' pronta para hospedar (Netlify, GitHub Pages) a partir das páginas do site."""
import os, re, shutil, sys
SRC = os.path.dirname(os.path.abspath(__file__)); DIST = os.path.join(SRC, "dist")
HEAD = ('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}'
        'body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n')
def wrap(html):
    i = html.find("</style>") + len("</style>")
    return HEAD + html[:i] + "\n</head>\n<body>\n" + html[i:] + "\n</body>\n</html>\n"
shutil.rmtree(DIST, ignore_errors=True)
for rel in ["index.html", "ingles-em-familia/index.html"]:
    os.makedirs(os.path.dirname(os.path.join(DIST, rel)) or DIST, exist_ok=True)
    open(os.path.join(DIST, rel), "w").write(wrap(open(os.path.join(SRC, rel)).read()))
shutil.copy(os.path.join(SRC, "ingles-em-familia/capa.jpg"), os.path.join(DIST, "ingles-em-familia/capa.jpg"))
open(os.path.join(DIST, "CNAME"), "w").write("rielsonfragoso.com.br\n")   # domínio do GitHub Pages
amostra = os.path.join(SRC, "..", "ebook", "Amostra_Gratis_Ingles_em_Familia.pdf")
if os.path.exists(amostra):   # rielsonfragoso.com.br/ingles-em-familia/amostra.pdf
    shutil.copy(amostra, os.path.join(DIST, "ingles-em-familia", "amostra.pdf"))
print("dist pronto")

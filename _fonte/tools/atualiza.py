"""Uso: python3 atualiza.py '<início exato do B(...)>' <foto_nova|-> <imagem|-> '<medidas>' <peso>
Troca a foto (se dada), acrescenta medidas/peso ao livro já cadastrado, reconstrói o site."""
import sys, re, subprocess
from PIL import Image, ImageOps
chave, foto, img, med, peso = sys.argv[1:6]
preco = sys.argv[6] if len(sys.argv) > 6 else None
D = "/home/claude/site/v2/livros_dados.py"
s = open(D).read()
assert s.count(chave) == 1, f"chave encontrada {s.count(chave)}x"
i = s.index(chave); d = 0; j = i + 1
while True:
    ch = s[j]
    if ch == '"': j = s.index('"', j + 1)
    elif ch == '(': d += 1
    elif ch == ')':
        d -= 1
        if d == 0: break
    j += 1
call = s[i:j]
if foto != "-":
    im = ImageOps.exif_transpose(Image.open(img)).convert("RGB")
    ImageOps.fit(im, (900, 1200)).save(f"/home/claude/site-repo/livros/img/{foto}.jpg", quality=86, optimize=True)
    args = re.match(r'(B\("(?:[^"]*)",\s*"(?:[^"]*)",\s*[\d.]+,\s*\d+,\s*(?:"[^"]*"|\w+),\s*)"([^"]*)"', call)
    assert args, call
    call = call[:args.end(1)] + f'"{foto}"' + call[args.end():]
if preco:
    call = re.sub(r'^(B\("[^"]*",\s*"[^"]*",\s*)[\d.]+', lambda m: m.group(1) + f"{float(preco.replace(',', '.')):.2f}", call)
call = re.sub(r',\s*medidas="[^"]*"', "", call); call = re.sub(r',\s*peso=\d+', "", call)
call += f', medidas="{med}", peso={peso}'
s = s[:i] + call + s[j:]
open(D, "w").write(s)
print(subprocess.run(["python3", "build.py"], cwd="/home/claude/site/v2", capture_output=True, text=True).stdout.strip()[-20:])
print(call[:160])

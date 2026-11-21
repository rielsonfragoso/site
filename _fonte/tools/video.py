"""Uso: python3 video.py <url> '<chave B(...)>=<segundo>' ...  -> liga o vídeo aos livros e reconstrói o site."""
import re, sys, subprocess
V = sys.argv[1].split("?")[0]
D = "/home/claude/site/v2/livros_dados.py"; s = open(D).read()
for arg in sys.argv[2:]:
    k, t = arg.rsplit("=", 1)
    assert s.count(k) == 1, (k, s.count(k))
    i = s.index(k); d = 0; j = i + 1
    while True:
        ch = s[j]
        if ch == '"': j = s.index('"', j + 1)
        elif ch == '(': d += 1
        elif ch == ')':
            d -= 1
            if d == 0: break
        j += 1
    call = re.sub(r',\s*video="[^"]*"', '', s[i:j]); call = re.sub(r',\s*video_t=\d+', '', call)
    s = s[:i] + call + f', video="{V}", video_t={int(t)}' + s[j:]
open(D, "w").write(s)
print(subprocess.run(["python3", "build.py"], cwd="/home/claude/site/v2", capture_output=True, text=True).stdout.strip()[-10:])

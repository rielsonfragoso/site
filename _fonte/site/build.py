"""Gera o site rielsonfragoso.com.br (direção B · Quadro & Caderno) em /home/claude/site-repo.
Páginas: / · /concursos/ · /sobre/   (a /ingles-em-familia/ tem build próprio em site/lp_v2)"""
import os, shutil, html, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import livros, aulas, politicas, datetime
from urllib.parse import quote
OUT = "/home/claude/site-repo"; HERE = os.path.dirname(os.path.abspath(__file__))
WA = "https://wa.me/5521964446262?text=" + quote("Oi, Rielson! Vim pelo site.")
YT = "https://www.youtube.com/@AcademiaMatem%C3%A1ticarj"; TG = "https://t.me/rielsonfragoso"; LT = "https://linktr.ee/academiamatematicarj"
IEF = "https://go.hotmart.com/E108477851B"
EMAIL = "academiamatematica.rj@gmail.com"
FORM_ENDPOINT = "https://formsubmit.co/ajax/" + EMAIL

def src(url, tag):
    if "hotmart" not in url and "hotm.art" not in url: return url
    return url + ("&" if "?" in url else "?") + "src=" + tag

EBOOKS = [  # título, detalhe, banca, link
    ("Mapa do RLM · Volume 1", "Raciocínio lógico com questões comentadas passo a passo", "Instituto Seleção", "https://go.hotmart.com/H104483701D"),
    ("Mapa do RLM · Volume 2", "Raciocínio lógico com questões comentadas passo a passo", "IBDO", "https://mapa-rlm-i4juerxq.manus.space"),
    ("Quebrando a Banca #1", "51 questões de matemática comentadas", "IDIB", "https://hotm.art/idib-matematica"),
    ("Quebrando a Banca · Matemática Básica", "Questões de matemática básica comentadas", "IDECAN", "https://hotmart.com/pt-br/marketplace/produtos/quebrando-a-banca-idecan-matematica-basica/G101803984M"),
]
SIMS = [  # título, cargo/detalhe, banca, link, destaque
    ("PRODERJ 2026", "Assistente Administrativo", "IBDO", "https://go.hotmart.com/W104324926I", True),
    ("TRT RJ 2025", "Conhecimentos Gerais · 35 questões · todos os cargos", "FCC", "https://go.hotmart.com/C98694845P?dp=1", True),
    ("UNIRIO 2025", "Assistente em Administração", "", "https://go.hotmart.com/C103584769A?dp=1", True),
    ("Nova Iguaçu 2025 · 2º simulado", "Técnico de Controle Interno", "Consulplan", "https://hotmart.com/pt-br/marketplace/produtos/2o-simulado-tecnico-de-controle-interno-2025-nova-iguacu-rj-instituto-consulplan/N98062683H", False),
    ("Nova Iguaçu 2025", "Técnico de Controle Interno", "Consulplan", "https://go.hotmart.com/H97645608B", False),
    ("Nova Iguaçu 2025", "Analista de Controle Interno Jurídico", "Consulplan", "https://go.hotmart.com/C98331270U?dp=1", False),
    ("Duque de Caxias 2025", "Agente de Combate às Endemias", "Consulplan", "https://hotmart.com/pt-br/marketplace/produtos/simulado-agente-de-combate-as-endemias-duque-de-caxias-rj-2025-instituto-consulplan/O98049432J", False),
    ("Magé 2025", "Professor II", "IAN", "https://go.hotmart.com/K97786315U?dp=1", False),
    ("Niterói 2025", "Guarda Municipal · 100 questões", "Selecon", "https://go.hotmart.com/W97110610T", False),
]
e = html.escape

ARROW = ('<svg class="arrow" viewBox="0 0 120 60" aria-hidden="true"><path d="M4 12 C 40 4, 80 14, 104 44" fill="none" stroke="currentColor" '
         'stroke-width="3" stroke-linecap="round"/><path d="M92 42 L105 46 L104 32" fill="none" stroke="currentColor" stroke-width="3" '
         'stroke-linecap="round" stroke-linejoin="round"/></svg>')

def head(title, desc, path, og="og-site.jpg", extra_css=""):
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:type" content="website"><meta property="og:locale" content="pt_BR">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">
<link rel="canonical" href="https://rielsonfragoso.com.br{path}">
<meta property="og:url" content="https://rielsonfragoso.com.br{path}"><meta property="og:image" content="https://rielsonfragoso.com.br/{og}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#1B2A4E">
<meta name="google-site-verification" content="aLdDBJ0eH36Q4Qbf-sTwIbmToy9CROETqgIYNNR8cwI" />
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&family=Nunito+Sans:wght@400;700&family=Caveat:wght@600&display=swap">
<link rel="stylesheet" href="/site.css">
<style>{extra_css}</style>
</head>
<body>
'''

def nav(cur):
    items = [("/", "Início"), ("/concursos/", "Concursos"), ("/ingles-em-familia/", "Inglês em Família"), ("/aulas/", "Resoluções"), ("/livros/", "Livros"), ("/#gratis", "Grátis"), ("/sobre/", "Sobre")]
    li = "".join(f'<li><a href="{h}"{" aria-current=\"page\"" if h == cur else ""}>{t}</a></li>' for h, t in items)
    return (f'<header class="nav"><div class="wrap"><a class="logo" href="/"><i>RF</i>Rielson Fragoso</a><nav aria-label="Principal"><ul>{li}</ul></nav></div></header>'
            '<script>(function(){var a=document.querySelector(".nav [aria-current]");if(a&&a.parentNode){var n=a.closest("nav");n.scrollLeft=Math.max(0,a.offsetLeft-n.clientWidth/2+a.offsetWidth/2);}})();</script>\n')

FOOT = f'''<footer>
  <div class="wrap">
    <div class="cols">
      <div class="stack" style="gap:10px"><a class="logo" href="/"><i>RF</i>Rielson Fragoso</a>
        <p>Material sério, bem explicado, para quem estuda por conta própria.</p>
        <p class="hand" style="color:var(--yellow)">Dúvida sobre um material? Me chama.</p></div>
      <div><h3>Contato</h3><ul>
        <li><a href="mailto:{EMAIL}">E-mail · {EMAIL}</a></li>
        <li><a href="{TG}" target="_blank" rel="noopener">Telegram · avisos de materiais</a></li>
        <li><a href="{YT}" target="_blank" rel="noopener">YouTube · Academia Matemática RJ</a></li>
        <li><a href="{LT}" target="_blank" rel="noopener">Todos os links</a></li></ul></div>
      <div><h3>Materiais</h3><ul>
        <li><a href="/concursos/">Concursos: e-books e simulados</a></li>
        <li><a href="/ingles-em-familia/">Inglês em Família</a></li>
        <li><a href="/aulas/">Resolução de questões em vídeo</a></li>
        <li><a href="/livros/">Livros usados à venda</a></li>
        <li><a href="/sobre/">Sobre mim</a></li>
        <li><a href="/trocas/">Trocas e devoluções</a></li>
        <li><a href="/privacidade/">Privacidade</a></li></ul></div>
    </div>
    <p class="copy">© 2026 Rielson Fragoso · Rio de Janeiro. E-books e simulados: pagamento pela Hotmart. Livros usados e resoluções: pagamento via Pix. · <a href="/trocas/">Trocas, devoluções e envio</a> · <a href="/privacidade/">Privacidade</a></p>
  </div>
</footer>
</body>
</html>
'''

def bub(letter_on):  # bolhas A–E com uma marcada
    return '<span class="bubbles" aria-hidden="true">' + "".join(
        f'<span class="{"on" if L == letter_on else ""}">{L}</span>' for L in "ABCDE") + '</span>'

def sim_card(t, d, banca, url, tag):
    b = f'<span class="banca">{e(banca)}</span>' if banca else '<span class="banca">Simulado</span>'
    return (f'<article class="card" data-banca="{e(banca or "Outras")}">{b}<h3>{e(t)}</h3><p class="meta">{e(d)}</p>'
            f'<a class="go" href="{e(src(url, tag))}" target="_blank" rel="noopener">Ver simulado</a></article>')

def ebook_card(t, d, banca, url, tag):
    return (f'<article class="card" data-banca="{e(banca)}"><span class="banca">{e(banca)}</span><h3>{e(t)}</h3><p class="meta">{e(d)}</p>'
            f'<a class="go" href="{e(src(url, tag))}" target="_blank" rel="noopener">Ver e-book</a></article>')

METHOD = f'''<ol class="method">
  <li>{bub("A")}<h3>Edital</h3><p>Leio o edital e a estrutura da prova do cargo: matérias, número de questões, peso.</p></li>
  <li>{bub("B")}<h3>Banca</h3><p>Seleciono questões reais da mesma banca, nos mesmos assuntos e no mesmo estilo.</p></li>
  <li>{bub("C")}<h3>Simulação</h3><p>Monto na mesma composição da prova, para você treinar tempo e estratégia.</p></li>
</ol>'''
METHOD_CSS = '''
.method{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.method li{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:20px;display:flex;flex-direction:column;gap:8px;min-width:0}
.method p{color:var(--muted)}
.stamp{display:inline-block;align-self:flex-start;border:2.5px solid var(--red);color:var(--red);border-radius:10px;padding:10px 16px;
  font-family:var(--display);font-weight:700;font-size:clamp(1rem,2.4vw,1.25rem);line-height:1.3;transform:rotate(-1.5deg);max-width:640px;background:var(--surface)}
@media (max-width:760px){.method{grid-template-columns:1fr}}
'''

# ---------------- home ----------------
HOME_CSS = METHOD_CSS + '''
.hero{padding-block:clamp(48px,8vw,96px) clamp(40px,6vw,72px)}
.hero .top{display:grid;grid-template-columns:1.4fr .6fr;gap:24px;align-items:center}
.hero .top>*{min-width:0}
.hero h1{color:var(--chalk)}
.hero h1 span{color:var(--yellow)}
.mono{justify-self:center;width:min(200px,40vw);aspect-ratio:1;border:2px dashed var(--chalk-dim);border-radius:50%;display:grid;place-items:center;
  font-family:var(--display);font-weight:700;font-size:clamp(3rem,8vw,4.6rem);color:var(--yellow);position:relative}
.mono small{position:absolute;bottom:-38px;left:50%;transform:translateX(-50%) rotate(-3deg);white-space:nowrap;font-family:var(--hand);font-size:1.35rem;color:var(--chalk-dim);font-weight:600}
.mono.foto{border:none;padding:0}
.mono.foto img{width:100%;height:100%;border-radius:50%;object-fit:cover;object-position:50% 20%;border:3px solid var(--yellow);box-shadow:0 18px 40px -18px rgba(0,0,0,.6)}
@media (max-width:760px){.hero .mono.foto{display:grid;width:150px;justify-self:start;margin-bottom:34px}.hero .mono.foto small{left:0;transform:rotate(-3deg)}}
.pick{margin-top:clamp(36px,5vw,56px);display:flex;flex-direction:column;gap:10px}
.pick .hand{display:flex;align-items:flex-end;gap:8px}
.arrow{width:72px;height:36px;color:var(--yellow);flex:none}
.doors{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.door{border-radius:var(--r);padding:24px;text-decoration:none;display:flex;flex-direction:column;gap:8px;min-width:0;transition:transform .15s;position:relative;overflow:hidden}
.door:hover{transform:translateY(-3px)}
.door b{font-family:var(--display);font-size:clamp(1.25rem,2.6vw,1.6rem);line-height:1.2}
.door span{color:var(--muted)}
.door em{font-style:normal;font-family:var(--display);font-weight:600;margin-top:6px}
.door.c{background-color:#FFFFFF;color:#16233F;background-image:linear-gradient(#D9E1EE 1px,transparent 1px),linear-gradient(90deg,#D9E1EE 1px,transparent 1px);background-size:22px 22px}
.door.c span{color:#56607A}.door.c em{color:#1B2A4E}
.door.f{background:#FBF7EF;color:#2F3A33;padding-right:clamp(24px,24%,150px)}
.door.f span{color:#5F6B63}.door.f em{color:#4E7D5B}
.door.f img{position:absolute;right:-10px;top:16px;width:clamp(90px,20%,130px);transform:rotate(6deg);border-radius:8px;box-shadow:0 10px 24px -12px rgba(0,0,0,.4)}
@media (prefers-reduced-motion:reduce){.door{transition:none}.door:hover{transform:none}}
.feat{display:grid;grid-template-columns:.75fr 1.25fr;gap:clamp(24px,5vw,56px);align-items:center}
.feat>*{min-width:0}
.feat img{border-radius:12px;box-shadow:0 24px 50px -24px rgba(30,50,35,.45);transform:rotate(-1.5deg);max-width:270px;justify-self:center;width:100%}
.ief .eyebrow{color:var(--green)}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chips span{background:var(--green-soft);color:var(--green);font-weight:700;font-size:.88rem;padding:5px 12px;border-radius:999px}
.row{display:flex;flex-wrap:wrap;gap:12px;align-items:center}
.free .card{gap:8px;text-decoration:none}
.free .card b{font-family:var(--display);font-size:1.1rem}
.free .card span{color:var(--muted)}
.free .card em{font-style:normal;font-family:var(--display);font-weight:600;margin-top:auto;color:var(--navy)}
:root[data-theme="dark"] .free .card em{color:var(--yellow)}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]) .free .card em{color:var(--yellow)}}
.about{display:grid;grid-template-columns:auto 1fr;gap:clamp(20px,4vw,40px);align-items:start;max-width:900px}
.about>*{min-width:0}
.about .rf{width:96px;height:96px;border-radius:24px;background:var(--navy);color:var(--yellow);border:2px solid var(--yellow);display:grid;place-items:center;font:700 2rem var(--display);transform:rotate(-3deg)}
@media (max-width:760px){.hero .top,.doors,.feat{grid-template-columns:1fr}.mono{display:none}.feat img{max-width:240px}}
@media (max-width:520px){.about{grid-template-columns:1fr}.door.f{padding-right:92px}.door.f img{width:76px}}
'''
HOME_LD = '<script type="application/ld+json">' + '{"@context": "https://schema.org", "@graph": [{"@type": "Person", "@id": "https://rielsonfragoso.com.br/#rielson", "name": "Rielson Fragoso", "url": "https://rielsonfragoso.com.br/", "jobTitle": "Educador de matemática e empreendedor", "address": {"@type": "PostalAddress", "addressLocality": "Rio de Janeiro", "addressRegion": "RJ", "addressCountry": "BR"}, "sameAs": ["https://www.youtube.com/@AcademiaMatem%C3%A1ticarj", "https://t.me/rielsonfragoso", "https://linktr.ee/academiamatematicarj", "https://hotmart.com/pt-br/marketplace/especialista/rielson-fragoso/EEWWNW3SCW"]}, {"@type": "WebSite", "url": "https://rielsonfragoso.com.br/", "name": "Rielson Fragoso · Academia Matemática RJ", "inLanguage": "pt-BR", "publisher": {"@id": "https://rielsonfragoso.com.br/#rielson"}}]}' + '</script>'

def mono():
    """Foto do Rielson no topo da home (se existir rielson.jpg ao lado do build); senão, o monograma RF."""
    src = os.path.join(HERE, "rielson.jpg")
    if not os.path.exists(src):
        return '<div class="mono" aria-hidden="true">RF<small>empreendedor e educador</small></div>'
    from PIL import Image, ImageOps
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    lado = min(im.size); x = (im.width - lado) // 2; y = max(0, min((im.height - lado) // 4, im.height - lado))
    os.makedirs(os.path.join(OUT, "img"), exist_ok=True)
    im.crop((x, y, x + lado, y + lado)).resize((440, 440), Image.LANCZOS).save(os.path.join(OUT, "img", "rielson.webp"), quality=84)
    return ('<div class="mono foto"><img src="/img/rielson.webp" width="440" height="440" '
            'alt="Rielson Fragoso, de braços cruzados, sorrindo"><small>empreendedor e educador</small></div>')

def home():
    MONO = mono()
    feat = "".join(sim_card(t, d, b, u, "site_home") for t, d, b, u, f in SIMS if f)
    return head("Rielson Fragoso · Matemática para concursos e inglês em família",
                "Simulados e e-books de matemática e raciocínio lógico para concursos, e o e-book Inglês em Família para pais e filhos.", "/", extra_css=HOME_CSS) + nav("/") + HOME_LD + f'''
<main>
<section class="board hero">
  <div class="wrap">
    <div class="top">
      <div class="stack">
        <span class="eyebrow">Rielson Fragoso · Academia Matemática RJ</span>
        <h1>Matemática para <span class="chalk-u">passar</span>.<br>Inglês para aprender <span class="chalk-u">em família</span>.</h1>
        <p class="lead">Faço materiais para quem estuda por conta própria: simulados e questões comentadas para concursos, e um jeito leve de aprender inglês com os filhos.</p>
      </div>
      {MONO}
    </div>
    <div class="pick">
      <p class="hand">{ARROW} escolha por onde começar</p>
      <div class="doors">
        <a class="door c" href="/concursos/"><b>Vai fazer concurso?</b><span>Simulados montados a partir do edital e e-books de questões comentadas da banca.</span><em>Ver materiais de concursos →</em></a>
        <a class="door f" href="/ingles-em-familia/"><b>Quer aprender inglês com seus filhos?</b><span>Sessões de 30 minutos com um desenho da Netflix. Você não precisa saber inglês.</span><em>Conhecer o Inglês em Família →</em><img src="/ingles-em-familia/capa.jpg" alt="" width="637" height="900"></a>
      </div>
    </div>
  </div>
</section>

<section class="grid-paper" id="concursos">
  <div class="wrap stack" style="gap:22px">
    <span class="eyebrow">Concursos · Matemática e Raciocínio Lógico</span>
    <h2>Simulados feitos para a prova que você vai fazer</h2>
    <p class="stamp">“Mais realista do que isso, só se eu entregasse a prova antes da hora.” <small style="display:block;font-size:.72em;font-weight:600;opacity:.85">— Rielson Fragoso, sobre os simulados</small></p>
    {METHOD}
    <h3 style="margin-top:8px">Alguns simulados</h3>
    <div class="cards">{feat}</div>
    <div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn" href="/concursos/">Ver todos os 13 materiais →</a><a class="btn line" href="/concursos/#pedir">Pedir o simulado do meu concurso</a><a class="btn line" href="/aulas/">Resolução de questões em vídeo</a></div>
  </div>
</section>

<section class="plain ief">
  <div class="wrap feat">
    <img src="/ingles-em-familia/capa.jpg" width="637" height="900" alt="Capa do e-book Inglês em Família, Volume 1" loading="lazy">
    <div class="stack">
      <span class="eyebrow">Novo · E-book interativo</span>
      <h2>Inglês em Família · Volume 1</h2>
      <p class="lead">Pais e filhos aprendendo inglês juntos com os episódios de <i>Trash Truck</i> (<i>Zé Coleta</i>). 5 palavras, o episódio em inglês e uma revisão rápida. Mesmo que você não saiba inglês.</p>
      <div class="chips"><span>28 episódios</span><span>140 palavras</span><span>30 min por sessão</span><span>Garantia de 7 dias</span></div>
      <div class="row"><a class="btn green" href="/ingles-em-familia/">Testar um capítulo grátis</a><a class="btn line" style="color:var(--green)" href="{src(IEF, "site_home")}" target="_blank" rel="noopener">Comprar · R$ 24,90</a></div>
    </div>
  </div>
</section>

<section id="gratis">
  <div class="wrap stack" style="gap:22px">
    <span class="eyebrow">Grátis</span>
    <h2>Comece sem gastar nada</h2>
    <div class="cards free">
      <a class="card" href="{YT}" target="_blank" rel="noopener"><b>Canal no YouTube</b><span>Matemática para todas as idades: das Olimpíadas Mirins aos concursos públicos.</span><em>Assistir →</em></a>
      <a class="card" href="{TG}" target="_blank" rel="noopener"><b>Canal no Telegram</b><span>Avisos de novos simulados, materiais e aulas, direto no celular.</span><em>Entrar no canal →</em></a>
      <a class="card" href="/ingles-em-familia/amostra.pdf" target="_blank" rel="noopener"><b>Capítulo grátis de inglês</b><span>O Capítulo 5 do Inglês em Família completo, interativo, para fazer hoje com a família.</span><em>Baixar a amostra →</em></a>
    </div>
  </div>
</section>

<section class="grid-paper">
  <div class="wrap about">
    <div class="rf" aria-hidden="true">RF</div>
    <div class="stack">
      <span class="eyebrow">Sobre</span>
      <h2>Empreendedor no mundo real. Educador no digital.</h2>
      <p>Desde 2019 empreendo com a minha esposa no ramo de banho e tosa e transporte pet. Em paralelo, fundei em 2024 a Academia Matemática RJ, meu projeto de educação, com matemática das Olimpíadas Mirins aos concursos públicos. Dos estudos com as minhas filhas nasceu o Inglês em Família.</p>
      <div><a class="btn line" href="/sobre/">Conhecer a minha história →</a></div>
    </div>
  </div>
</section>
</main>
''' + FOOT

# ---------------- concursos ----------------
CONC_CSS = METHOD_CSS + '''
.phero{padding-block:clamp(44px,7vw,80px)}
.phero h1{color:var(--chalk);font-size:clamp(2rem,5vw,3.1rem)}
.filters{display:flex;flex-wrap:wrap;gap:8px}
.filters button{font:600 .9rem var(--display);border:1.5px solid var(--line);background:var(--surface);color:var(--muted);border-radius:999px;padding:7px 14px;cursor:pointer;display:inline-flex;gap:8px;align-items:center}
.filters button::before{content:"";width:12px;height:12px;border-radius:50%;border:1.5px solid currentColor}
.filters button[aria-pressed="true"]{border-color:var(--navy);color:var(--ink)}
.filters button[aria-pressed="true"]::before{background:var(--navy);border-color:var(--navy)}
:root[data-theme="dark"] .filters button[aria-pressed="true"]{border-color:var(--yellow)}
:root[data-theme="dark"] .filters button[aria-pressed="true"]::before{background:var(--yellow);border-color:var(--yellow)}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]) .filters button[aria-pressed="true"]{border-color:var(--yellow)}
 :root:not([data-theme="light"]) .filters button[aria-pressed="true"]::before{background:var(--yellow);border-color:var(--yellow)}}
.empty{color:var(--muted)}
.ask{background:var(--yellow-soft);border-radius:var(--r);padding:clamp(20px,4vw,36px);display:flex;flex-direction:column;gap:20px;scroll-margin-top:90px}
.pform{display:flex;flex-direction:column;gap:14px}
.f2{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.f2>*{min-width:0}
.pform label{display:flex;flex-direction:column;gap:6px;font-family:var(--display);font-weight:600;font-size:.9rem}
.pform input,.pform textarea{font:inherit;font-family:var(--body);font-weight:400;font-size:1rem;color:var(--ink);background:var(--surface);border:1.5px solid var(--line);border-radius:10px;padding:11px 12px;width:100%}
.pform input:focus,.pform textarea:focus{outline:none;border-color:var(--navy);box-shadow:0 0 0 3px color-mix(in srgb,var(--yellow) 55%,transparent)}
.pform input[aria-invalid="true"]{border-color:var(--red)}
.hp{position:absolute;left:-9999px;width:1px;height:1px;opacity:0}
.factions{display:flex;flex-wrap:wrap;gap:10px 16px;align-items:center}
.factions .btn{border:0;cursor:pointer;font-size:1rem}
.factions .btn[disabled]{opacity:.6;cursor:wait}
.fnote{font-size:.88rem;color:var(--muted)}
.fmsg{font-weight:700;padding:12px 14px;border-radius:10px;background:var(--surface);border-left:4px solid var(--green)}
.fmsg.err{border-left-color:var(--red)}
.alt{font-size:.95rem;color:var(--muted)}
.alt a{color:var(--ink)}
@media (max-width:640px){.f2{grid-template-columns:1fr}}
.tg{background:var(--yellow-soft);border-radius:var(--r);padding:22px;display:flex;flex-wrap:wrap;gap:12px 20px;align-items:center;justify-content:space-between}
.tg p{flex:1 1 280px;min-width:0}
'''
def concursos():
    bancas = sorted({b for *_, b, _ in EBOOKS} | {b or "Outras" for _, _, b, _, _ in SIMS}, key=lambda x: (x == "Outras", x))
    chips = '<button type="button" aria-pressed="true" data-f="*">Todas</button>' + "".join(
        f'<button type="button" aria-pressed="false" data-f="{e(b)}">{e(b)}</button>' for b in bancas)
    sims = "".join(sim_card(t, d, b, u, "site_concursos") for t, d, b, u, f in SIMS)
    ebs = "".join(ebook_card(t, d, b, u, "site_concursos") for t, d, b, u in EBOOKS)
    js = '''<script>
(function(){
  var btns=[].slice.call(document.querySelectorAll('.filters button'));
  var cards=[].slice.call(document.querySelectorAll('[data-banca]'));
  btns.forEach(function(b){b.addEventListener('click',function(){
    var f=b.getAttribute('data-f');
    btns.forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});
    cards.forEach(function(c){c.hidden=!(f==='*'||c.getAttribute('data-banca')===f)});
    ['ebooks','simulados'].forEach(function(id){var s=document.getElementById(id);
      var vis=s.querySelectorAll('[data-banca]:not([hidden])').length; s.querySelector('.empty').hidden=vis>0;});
  });});
  var f=document.getElementById('form-pedido'), msg=document.getElementById('fmsg');
  if(f){f.addEventListener('submit',function(ev){
    ev.preventDefault();
    var req=[f.concurso,f.cargo], ok=true;
    req.forEach(function(i){var bad=!i.value.trim(); i.setAttribute('aria-invalid',bad?'true':'false'); if(bad&&ok){i.focus();ok=false;}});
    if(!ok){show('Preencha o concurso e o cargo, por favor.',true);return;}
    if(f._honey.value){return;}
    var data={}; [].forEach.call(f.elements,function(el){if(el.name&&el.name!=='_honey')data[el.name]=el.value.trim();});
    data._subject='Pedido de simulado: '+data.concurso+' · '+data.cargo;
    data._template='table'; data._captcha='false'; data.origem='rielsonfragoso.com.br/concursos';
    var btn=f.querySelector('button[type=submit]'); btn.disabled=true; btn.textContent='Enviando…';
    fetch('__ENDPOINT__',{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify(data)})
      .then(function(r){return r.json().then(function(j){if(!r.ok||String(j.success)==='false')throw new Error(j.message||'erro');});})
      .then(function(){f.reset();show('Pedido enviado! Obrigado. Se você deixou um contato, eu aviso quando o simulado sair.',false);})
      .catch(function(){
        var body='Concurso: '+data.concurso+'%0ACargo: '+data.cargo+'%0ABanca: '+data.banca+'%0AData da prova: '+data.data_prova+'%0ANome: '+data.nome+'%0AContato: '+data.contato+'%0A%0A'+data.mensagem;
        msg.innerHTML='Não consegui enviar por aqui. <a href="mailto:__EMAIL__?subject='+encodeURIComponent(data._subject)+'&body='+body.replace(/ /g,'%20')+'">Toque aqui para mandar por e-mail</a> ou escreva para __EMAIL__.';
        msg.className='fmsg err'; msg.hidden=false;})
      .then(function(){btn.disabled=false;btn.textContent='Enviar pedido';});
  });}
  function show(t,err){msg.textContent=t;msg.className='fmsg'+(err?' err':'');msg.hidden=false;}
})();
</script>'''.replace('__ENDPOINT__', FORM_ENDPOINT).replace('__EMAIL__', EMAIL)
    return head("Concursos · Simulados e e-books de matemática | Rielson Fragoso",
                "Simulados montados a partir do edital com questões reais da banca e e-books de matemática e raciocínio lógico comentados.",
                "/concursos/", extra_css=CONC_CSS) + nav("/concursos/") + f'''
<main>
<section class="board phero">
  <div class="wrap stack">
    <span class="eyebrow">Concursos · Matemática e Raciocínio Lógico</span>
    <h1>Treine com a prova que você vai fazer</h1>
    <p class="lead">Cada simulado é montado a partir do edital, com questões escolhidas a dedo entre provas anteriores da própria banca. O objetivo é você chegar no dia da prova sem surpresas.</p>
  </div>
</section>
<section class="grid-paper">
  <div class="wrap stack" style="gap:22px">
    <p class="stamp">“Mais realista do que isso, só se eu entregasse a prova antes da hora.” <small style="display:block;font-size:.72em;font-weight:600;opacity:.85">— Rielson Fragoso, sobre os simulados</small></p>
    {METHOD}
  </div>
</section>
<section style="padding-top:clamp(36px,5vw,56px)">
  <div class="wrap stack" style="gap:26px">
    <div class="stack" style="gap:10px"><span class="eyebrow">Filtrar por banca</span><div class="filters" role="group" aria-label="Filtrar por banca">{chips}</div></div>
    <div class="stack" id="simulados"><h2>Simulados</h2><div class="cards">{sims}</div><p class="empty" hidden>Nenhum simulado desta banca por enquanto.</p></div>
    <div class="stack" id="ebooks"><h2>E-books de questões comentadas</h2><p class="lead">Soluções passo a passo, com o meu jeito de explicar.</p><div class="cards">{ebs}</div><p class="empty" hidden>Nenhum e-book desta banca por enquanto.</p></div>
    <div class="ask" id="pedir">
      <div class="stack" style="gap:10px">
        <span class="eyebrow">Seu concurso não está aqui?</span>
        <h2>Peça o simulado do seu concurso</h2>
        <p class="lead">Me diga qual concurso e cargo você vai fazer. Os pedidos mostram onde está a procura, e os concursos mais pedidos ganham simulado primeiro. Se você deixar um contato, eu aviso quando o seu sair.</p>
        <p class="hand" style="color:var(--red)">quanto mais gente pedir, mais rápido sai!</p>
      </div>
      <form id="form-pedido" class="pform" novalidate>
        <div class="f2">
          <label>Concurso / órgão *<input name="concurso" required maxlength="120" placeholder="Ex.: Prefeitura de Maricá 2026"></label>
          <label>Cargo *<input name="cargo" required maxlength="120" placeholder="Ex.: Assistente Administrativo"></label>
        </div>
        <div class="f2">
          <label>Banca (se souber)<input name="banca" maxlength="60" placeholder="Ex.: Consulplan"></label>
          <label>Data da prova (se souber)<input name="data_prova" maxlength="40" placeholder="Ex.: março de 2027"></label>
        </div>
        <div class="f2">
          <label>Seu nome<input name="nome" maxlength="80" autocomplete="name"></label>
          <label>E-mail ou WhatsApp para eu te avisar<input name="contato" maxlength="120" autocomplete="email"></label>
        </div>
        <label>Quer comentar algo? (opcional)<textarea name="mensagem" rows="3" maxlength="800" placeholder="Ex.: quero focar em matemática e raciocínio lógico"></textarea></label>
        <input type="text" name="_honey" tabindex="-1" autocomplete="off" class="hp" aria-hidden="true">
        <div class="factions">
          <button class="btn" type="submit">Enviar pedido</button>
          <span class="fnote">Seu contato é usado só para avisar sobre esse material.</span>
        </div>
        <p class="fmsg" id="fmsg" role="status" hidden></p>
      </form>
      <p class="alt">Prefere outro canal? Escreva para <a href="mailto:{EMAIL}">{EMAIL}</a> ou entre no <a href="{TG}" target="_blank" rel="noopener">canal do Telegram</a> para saber dos lançamentos.</p>
    </div>

  </div>
</section>
</main>
{js}
''' + FOOT

# ---------------- sobre ----------------
SOBRE_CSS = '''
.phero{padding-block:clamp(44px,7vw,80px)}
.phero h1{color:var(--chalk);font-size:clamp(2rem,5vw,3.1rem)}
.prose{max-width:68ch;display:flex;flex-direction:column;gap:16px;font-size:1.1rem}
.fronts{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.fronts>*{min-width:0}
.front{border-radius:var(--r);padding:26px;display:flex;flex-direction:column;gap:12px;border:1px solid var(--line);background:var(--surface)}
.front .tag{font-family:var(--hand);font-size:1.6rem;font-weight:600;line-height:1;color:var(--red)}
.front ul{margin:0;padding-left:1.1em;display:flex;flex-direction:column;gap:6px;color:var(--muted)}
.front.digital{border:2px solid var(--navy)}
:root[data-theme="dark"] .front.digital{border-color:var(--yellow)}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]) .front.digital{border-color:var(--yellow)}}
.ages{display:flex;flex-wrap:wrap;align-items:center;gap:8px;font-family:var(--display);font-weight:600;font-size:.9rem}
.ages span{background:var(--yellow-soft);border-radius:999px;padding:5px 12px}
.ages i{font-style:normal;color:var(--muted)}
.belief{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.belief>div{border-top:3px solid var(--yellow);padding-top:14px;display:flex;flex-direction:column;gap:6px;min-width:0}
.belief p{color:var(--muted)}
.two{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.two>*{min-width:0}
@media (max-width:760px){.fronts,.belief,.two{grid-template-columns:1fr}}
'''
def sobre():
    return head("Sobre · Rielson Fragoso", "Empreendedor no Rio de Janeiro: um negócio presencial de banho e tosa e transporte pet e, em paralelo, projetos digitais de educação, com a Academia Matemática RJ à frente.",
                "/sobre/", extra_css=SOBRE_CSS) + nav("/sobre/") + f'''
<main>
<section class="board phero">
  <div class="wrap stack">
    <span class="eyebrow">Sobre</span>
    <h1>Empreendedor no mundo real. Educador no digital.</h1>
    <p class="lead">Durante o dia, cuido de um negócio de verdade, com clientes, agenda e contas para pagar. Em paralelo, construo projetos de educação que ajudam gente de todas as idades a estudar melhor.</p>
    <p class="hand">— Rielson Fragoso, Ilha do Governador, Rio de Janeiro</p>
  </div>
</section>
<section>
  <div class="wrap prose">
    <p>Antes de empreender, trabalhei em aeroporto, farmácia e padaria. Aprendi cedo o valor de atender bem, de cumprir horário e de fazer a conta fechar no fim do mês.</p>
    <p>Em 2019 comecei a empreender junto com a minha esposa, no ramo de banho e tosa e transporte pet. É o negócio que sustenta a nossa casa e onde aprendi, na prática, a vender soluções, cuidar de cliente e crescer com pé no chão.</p>
    <p>Em paralelo, nunca larguei a vontade de ensinar. Em 2024 criei a <b>Academia Matemática RJ</b>, meu principal projeto digital, e de lá vieram os e-books, os simulados e, mais recentemente, o <b>Inglês em Família</b>, criado a partir dos estudos com as minhas filhas.</p>
  </div>
</section>
<section class="grid-paper">
  <div class="wrap stack" style="gap:26px">
    <span class="eyebrow">Duas frentes</span>
    <h2>O presencial paga as contas. O digital constrói o futuro.</h2>
    <div class="fronts">
      <div class="front">
        <span class="tag">presencial</span>
        <h3>Banho e tosa e transporte pet</h3>
        <p>O negócio que toco com a minha esposa desde 2019 e minha principal fonte de renda.</p>
        <ul><li>Banho e tosa</li><li>Táxi dog e transporte particular de pets</li><li>Soluções de transporte sob medida para cada cliente</li></ul>
      </div>
      <div class="front digital">
        <span class="tag">digital</span>
        <h3>Academia Matemática RJ e produtos educacionais</h3>
        <p>Meu projeto de conteúdo educacional, com matemática para todas as idades.</p>
        <div class="ages"><span>Olimpíadas Mirins · a partir do 2º ano</span><i>→</i><span>Concursos públicos</span></div>
        <ul><li>Canal no YouTube com aulas e resoluções</li><li>E-books de questões comentadas e simulados de concursos</li><li>Inglês em Família, para pais e filhos</li></ul>
      </div>
    </div>
  </div>
</section>
<section>
  <div class="wrap stack" style="gap:26px">
    <span class="eyebrow">Como eu trabalho</span>
    <h2>O que o balcão me ensinou e eu levo para os materiais</h2>
    <div class="belief">
      <div><h3>Resolver o problema do cliente</h3><p>Material bom é o que funciona para quem vai usar. Cada simulado é montado para a prova real, cada capítulo para caber na rotina.</p></div>
      <div><h3>Prometer só o que entrego</h3><p>Sem promessa milagrosa. Eu digo o que o material faz e o que não faz, e ofereço garantia.</p></div>
      <div><h3>Crescer com consistência</h3><p>Nada aqui surgiu de uma vez. É um material de cada vez, um aluno de cada vez, do mesmo jeito que se constrói um negócio.</p></div>
    </div>
  </div>
</section>
<section class="plain">
  <div class="wrap stack" style="gap:22px">
    <h2>Conheça os projetos</h2>
    <div class="two">
      <a class="card" href="/concursos/" style="text-decoration:none"><span class="banca">Concursos</span><h3>Simulados e e-books de matemática</h3><p class="meta">Para quem vai fazer prova de concurso e quer treinar com o estilo real da banca.</p><span class="go" style="font-family:var(--display);font-weight:600;margin-top:auto">Ver materiais →</span></a>
      <a class="card" href="/ingles-em-familia/" style="text-decoration:none"><span class="banca">Família</span><h3>Inglês em Família</h3><p class="meta">Para pais e filhos que querem começar o inglês juntos, mesmo sem saber nada.</p><span class="go" style="font-family:var(--display);font-weight:600;margin-top:auto">Conhecer →</span></a>
    </div>
    <div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn" href="mailto:{EMAIL}">Falar comigo por e-mail</a><a class="btn line" href="{YT}" target="_blank" rel="noopener">Ver o canal no YouTube</a></div>
  </div>
</section>
</main>
''' + FOOT

def og():
    from PIL import Image, ImageDraw, ImageFont
    F = "/usr/share/fonts/truetype/google-fonts/Poppins-"
    im = Image.new("RGB", (1200, 630), "#1B2A4E"); d = ImageDraw.Draw(im)
    d.rounded_rectangle((24, 24, 1176, 606), radius=10, outline="#F2C230", width=3)
    d.rounded_rectangle((80, 90, 180, 190), radius=22, outline="#F2C230", width=4)
    d.text((130, 140), "RF", font=ImageFont.truetype(F + "Bold.ttf", 46), fill="#F2C230", anchor="mm")
    d.text((210, 115), "Rielson Fragoso", font=ImageFont.truetype(F + "Bold.ttf", 44), fill="#F4F1E8")
    d.text((210, 168), "Academia Matemática RJ", font=ImageFont.truetype(F + "Medium.ttf", 26), fill="#C9CEDB")
    y = 270
    for l, c in [("Matemática para passar.", "#F4F1E8"), ("Inglês para aprender em família.", "#F2C230")]:
        d.text((80, y), l, font=ImageFont.truetype(F + "Bold.ttf", 60), fill=c); y += 86
    d.text((80, 480), "Simulados · e-books de questões comentadas · Inglês em Família", font=ImageFont.truetype(F + "Medium.ttf", 26), fill="#C9CEDB")
    im.save(os.path.join(OUT, "og-site.jpg"), quality=85)

if __name__ == "__main__":
    for rel, fn in [("index.html", home), ("concursos/index.html", concursos), ("sobre/index.html", sobre), ("livros/index.html", lambda: livros.page(head, nav, FOOT)), ("aulas/index.html", lambda: aulas.page(head, nav, FOOT)), ("privacidade/index.html", lambda: politicas.privacidade(head, nav, FOOT)), ("trocas/index.html", lambda: politicas.trocas(head, nav, FOOT)), ("404.html", lambda: politicas.nao_encontrada(head, nav, FOOT))]:
        p = os.path.join(OUT, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, "w").write(fn())
    shutil.copy(os.path.join(HERE, "site.css"), os.path.join(OUT, "site.css"))
    open(os.path.join(OUT, "favicon.svg"), "w").write(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#1B2A4E"/>'
        '<rect x="5" y="5" width="54" height="54" rx="10" fill="none" stroke="#F2C230" stroke-width="3"/>'
        '<text x="32" y="42" font-family="Arial,Helvetica,sans-serif" font-weight="700" font-size="26" fill="#F2C230" text-anchor="middle">RF</text></svg>')
    open(os.path.join(OUT, "robots.txt"), "w").write("User-agent: *\nAllow: /\nSitemap: https://rielsonfragoso.com.br/sitemap.xml\n")
    open(os.path.join(OUT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        + "".join(f"<url><loc>https://rielsonfragoso.com.br{u}</loc><lastmod>{datetime.date.today().isoformat()}</lastmod></url>" for u in ["/", "/concursos/", "/ingles-em-familia/", "/sobre/", "/livros/", "/aulas/", "/trocas/", "/privacidade/"]) + "</urlset>\n")
    extra = livros.build(OUT, head, nav, FOOT)
    sm = open(os.path.join(OUT, 'sitemap.xml')).read().replace('</urlset>', ''.join(f'<url><loc>https://rielsonfragoso.com.br{u}</loc><lastmod>{datetime.date.today().isoformat()}</lastmod></url>' for u in extra) + '</urlset>')
    open(os.path.join(OUT, 'sitemap.xml'), 'w').write(sm)
    og(); print("ok")

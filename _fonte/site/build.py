"""Gera o site rielsonfragoso.com.br (direção B · Quadro & Caderno) em /home/claude/site-repo.
Páginas: / · /concursos/ · /sobre/   (a /ingles-em-familia/ tem build próprio em site/lp_v2)"""
import os, shutil, html
from urllib.parse import quote
OUT = "/home/claude/site-repo"; HERE = os.path.dirname(os.path.abspath(__file__))
WA = "https://wa.me/5521964446262?text=" + quote("Oi, Rielson! Vim pelo site.")
YT = "https://www.youtube.com/@AcademiaMatem%C3%A1ticarj"; TG = "https://t.me/rielsonfragoso"; LT = "https://linktr.ee/academiamatematicarj"
IEF = "https://go.hotmart.com/E108477851B"

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
<meta property="og:url" content="https://rielsonfragoso.com.br{path}"><meta property="og:image" content="https://rielsonfragoso.com.br/{og}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#1B2A4E">
<meta name="google-site-verification" content="aLdDBJ0eH36Q4Qbf-sTwIbmToy9CROETqgIYNNR8cwI" />
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700&family=Nunito+Sans:ital,opsz,wght@0,6..12,400;0,6..12,600;0,6..12,700;1,6..12,400&family=Caveat:wght@600&display=swap">
<link rel="stylesheet" href="/site.css">
<style>{extra_css}</style>
</head>
<body>
'''

def nav(cur):
    items = [("/", "Início"), ("/concursos/", "Concursos"), ("/ingles-em-familia/", "Inglês em Família"), ("/#gratis", "Grátis"), ("/sobre/", "Sobre")]
    li = "".join(f'<li><a href="{h}"{" aria-current=\"page\"" if h == cur else ""}>{t}</a></li>' for h, t in items)
    return f'<header class="nav"><div class="wrap"><a class="logo" href="/"><i>RF</i>Rielson Fragoso</a><nav aria-label="Principal"><ul>{li}</ul></nav></div></header>\n'

FOOT = f'''<footer>
  <div class="wrap">
    <div class="cols">
      <div class="stack" style="gap:10px"><a class="logo" href="/"><i>RF</i>Rielson Fragoso</a>
        <p>Material sério, bem explicado, para quem estuda por conta própria.</p>
        <p class="hand" style="color:var(--yellow)">Dúvida sobre um material? Me chama.</p></div>
      <div><h3>Contato</h3><ul>
        <li><a href="{WA}" target="_blank" rel="noopener">WhatsApp · (21) 96444-6262</a></li>
        <li><a href="{TG}" target="_blank" rel="noopener">Telegram · avisos de materiais</a></li>
        <li><a href="{YT}" target="_blank" rel="noopener">YouTube · Academia Matemática RJ</a></li>
        <li><a href="{LT}" target="_blank" rel="noopener">Todos os links</a></li></ul></div>
      <div><h3>Materiais</h3><ul>
        <li><a href="/concursos/">Concursos: e-books e simulados</a></li>
        <li><a href="/ingles-em-familia/">Inglês em Família</a></li>
        <li><a href="/sobre/">Sobre mim</a></li></ul></div>
    </div>
    <p class="copy">© 2026 Rielson Fragoso · Rio de Janeiro. Pagamentos processados pela Hotmart.</p>
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
def home():
    feat = "".join(sim_card(t, d, b, u, "site_home") for t, d, b, u, f in SIMS if f)
    return head("Rielson Fragoso · Matemática para concursos e inglês em família",
                "Simulados e e-books de matemática e raciocínio lógico para concursos, e o e-book Inglês em Família para pais e filhos.", "/", extra_css=HOME_CSS) + nav("/") + f'''
<main>
<section class="board hero">
  <div class="wrap">
    <div class="top">
      <div class="stack">
        <span class="eyebrow">Rielson Fragoso · Academia Matemática RJ</span>
        <h1>Matemática para <span class="chalk-u">passar</span>.<br>Inglês para aprender <span class="chalk-u">em família</span>.</h1>
        <p class="lead">Faço materiais para quem estuda por conta própria: simulados e questões comentadas para concursos, e um jeito leve de aprender inglês com os filhos.</p>
      </div>
      <div class="mono" aria-hidden="true">RF<small>aprendi sozinho. ensino assim.</small></div>
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
    <p class="stamp">“Mais realista do que isso, só se eu entregasse a prova antes da hora.”</p>
    {METHOD}
    <h3 style="margin-top:8px">Alguns simulados</h3>
    <div class="cards">{feat}</div>
    <div><a class="btn" href="/concursos/">Ver todos os 13 materiais →</a></div>
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
      <div class="row"><a class="btn green" href="/ingles-em-familia/">Testar um capítulo grátis</a><a class="btn line" style="color:var(--green)" href="{src(IEF, "site_home")}" target="_blank" rel="noopener">Comprar · R$ 37</a></div>
    </div>
  </div>
</section>

<section id="gratis">
  <div class="wrap stack" style="gap:22px">
    <span class="eyebrow">Grátis</span>
    <h2>Comece sem gastar nada</h2>
    <div class="cards free">
      <a class="card" href="{YT}" target="_blank" rel="noopener"><b>Canal no YouTube</b><span>Aulas e resoluções de provas de concursos da Academia Matemática RJ.</span><em>Assistir →</em></a>
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
      <h2>Aprendi estudando por conta própria. É isso que eu ensino.</h2>
      <p>Sou educador de matemática e fundador da Academia Matemática RJ, onde ensino matemática e raciocínio lógico para concursos desde 2024. Aprendi inglês sozinho, ainda criança, jogando Pokémon com um dicionário do lado. Hoje estudo inglês com as minhas filhas, e foi daí que nasceu o Inglês em Família.</p>
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
})();
</script>'''
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
    <p class="stamp">“Mais realista do que isso, só se eu entregasse a prova antes da hora.”</p>
    {METHOD}
  </div>
</section>
<section style="padding-top:clamp(36px,5vw,56px)">
  <div class="wrap stack" style="gap:26px">
    <div class="stack" style="gap:10px"><span class="eyebrow">Filtrar por banca</span><div class="filters" role="group" aria-label="Filtrar por banca">{chips}</div></div>
    <div class="stack" id="simulados"><h2>Simulados</h2><div class="cards">{sims}</div><p class="empty" hidden>Nenhum simulado desta banca por enquanto.</p></div>
    <div class="stack" id="ebooks"><h2>E-books de questões comentadas</h2><p class="lead">Soluções passo a passo, com o meu jeito de explicar.</p><div class="cards">{ebs}</div><p class="empty" hidden>Nenhum e-book desta banca por enquanto.</p></div>
    <div class="tg"><p><b>Seu concurso não está aqui?</b> Entre no canal do Telegram para saber quando sair um novo simulado, ou me chame no WhatsApp.</p>
      <div class="row" style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn" href="{TG}" target="_blank" rel="noopener">Entrar no Telegram</a><a class="btn line" href="{WA}" target="_blank" rel="noopener">WhatsApp</a></div></div>
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
.timeline{list-style:none;margin:0;padding:0;border-left:3px solid var(--navy);display:flex;flex-direction:column;gap:22px;max-width:720px}
:root[data-theme="dark"] .timeline{border-color:var(--yellow)}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]) .timeline{border-color:var(--yellow)}}
.timeline li{position:relative;padding-left:26px}
.timeline li::before{content:"";position:absolute;left:-10px;top:6px;width:17px;height:17px;border-radius:50%;background:var(--yellow);border:3px solid var(--navy)}
.timeline .y{font-family:var(--hand);font-size:1.6rem;font-weight:600;color:var(--red);line-height:1}
.timeline h3{margin:4px 0}
.timeline p{color:var(--muted)}
.two{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.two>*{min-width:0}
@media (max-width:760px){.two{grid-template-columns:1fr}}
'''
def sobre():
    return head("Sobre · Rielson Fragoso", "Educador de matemática, fundador da Academia Matemática RJ, pai de duas meninas e autodidata em inglês.",
                "/sobre/", extra_css=SOBRE_CSS) + nav("/sobre/") + f'''
<main>
<section class="board phero">
  <div class="wrap stack">
    <span class="eyebrow">Sobre</span>
    <h1>Aprendi estudando por conta própria. É isso que eu ensino.</h1>
    <p class="hand">— Rielson Fragoso, carioca da Ilha do Governador</p>
  </div>
</section>
<section>
  <div class="wrap prose">
    <p>Sou educador de matemática e fundador da <b>Academia Matemática RJ</b>, onde ensino matemática e raciocínio lógico para concursos desde 2024. Sou pai de duas meninas, e boa parte do que eu crio hoje nasce da nossa rotina de estudo em casa.</p>
    <p>Aprendi inglês sozinho, ainda criança. Os jogos de Pokémon no Game Boy não tinham tradução, então eu jogava com um dicionário inglês-português do lado. Depois vieram os livros <i>Inglês Sem Mestre</i> do meu avô. Anos mais tarde, esse inglês me levou a trabalhar como recepcionista bilíngue, inclusive no Aeroporto Internacional do Rio de Janeiro.</p>
    <p>Por isso eu acredito em material que a pessoa consegue usar sozinha: bem explicado, organizado e honesto sobre o que entrega. Nos concursos, isso vira simulados montados a partir do edital. Em casa, virou o <b>Inglês em Família</b>.</p>
  </div>
</section>
<section class="grid-paper">
  <div class="wrap stack" style="gap:26px">
    <h2>Linha do tempo</h2>
    <ol class="timeline">
      <li><span class="y">infância</span><h3>Pokémon, dicionário e o Inglês Sem Mestre</h3><p>O inglês começou como curiosidade e virou disciplina de estudo.</p></li>
      <li><span class="y">2014–2016</span><h3>Recepcionista bilíngue no RIOgaleão</h3><p>Atendendo passageiros do mundo inteiro no aeroporto internacional do Rio.</p></li>
      <li><span class="y">2024</span><h3>Nasce a Academia Matemática RJ</h3><p>Canal no YouTube, e-books de questões comentadas e simulados de concursos.</p></li>
      <li><span class="y">2026</span><h3>Inglês em Família · Volume 1</h3><p>O método que uso com as minhas filhas, organizado em 28 sessões para outras famílias.</p></li>
    </ol>
  </div>
</section>
<section>
  <div class="wrap stack" style="gap:22px">
    <h2>O que eu faço hoje</h2>
    <div class="two">
      <a class="card" href="/concursos/" style="text-decoration:none"><span class="banca">Concursos</span><h3>Simulados e e-books de matemática</h3><p class="meta">Para quem vai fazer prova de concurso e quer treinar com o estilo real da banca.</p><span class="go" style="font-family:var(--display);font-weight:600;margin-top:auto">Ver materiais →</span></a>
      <a class="card" href="/ingles-em-familia/" style="text-decoration:none"><span class="banca">Família</span><h3>Inglês em Família</h3><p class="meta">Para pais e filhos que querem começar o inglês juntos, mesmo sem saber nada.</p><span class="go" style="font-family:var(--display);font-weight:600;margin-top:auto">Conhecer →</span></a>
    </div>
    <div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn" href="{WA}" target="_blank" rel="noopener">Falar comigo no WhatsApp</a><a class="btn line" href="{YT}" target="_blank" rel="noopener">Ver o canal no YouTube</a></div>
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
    for rel, fn in [("index.html", home), ("concursos/index.html", concursos), ("sobre/index.html", sobre)]:
        p = os.path.join(OUT, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, "w").write(fn())
    shutil.copy(os.path.join(HERE, "site.css"), os.path.join(OUT, "site.css"))
    open(os.path.join(OUT, "favicon.svg"), "w").write(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#1B2A4E"/>'
        '<rect x="5" y="5" width="54" height="54" rx="10" fill="none" stroke="#F2C230" stroke-width="3"/>'
        '<text x="32" y="42" font-family="Arial,Helvetica,sans-serif" font-weight="700" font-size="26" fill="#F2C230" text-anchor="middle">RF</text></svg>')
    open(os.path.join(OUT, "robots.txt"), "w").write("User-agent: *\nAllow: /\nSitemap: https://rielsonfragoso.com.br/sitemap.xml\n")
    open(os.path.join(OUT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        + "".join(f"<url><loc>https://rielsonfragoso.com.br{u}</loc></url>" for u in ["/", "/concursos/", "/ingles-em-familia/", "/sobre/"]) + "</urlset>\n")
    og(); print("ok")

"""Página /livros/ — desapego de livros (Matemática, Física e outras áreas).
Para marcar um livro como vendido: mude vendido=False para True (ou diminua qtd)."""
import html, json
from urllib.parse import quote
e = html.escape

WA_LIVROS = "5521972464789"
VIDEO_ID = "d3m-W96kx5c"
FRETE_GRATIS = 100

# (título, autor/detalhe, preço, qtd, categoria, foto, vendido)
L = [
    ("Álgebra Linear e Geometria Analítica", "Antonio dos Santos Machado", 36, 2, "Graduação", "machado", False),
    ("Cálculo · Volume 1", "James Stewart · tradução da 6ª edição", 54, 2, "Graduação", "stewart", False),
    ("Cálculo · Volume 1", "George B. Thomas Jr.", 25, 1, "Graduação", "thomas", False),
    ("Cálculo · Volume 2", "George B. Thomas Jr.", 25, 1, "Graduação", "thomas", False),
    ("Cálculo · Volume 3", "George B. Thomas Jr.", 25, 1, "Graduação", "thomas", False),
    ("Matemática para os Cursos de Economia, Administração e Ciências Contábeis · Vol. 1", "Medeiros · 3ª edição", 23, 1, "Graduação", "medeiros-alcantara", False),
    ("Fundamentos de Matemática Elementar 1 · Conjuntos e Funções", "Iezzi e Murakami · edição recente", 50, 1, "Ensino médio", "fme-novos", False),
    ("Fundamentos de Matemática Elementar 2 · Logaritmos", "Iezzi, Dolce e Murakami · edição recente", 50, 1, "Ensino médio", "fme-novos", False),
    ("Fundamentos de Matemática Elementar 3 · Trigonometria", "Gelson Iezzi · edição recente", 50, 1, "Ensino médio", "fme-novos", False),
    ("Fundamentos de Matemática Elementar 2 · Logaritmos", "Iezzi, Dolce e Murakami · edição antiga (anos 80)", 32, 1, "Coleções clássicas", "fme-antigos", False),
    ("Fundamentos de Matemática Elementar 3 · Trigonometria", "Gelson Iezzi · edição antiga (anos 80)", 32, 1, "Coleções clássicas", "fme-antigos", False),
    ("Fundamentos de Matemática Elementar 4 · Sequências, Matrizes, Determinantes e Sistemas", "Iezzi e Hazzan · edição antiga (anos 80)", 32, 1, "Coleções clássicas", "fme-antigos", False),
    ("Fundamentos de Matemática Elementar 5 · Combinatória e Probabilidade", "Samuel Hazzan · edição antiga (anos 80)", 32, 1, "Coleções clássicas", "fme-antigos", False),
    ("Matemática · Segundo Ano Colegial", "Ary Quintella · Companhia Editora Nacional", 27, 1, "Coleções clássicas", "quintella", False),
    ("Matemática · Terceiro Ano Colegial", "Ary Quintella · Companhia Editora Nacional", 27, 1, "Coleções clássicas", "quintella", False),
    ("Matemática · 3ª Série Ginasial", "Ary Quintella · Companhia Editora Nacional", 27, 1, "Coleções clássicas", "quintella", False),
    ("Matemática · 4ª Série Ginasial", "Ary Quintella · Companhia Editora Nacional", 27, 1, "Coleções clássicas", "quintella", False),
    ("Pitágoras · Matemática II, Livro I: Geometria Plana (1ª parte)", "Coleção Pitágoras", 15, 1, "Coleções clássicas", "pitagoras-minimanual", False),
    ("Matemática · Box Moderna Plus Vol. 1 (completo)", "Manoel Paiva", 45, 1, "Ensino médio", "paiva", False),
    ("Matemática · Box Moderna Plus Vol. 2 (incompleto)", "Manoel Paiva", 23, 1, "Ensino médio", "paiva", False),
    ("Matemática · Box Moderna Plus Vol. 3 (completo)", "Manoel Paiva", 45, 1, "Ensino médio", "paiva", False),
    ("Minimanual Compacto de Matemática · Ensino Médio", "Editora Rideel", 23, 1, "Ensino médio", "pitagoras-minimanual", False),
    ("Novo Praticando Matemática · Vol. 2", "Álvaro Andrini e Maria José Vasconcellos", 23, 1, "Ensino fundamental", "praticando", False),
    ("Novo Praticando Matemática · Vol. 3", "Álvaro Andrini e Maria José Vasconcellos", 23, 1, "Ensino fundamental", "praticando", False),
    ("Novo Praticando Matemática · Vol. 4", "Álvaro Andrini e Maria José Vasconcellos", 23, 1, "Ensino fundamental", "praticando", False),
    ("Vivendo a Matemática · A Numeração Indo-Arábica", "Luiz Márcio Imenes · Scipione", 15, 1, "Ensino fundamental", "imenes", False),
    ("Experiências de Ciências para o Ensino Fundamental", "Alberto Gaspar · Ática", 20, 1, "Ensino fundamental", "gaspar", False),
    ("Matemática para Concursos", "Flávio Alcântara · teoria e questões comentadas", 23, 1, "Concursos", "medeiros-alcantara", False),
    ("Matemática Financeira · Série Provas e Concursos", "Benjamin Cesar · 7ª edição", 23, 1, "Concursos", "financeira-puccini-cesar", False),
    ("Matemática Básica", "Aref Antar Neto", 18, 1, "Concursos", "estatistica-basica", False),
    ("Matemática Financeira · Objetiva e Aplicada", "Abelardo de Lima Puccini · 6ª edição", 23, 1, "Financeira e Estatística", "financeira-puccini-cesar", False),
    ("Matemática Financeira · mais de 600 exercícios resolvidos e propostos", "Washington Franco Mathias e José Maria Gomes · Atlas", 23, 1, "Financeira e Estatística", "ross-mathias", False),
    ("Princípios de Administração Financeira", "Ross, Westerfield e Jordan · Atlas", 20, 1, "Financeira e Estatística", "ross-mathias", False),
    ("Curso de Estatística · Elementos", "Ruy Aguiar da Silva Leme", 18, 1, "Financeira e Estatística", "estatistica-basica", False),
    ("The Feynman Lectures on Physics · Vol. III: Quantum Mechanics", "Feynman, Leighton e Sands · em inglês", 54, 1, "Física", "feynman-lectures", False),
    ("The Character of Physical Law", "Richard Feynman · em inglês", 30, 1, "Física", "feynman-leis", False),
    ("Sobre as Leis da Física", "Richard Feynman · Contraponto / PUC-Rio", 30, 1, "Física", "feynman-leis", False),
    ("Os Tópicos da Física 2 · Termologia, Ondas e Óptica", "Gualter, Newton e Helou Doca · Saraiva", 25, 1, "Física", "topicos-fisica", False),
    ("Os Tópicos da Física 3 · Eletricidade", "Gualter, Newton e Helou Doca · Saraiva", 25, 1, "Física", "topicos-fisica", False),
    ("Física Básica · Volume Único", "Nicolau, Toledo e Ronaldo · Atual", 25, 1, "Física", "fisica-basica", False),
    ("La Gaceta de la Real Sociedad Matemática Española · Vol. 21, nº 3 (2018)", "Revista, em espanhol", 18, 1, "Outros", "gaceta", False),
    ("Astronomia & Budismo · Uma Jornada Rumo ao Distante Universo", "Ronaldo Rogério de Freitas Mourão e Daisaku Ikeda", 15, 1, "Outros", "astronomia", False),
]
CATS = ["Ensino fundamental", "Ensino médio", "Coleções clássicas", "Concursos", "Graduação", "Financeira e Estatística", "Física", "Outros"]

def preco(v):
    return f"R$ {v:.2f}".replace(".", ",")

CSS = '''
.phero{padding-block:clamp(36px,6vw,64px)}
.lhero{display:grid;grid-template-columns:1.05fr .95fr;gap:clamp(20px,4vw,48px);align-items:center}
.lhero>*{min-width:0}
.lhero h1{color:var(--chalk);font-size:clamp(2rem,5vw,3.1rem)}
.lhero img{border-radius:14px;border:2px solid var(--yellow);width:100%;height:auto}
.facts{display:flex;flex-wrap:wrap;gap:8px}
.facts span{background:color-mix(in srgb,var(--yellow) 18%,transparent);color:var(--chalk);border:1px solid color-mix(in srgb,var(--yellow) 60%,transparent);border-radius:999px;padding:5px 12px;font:600 .88rem var(--display)}
.video{position:relative;aspect-ratio:16/9;max-width:860px;width:100%;border-radius:14px;overflow:hidden;background:#000}
.video iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.filters{display:flex;flex-wrap:wrap;gap:8px}
.filters button{font:600 .9rem var(--display);border:1.5px solid var(--line);background:var(--surface);color:var(--muted);border-radius:999px;padding:7px 14px;cursor:pointer}
.filters button[aria-pressed="true"]{border-color:var(--navy);background:var(--navy);color:#fff}
:root[data-theme="dark"] .filters button[aria-pressed="true"]{border-color:var(--yellow);background:var(--yellow);color:var(--on-yellow)}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]) .filters button[aria-pressed="true"]{border-color:var(--yellow);background:var(--yellow);color:var(--on-yellow)}}
.books{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:16px}
.book{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);overflow:hidden;display:flex;flex-direction:column;min-width:0}
.book .ph{aspect-ratio:4/3;overflow:hidden;background:var(--line)}
.book .ph img{width:100%;height:100%;object-fit:cover;display:block}
.book .bd{padding:14px 16px 16px;display:flex;flex-direction:column;gap:6px;flex:1}
.book h3{font-size:1rem;line-height:1.3}
.book .au{font-size:.88rem;color:var(--muted)}
.book .cat{font:600 .72rem var(--display);letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
.book .row{display:flex;align-items:center;justify-content:space-between;gap:8px;margin-top:auto;padding-top:8px;flex-wrap:wrap}
.book .pr{font:700 1.25rem var(--display);color:var(--ink)}
.book .pr small{font:500 .78rem var(--body);color:var(--muted);display:block}
.book .acts{display:flex;gap:6px}
.add{font:600 .85rem var(--display);border:1.5px solid var(--navy);color:var(--navy);background:transparent;border-radius:999px;padding:7px 12px;cursor:pointer}
.add[aria-pressed="true"]{background:var(--navy);color:#fff}
:root[data-theme="dark"] .add{border-color:var(--yellow);color:var(--yellow)}
:root[data-theme="dark"] .add[aria-pressed="true"]{background:var(--yellow);color:var(--on-yellow)}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]) .add{border-color:var(--yellow);color:var(--yellow)}
 :root:not([data-theme="light"]) .add[aria-pressed="true"]{background:var(--yellow);color:var(--on-yellow)}}
.wa{display:inline-grid;place-items:center;width:36px;height:36px;border-radius:50%;background:#1FA855;color:#fff;text-decoration:none}
.wa svg{width:19px;height:19px}
.book.sold{opacity:.55}
.book.sold .pr{text-decoration:line-through}
.soldtag{position:absolute;top:10px;left:10px;background:var(--red);color:#fff;font:700 .75rem var(--display);padding:4px 10px;border-radius:999px}
.book .ph{position:relative}
.cart{position:fixed;left:0;right:0;bottom:0;z-index:20;background:var(--navy);color:var(--chalk);border-top:3px solid var(--yellow);
  padding:10px max(16px, env(safe-area-inset-right, 0px)) calc(10px + env(safe-area-inset-bottom, 0px)) max(16px, env(safe-area-inset-left, 0px));
  display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;transform:translateY(110%);transition:transform .25s}
.cart.show{transform:none}
.cart .sum{font-family:var(--display);line-height:1.2}
.cart .sum b{color:var(--yellow);font-size:1.15rem}
.cart .sum small{display:block;font-family:var(--body);font-size:.82rem;color:var(--chalk-dim)}
.cart .cbtns{display:flex;gap:8px;align-items:center}
.cart .clear{background:transparent;border:0;color:var(--chalk-dim);font:600 .85rem var(--display);cursor:pointer;text-decoration:underline}
.btn.wabtn{background:#1FA855;color:#fff}
body.has-cart{padding-bottom:84px}
.info{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.info>div{background:var(--yellow-soft);border-radius:var(--r);padding:16px;min-width:0}
.info b{font-family:var(--display);display:block;margin-bottom:4px}
@media (max-width:760px){.lhero,.info{grid-template-columns:1fr}}
@media (prefers-reduced-motion:reduce){.cart{transition:none}}
'''

WA_SVG = ('<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3a.5.5 0 0 0 0-.5l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .1-1.2c0-.1-.2-.2-.5-.3Z"/></svg>')

def wa_link(msg):
    return f"https://wa.me/{WA_LIVROS}?text=" + quote(msg)

def page(head, nav, foot):
    cards = []
    for i, (t, a, p, q, c, f, sold) in enumerate(L):
        nome = f"{t} – {a.split(' · ')[0]}"
        msg = f"Olá, Rielson! Vi no site e tenho interesse no livro: {nome} ({preco(p)}). Ainda está disponível?"
        qtxt = f"{q} unidades · preço cada" if q > 1 else "1 unidade"
        tag = '<span class="soldtag">Vendido</span>' if sold else ""
        acts = "" if sold else (
            f'<button type="button" class="add" aria-pressed="false" data-i="{i}">+ Lote</button>'
            f'<a class="wa" href="{e(wa_link(msg))}" target="_blank" rel="noopener" aria-label="Perguntar no WhatsApp sobre {e(t)}">{WA_SVG}</a>')
        cards.append(
            f'<article class="book{" sold" if sold else ""}" data-cat="{e(c)}">'
            f'<div class="ph">{tag}<img src="img/{f}.jpg" alt="Foto de {e(t)}" loading="lazy" width="900" height="1200"></div>'
            f'<div class="bd"><span class="cat">{e(c)}</span><h3>{e(t)}</h3><p class="au">{e(a)}</p>'
            f'<div class="row"><span class="pr">{preco(p)}<small>{qtxt}</small></span><span class="acts">{acts}</span></div></div></article>')
    chips = '<button type="button" aria-pressed="true" data-f="*">Todos</button>' + "".join(
        f'<button type="button" aria-pressed="false" data-f="{e(c)}">{e(c)}</button>' for c in CATS if any(x[4] == c for x in L))
    dados = json.dumps([{"t": f"{t} – {a.split(' · ')[0]}", "p": p} for t, a, p, q, c, f, s in L], ensure_ascii=False).replace("</", "<\\/")
    disp = sum(1 for x in L if not x[6])
    js = '''<script id="lv-data" type="application/json">__DADOS__</script>
<script>
(function(){
  var D=JSON.parse(document.getElementById('lv-data').textContent), sel={}, FG=__FG__, WA='__WA__';
  function brl(v){return 'R$ '+v.toFixed(2).replace('.',',');}
  var cart=document.getElementById('cart'), sum=document.getElementById('csum'), send=document.getElementById('csend');
  function upd(){
    var ks=Object.keys(sel), tot=ks.reduce(function(s,k){return s+D[k].p},0);
    cart.classList.toggle('show',ks.length>0); document.body.classList.toggle('has-cart',ks.length>0);
    var falta=FG-tot;
    sum.innerHTML='<b>'+ks.length+(ks.length===1?' livro':' livros')+' · '+brl(tot)+'</b><small>'+(falta>0?'Faltam '+brl(falta)+' para o frete grátis':'Frete grátis garantido')+'</small>';
    var msg='Olá, Rielson! Vi no site e tenho interesse nestes livros:\\n'+ks.map(function(k){return '• '+D[k].t+' ('+brl(D[k].p)+')'}).join('\\n')+'\\nTotal: '+brl(tot)+'. Estão disponíveis?';
    send.href='https://wa.me/'+WA+'?text='+encodeURIComponent(msg);
  }
  [].forEach.call(document.querySelectorAll('.add'),function(b){b.addEventListener('click',function(){
    var i=b.getAttribute('data-i'); if(sel[i]){delete sel[i];b.setAttribute('aria-pressed','false');b.textContent='+ Lote';}
    else{sel[i]=1;b.setAttribute('aria-pressed','true');b.textContent='✓ No lote';} upd();});});
  document.getElementById('cclear').addEventListener('click',function(){sel={};[].forEach.call(document.querySelectorAll('.add'),function(b){b.setAttribute('aria-pressed','false');b.textContent='+ Lote';});upd();});
  var fb=[].slice.call(document.querySelectorAll('.filters button')), cards=[].slice.call(document.querySelectorAll('.book'));
  fb.forEach(function(b){b.addEventListener('click',function(){var f=b.getAttribute('data-f');
    fb.forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});
    cards.forEach(function(c){c.hidden=!(f==='*'||c.getAttribute('data-cat')===f)});});});
})();
</script>'''.replace("__DADOS__", dados).replace("__FG__", str(FRETE_GRATIS)).replace("__WA__", WA_LIVROS)
    geral = wa_link("Olá, Rielson! Vi no site os livros à venda e queria saber mais.")
    return head("Livros à venda · Matemática, Física e mais | Rielson Fragoso",
                f"Desapego de {len(L)} livros de Matemática, Física, Matemática Financeira e Estatística, com fotos e preços. Ilha do Governador, RJ. Frete grátis a partir de R$ 100.",
                "/livros/", og="livros/img/capa.jpg", extra_css=CSS) + nav("/livros/") + f'''
<main>
<section class="board phero">
  <div class="wrap lhero">
    <div class="stack">
      <span class="eyebrow">Desapego · livros usados</span>
      <h1>Livros de Matemática, Física e outras áreas</h1>
      <p class="lead">Livros de graduação, ensino médio, concursos e coleções clássicas que passaram pelas minhas mãos. Monte seu lote e me chame no WhatsApp.</p>
      <div class="facts"><span>{disp} títulos disponíveis</span><span>Frete grátis acima de R$ 100</span><span>Ilha do Governador · RJ</span><span>Aceito ofertas para lote</span></div>
      <div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn" href="#catalogo">Ver os livros ↓</a><a class="btn wabtn" href="{e(geral)}" target="_blank" rel="noopener">Falar no WhatsApp</a></div>
    </div>
    <img src="img/capa.jpg" alt="Rielson ao lado de uma pilha de livros de matemática e física" width="1400" height="788">
  </div>
</section>
<section style="padding-bottom:24px">
  <div class="wrap stack" style="gap:16px">
    <div class="info">
      <div><b>Como comprar</b>Toque em “+ Lote” nos livros que quiser e envie a lista pelo WhatsApp. Ou toque no ícone verde para perguntar por um livro só.</div>
      <div><b>Entrega</b>Estou na Ilha do Governador (RJ). Frete grátis em compras a partir de R$ 100; para valores menores, combinamos pelo WhatsApp.</div>
      <div><b>Negociação</b>Aberto a ofertas para quem levar vários livros ou o lote completo.</div>
    </div>
    <h2 style="margin-top:12px">Veja todos os livros no vídeo</h2>
    <div class="video"><iframe src="https://www.youtube-nocookie.com/embed/{VIDEO_ID}" title="Vídeo mostrando os livros à venda" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
    <p class="meta" style="color:var(--muted)">Também anunciei no Facebook: <a href="https://www.facebook.com/share/p/1A1cEqjhG5/" target="_blank" rel="noopener">ver a publicação</a>.</p>
  </div>
</section>
<section id="catalogo" style="padding-top:24px;scroll-margin-top:80px">
  <div class="wrap stack" style="gap:20px">
    <h2>Catálogo</h2>
    <div class="filters" role="group" aria-label="Filtrar por área">{chips}</div>
    <div class="books">{"".join(cards)}</div>
    <p class="meta" style="color:var(--muted)">Livros usados, vendidos conforme disponibilidade. As fotos mostram os exemplares reais. Algumas fotos mostram mais de um livro: o preço é de cada título.</p>
  </div>
</section>
</main>
<div class="cart" id="cart" aria-live="polite"><span class="sum" id="csum"></span><span class="cbtns"><button type="button" class="clear" id="cclear">Limpar</button><a class="btn wabtn" id="csend" href="#" target="_blank" rel="noopener">Enviar lote no WhatsApp</a></span></div>
''' + js + foot

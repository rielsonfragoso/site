"""Página /livros/ (catálogo + carrinho + pedido pelo WhatsApp) e páginas individuais /livros/<slug>/.
Os dados ficam em livros_dados.py."""
import html, json, os, re, unicodedata
e = html.escape
HERE = os.path.dirname(os.path.abspath(__file__))
from livros_dados import LIVROS, CATS, COMBOS, CIENCIA

WA_LIVROS = "5521972464789"
VIDEO_ID = "d3m-W96kx5c"
FRETE_GRATIS = 100
FRETE = 20
SITE = "https://rielsonfragoso.com.br"

def preco(v):
    return f"R$ {v:.2f}".replace(".", ",")

def slugify(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:70].strip("-")

# slugs únicos
_seen = set()
for b in LIVROS:
    s = b["slug"] or slugify(b["titulo"] + " " + b["autor"].split(" e ")[0].split(",")[0])
    base, n = s, 2
    while s in _seen:
        s = f"{base}-{n}"; n += 1
    b["slug"] = s; _seen.add(s)

def yt(link):
    """Aceita link completo do YouTube (normal, youtu.be ou Shorts) ou só o ID. Retorna (id, vertical)."""
    if not link: return None, False
    m = re.search(r"(?:shorts/|youtu\.be/|v=|embed/)([A-Za-z0-9_-]{11})", link)
    return (m.group(1) if m else link.strip()), ("shorts/" in link)

def yt_url(b):
    vid, _ = yt(b["video"])
    return f"https://www.youtube.com/watch?v={vid}" + (f"&t={b['video_t']}s" if b.get("video_t") else "")

def disp(b):
    return (not b["vendido"]) and b["qtd"] > 0

CSS = open(os.path.join(HERE, "livros.css")).read()

def card(b, i):
    sold = not disp(b)
    tag = '<span class="soldtag">Vendido</span>' if sold else ""
    lang = f'<span class="lang">{e(b["idioma"])}</span>' if b["idioma"] != "Português" else ""
    qtxt = f'{b["qtd"]} disponíveis' if b["qtd"] > 1 and not sold else ("" if sold else "1 disponível")
    act = "" if sold else f'<button type="button" class="add" aria-pressed="false" data-k="{b["slug"]}">+ Pedido</button>'
    busca = e(unicodedata.normalize("NFKD", (b["titulo"] + " " + b["autor"]).lower()).encode("ascii", "ignore").decode())
    return (f'<article class="book{" sold" if sold else ""}" data-cat="{e(b["cat"])}" data-lang="{e(b["idioma"])}" data-q="{busca}">'
            f'<a class="ph" href="{b["slug"]}/">{tag}{lang}<img src="img/{b["foto"]}.jpg" alt="Foto do exemplar de {e(b["titulo"])}, de {e(b["autor"])}" loading="lazy" width="900" height="1200"></a>'
            f'<div class="bd"><span class="cat">{e(b["cat"])}</span><h3><a href="{b["slug"]}/">{e(b["titulo"])}</a></h3><p class="au">{e(b["autor"])}</p>'
            f'<p class="st">Usado{" · " + e(b["cond"]) if b["cond"] else ""}</p>'
            + (f'<a class="vlink" href="{b["slug"]}/#video">▶ Ver vídeo do exemplar</a>' if b["video"] else "")
            + (f'<a class="vlink yt" href="{yt_url(b)}" target="_blank" rel="noopener" aria-label="Ver no YouTube">YouTube ↗</a>' if b["video"] else "")
            + f'<div class="row"><span class="pr">{preco(b["preco"])}<small>{qtxt}</small></span><span class="acts">{act}</span></div></div></article>')

def combo_card(c):
    itens = {b["slug"]: b for b in LIVROS}
    ok = all(disp(itens[s]) for s in c["itens"])
    soma = sum(itens[s]["preco"] for s in c["itens"])
    btn = (f'<button type="button" class="btn addcombo" data-c="{c["id"]}">Adicionar os 3 ao pedido</button>' if ok
           else '<span class="soldtag" style="position:static">Esgotado</span>')
    return (f'<div class="combo"><img src="img/{c["foto"]}.jpg" alt="Os três livros de Shakespeare do combo" loading="lazy" width="900" height="1200">'
            f'<div class="stack" style="gap:8px"><span class="eyebrow">Promoção</span><h3>{e(c["nome"])}: 3 livros por {preco(c["preco"])}</h3>'
            f'<p>{e(c["desc"])} Economia de {preco(soma - c["preco"])}.</p>'
            f'<p class="note">O desconto também vale se você adicionar os três separadamente.</p><div class="row" style="display:flex;gap:10px;flex-wrap:wrap;align-items:center">{btn}'
            + (f'<a class="vlink" href="{c["itens"][0]}/#video">▶ Ver vídeo dos exemplares</a>' if c.get("video") else "") + '</div></div></div>')

def dados_js():
    d = {b["slug"]: {"t": b["titulo"], "a": b["autor"], "p": b["preco"], "q": b["qtd"] if disp(b) else 0} for b in LIVROS}
    c = [{"id": x["id"], "nome": x["nome"], "p": x["preco"], "itens": x["itens"]} for x in COMBOS]
    return json.dumps({"livros": d, "combos": c}, ensure_ascii=False).replace("</", "<\\/")

def checkout_html():
    return open(os.path.join(HERE, "livros_checkout.html")).read()

def checkout_js():
    return (open(os.path.join(HERE, "livros_checkout.js.html")).read()
            .replace("__DADOS__", dados_js()).replace("__FG__", str(FRETE_GRATIS)).replace("__FRETE__", str(FRETE)).replace("__WA__", WA_LIVROS))

def page(head, nav, foot):
    n_disp = sum(1 for b in LIVROS if disp(b))
    chips = '<button type="button" aria-pressed="true" data-f="*">Todos</button>' + "".join(
        f'<button type="button" aria-pressed="false" data-f="{e(c)}">{e(c)}</button>' for c in CATS if any(b["cat"] == c for b in LIVROS))
    langs = sorted({b["idioma"] for b in LIVROS}, key=lambda x: (x != "Português", x))
    lopts = '<option value="*">Todos os idiomas</option>' + "".join(f'<option>{e(l)}</option>' for l in langs)
    destaque = "".join(card(b, i) for i, b in enumerate(LIVROS) if b["cat"] == CIENCIA)
    todos = "".join(card(b, i) for i, b in enumerate(LIVROS))
    combos = "".join(combo_card(c) for c in COMBOS)
    return head("Livros usados à venda · Ciência, Literatura e Matemática | Rielson Fragoso",
                f"Livros usados com preços acessíveis: Heisenberg, Weinberg, Schrödinger, Hawking, Shakespeare, Feynman e livros de matemática. Fotos reais, frete fixo de R$ 20 e grátis a partir de R$ 100.",
                "/livros/", og="livros/img/capa.jpg", extra_css=CSS) + nav("/livros/") + f'''
<main>
<section class="board phero">
  <div class="wrap lhero">
    <div class="stack">
      <span class="eyebrow">Livros usados · Ilha do Governador, RJ</span>
      <h1>Livros usados, preços acessíveis e oportunidades de leitura</h1>
      <p class="lead">Os livros são usados e, por isso, custam menos do que exemplares novos. Todas as fotos são dos exemplares reais. Monte seu pedido, preencha os dados de envio e finalize pelo WhatsApp.</p>
      <div class="facts"><span>{n_disp} títulos disponíveis</span><span>Frete fixo de R$ 20 para todo o Brasil</span><span>Frete grátis a partir de R$ 100</span><span>A partir de 10 livros: desconto especial</span></div>
      <div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn" href="#catalogo">Montar meu pedido ↓</a></div>
    </div>
    <img src="img/capa.jpg" alt="Rielson ao lado de uma pilha de livros de matemática e física" width="1400" height="788">
  </div>
</section>
<section style="padding-bottom:20px">
  <div class="wrap stack" style="gap:16px">
    <div class="info">
      <div><b>Como comprar</b>1. Toque em “+ Pedido” nos livros que quiser. 2. Toque em “Finalizar pedido” e preencha os dados de envio. 3. O pedido chega no meu WhatsApp e eu envio a chave Pix. O pedido é confirmado após o pagamento.</div>
      <div><b>Frete</b>Frete fixo de <b style="display:inline">R$ 20</b> para todo o Brasil, pelos Correios. <b style="display:inline">Grátis</b> para compras a partir de R$ 100 (valor dos livros, já com descontos).</div>
      <div><b>Livros usados, com transparência</b>Fotos reais de cada exemplar. Marcas de uso, grifos ou anotações são informados na descrição. Ficou em dúvida sobre o estado de um livro? Pergunte ao finalizar o pedido.</div>
    </div>
    <p class="trust">Já realizamos vendas e enviamos livros para nossos clientes. Nossa loja está presente em comunidades de leitores e compradores de livros usados, com clientes que acompanham nossas publicações e compartilham suas experiências.</p>
  </div>
</section>
<section style="padding-top:12px;padding-bottom:20px">
  <div class="wrap stack" style="gap:16px">
    <span class="eyebrow">Destaque</span>
    <h2>{e(CIENCIA)}</h2>
    <p class="lead" style="font-size:1rem">Heisenberg, Weinberg, Schrödinger, Simon Singh, Stephen Hawking e Feynman. Vários em inglês, na edição original.</p>
    <div class="books">{destaque}</div>
    {combos}
  </div>
</section>
<section id="catalogo" style="padding-top:24px;scroll-margin-top:80px">
  <div class="wrap stack" style="gap:18px">
    <h2>Catálogo completo</h2>
    <div class="tools">
      <label class="search"><span class="sr">Buscar por título ou autor</span><input type="search" id="q" placeholder="Buscar por título ou autor" autocomplete="off"></label>
      <label class="langsel"><span class="sr">Idioma</span><select id="lang">{lopts}</select></label>
    </div>
    <div class="filters" role="group" aria-label="Filtrar por categoria">{chips}</div>
    <p class="none" id="none" hidden>Nenhum livro encontrado com esses filtros.</p>
    <div class="books" id="todos">{todos}</div>
    <p class="meta" style="color:var(--muted)">Algumas fotos mostram mais de um livro da mesma coleção; o preço é de cada título.</p>
    <h2 style="margin-top:12px">Veja os livros no vídeo</h2>
    <div class="video"><iframe src="https://www.youtube-nocookie.com/embed/{VIDEO_ID}" title="Vídeo mostrando livros à venda" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
    <p class="meta" style="color:var(--muted)">Também anunciei no Facebook: <a href="https://www.facebook.com/share/p/1A1cEqjhG5/" target="_blank" rel="noopener">ver a publicação</a>.</p>
  </div>
</section>
</main>
''' + checkout_html() + checkout_js() + foot

def product_page(b, head, nav, foot):
    sold = not disp(b)
    combo = next((c for c in COMBOS if b["slug"] in c["itens"]), None)
    url = f"{SITE}/livros/{b['slug']}/"
    ld = {"@context": "https://schema.org", "@type": "Product", "name": b["titulo"], "image": f"{SITE}/livros/img/{b['foto']}.jpg",
          "description": b["desc"] or f"{b['titulo']}, de {b['autor']}. Livro usado.", "brand": {"@type": "Brand", "name": b["autor"]},
          "category": b["cat"], "url": url,
          "offers": {"@type": "Offer", "price": f"{b['preco']:.2f}", "priceCurrency": "BRL", "url": url,
                     "availability": "https://schema.org/SoldOut" if sold else "https://schema.org/InStock",
                     "itemCondition": "https://schema.org/UsedCondition"},
          "additionalProperty": [{"@type": "PropertyValue", "name": "Autor", "value": b["autor"]},
                                 {"@type": "PropertyValue", "name": "Idioma", "value": b["idioma"]}]}
    if b["editora"]: ld["additionalProperty"].append({"@type": "PropertyValue", "name": "Editora/edição", "value": b["editora"]})
    vid, vert = yt(b["video"] or (combo or {}).get("video", ""))
    vstart = f"?start={b['video_t']}" if b["video"] and b.get("video_t") else ""
    video = (f'<h2 id="video">Vídeo do exemplar real</h2><p class="note">Veja o estado do livro que você vai receber.</p>'
             f'<div class="video{" vert" if vert else ""}"><iframe src="https://www.youtube-nocookie.com/embed/{e(vid)}{vstart}" title="Vídeo de {e(b["titulo"])}" loading="lazy" allow="encrypted-media; picture-in-picture" allowfullscreen></iframe></div>'
             if vid else "")
    vbtn = ('<a class="vlink big" href="#video">▶ Ver vídeo do exemplar</a>' + (f'<a class="vlink big yt" href="{yt_url(b)}" target="_blank" rel="noopener">Abrir no YouTube ↗</a>' if b["video"] else "")) if vid else ""
    rows = [("Autor", b["autor"]), ("Idioma", b["idioma"]), ("Categoria", b["cat"])]
    if b["editora"]: rows.append(("Editora / edição", b["editora"]))
    rows.append(("Estado", "Usado" + (f" · {b['cond']}" if b["cond"] else " · veja as fotos do exemplar real")))
    rows.append(("Disponível", "vendido" if sold else f"{b['qtd']} exemplar{'es' if b['qtd'] > 1 else ''}"))
    dl = "".join(f"<dt>{e(k)}</dt><dd>{e(v)}</dd>" for k, v in rows)
    act = ('<span class="soldtag" style="position:static">Vendido</span>' if sold else
           f'<button type="button" class="btn add big" aria-pressed="false" data-k="{b["slug"]}">+ Adicionar ao pedido</button>')
    combotxt = (f'<p class="combo-note">Faz parte do <b>{e(combo["nome"])}</b>: os 3 por {preco(combo["preco"])}. '
                f'<a href="../#catalogo">Ver o combo</a></p>' if combo else "")
    return head(f"{b['titulo']} – {b['autor']} (usado) | Livros Rielson Fragoso",
                (b["desc"] or f"{b['titulo']}, de {b['autor']}. Livro usado") + f" Preço: {preco(b['preco'])}. Frete fixo R$ 20, grátis a partir de R$ 100.",
                f"/livros/{b['slug']}/", og=f"livros/img/{b['foto']}.jpg", extra_css=CSS) + nav("/livros/") + f'''
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<main>
<section style="padding-top:clamp(24px,5vw,48px)">
  <div class="wrap">
    <p class="crumb"><a href="../">Livros usados</a> › {e(b["cat"])}</p>
    <div class="prod">
      <img src="../img/{b["foto"]}.jpg" alt="Foto do exemplar de {e(b["titulo"])}, de {e(b["autor"])}" width="900" height="1200">
      <div class="stack" style="gap:14px">
        <h1 class="ptitle">{e(b["titulo"])}</h1>
        <p class="au" style="font-size:1.1rem">{e(b["autor"])}</p>
        <p class="pprice">{preco(b["preco"])}</p>
        <div style="display:flex;gap:12px;flex-wrap:wrap;align-items:center">{act}{vbtn}</div>
        {combotxt}
        {f'<p>{e(b["desc"])}</p>' if b["desc"] else ''}
        <dl class="specs">{dl}</dl>
        <p class="note">Frete fixo de R$ 20 para todo o Brasil; grátis a partir de R$ 100 em livros. Pagamento via Pix, combinado pelo WhatsApp ao finalizar o pedido.</p>
        <p><a href="../#catalogo">← Ver todos os livros</a></p>
      </div>
    </div>
    {video}
  </div>
</section>
</main>
''' + checkout_html() + checkout_js() + foot

def build(out_dir, head, nav, foot):
    for b in LIVROS:
        p = os.path.join(out_dir, "livros", b["slug"]); os.makedirs(p, exist_ok=True)
        open(os.path.join(p, "index.html"), "w").write(product_page(b, head, nav, foot))
    return [f"/livros/{b['slug']}/" for b in LIVROS]

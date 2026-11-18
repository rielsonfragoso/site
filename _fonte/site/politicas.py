"""Páginas /privacidade/, /trocas/ e 404. RASCUNHO para revisão do Rielson (não é aconselhamento jurídico)."""
EMAIL = "academiamatematica.rj@gmail.com"
CSS = '''.legal{max-width:72ch;display:flex;flex-direction:column;gap:14px;font-size:1.02rem}
.legal h2{font-size:1.25rem;margin-top:14px}.legal ul{margin:0;padding-left:1.2em;display:flex;flex-direction:column;gap:6px}
.legal .upd{color:var(--muted);font-size:.9rem}
.phero{padding-block:clamp(36px,6vw,64px)}.phero h1{color:var(--chalk);font-size:clamp(1.9rem,5vw,2.8rem)}'''

def _pg(head, nav, foot, path, title, desc, h1, body):
    return head(title, desc, path, extra_css=CSS) + nav(path) + f'''<main>
<section class="board phero"><div class="wrap stack"><h1>{h1}</h1></div></section>
<section><div class="wrap legal">{body}</div></section></main>''' + foot

def privacidade(head, nav, foot):
    return _pg(head, nav, foot, "/privacidade/", "Política de Privacidade | Rielson Fragoso",
        "Como tratamos os dados de quem compra livros, materiais e serviços em rielsonfragoso.com.br.", "Política de Privacidade", f'''
<p class="upd">Atualizada em 17 de novembro de 2026.</p>
<p>Este site é mantido por Rielson Fragoso (Academia Matemática RJ), no Rio de Janeiro. Coletamos o mínimo de dados necessário para atender você, de acordo com a Lei Geral de Proteção de Dados (LGPD).</p>
<h2>Quais dados e para quê</h2>
<ul>
<li><b>Pedidos de livros:</b> nome, CPF, telefone e endereço que você digita no pedido (o CPF é exigido pelos Correios na postagem). Esses dados não ficam guardados no site: eles vão apenas na mensagem que você mesmo envia pelo WhatsApp, e são usados só para combinar o pagamento e postar o envio pelos Correios.</li>
<li><b>Pedidos de resolução de questões e de simulados:</b> as informações que você preenche (nome, concurso, assunto) chegam por WhatsApp ou por e-mail e são usadas só para responder ao seu pedido.</li>
<li><b>Avaliações:</b> nome público, nota e comentário, enviados por e-mail. Só são publicados com a sua autorização e após aprovação. Nunca publicamos telefone, e-mail ou endereço.</li>
<li><b>Compras na Hotmart</b> (e-books e simulados): os dados de pagamento são tratados pela Hotmart, conforme a política dela.</li>
</ul>
<h2>Armazenamento no seu aparelho</h2>
<p>O carrinho de livros fica salvo apenas no seu navegador (armazenamento local), para você não perder a seleção ao navegar. Não usamos cookies de rastreamento nem anúncios.</p>
<h2>Serviços de terceiros</h2>
<ul><li>Hospedagem: GitHub Pages.</li><li>Fontes: Google Fonts.</li><li>Vídeos: YouTube em modo de privacidade aprimorada.</li>
<li>Formulários: FormSubmit (encaminha o envio para o nosso e-mail).</li><li>Busca de endereço pelo CEP: ViaCEP (só o CEP é enviado).</li></ul>
<h2>Compartilhamento</h2>
<p>Não vendemos nem repassamos seus dados. O nome, o CPF e o endereço de entrega são informados apenas aos Correios, na postagem.</p>
<h2>Seus direitos</h2>
<p>Você pode pedir a qualquer momento acesso, correção ou exclusão dos seus dados, ou a retirada de uma avaliação publicada, pelo e-mail <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>''')

def trocas(head, nav, foot):
    return _pg(head, nav, foot, "/trocas/", "Trocas, Devoluções e Envio | Rielson Fragoso",
        "Prazo de envio, direito de arrependimento, trocas e devoluções dos livros usados e dos materiais.", "Trocas, devoluções e envio", f'''
<p class="upd">Atualizada em 17 de novembro de 2026.</p>
<h2>Livros usados</h2>
<ul>
<li><b>Estado do livro:</b> todos os livros são usados. As fotos e os vídeos mostram o exemplar real que você vai receber, e marcas de uso, grifos ou anotações são informados.</li>
<li><b>Envio:</b> pelos Correios, em até 2 dias úteis após a confirmação do pagamento. Frete fixo de R$ 20 para todo o Brasil e grátis a partir de R$ 100 em livros. Você recebe o código de rastreio pelo WhatsApp.</li>
<li><b>Direito de arrependimento:</b> como a compra é feita à distância, você pode desistir em até 7 dias corridos após receber o livro (art. 49 do Código de Defesa do Consumidor). Avise pelo WhatsApp ou e-mail, devolva o livro no mesmo estado em que recebeu e o valor pago, incluindo o frete, é devolvido via Pix.</li>
<li><b>Problema no pedido:</b> se o livro chegar avariado no transporte ou diferente do anunciado, avise em até 7 dias com fotos. Fazemos a troca, quando houver outro exemplar, ou devolvemos o valor.</li>
<li><b>Extravio:</b> se o pacote se perder nos Correios, reenviamos (havendo exemplar) ou devolvemos o valor integral.</li>
</ul>
<h2>E-books e simulados (Hotmart)</h2>
<p>Têm garantia de 7 dias pela própria Hotmart: o reembolso é solicitado direto na plataforma, sem burocracia.</p>
<h2>Resolução de questões em vídeo</h2>
<p>É um serviço feito sob medida. Se não for entregue no prazo combinado, você pode pedir o reembolso integral. Se encontrar um erro em alguma resolução, corrigimos sem custo.</p>
<h2>Contato</h2>
<p>E-mail: <a href="mailto:{EMAIL}">{EMAIL}</a> · Livros: WhatsApp (21) 97246-4789.</p>''')

def nao_encontrada(head, nav, foot):
    return head("Página não encontrada | Rielson Fragoso", "Esta página não existe.", "/404.html") + nav("") + '''<main>
<section class="board phero"><div class="wrap stack"><span class="eyebrow">Erro 404</span><h1 style="color:var(--chalk)">Essa página não existe (ou mudou de lugar)</h1>
<p class="lead">Talvez o livro já tenha sido vendido ou o link esteja incompleto.</p>
<div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn" href="/livros/">Ver livros à venda</a><a class="btn line" style="color:var(--chalk)" href="/">Ir para o início</a></div></div></section></main>''' + foot

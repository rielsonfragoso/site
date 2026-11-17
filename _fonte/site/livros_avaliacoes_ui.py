"""Seção 'Quem já comprou, recomenda!' + formulário de avaliação (moderado)."""
import html
from datetime import date
from livros_avaliacoes import AVALIACOES
e = html.escape
EMAIL = "academiamatematica.rj@gmail.com"
ENDPOINT = "https://formsubmit.co/ajax/" + EMAIL
VISIVEIS = 6

def estrelas(n):
    n = max(1, min(5, int(n)))
    return f'<span class="rv-stars" aria-label="{n} de 5 estrelas">' + "★" * n + '<span class="off">' + "★" * (5 - n) + "</span></span>"

def _data(s):
    try:
        y, m, d = s.split("-"); meses = "jan fev mar abr mai jun jul ago set out nov dez".split()
        return f"{int(d)} {meses[int(m)-1]} {y}"
    except Exception:
        return ""

def secao():
    revs = sorted(AVALIACOES, key=lambda r: r.get("data", ""), reverse=True)
    cards = []
    for i, r in enumerate(revs):
        conf = '<span class="rv-ok">✓ Compra confirmada</span>' if r.get("confirmada") else ""
        livro = f'<p class="rv-book">Livro: {e(r["livro"])}</p>' if r.get("livro") else ""
        dt = f'<time datetime="{e(r["data"])}">{_data(r["data"])}</time>' if r.get("data") else ""
        cards.append(f'<article class="rv"{" hidden data-more" if i >= VISIVEIS else ""}>{estrelas(r["nota"])}'
                     f'<p class="rv-txt">“{e(r["texto"])}”</p>{livro}<p class="rv-who"><b>{e(r["nome"])}</b>{conf}{dt}</p></article>')
    if cards:
        lista = f'<div class="rv-grid">{"".join(cards)}</div>'
        if len(revs) > VISIVEIS:
            lista += '<button type="button" class="btn line rv-more" id="rv-more">Ver mais avaliações</button>'
    else:
        lista = ('<div class="rv-empty"><p><b>Ainda estamos reunindo os primeiros depoimentos publicados.</b> '
                 'Só exibimos aqui avaliações reais, enviadas por clientes e autorizadas por eles.</p></div>')
    return f'''
<section class="rv-band" id="avaliacoes">
  <div class="wrap stack" style="gap:18px">
    <span class="eyebrow">Avaliações de clientes</span>
    <h2>Quem já comprou, recomenda!</h2>
    <p class="lead">A melhor forma de conhecer nossa loja é ouvir quem já recebeu seus livros.</p>
    <div class="rv-intro">
      <p>Comprar livros usados pela internet exige confiança. Por isso, queremos que você conheça a experiência de quem já comprou conosco.</p>
      <p>Aqui você encontra opiniões reais de clientes que receberam seus livros e compartilharam sua experiência.</p>
      <p>Nossa proposta é simples: livros usados, preços acessíveis, informações transparentes e compromisso com cada pedido.</p>
      <p><b>Já comprou conosco? Sua opinião é muito importante!</b></p>
    </div>
    {lista}
    <div class="rv-cta"><p>Já comprou conosco? Conte como foi sua experiência e ajude outros leitores a comprar com confiança.</p>
      <button type="button" class="btn" id="rv-open">Já comprei. Quero avaliar!</button></div>
  </div>
</section>
<div class="co" id="rv-modal" role="dialog" aria-modal="true" aria-labelledby="rv-title" hidden>
  <div class="co-box">
    <div class="co-head"><h2 id="rv-title">Avaliar minha compra</h2><button type="button" class="co-x" id="rv-close" aria-label="Fechar">✕</button></div>
    <form id="rv-form" novalidate>
      <label>Nome que deseja exibir *<input name="nome" maxlength="40" autocomplete="given-name" placeholder="Ex.: Tiago, ou Tiago S."></label>
      <fieldset class="rv-rate"><legend>Sua nota *</legend>
        <div class="rv-pick">{"".join(f'<input type="radio" name="nota" id="n{n}" value="{n}"><label for="n{n}" title="{n} estrela{"s" if n>1 else ""}">★</label>' for n in range(5,0,-1))}</div></fieldset>
      <label>Comentário sobre a experiência *<textarea name="texto" rows="4" minlength="10" maxlength="600" placeholder="Como foi a compra, o envio e o estado do livro?"></textarea></label>
      <label>Livro adquirido (opcional)<input name="livro" maxlength="120"></label>
      <label class="rv-consent"><input type="checkbox" name="autorizo"> <span>Autorizo a publicação do meu depoimento nesta página. *</span></label>
      <p class="co-note">Seu depoimento poderá ser publicado nesta página para ajudar outros leitores a conhecerem nossa loja. Não publicaremos seu telefone, endereço ou outros dados pessoais. Toda avaliação passa por aprovação antes de aparecer aqui.</p>
      <input type="text" name="_honey" tabindex="-1" autocomplete="off" class="hp" aria-hidden="true">
      <p class="co-msg" id="rv-msg" role="alert" hidden></p>
      <button class="btn co-send" type="submit">Enviar avaliação</button>
    </form>
    <div id="rv-done" hidden><p class="rv-thanks"><b>Obrigado pela avaliação!</b> Ela foi recebida e vai aparecer aqui depois de aprovada.</p></div>
  </div>
</div>
<script>
(function(){{
  var m=document.getElementById('rv-modal'), f=document.getElementById('rv-form'), msg=document.getElementById('rv-msg'), t0=0;
  function open(){{m.hidden=false;document.body.classList.add('co-open');t0=Date.now();f.nome.focus();}}
  function close(){{m.hidden=true;document.body.classList.remove('co-open');}}
  document.getElementById('rv-open').addEventListener('click',open);
  document.getElementById('rv-close').addEventListener('click',close);
  document.addEventListener('keydown',function(ev){{if(ev.key==='Escape'&&!m.hidden)close();}});
  var more=document.getElementById('rv-more'); if(more)more.addEventListener('click',function(){{[].forEach.call(document.querySelectorAll('[data-more]'),function(x){{x.hidden=false;}});more.hidden=true;}});
  function clean(s){{return s.replace(/<[^>]*>/g,'').replace(/[\\u0000-\\u0008\\u000B\\u000C\\u000E-\\u001F]/g,'').replace(/https?:\\/\\/\\S+/gi,'[link removido]').trim();}}
  f.addEventListener('submit',function(ev){{
    ev.preventDefault(); msg.hidden=true;
    if(f._honey.value)return;
    if(Date.now()-t0<4000){{msg.textContent='Aguarde um instante e tente de novo.';msg.hidden=false;return;}}
    var nome=clean(f.nome.value), texto=clean(f.texto.value), livro=clean(f.livro.value), nota=(f.querySelector('input[name=nota]:checked')||{{}}).value;
    var err=!nome?'Informe o nome que deseja exibir.':!nota?'Escolha uma nota de 1 a 5 estrelas.':texto.length<10?'Escreva um comentário (pelo menos 10 caracteres).':!f.autorizo.checked?'Para enviar, é preciso autorizar a publicação.':'';
    f.nome.setAttribute('aria-invalid',nome?'false':'true'); f.texto.setAttribute('aria-invalid',texto.length>=10?'false':'true');
    if(err){{msg.textContent=err;msg.hidden=false;return;}}
    try{{if(localStorage.getItem('rv-sent'))
      {{msg.textContent='Você já enviou uma avaliação deste aparelho. Obrigado!';msg.hidden=false;return;}}}}catch(e){{}}
    var btn=f.querySelector('button[type=submit]'); btn.disabled=true; btn.textContent='Enviando…';
    var data={{_subject:'Avaliação de livros (pendente): '+nome+' – '+nota+' estrelas',_template:'table',_captcha:'false',
      nome_publico:nome,nota:nota+' de 5',comentario:texto,livro:livro||'(não informado)',autorizou_publicacao:'sim',
      enviado_em:new Date().toLocaleString('pt-BR'),status:'PENDENTE DE APROVAÇÃO'}};
    fetch('{ENDPOINT}',{{method:'POST',headers:{{'Content-Type':'application/json','Accept':'application/json'}},body:JSON.stringify(data)}})
      .then(function(r){{return r.json().then(function(j){{if(!r.ok||String(j.success)==='false')throw 0;}});}})
      .then(function(){{try{{localStorage.setItem('rv-sent','1');}}catch(e){{}} f.hidden=true; document.getElementById('rv-done').hidden=false;}})
      .catch(function(){{msg.textContent='Não foi possível enviar agora. Tente de novo em alguns minutos.';msg.hidden=false;}})
      .then(function(){{btn.disabled=false;btn.textContent='Enviar avaliação';}});
  }});
}})();
</script>'''

CSS = '''
.rv-band{background:var(--navy);color:var(--chalk);border-block:3px solid var(--yellow)}
.rv-band h2{color:var(--chalk)}
.rv-band .eyebrow{color:var(--yellow)}
.rv-band .lead{color:var(--chalk-dim)}
.rv-intro{display:flex;flex-direction:column;gap:8px;max-width:70ch;color:var(--chalk-dim)}
.rv-intro b{color:var(--chalk)}
.rv-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px}
.rv{background:#FFFFFF;color:#16233F;border-radius:14px;padding:16px 18px;display:flex;flex-direction:column;gap:8px;border-top:4px solid var(--yellow);min-width:0}
.rv[hidden]{display:none}
.rv-stars{color:#E0A800;font-size:1.15rem;letter-spacing:2px}
.rv-stars .off{color:#D5D9E3}
.rv-txt{font-size:.98rem;line-height:1.5}
.rv-book{font-size:.85rem;color:#56607A}
.rv-who{display:flex;flex-wrap:wrap;gap:6px 10px;align-items:center;font-size:.9rem;color:#56607A;margin-top:auto}
.rv-who b{color:#16233F}
.rv-ok{background:#E3EDE2;color:#2F6B3E;font:700 .75rem var(--display);border-radius:999px;padding:2px 9px}
.rv-empty{background:rgba(255,255,255,.07);border:1px dashed var(--yellow);border-radius:14px;padding:16px 18px;color:var(--chalk-dim)}
.rv-empty b{color:var(--chalk)}
.rv-more{color:var(--chalk);align-self:flex-start}
.rv-cta{display:flex;flex-wrap:wrap;gap:12px 18px;align-items:center;justify-content:space-between;border-top:1px solid rgba(255,255,255,.15);padding-top:16px}
.rv-cta p{flex:1 1 300px;color:var(--chalk-dim);min-width:0}
#rv-form{display:flex;flex-direction:column;gap:12px}
#rv-form label{display:flex;flex-direction:column;gap:5px;font:600 .88rem var(--display)}
#rv-form input[type=text],#rv-form input:not([type]),#rv-form textarea{font:400 1rem var(--body);color:var(--ink);background:var(--surface);border:1.5px solid var(--line);border-radius:10px;padding:11px 12px;width:100%}
#rv-form [aria-invalid="true"]{border-color:var(--red)}
.rv-rate{border:0;margin:0;padding:0}
.rv-rate legend{font:600 .88rem var(--display);margin-bottom:4px}
.rv-pick{display:inline-flex;flex-direction:row-reverse;gap:4px}
.rv-pick input{position:absolute;opacity:0;width:1px;height:1px}
.rv-pick label{font-size:2.2rem!important;color:#C9CEDB;cursor:pointer;line-height:1}
.rv-pick input:checked~label,.rv-pick label:hover,.rv-pick label:hover~label{color:#E0A800}
.rv-pick input:focus-visible+label{outline:3px solid var(--yellow);outline-offset:2px;border-radius:4px}
#rv-form .rv-consent{flex-direction:row;align-items:flex-start;gap:10px;font-weight:500}
.rv-consent input{width:20px;height:20px;margin-top:2px;flex:none;accent-color:var(--navy)}
.hp{position:absolute!important;left:-9999px;width:1px;height:1px;opacity:0}
.rv-thanks{background:var(--green-soft);border-radius:12px;padding:16px}
'''

"""Página /aulas/ — pedido de aula particular de matemática (online) pelo WhatsApp."""
WA = "5521972464789"
PRECO = 50

CSS = '''
.phero{padding-block:clamp(40px,7vw,76px)}
.phero h1{color:var(--chalk);font-size:clamp(2rem,5vw,3.1rem)}
.ahero{display:grid;grid-template-columns:1.2fr .8fr;gap:clamp(20px,4vw,48px);align-items:center}
.ahero>*{min-width:0}
.price-card{background:var(--chalk);color:#16233F;border-radius:16px;padding:22px;display:flex;flex-direction:column;gap:6px;transform:rotate(1.5deg);box-shadow:8px 8px 0 var(--yellow)}
.price-card .v{font:700 clamp(2.4rem,6vw,3.2rem) var(--display);line-height:1}
.price-card .v small{font-size:.4em;font-weight:600}
.price-card p{color:#56607A}
.levels{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.levels>div{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:18px;display:flex;flex-direction:column;gap:6px;min-width:0}
.levels p{color:var(--muted);font-size:.95rem}
.sched{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;max-width:640px}
.sched>div{background:var(--yellow-soft);border-radius:14px;padding:14px;text-align:center;min-width:0}
.sched b{display:block;font:700 1.1rem var(--display)}
.sched span{color:var(--muted);font-size:.92rem}
.aform{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:clamp(18px,4vw,30px);display:flex;flex-direction:column;gap:14px;max-width:760px;scroll-margin-top:90px}
.aform label,.aform legend{display:flex;flex-direction:column;gap:6px;font:600 .9rem var(--display)}
.aform input[type=text],.aform input[type=date],.aform select,.aform textarea{font:400 1rem var(--body);color:var(--ink);background:var(--bg);border:1.5px solid var(--line);border-radius:10px;padding:11px 12px;width:100%}
.aform [aria-invalid="true"]{border-color:var(--red)!important}
.aform fieldset{border:0;margin:0;padding:0;display:flex;flex-direction:column;gap:8px;min-width:0}
.aform .f2{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.aform .f2>*{min-width:0}
.pills{display:flex;flex-wrap:wrap;gap:8px}
.pills label{flex-direction:row;align-items:center;gap:8px;font:600 .92rem var(--display);background:var(--bg);border:1.5px solid var(--line);border-radius:999px;padding:8px 14px;cursor:pointer}
.pills input{accent-color:var(--navy);width:16px;height:16px}
:root[data-theme="dark"] .pills input{accent-color:var(--yellow)}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]) .pills input{accent-color:var(--yellow)}}
.pills label:has(input:checked){border-color:var(--navy);background:var(--yellow-soft)}
.amsg{color:var(--red);font-weight:700}
.anote{font-size:.9rem;color:var(--muted)}
.btn.wabtn{background:#1FA855;color:#fff;border:0;cursor:pointer;font-size:1.05rem;justify-content:center}
@media (max-width:860px){.levels{grid-template-columns:1fr 1fr}}
@media (max-width:640px){.ahero,.aform .f2{grid-template-columns:1fr}.levels{grid-template-columns:1fr}.sched{grid-template-columns:1fr 1fr 1fr}}
'''

JS = '''<script>
(function(){
  var f=document.getElementById('aula-form'), msg=document.getElementById('amsg');
  function checked(n){return [].map.call(f.querySelectorAll('input[name="'+n+'"]:checked'),function(i){return i.value;});}
  f.addEventListener('submit',function(ev){
    ev.preventDefault(); msg.hidden=true;
    var bad=null;
    [['nome',f.nome],['nivel',f.nivel],['assunto',f.assunto]].forEach(function(p){var ok=!!p[1].value.trim();p[1].setAttribute('aria-invalid',ok?'false':'true');if(!ok&&!bad)bad=p[1];});
    if(bad){msg.textContent='Preencha nome, nível e assunto, por favor.';msg.hidden=false;bad.focus();return;}
    var dias=checked('dia'), hrs=checked('hora');
    var L=['*Pedido de aula particular · rielsonfragoso.com.br*','',
      'Nome: '+f.nome.value.trim(),
      'Nível: '+f.nivel.value,
      'Assunto: '+f.assunto.value.trim()];
    if(f.concurso.value.trim())L.push('Concurso / prova: '+f.concurso.value.trim());
    L.push('Formato: '+f.formato.value);
    L.push('Dias preferidos: '+(dias.length?dias.join(', '):'qualquer um dos disponíveis'));
    L.push('Horário preferido: '+(hrs.length?hrs.join(', '):'qualquer um entre 19h e 22h'));
    if(f.inicio.value){var d=f.inicio.value.split('-');L.push('Gostaria de começar a partir de: '+d[2]+'/'+d[1]+'/'+d[0]);}
    if(f.obs.value.trim())L.push('','Obs.: '+f.obs.value.trim());
    L.push('','Aguardo a confirmação da data e do horário.');
    var url='https://wa.me/__WA__?text='+encodeURIComponent(L.join('\\n'));
    document.getElementById('ago').href=url; document.getElementById('adone').hidden=false;
    window.location.href=url;
  });
})();
</script>'''.replace("__WA__", WA)

def page(head, nav, foot):
    from urllib.parse import quote
    geral = f"https://wa.me/{WA}?text=" + quote("Olá, Rielson! Vi no site e queria saber mais sobre as aulas particulares de matemática.")
    return head("Aula particular de matemática online | Rielson Fragoso",
                f"Aulas particulares de matemática online: ensino fundamental, ensino médio, olimpíadas e concursos públicos. R$ {PRECO} a hora, com pacotes negociáveis.",
                "/aulas/", extra_css=CSS) + nav("/aulas/") + f'''
<main>
<section class="board phero">
  <div class="wrap ahero">
    <div class="stack">
      <span class="eyebrow">Aula particular · online</span>
      <h1>Aula de matemática no seu ritmo, com quem explica passo a passo</h1>
      <p class="lead">Aulas online e individuais, do ensino fundamental aos concursos públicos. Você me diz o assunto, eu preparo a aula para a sua dúvida.</p>
      <div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn" href="#pedido-sec">Pedir uma aula</a><a class="btn line" style="color:var(--chalk)" href="{geral}" target="_blank" rel="noopener">Tirar dúvida no WhatsApp</a></div>
    </div>
    <div class="price-card">
      <span class="eyebrow" style="color:#56607A">Valor</span>
      <span class="v">R$ {PRECO}<small> / hora</small></span>
      <p>Aula online, individual. Pacotes com várias aulas podem ser negociados.</p>
    </div>
  </div>
</section>

<section class="grid-paper">
  <div class="wrap stack" style="gap:22px">
    <span class="eyebrow">Para quem é</span>
    <h2>Matemática para todas as idades</h2>
    <div class="levels">
      <div><span class="banca">Ensino fundamental</span><h3>Base forte</h3><p>Operações, frações, porcentagem, equações e a matéria da escola.</p></div>
      <div><span class="banca">Olimpíadas</span><h3>Raciocínio</h3><p>Preparação para olimpíadas de matemática, inclusive as mirins.</p></div>
      <div><span class="banca">Ensino médio</span><h3>Escola e vestibular</h3><p>Funções, geometria, trigonometria, combinatória e revisão para provas.</p></div>
      <div><span class="banca">Concursos</span><h3>Foco na banca</h3><p>Matemática, raciocínio lógico e matemática financeira no estilo da sua prova.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap stack" style="gap:22px">
    <span class="eyebrow">Horários</span>
    <h2>Quando acontecem as aulas</h2>
    <div class="sched"><div><b>Terça</b><span>19h às 22h</span></div><div><b>Quarta</b><span>19h às 22h</span></div><div><b>Sexta</b><span>19h às 22h</span></div></div>
    <p class="lead" style="font-size:1.02rem">Depois do seu pedido, eu confirmo a data pelo WhatsApp. Dependendo do assunto, preciso de um tempo para preparar a aula do jeito certo para você.</p>
  </div>
</section>

<section class="plain" id="pedido-sec">
  <div class="wrap stack" style="gap:20px">
    <span class="eyebrow">Pedido de aula</span>
    <h2>Conte o que você precisa</h2>
    <form class="aform" id="aula-form" novalidate>
      <div class="f2">
        <label>Seu nome *<input type="text" name="nome" autocomplete="name" maxlength="80"></label>
        <label>Nível *<select name="nivel"><option value="">Escolha</option><option>Ensino fundamental</option><option>Ensino médio</option><option>Olimpíadas de matemática</option><option>Concurso público</option><option>Faculdade / outro</option></select></label>
      </div>
      <label>Assunto da aula *<input type="text" name="assunto" maxlength="160" placeholder="Ex.: frações, função do 2º grau, porcentagem, raciocínio lógico"></label>
      <label>Concurso ou prova (se tiver)<input type="text" name="concurso" maxlength="120" placeholder="Ex.: Prefeitura de Niterói 2026, banca Selecon"></label>
      <fieldset><legend>Formato</legend>
        <div class="pills"><label><input type="radio" name="formato" value="Aula avulsa (1 hora)" checked>Aula avulsa</label><label><input type="radio" name="formato" value="Quero saber de pacote com várias aulas">Pacote de aulas</label></div></fieldset>
      <fieldset><legend>Dias de preferência</legend>
        <div class="pills"><label><input type="checkbox" name="dia" value="terça">Terça</label><label><input type="checkbox" name="dia" value="quarta">Quarta</label><label><input type="checkbox" name="dia" value="sexta">Sexta</label></div></fieldset>
      <fieldset><legend>Horário de preferência</legend>
        <div class="pills"><label><input type="checkbox" name="hora" value="19h">19h</label><label><input type="checkbox" name="hora" value="20h">20h</label><label><input type="checkbox" name="hora" value="21h">21h</label></div></fieldset>
      <label>A partir de quando? (opcional)<input type="date" name="inicio"></label>
      <label>Algo mais que eu deva saber?<textarea name="obs" rows="3" maxlength="500" placeholder="Ex.: tenho prova dia 20; estou com dificuldade em interpretar os enunciados"></textarea></label>
      <p class="anote">Ao enviar, o seu WhatsApp abre com o pedido já escrito para mim. Eu respondo confirmando a data, o horário e o link da aula. Valor: R$ {PRECO} por hora.</p>
      <p class="amsg" id="amsg" role="alert" hidden></p>
      <button class="btn wabtn" type="submit">Enviar pedido pelo WhatsApp</button>
      <p class="anote" id="adone" hidden>O WhatsApp não abriu? <a id="ago" href="#" target="_blank" rel="noopener">Toque aqui para abrir com o pedido</a>.</p>
    </form>
  </div>
</section>
</main>
''' + JS + foot

"""Página /aulas/ — Resolução de questões sob demanda: a pessoa manda a lista, recebe a resolução explicada em vídeo + PDF.
Pedido enviado pelo WhatsApp com o máximo de contexto. (A URL continua /aulas/ para não quebrar links.)"""
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
.train{background:var(--navy);color:var(--chalk);border-radius:var(--r);padding:clamp(20px,4vw,32px);display:flex;flex-direction:column;gap:10px;border:2px solid var(--yellow)}
.train h2{color:var(--chalk)}
.train p{color:var(--chalk-dim);max-width:70ch}
.train b{color:var(--yellow)}
.train .tag{font-family:var(--hand);font-size:1.6rem;font-weight:600;color:var(--yellow);line-height:1}
.steps{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,1fr);gap:14px;counter-reset:s}
.steps li{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:18px;display:flex;flex-direction:column;gap:6px;min-width:0}
.steps li::before{counter-increment:s;content:counter(s);display:grid;place-items:center;width:32px;height:32px;border-radius:50%;background:var(--yellow);color:var(--on-yellow);font:700 .95rem var(--display)}
.steps p{color:var(--muted);font-size:.95rem}
.get{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.get>div{border-top:3px solid var(--yellow);padding-top:12px;display:flex;flex-direction:column;gap:6px;min-width:0}
.get p{color:var(--muted);font-size:.96rem}
.who{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.who>div{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:22px;display:flex;flex-direction:column;gap:8px;min-width:0}
.who .tag{font-family:var(--hand);font-size:1.5rem;font-weight:600;color:var(--red);line-height:1}
.who p{color:var(--muted)}
.simu{background:var(--yellow-soft);border-radius:var(--r);padding:18px 20px;display:flex;flex-wrap:wrap;gap:10px 18px;align-items:center;justify-content:space-between}
.simu p{flex:1 1 300px;min-width:0}
.aform{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:clamp(18px,4vw,30px);display:flex;flex-direction:column;gap:16px;max-width:780px;scroll-margin-top:90px}
.aform h3{font-size:1.05rem;padding-top:6px;border-top:1px dashed var(--line)}
.aform h3:first-child{border-top:0;padding-top:0}
.aform label,.aform legend{display:flex;flex-direction:column;gap:6px;font:600 .9rem var(--display)}
.aform .hint{font:400 .85rem var(--body);color:var(--muted)}
.aform input[type=text],.aform input[type=date],.aform input[type=url],.aform select,.aform textarea{font:400 1rem var(--body);color:var(--ink);background:var(--bg);border:1.5px solid var(--line);border-radius:10px;padding:11px 12px;width:100%}
.aform [aria-invalid="true"]{border-color:var(--red)!important}
.aform fieldset{border:0;margin:0;padding:0;display:flex;flex-direction:column;gap:8px;min-width:0}
.aform .f2{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.aform .f2>*{min-width:0}
.cond{display:flex;flex-direction:column;gap:14px;background:var(--bg);border-left:4px solid var(--yellow);border-radius:10px;padding:14px}
.pills{display:flex;flex-wrap:wrap;gap:8px}
.pills label{flex-direction:row;align-items:center;gap:8px;font:600 .92rem var(--display);background:var(--bg);border:1.5px solid var(--line);border-radius:999px;padding:8px 14px;cursor:pointer}
.pills input{accent-color:var(--navy);width:16px;height:16px;flex:none}
:root[data-theme="dark"] .pills input{accent-color:var(--yellow)}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]) .pills input{accent-color:var(--yellow)}}
.pills label:has(input:checked){border-color:var(--navy);background:var(--yellow-soft)}
.rec{font:700 .7rem var(--display);background:var(--green-soft);color:var(--green);border-radius:999px;padding:2px 8px;margin-left:4px}
.amsg{color:var(--red);font-weight:700}
.anote{font-size:.9rem;color:var(--muted)}
.btn.wabtn{background:#1FA855;color:#fff;border:0;cursor:pointer;font-size:1.05rem;justify-content:center}
@media (max-width:860px){.steps{grid-template-columns:1fr 1fr}.get{grid-template-columns:1fr}}
@media (max-width:640px){.ahero,.who,.aform .f2{grid-template-columns:1fr}.steps{grid-template-columns:1fr}}
'''

JS = r'''<script>
(function(){
  var f=document.getElementById('aula-form'), msg=document.getElementById('amsg');
  function v(n){var el=f.elements[n];return el&&el.value?el.value.trim():'';}
  function radio(n){var el=f.querySelector('input[name="'+n+'"]:checked');return el?el.value:'';}
  function checked(n){return [].map.call(f.querySelectorAll('input[name="'+n+'"]:checked'),function(i){return i.value;});}
  function sync(){var obj=radio('objetivo');
    document.getElementById('c-escola').hidden=obj!=='escola';
    document.getElementById('c-concurso').hidden=obj!=='concurso';
    document.getElementById('c-outro').hidden=obj!=='outro';}
  f.addEventListener('change',sync); sync();
  function need(list){var bad=null;list.forEach(function(n){var el=f.elements[n];var ok=!!(el&&el.value.trim());if(el)el.setAttribute('aria-invalid',ok?'false':'true');if(!ok&&!bad)bad=el;});return bad;}
  function dt(s){if(!s)return '';var d=s.split('-');return d[2]+'/'+d[1]+'/'+d[0];}
  f.addEventListener('submit',function(ev){
    ev.preventDefault(); msg.hidden=true;
    var obj=radio('objetivo');
    if(!obj){msg.textContent='Escolha para que são as questões.';msg.hidden=false;return;}
    var req=['nome','assunto'];
    if(obj==='escola')req.push('serie');
    if(obj==='concurso')req=req.concat(['concurso','cargo']);
    var bad=need(req);
    if(bad){msg.textContent='Preencha os campos marcados com *.';msg.hidden=false;bad.focus();return;}
    var L=['*Pedido de resolução de questões · rielsonfragoso.com.br*','','Nome: '+v('nome'),
      'Objetivo: '+{concurso:'concurso público',escola:'escola / vestibular',outro:'outro'}[obj]];
    if(obj==='concurso'){L.push('Concurso/órgão: '+v('concurso'),'Cargo: '+v('cargo'));
      if(v('banca'))L.push('Banca: '+v('banca')); if(v('concurso_data'))L.push('Data da prova: '+dt(v('concurso_data')));}
    if(obj==='escola'){L.push('Série/ano: '+v('serie')); if(v('escola_livro'))L.push('Livro/apostila: '+v('escola_livro'));
      if(v('escola_data'))L.push('Data da prova: '+dt(v('escola_data')));}
    if(obj==='outro'&&v('outro_det'))L.push('Detalhes: '+v('outro_det'));
    L.push('','*Assunto(s):* '+v('assunto'));
    L.push('Quantidade de questões: '+radio('qtd'));
    if(v('trava'))L.push('Onde trava: '+v('trava'));
    if(v('prazo'))L.push('Preciso receber até: '+dt(v('prazo')));
    var mats=checked('mat'); L.push('','Vou mandar nesta conversa: '+(mats.length?mats.join(', '):'as questões')+'.');
    if(v('obs'))L.push('','Obs.: '+v('obs'));
    L.push('','Aguardo a confirmação do prazo e do valor.');
    var url='https://wa.me/__WA__?text='+encodeURIComponent(L.join('\n'));
    document.getElementById('ago').href=url; document.getElementById('adone').hidden=false;
    window.location.href=url;
  });
})();
</script>'''.replace("__WA__", WA)

def page(head, nav, foot):
    from urllib.parse import quote
    geral = f"https://wa.me/{WA}?text=" + quote("Olá, Rielson! Vi no site e queria saber mais sobre a resolução de questões em vídeo.")
    return head("Resolução de questões em vídeo | Rielson Fragoso",
                f"Mande sua lista de 10 a 20 questões de matemática e receba a resolução explicada em vídeo e em PDF por R$ {PRECO}. Ideal para concursos e para quem quer tirar dúvidas específicas.",
                "/aulas/", extra_css=CSS) + nav("/aulas/") + f'''
<main>
<section class="board phero">
  <div class="wrap ahero">
    <div class="stack">
      <span class="eyebrow">Resolução de questões sob demanda</span>
      <h1>Mande as questões que te travaram. Eu resolvo explicando, em vídeo.</h1>
      <p class="lead">Você junta os exercícios e as questões de matemática que geraram dúvida. Eu gravo a resolução explicada, passo a passo, e envio o vídeo e o PDF com as soluções para você rever quantas vezes quiser.</p>
      <div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn" href="#pedido-sec">Enviar minha lista</a><a class="btn line" style="color:var(--chalk)" href="{geral}" target="_blank" rel="noopener">Tirar dúvida no WhatsApp</a></div>
    </div>
    <div class="price-card">
      <span class="eyebrow" style="color:#56607A">Lista de 10 a 20 questões</span>
      <span class="v">R$ {PRECO}</span>
      <p>Resolução explicada em vídeo + PDF com as soluções. Listas maiores: valor combinado pelo WhatsApp.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap stack" style="gap:22px">
    <div class="train">
      <span class="tag">o segredo é o treino</span>
      <h2>Subir de nível é resolver o que você ainda não resolve</h2>
      <p>Assistir aula ajuda, mas o salto vem quando você entende exatamente as questões em que errou ou travou. Resolução explicada é o meu ponto forte: o raciocínio, o caminho e onde costuma estar a pegadinha, com a teoria entrando na hora em que ela destrava a questão.</p>
      <p><b>O ideal:</b> junte as questões que você não conseguiu fazer ou que te deixaram em dúvida. Elas mostram onde está a dificuldade, e a resolução vai direto ao ponto.</p>
    </div>
    <span class="eyebrow">Como funciona</span>
    <h2>Do seu pedido ao vídeo pronto</h2>
    <ol class="steps">
      <li><h3>Você monta a lista</h3><p>De 10 a 20 exercícios ou questões de matemática: do livro, da apostila, da lista do professor ou de provas anteriores.</p></li>
      <li><h3>Envia pelo WhatsApp</h3><p>Preencha o pedido abaixo e mande as fotos ou o PDF das questões na mesma conversa.</p></li>
      <li><h3>Eu confirmo o prazo</h3><p>Combinamos o prazo de entrega conforme o tamanho e o assunto da lista.</p></li>
      <li><h3>Você recebe</h3><p>O vídeo com a resolução explicada e o PDF com as soluções, para rever quando quiser.</p></li>
    </ol>
    <span class="eyebrow" style="margin-top:12px">O que você recebe</span>
    <div class="get">
      <div><h3>Vídeo explicado</h3><p>Cada questão resolvida passo a passo, com o porquê de cada etapa. Pausa, volta e reassiste quantas vezes precisar.</p></div>
      <div><h3>PDF das soluções</h3><p>As resoluções por escrito, para consultar rápido na revisão antes da prova.</p></div>
      <div><h3>Foco no que importa</h3><p>Nada de aula genérica: só as questões que você escolheu, no nível e no estilo da sua prova.</p></div>
    </div>
  </div>
</section>

<section class="grid-paper">
  <div class="wrap stack" style="gap:22px">
    <span class="eyebrow">Para quem é</span>
    <h2>Para quem quer tirar dúvidas específicas e avançar mais rápido</h2>
    <div class="who">
      <div><span class="tag">concurseiros</span><h3>Concursos públicos</h3><p>Você já estuda, mas algumas questões da banca ainda te derrubam. Mande as que você erra: matemática, raciocínio lógico, matemática financeira. Com o concurso, o cargo e a banca, eu resolvo no estilo da sua prova.</p></div>
      <div><span class="tag">estudantes</span><h3>Escola e vestibular</h3><p>Do ensino fundamental ao médio e ao ENEM. Vá juntando os exercícios do livro, da lista ou dos testes que ficaram sem resposta e mande tudo de uma vez antes da prova.</p></div>
    </div>
    <div class="simu"><p><b>Quer um simulado completo do seu concurso?</b> Simulados eu monto a partir do edital e da banca, e lanço para todos os candidatos. Peça o do seu concurso na página de concursos.</p><a class="btn" href="/concursos/#pedir">Pedir simulado</a></div>
  </div>
</section>

<section class="plain" id="pedido-sec" style="scroll-margin-top:80px">
  <div class="wrap stack" style="gap:20px">
    <span class="eyebrow">Pedido</span>
    <h2>Conte o que você precisa</h2>
    <form class="aform" id="aula-form" novalidate>
      <h3>1. Para que são as questões?</h3>
      <label>Seu nome *<input type="text" name="nome" autocomplete="name" maxlength="80"></label>
      <fieldset><legend>Objetivo *</legend>
        <div class="pills">
          <label><input type="radio" name="objetivo" value="concurso">Concurso público</label>
          <label><input type="radio" name="objetivo" value="escola">Escola / vestibular</label>
          <label><input type="radio" name="objetivo" value="outro">Outro</label>
        </div></fieldset>
      <div class="cond" id="c-concurso" hidden>
        <div class="f2">
          <label>Concurso / órgão *<input type="text" name="concurso" maxlength="120" placeholder="Ex.: Prefeitura de Niterói 2026"></label>
          <label>Cargo *<input type="text" name="cargo" maxlength="120" placeholder="Ex.: Assistente Administrativo"></label>
        </div>
        <div class="f2">
          <label>Banca<input type="text" name="banca" maxlength="60" placeholder="Ex.: Selecon, FGV, Cebraspe"></label>
          <label>Data da prova<input type="date" name="concurso_data"></label>
        </div>
      </div>
      <div class="cond" id="c-escola" hidden>
        <div class="f2">
          <label>Série / ano *<select name="serie"><option value="">Escolha</option><option>2º ano – Fundamental</option><option>3º ano – Fundamental</option><option>4º ano – Fundamental</option><option>5º ano – Fundamental</option><option>6º ano – Fundamental</option><option>7º ano – Fundamental</option><option>8º ano – Fundamental</option><option>9º ano – Fundamental</option><option>1º ano – Médio</option><option>2º ano – Médio</option><option>3º ano – Médio</option><option>Pré-vestibular / ENEM</option><option>EJA / supletivo</option></select></label>
          <label>Data da prova<input type="date" name="escola_data"></label>
        </div>
        <label>Livro ou apostila<input type="text" name="escola_livro" maxlength="160" placeholder="Ex.: Praticando Matemática 8º ano, capítulo 5"></label>
      </div>
      <div class="cond" id="c-outro" hidden>
        <label>Conte um pouco mais<input type="text" name="outro_det" maxlength="200" placeholder="Ex.: olimpíada de matemática; Cálculo I na faculdade"></label>
      </div>

      <h3>2. As questões</h3>
      <label>Assunto(s) das questões *<span class="hint">O mais específico possível. Ex.: “porcentagem: aumentos e descontos sucessivos”, “trigonometria no triângulo retângulo”, “juros compostos”.</span>
        <textarea name="assunto" rows="2" maxlength="400"></textarea></label>
      <fieldset><legend>Quantidade</legend>
        <div class="pills">
          <label><input type="radio" name="qtd" value="10 a 20 questões (R$ 50)" checked>10 a 20 questões · R$ {PRECO}</label>
          <label><input type="radio" name="qtd" value="menos de 10 questões (combinar)">Menos de 10</label>
          <label><input type="radio" name="qtd" value="mais de 20 questões (orçamento)">Mais de 20</label>
        </div></fieldset>
      <label>Onde você trava?<span class="hint">Ex.: não sei por onde começar; erro na interpretação; chego numa resposta que não está nas alternativas.</span>
        <textarea name="trava" rows="2" maxlength="400"></textarea></label>
      <label>Até quando precisa receber?<input type="date" name="prazo"></label>

      <h3>3. Material</h3>
      <fieldset><legend>O que vai mandar na conversa (foto ou PDF)?</legend>
        <div class="pills">
          <label><input type="checkbox" name="mat" value="as questões com dúvida" checked>As questões <span class="rec">essencial</span></label>
          <label><input type="checkbox" name="mat" value="gabarito oficial">Gabarito oficial</label>
          <label><input type="checkbox" name="mat" value="minha tentativa de resolução">Minha tentativa de resolução</label>
          <label><input type="checkbox" name="mat" value="edital">Edital</label>
        </div></fieldset>
      <label>Algo mais que eu deva saber?<textarea name="obs" rows="2" maxlength="500"></textarea></label>

      <p class="anote">Ao enviar, o seu WhatsApp abre com o pedido já escrito para mim. Logo em seguida, mande as fotos ou o PDF das questões na mesma conversa. Eu respondo confirmando prazo e valor.</p>
      <p class="amsg" id="amsg" role="alert" hidden></p>
      <button class="btn wabtn" type="submit">Enviar pedido pelo WhatsApp</button>
      <p class="anote" id="adone" hidden>O WhatsApp não abriu? <a id="ago" href="#" target="_blank" rel="noopener">Toque aqui para abrir com o pedido</a>.</p>
    </form>
  </div>
</section>
</main>
''' + JS + foot

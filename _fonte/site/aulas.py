"""Página /aulas/ — pedido de aula particular de matemática (ao vivo online ou gravada sob demanda) pelo WhatsApp.
O formulário muda conforme a modalidade e o objetivo, para o pedido chegar com o máximo de contexto."""
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
.modes{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.modes>div{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:22px;display:flex;flex-direction:column;gap:10px;min-width:0}
.modes .tag{font-family:var(--hand);font-size:1.5rem;font-weight:600;color:var(--red);line-height:1}
.modes ul{margin:0;padding-left:1.1em;color:var(--muted);display:flex;flex-direction:column;gap:5px}
.levels{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.levels>div{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:18px;display:flex;flex-direction:column;gap:6px;min-width:0}
.levels p{color:var(--muted);font-size:.95rem}
.sched{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;max-width:640px}
.sched>div{background:var(--yellow-soft);border-radius:14px;padding:14px;text-align:center;min-width:0}
.sched b{display:block;font:700 1.1rem var(--display)}
.sched span{color:var(--muted);font-size:.92rem}
.ctx{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.ctx>div{border-top:3px solid var(--yellow);padding-top:12px;display:flex;flex-direction:column;gap:6px;min-width:0}
.ctx p{color:var(--muted);font-size:.96rem}
.ctx .ex{font-size:.92rem}
.ctx .ex s{color:var(--red)}
.aform{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:clamp(18px,4vw,30px);display:flex;flex-direction:column;gap:16px;max-width:780px;scroll-margin-top:90px}
.aform h3{font-size:1.05rem;padding-top:6px;border-top:1px dashed var(--line)}
.aform h3:first-child{border-top:0;padding-top:0}
.aform label,.aform legend{display:flex;flex-direction:column;gap:6px;font:600 .9rem var(--display)}
.aform .hint{font:400 .85rem var(--body);color:var(--muted)}
.aform input[type=text],.aform input[type=date],.aform input[type=url],.aform select,.aform textarea{font:400 1rem var(--body);color:var(--ink);background:var(--bg);border:1.5px solid var(--line);border-radius:10px;padding:11px 12px;width:100%}
.aform [aria-invalid="true"]{border-color:var(--red)!important}
.aform fieldset{border:0;margin:0;padding:0;display:flex;flex-direction:column;gap:8px;min-width:0}
.aform .f2{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.aform .f3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px}
.aform .f2>*,.aform .f3>*{min-width:0}
.cond{display:flex;flex-direction:column;gap:14px;background:var(--bg);border-left:4px solid var(--yellow);border-radius:10px;padding:14px}
.pills{display:flex;flex-wrap:wrap;gap:8px}
.pills label{flex-direction:row;align-items:center;gap:8px;font:600 .92rem var(--display);background:var(--bg);border:1.5px solid var(--line);border-radius:999px;padding:8px 14px;cursor:pointer}
.cond .pills label{background:var(--surface)}
.pills input{accent-color:var(--navy);width:16px;height:16px;flex:none}
:root[data-theme="dark"] .pills input{accent-color:var(--yellow)}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]) .pills input{accent-color:var(--yellow)}}
.pills label:has(input:checked){border-color:var(--navy);background:var(--yellow-soft)}
.pills.big label{border-radius:14px;padding:12px 14px;flex:1 1 220px;align-items:flex-start}
.pills.big label span{display:flex;flex-direction:column;gap:2px}
.pills.big label small{font:400 .84rem var(--body);color:var(--muted)}
.rec{font:700 .7rem var(--display);background:var(--green-soft);color:var(--green);border-radius:999px;padding:2px 8px;margin-left:4px}
.amsg{color:var(--red);font-weight:700}
.anote{font-size:.9rem;color:var(--muted)}
.btn.wabtn{background:#1FA855;color:#fff;border:0;cursor:pointer;font-size:1.05rem;justify-content:center}
@media (max-width:860px){.levels{grid-template-columns:1fr 1fr}.ctx{grid-template-columns:1fr}}
@media (max-width:640px){.ahero,.modes,.aform .f2,.aform .f3{grid-template-columns:1fr}.levels{grid-template-columns:1fr}.sched{grid-template-columns:1fr 1fr 1fr}}
'''

JS = r'''<script>
(function(){
  var f=document.getElementById('aula-form'), msg=document.getElementById('amsg');
  function v(n){var el=f.elements[n];return el&&el.value?el.value.trim():'';}
  function radio(n){var el=f.querySelector('input[name="'+n+'"]:checked');return el?el.value:'';}
  function checked(n){return [].map.call(f.querySelectorAll('input[name="'+n+'"]:checked'),function(i){return i.value;});}
  function sync(){
    var modo=radio('modo'), obj=radio('objetivo');
    document.getElementById('c-vivo').hidden=modo!=='ao vivo';
    document.getElementById('c-gravada').hidden=modo!=='gravada';
    document.getElementById('c-escola').hidden=obj!=='escola';
    document.getElementById('c-concurso').hidden=obj!=='concurso';
    document.getElementById('c-outro').hidden=!(obj==='olimpiada'||obj==='outro');
  }
  f.addEventListener('change',sync); sync();
  function need(list){var bad=null;list.forEach(function(n){var el=f.elements[n];var ok=!!(el&&el.value.trim());if(el)el.setAttribute('aria-invalid',ok?'false':'true');if(!ok&&!bad)bad=el;});return bad;}
  function dt(s){if(!s)return '';var d=s.split('-');return d[2]+'/'+d[1]+'/'+d[0];}
  f.addEventListener('submit',function(ev){
    ev.preventDefault(); msg.hidden=true;
    var modo=radio('modo'), obj=radio('objetivo');
    if(!modo||!obj){msg.textContent='Escolha a modalidade e o objetivo da aula.';msg.hidden=false;return;}
    var req=['nome','assunto'];
    if(obj==='escola')req=req.concat(['serie']);
    if(obj==='concurso')req=req.concat(['concurso','cargo']);
    var bad=need(req);
    if(bad){msg.textContent='Preencha os campos marcados com *.';msg.hidden=false;bad.focus();return;}
    var L=['*Pedido de aula particular · rielsonfragoso.com.br*','','Nome: '+v('nome'),
      'Modalidade: '+(modo==='ao vivo'?'aula ao vivo, online (R$ __PRECO__/h)':'aula gravada sob demanda')];
    var objt={escola:'prova ou matéria da escola',concurso:'concurso público',olimpiada:'olimpíada de matemática',outro:'outro objetivo'}[obj];
    L.push('Objetivo: '+objt);
    if(obj==='escola'){
      L.push('Série/ano: '+v('serie'));
      if(v('escola_livro'))L.push('Livro e capítulo: '+v('escola_livro'));
      if(v('escola_data'))L.push('Data da prova/teste: '+dt(v('escola_data')));
    }
    if(obj==='concurso'){
      L.push('Concurso/órgão: '+v('concurso'),'Cargo: '+v('cargo'));
      if(v('banca'))L.push('Banca: '+v('banca'));
      if(v('concurso_data'))L.push('Data da prova: '+dt(v('concurso_data')));
      if(v('edital'))L.push('Edital: '+v('edital'));
    }
    if((obj==='olimpiada'||obj==='outro')&&v('outro_det'))L.push('Detalhes: '+v('outro_det'));
    L.push('','*Assunto específico:* '+v('assunto'));
    if(v('trava'))L.push('Onde trava / o que já sabe: '+v('trava'));
    L.push('Foco da aula: '+radio('foco'));
    if(modo==='ao vivo'){
      L.push('Quantidade: '+radio('qtd'));
      var d=checked('dia'),h=checked('hora');
      L.push('Dias preferidos: '+(d.length?d.join(', '):'qualquer um (terça, quarta ou sexta)'));
      L.push('Horário preferido: '+(h.length?h.join(', '):'qualquer um entre 19h e 22h'));
      if(v('inicio'))L.push('A partir de: '+dt(v('inicio')));
    }else{
      if(v('prazo'))L.push('Preciso receber até: '+dt(v('prazo')));
    }
    var mats=checked('mat');
    if(mats.length)L.push('','Vou mandar nesta conversa: '+mats.join(', ')+'.');
    if(v('obs'))L.push('','Obs.: '+v('obs'));
    L.push('','Aguardo a confirmação'+(modo==='ao vivo'?' da data e do horário.':' do prazo e do valor.'));
    var url='https://wa.me/__WA__?text='+encodeURIComponent(L.join('\n'));
    document.getElementById('ago').href=url; document.getElementById('adone').hidden=false;
    window.location.href=url;
  });
})();
</script>'''.replace("__WA__", WA).replace("__PRECO__", str(PRECO))

def page(head, nav, foot):
    from urllib.parse import quote
    geral = f"https://wa.me/{WA}?text=" + quote("Olá, Rielson! Vi no site e queria saber mais sobre as aulas particulares de matemática.")
    return head("Aula particular de matemática online | Rielson Fragoso",
                f"Aulas particulares de matemática ao vivo (online, R$ {PRECO} a hora) ou gravadas sob demanda, para prova da escola, olimpíadas e concursos públicos.",
                "/aulas/", extra_css=CSS) + nav("/aulas/") + f'''
<main>
<section class="board phero">
  <div class="wrap ahero">
    <div class="stack">
      <span class="eyebrow">Aula particular de matemática</span>
      <h1>Uma aula montada para a sua prova, não uma aula genérica</h1>
      <p class="lead">Ao vivo pela internet ou gravada sob demanda. Você me conta o assunto, a prova e onde trava; eu preparo a aula com teoria e os exercícios mais próximos da realidade que você vai enfrentar.</p>
      <div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn" href="#pedido-sec">Pedir uma aula</a><a class="btn line" style="color:var(--chalk)" href="{geral}" target="_blank" rel="noopener">Tirar dúvida no WhatsApp</a></div>
    </div>
    <div class="price-card">
      <span class="eyebrow" style="color:#56607A">Aula ao vivo</span>
      <span class="v">R$ {PRECO}<small> / hora</small></span>
      <p>Online e individual. Pacotes com várias aulas podem ser negociados. Aula gravada: valor combinado conforme o conteúdo.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap stack" style="gap:22px">
    <span class="eyebrow">Duas modalidades</span>
    <h2>Escolha como prefere estudar</h2>
    <div class="modes">
      <div><span class="tag">ao vivo</span><h3>Aula online, em tempo real</h3>
        <ul><li>Terça, quarta ou sexta, entre 19h e 22h</li><li>Você tira dúvidas na hora e resolve exercícios comigo</li><li>Sempre que possível, a aula fica gravada para você reassistir</li><li>R$ {PRECO} por hora, com pacotes negociáveis</li></ul></div>
      <div><span class="tag">gravada</span><h3>Aula sob demanda, feita para você</h3>
        <ul><li>Você me diz o assunto e o objetivo: prova da escola, concurso X para o cargo Y da banca Z</li><li>Eu monto a aula com teoria e uma lista de problemas no nível e no estilo da sua prova</li><li>Você recebe o vídeo e assiste quantas vezes quiser</li><li>Valor combinado conforme o tamanho do conteúdo</li></ul></div>
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
    <span class="eyebrow">Quanto mais contexto, melhor a aula</span>
    <h2>O que me ajuda a preparar a aula certa</h2>
    <div class="ctx">
      <div><h3>Assunto bem específico</h3><p>Não só o tema geral: diga exatamente a parte que precisa.</p>
        <p class="ex"><s>trigonometria</s> → “trigonometria no triângulo retângulo” ou “funções trigonométricas”</p></div>
      <div><h3>Prova da escola</h3><p>Série, livro e capítulo, data da prova. Fotos do livro, do caderno, de provas e testes anteriores ou da lista do professor.</p></div>
      <div><h3>Concurso</h3><p>Concurso, cargo e banca. Com o edital, eu confiro o conteúdo e monto a aula com questões da própria banca.</p></div>
    </div>
    <div style="display:flex;flex-direction:column;gap:10px">
      <h3>Horários das aulas ao vivo</h3>
      <div class="sched"><div><b>Terça</b><span>19h às 22h</span></div><div><b>Quarta</b><span>19h às 22h</span></div><div><b>Sexta</b><span>19h às 22h</span></div></div>
      <p class="anote">Depois do pedido, eu confirmo a data pelo WhatsApp. Dependendo do assunto, preciso de um tempo para preparar a aula do jeito certo.</p>
    </div>
  </div>
</section>

<section class="plain" id="pedido-sec" style="scroll-margin-top:80px">
  <div class="wrap stack" style="gap:20px">
    <span class="eyebrow">Pedido de aula</span>
    <h2>Conte o que você precisa</h2>
    <form class="aform" id="aula-form" novalidate>
      <h3>1. Modalidade e objetivo</h3>
      <label>Seu nome *<input type="text" name="nome" autocomplete="name" maxlength="80"></label>
      <fieldset><legend>Modalidade *</legend>
        <div class="pills big">
          <label><input type="radio" name="modo" value="ao vivo" checked><span>Aula ao vivo<small>Online, terça, quarta ou sexta, 19h às 22h · R$ {PRECO}/h</small></span></label>
          <label><input type="radio" name="modo" value="gravada"><span>Aula gravada sob demanda<small>Montada para o seu objetivo · valor a combinar</small></span></label>
        </div></fieldset>
      <fieldset><legend>Para quê? *</legend>
        <div class="pills">
          <label><input type="radio" name="objetivo" value="escola">Prova ou matéria da escola</label>
          <label><input type="radio" name="objetivo" value="concurso">Concurso público</label>
          <label><input type="radio" name="objetivo" value="olimpiada">Olimpíada de matemática</label>
          <label><input type="radio" name="objetivo" value="outro">Outro</label>
        </div></fieldset>

      <div class="cond" id="c-escola" hidden>
        <div class="f2">
          <label>Série / ano *<select name="serie"><option value="">Escolha</option><option>2º ano – Fundamental</option><option>3º ano – Fundamental</option><option>4º ano – Fundamental</option><option>5º ano – Fundamental</option><option>6º ano – Fundamental</option><option>7º ano – Fundamental</option><option>8º ano – Fundamental</option><option>9º ano – Fundamental</option><option>1º ano – Médio</option><option>2º ano – Médio</option><option>3º ano – Médio</option><option>Pré-vestibular / ENEM</option><option>EJA / supletivo</option></select></label>
          <label>Data da prova ou teste<input type="date" name="escola_data"></label>
        </div>
        <label>Livro e capítulo que está estudando<input type="text" name="escola_livro" maxlength="160" placeholder="Ex.: Praticando Matemática 8º ano, capítulo 5 – Produtos notáveis"></label>
      </div>
      <div class="cond" id="c-concurso" hidden>
        <div class="f2">
          <label>Concurso / órgão *<input type="text" name="concurso" maxlength="120" placeholder="Ex.: Prefeitura de Niterói 2026"></label>
          <label>Cargo *<input type="text" name="cargo" maxlength="120" placeholder="Ex.: Assistente Administrativo"></label>
        </div>
        <div class="f2">
          <label>Banca<input type="text" name="banca" maxlength="60" placeholder="Ex.: Selecon, FGV, Cebraspe"></label>
          <label>Data da prova<input type="date" name="concurso_data"></label>
        </div>
        <label>Link do edital (se tiver)<input type="url" name="edital" maxlength="300" placeholder="https://"></label>
      </div>
      <div class="cond" id="c-outro" hidden>
        <label>Conte um pouco mais<input type="text" name="outro_det" maxlength="200" placeholder="Ex.: OBMEP Mirim nível 1; faculdade de Administração, Cálculo I"></label>
      </div>

      <h3>2. O conteúdo</h3>
      <label>Assunto específico *<span class="hint">Quanto mais específico, melhor. Ex.: “trigonometria no triângulo retângulo”, “juros compostos com taxas equivalentes”, “porcentagem: aumentos e descontos sucessivos”.</span>
        <textarea name="assunto" rows="2" maxlength="400"></textarea></label>
      <label>O que você já sabe e onde trava?<span class="hint">Ex.: entendo a fórmula, mas erro na interpretação dos problemas.</span>
        <textarea name="trava" rows="2" maxlength="400"></textarea></label>
      <fieldset><legend>Foco da aula</legend>
        <div class="pills">
          <label><input type="radio" name="foco" value="teoria + resolução de exercícios" checked>Teoria + exercícios <span class="rec">recomendado</span></label>
          <label><input type="radio" name="foco" value="mais resolução de exercícios e problemas">Mais exercícios</label>
          <label><input type="radio" name="foco" value="mais explicação teórica">Mais teoria</label>
          <label><input type="radio" name="foco" value="revisão rápida para a prova">Revisão para a prova</label>
        </div></fieldset>

      <h3>3. Quando</h3>
      <div class="cond" id="c-vivo">
        <fieldset><legend>Quantidade</legend>
          <div class="pills"><label><input type="radio" name="qtd" value="aula avulsa (1 hora)" checked>Aula avulsa</label><label><input type="radio" name="qtd" value="quero saber de pacote com várias aulas">Pacote de aulas</label></div></fieldset>
        <fieldset><legend>Dias de preferência</legend>
          <div class="pills"><label><input type="checkbox" name="dia" value="terça">Terça</label><label><input type="checkbox" name="dia" value="quarta">Quarta</label><label><input type="checkbox" name="dia" value="sexta">Sexta</label></div></fieldset>
        <fieldset><legend>Horário de preferência</legend>
          <div class="pills"><label><input type="checkbox" name="hora" value="19h">19h</label><label><input type="checkbox" name="hora" value="20h">20h</label><label><input type="checkbox" name="hora" value="21h">21h</label></div></fieldset>
        <label>A partir de quando?<input type="date" name="inicio"></label>
      </div>
      <div class="cond" id="c-gravada" hidden>
        <label>Até quando precisa receber a aula?<input type="date" name="prazo"></label>
      </div>

      <h3>4. Material de apoio</h3>
      <fieldset><legend>O que você pode me mandar por foto ou link na conversa?</legend>
        <div class="pills">
          <label><input type="checkbox" name="mat" value="páginas do livro">Páginas do livro</label>
          <label><input type="checkbox" name="mat" value="caderno">Caderno</label>
          <label><input type="checkbox" name="mat" value="provas ou testes anteriores">Provas ou testes anteriores</label>
          <label><input type="checkbox" name="mat" value="lista de exercícios do professor">Lista do professor</label>
          <label><input type="checkbox" name="mat" value="edital">Edital</label>
        </div></fieldset>
      <label>Algo mais que eu deva saber?<textarea name="obs" rows="2" maxlength="500"></textarea></label>

      <p class="anote">Ao enviar, o seu WhatsApp abre com o pedido já escrito para mim. Depois de enviar, mande as fotos ou links do material na mesma conversa. Eu respondo confirmando data, prazo e valor.</p>
      <p class="amsg" id="amsg" role="alert" hidden></p>
      <button class="btn wabtn" type="submit">Enviar pedido pelo WhatsApp</button>
      <p class="anote" id="adone" hidden>O WhatsApp não abriu? <a id="ago" href="#" target="_blank" rel="noopener">Toque aqui para abrir com o pedido</a>.</p>
    </form>
  </div>
</section>
</main>
''' + JS + foot

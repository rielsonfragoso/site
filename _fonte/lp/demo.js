
(function(){
  var D = JSON.parse(document.getElementById('dz-data').textContent);
  var $ = function(id){return document.getElementById(id)};
  function tts(t){return 'https://translate.google.com/?sl=en&tl=pt&op=translate&text='+encodeURIComponent(t)}
  function say(text){
    var a=document.createElement('a'); a.className='say'; a.href=tts(text); a.target='_blank'; a.rel='noopener';
    a.textContent='▶ ouvir'; a.setAttribute('aria-label','Ouvir: '+text);
    a.addEventListener('click',function(e){
      try{ if(window.speechSynthesis && window.SpeechSynthesisUtterance){
        e.preventDefault(); speechSynthesis.cancel();
        var u=new SpeechSynthesisUtterance(text); u.lang='en-US'; u.rate=.85; speechSynthesis.speak(u);} }catch(err){}
    });
    return a;
  }
  function el(tag,cls,txt){var e=document.createElement(tag); if(cls)e.className=cls; if(txt!=null)e.textContent=txt; return e}
  // tabs
  var tabs=[].slice.call(document.querySelectorAll('.tabs [role=tab]'));
  tabs.forEach(function(b){b.addEventListener('click',function(){
    tabs.forEach(function(x){x.setAttribute('aria-selected',x===b?'true':'false'); $(x.getAttribute('aria-controls')).hidden = x!==b;});
  });});
  // painel 1
  $('dz-about').innerHTML = D.sobre;
  D.words.forEach(function(w,i){
    var row=el('div','word'), a=el('div'), b=el('div');
    var t=el('b',null,(i+1)+'. '+w.w); a.appendChild(t); a.appendChild(el('span','pr','[ '+w.p+' ]')); a.appendChild(el('span','tr',w.t)); a.appendChild(say(w.w));
    b.appendChild(el('span','s',w.s)); b.appendChild(el('span','pr','[ '+w.sp+' ]')); b.appendChild(el('span','tr',w.st)); b.appendChild(say(w.s));
    row.appendChild(a); row.appendChild(b); $('dz-words').appendChild(row);
  });
  var ou=$('dz-ouvido'); ou.appendChild(el('b',null,'Fique de ouvido:'));
  D.ouvido.forEach(function(o){var s=el('span'); s.appendChild(el('b',null,o[0]+' ')); s.appendChild(document.createTextNode('('+o[1]+') ')); s.appendChild(say(o[0])); ou.appendChild(s);});
  // exercício 1
  D.words.forEach(function(w,i){
    var L=String.fromCharCode(65+i);
    $('dz-ex1').appendChild(el('span',null,L+'  '+w.w));
    var inp=el('input','box'); inp.maxLength=1; inp.id='dz-e1-'+i; inp.setAttribute('aria-label','Letra para '+D.ex1_right[i]); inp.autocomplete='off';
    $('dz-ex1').appendChild(inp); $('dz-ex1').appendChild(el('span','r',D.ex1_right[i]));
  });
  // exercício 2
  $('dz-bank').textContent='Palavras: '+D.words.map(function(w){return w.w}).join(' · ');
  D.ex2.forEach(function(x,k){
    var line=el('div','line'); line.appendChild(el('span',null,String.fromCharCode(97+k)+') '+x[0]));
    var inp=el('input','blank'); inp.id='dz-e2-'+k; inp.autocomplete='off'; inp.setAttribute('aria-label','Lacuna '+String.fromCharCode(97+k));
    line.appendChild(inp); if(x[1]) line.appendChild(el('span',null,x[1])); $('dz-ex2').appendChild(line);
  });
  // exercício 3
  D.ex3.forEach(function(ev,k){
    var line=el('div','line'); var inp=el('input','box'); inp.maxLength=1; inp.inputMode='numeric'; inp.id='dz-e3-'+k; inp.setAttribute('aria-label','Ordem do acontecimento');
    line.appendChild(inp); line.appendChild(el('span',null,ev)); $('dz-ex3').appendChild(line);
  });
  // estrelas
  function star(label){var s=el('button','star','☆'); s.type='button'; s.setAttribute('aria-pressed','false'); s.setAttribute('aria-label',label);
    s.addEventListener('click',function(e){e.stopPropagation(); var on=s.getAttribute('aria-pressed')!=='true'; s.setAttribute('aria-pressed',on?'true':'false'); s.textContent=on?'★':'☆';}); return s;}
  for(var i=0;i<5;i++) $('dz-stars').appendChild(star('Estrela '+(i+1)));
  // gabarito
  var g1=D.ex1_right.map(function(r,i){return '('+D.ex1_ans[i]+') '+r}).join(' · ');
  var g2=D.ex2.map(function(x,k){return String.fromCharCode(97+k)+') '+x[2]}).join('  ');
  $('dz-gabtxt').textContent='Gabarito — 1. '+g1+'   2. '+g2+'   3. '+D.ex3_ans.join(' · ');
  $('dz-gab').addEventListener('click',function(){var g=$('dz-gabtxt'); g.hidden=!g.hidden; this.setAttribute('aria-expanded',String(!g.hidden)); this.textContent=g.hidden?'Ver gabarito':'Esconder gabarito';});
  $('dz-clear').addEventListener('click',function(){[].forEach.call(document.querySelectorAll('#painel-2 input'),function(i){i.value=''}); [].forEach.call(document.querySelectorAll('#dz-stars .star'),function(s){s.setAttribute('aria-pressed','false'); s.textContent='☆'});});
  // cartões
  D.words.forEach(function(w,i){
    var c=el('div','card'), f=el('button','flip'); f.type='button'; f.setAttribute('aria-label','Cartão '+(i+1)+': '+w.w+'. Toque para virar');
    var fr=el('span','face front'); fr.appendChild(el('span','lab','CARTÃO '+(i+1))); fr.appendChild(el('b',null,w.w)); fr.appendChild(el('small',null,'toque para virar'));
    var bk=el('span','face back'); bk.appendChild(el('span','lab','CARTÃO '+(i+1)+' · '+w.w)); bk.appendChild(el('b',null,w.t)); bk.appendChild(el('span',null,w.s)); bk.appendChild(el('i',null,w.st));
    f.appendChild(fr); f.appendChild(bk); f.addEventListener('click',function(){c.classList.toggle('on')});
    var m=el('div','mem'); m.appendChild(el('span',null,'lembrei?')); m.appendChild(star('Lembrei '+w.w));
    c.appendChild(f); c.appendChild(m); $('dz-cards').appendChild(c);
  });
})();

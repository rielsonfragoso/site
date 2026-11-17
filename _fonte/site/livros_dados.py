"""Catálogo de livros usados — rielsonfragoso.com.br/livros/
COMO ATUALIZAR:
  • vendeu: diminua qtd; se zerar, mude vendido=True (o livro continua na página com o selo "Vendido").
  • conservação: preencha cond="..." (ex.: "Bom estado, com grifos a lápis nos capítulos 2 e 3").
  • vídeo do livro no YouTube: preencha video="LINK" (link normal, youtu.be ou Shorts). Aparece o botão "Ver vídeo do exemplar" no catálogo e o vídeo na página do livro.
  • vídeo de combo: preencha video="LINK" no COMBOS; vale para os livros do combo que não tiverem vídeo próprio.
"""

def B(titulo, autor, preco, qtd, cat, foto, vendido=False, idioma="Português", editora="", cond="", desc="", video="", slug=""):
    return dict(titulo=titulo, autor=autor, preco=float(preco), qtd=qtd, cat=cat, foto=foto, vendido=vendido,
                idioma=idioma, editora=editora, cond=cond, desc=desc, video=video, slug=slug)

CIENCIA = "Ciência, Física e Grandes Pensadores"
LIT = "Literatura e Clássicos"
FIN = "Finanças e Negócios"

LIVROS = [
    # ---------- Ciência, Física e Grandes Pensadores (destaque) ----------
    B("Encounters with Einstein: And Other Essays on People, Places, and Particles", "Werner Heisenberg", 74.90, 1, CIENCIA, "heisenberg-encounters",
      idioma="Inglês", editora="Princeton University Press (Princeton Science Library)",
      desc="Ensaios do Nobel de Física Werner Heisenberg sobre Einstein, outros cientistas, lugares e partículas: a física do século XX contada por um de seus protagonistas."),
    B("Physics and Philosophy: The Revolution in Modern Science", "Werner Heisenberg", 74.90, 1, CIENCIA, "heisenberg-physics-philosophy",
      idioma="Inglês", editora="Harper Perennial (Modern Thought)",
      desc="Clássico de Heisenberg sobre as consequências filosóficas da mecânica quântica. Edição com introdução de David Lindley."),
    B("The First Three Minutes: A Modern View of the Origin of the Universe", "Steven Weinberg", 64.90, 1, CIENCIA, "weinberg",
      idioma="Inglês", desc="O Nobel de Física de 1979 explica, passo a passo, o que aconteceu nos primeiros minutos do universo. Edição com posfácio do autor."),
    B("My View of the World", "Erwin Schrödinger", 74.90, 1, CIENCIA, "schrodinger",
      idioma="Inglês", desc="Ensaios filosóficos de Erwin Schrödinger, um dos fundadores da mecânica quântica, sobre consciência, ciência e a natureza da realidade."),
    B("Big Bang", "Simon Singh", 39.90, 1, CIENCIA, "big-bang",
      desc="Tudo sobre a mais importante descoberta científica de todos os tempos, pelo autor de O Último Teorema de Fermat e O Livro dos Códigos."),
    B("O Universo numa Casca de Noz", "Stephen Hawking", 21.90, 1, CIENCIA, "hawking-casca-de-noz", editora="ARX",
      desc="Stephen Hawking apresenta, com muitas ilustrações, as grandes ideias da física moderna: relatividade, buracos negros, tempo e o universo."),
    B("The Character of Physical Law", "Richard Feynman", 30, 1, CIENCIA, "feynman-leis", idioma="Inglês",
      desc="As famosas palestras de Feynman sobre o que as leis da física têm em comum."),
    B("Sobre as Leis da Física", "Richard Feynman", 30, 1, CIENCIA, "feynman-leis", editora="Contraponto / PUC-Rio",
      desc="Tradução de The Character of Physical Law: Feynman explica o que as leis da física têm em comum."),
    B("Astronomia & Budismo · Uma Jornada Rumo ao Distante Universo", "Ronaldo Rogério de Freitas Mourão e Daisaku Ikeda", 15, 1, CIENCIA, "astronomia"),

    # ---------- Literatura e Clássicos ----------
    B("Sonho de uma Noite de Verão", "William Shakespeare", 19.90, 1, LIT, "sonho-noite-verao",
      editora="L&PM Pocket · tradução de Beatriz Viégas-Faria", slug="shakespeare-sonho-de-uma-noite-de-verao"),
    B("Hamlet", "William Shakespeare", 19.90, 1, LIT, "hamlet",
      editora="L&PM Pocket · tradução de Millôr Fernandes", slug="shakespeare-hamlet"),
    B("O Rei Lear", "William Shakespeare", 19.90, 1, LIT, "rei-lear",
      editora="L&PM Pocket · tradução de Millôr Fernandes", slug="shakespeare-o-rei-lear"),

    # ---------- Finanças e Negócios ----------
    B("Pai Rico, Pai Pobre: O que os Ricos Ensinam a Seus Filhos sobre Dinheiro", "Robert T. Kiyosaki", 24.90, 2, FIN, "pai-rico",
      editora="Alta Books · edição atualizada e ampliada"),
    B("Princípios de Administração Financeira", "Ross, Westerfield e Jordan", 20, 1, FIN, "ross-mathias", editora="Atlas"),

    # ---------- Catálogo anterior (preservado) ----------
    B("Álgebra Linear e Geometria Analítica", "Antonio dos Santos Machado", 36, 2, "Graduação", "machado"),
    B("Cálculo · Volume 1", "James Stewart", 54, 1, "Graduação", "stewart", editora="Cengage · tradução da 6ª edição"),
    B("Cálculo · Volume 1", "George B. Thomas Jr.", 25, 1, "Graduação", "thomas"),
    B("Cálculo · Volume 2", "George B. Thomas Jr.", 25, 1, "Graduação", "thomas"),
    B("Cálculo · Volume 3", "George B. Thomas Jr.", 25, 1, "Graduação", "thomas"),
    B("Matemática para os Cursos de Economia, Administração e Ciências Contábeis · Vol. 1", "Medeiros", 23, 1, "Graduação", "medeiros-alcantara", editora="Atlas · 3ª edição"),
    B("Fundamentos de Matemática Elementar 1 · Conjuntos e Funções", "Iezzi e Murakami", 50, 1, "Ensino médio", "fme-novos", editora="Atual · edição recente"),
    B("Fundamentos de Matemática Elementar 2 · Logaritmos", "Iezzi, Dolce e Murakami", 50, 1, "Ensino médio", "fme-novos", editora="Atual · edição recente"),
    B("Fundamentos de Matemática Elementar 3 · Trigonometria", "Gelson Iezzi", 50, 1, "Ensino médio", "fme-novos", editora="Atual · edição recente"),
    B("Fundamentos de Matemática Elementar 2 · Logaritmos", "Iezzi, Dolce e Murakami", 32, 1, "Coleções clássicas", "fme-antigos", True, editora="Edição antiga (anos 80)", slug="fme-2-logaritmos-anos-80"),
    B("Fundamentos de Matemática Elementar 3 · Trigonometria", "Gelson Iezzi", 32, 1, "Coleções clássicas", "fme-antigos", True, editora="Edição antiga (anos 80)", slug="fme-3-trigonometria-anos-80"),
    B("Fundamentos de Matemática Elementar 4 · Sequências, Matrizes, Determinantes e Sistemas", "Iezzi e Hazzan", 32, 1, "Coleções clássicas", "fme-antigos", True, editora="Edição antiga (anos 80)", slug="fme-4-anos-80"),
    B("Fundamentos de Matemática Elementar 5 · Combinatória e Probabilidade", "Samuel Hazzan", 32, 1, "Coleções clássicas", "fme-antigos", True, editora="Edição antiga (anos 80)", slug="fme-5-anos-80"),
    B("Matemática · Segundo Ano Colegial", "Ary Quintella", 27, 1, "Coleções clássicas", "quintella", editora="Companhia Editora Nacional"),
    B("Matemática · Terceiro Ano Colegial", "Ary Quintella", 27, 1, "Coleções clássicas", "quintella", editora="Companhia Editora Nacional"),
    B("Matemática · 3ª Série Ginasial", "Ary Quintella", 27, 1, "Coleções clássicas", "quintella", editora="Companhia Editora Nacional"),
    B("Matemática · 4ª Série Ginasial", "Ary Quintella", 27, 1, "Coleções clássicas", "quintella", editora="Companhia Editora Nacional"),
    B("Pitágoras · Matemática II, Livro I: Geometria Plana (1ª parte)", "Coleção Pitágoras", 15, 1, "Coleções clássicas", "pitagoras-minimanual"),
    B("Matemática · Box Moderna Plus Vol. 1 (completo)", "Manoel Paiva", 45, 1, "Ensino médio", "paiva", editora="Moderna"),
    B("Matemática · Box Moderna Plus Vol. 2 (incompleto)", "Manoel Paiva", 23, 1, "Ensino médio", "paiva", editora="Moderna"),
    B("Matemática · Box Moderna Plus Vol. 3 (completo)", "Manoel Paiva", 45, 1, "Ensino médio", "paiva", editora="Moderna"),
    B("Minimanual Compacto de Matemática · Ensino Médio", "Editora Rideel", 23, 1, "Ensino médio", "pitagoras-minimanual", editora="Rideel"),
    B("Novo Praticando Matemática · Vol. 2", "Álvaro Andrini e Maria José Vasconcellos", 23, 1, "Ensino fundamental", "praticando", editora="Editora do Brasil"),
    B("Novo Praticando Matemática · Vol. 3", "Álvaro Andrini e Maria José Vasconcellos", 23, 1, "Ensino fundamental", "praticando", editora="Editora do Brasil"),
    B("Novo Praticando Matemática · Vol. 4", "Álvaro Andrini e Maria José Vasconcellos", 23, 1, "Ensino fundamental", "praticando", editora="Editora do Brasil"),
    B("Vivendo a Matemática · A Numeração Indo-Arábica", "Luiz Márcio Imenes", 15, 1, "Ensino fundamental", "imenes", editora="Scipione"),
    B("Experiências de Ciências para o Ensino Fundamental", "Alberto Gaspar", 20, 1, "Ensino fundamental", "gaspar", editora="Ática"),
    B("Matemática para Concursos", "Flávio Alcântara", 23, 1, "Concursos", "medeiros-alcantara", editora="Método · teoria e questões comentadas"),
    B("Matemática Financeira · Série Provas e Concursos", "Benjamin Cesar", 23, 1, "Concursos", "financeira-puccini-cesar", editora="Campus/Elsevier · 7ª edição"),
    B("Matemática Básica", "Aref Antar Neto", 18, 1, "Concursos", "estatistica-basica"),
    B("Matemática Financeira · Objetiva e Aplicada", "Abelardo de Lima Puccini", 23, 1, "Financeira e Estatística", "financeira-puccini-cesar", editora="Saraiva · 6ª edição"),
    B("Matemática Financeira · mais de 600 exercícios resolvidos e propostos", "Washington Franco Mathias e José Maria Gomes", 23, 1, "Financeira e Estatística", "ross-mathias", editora="Atlas"),
    B("Curso de Estatística · Elementos", "Ruy Aguiar da Silva Leme", 18, 1, "Financeira e Estatística", "estatistica-basica", editora="Ao Livro Técnico"),
    B("The Feynman Lectures on Physics · Vol. III: Quantum Mechanics", "Feynman, Leighton e Sands", 54, 1, "Física", "feynman-lectures", idioma="Inglês", editora="New Millennium Edition"),
    B("Os Tópicos da Física 2 · Termologia, Ondas e Óptica", "Gualter, Newton e Helou Doca", 25, 1, "Física", "topicos-fisica", editora="Saraiva"),
    B("Os Tópicos da Física 3 · Eletricidade", "Gualter, Newton e Helou Doca", 25, 1, "Física", "topicos-fisica", editora="Saraiva"),
    B("Física Básica · Volume Único", "Nicolau, Toledo e Ronaldo", 25, 1, "Física", "fisica-basica", editora="Atual"),
    B("La Gaceta de la Real Sociedad Matemática Española · Vol. 21, nº 3 (2018)", "Real Sociedad Matemática Española", 18, 1, "Outros", "gaceta", idioma="Espanhol"),
]

CATS = [CIENCIA, LIT, FIN, "Ensino fundamental", "Ensino médio", "Coleções clássicas", "Concursos", "Graduação", "Financeira e Estatística", "Física", "Outros"]

# Combo: livros vendidos juntos com desconto. O desconto vale também quando os itens são adicionados um a um.
COMBOS = [dict(id="shakespeare", nome="Combo Shakespeare", foto="shakespeare-trio", preco=49.90,
               itens=["shakespeare-sonho-de-uma-noite-de-verao", "shakespeare-hamlet", "shakespeare-o-rei-lear"],
               desc="Sonho de uma Noite de Verão, Hamlet e O Rei Lear (L&PM Pocket). Separados saem R$ 59,70.", video="")]

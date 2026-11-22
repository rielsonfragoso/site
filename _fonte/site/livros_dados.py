"""Catálogo de livros usados — rielsonfragoso.com.br/livros/
COMO ATUALIZAR:
  • vendeu: diminua qtd; se zerar, mude vendido=True (o livro continua na página com o selo "Vendido").
  • conservação: preencha cond="..." (ex.: "Bom estado, com grifos a lápis nos capítulos 2 e 3").
  • vídeo do livro no YouTube: preencha video="LINK" (link normal, youtu.be ou Shorts). Aparece o botão "Ver vídeo do exemplar" no catálogo e o vídeo na página do livro.
  • video_t=SEGUNDOS faz o vídeo abrir no trecho daquele livro.
  • vídeo de combo: preencha video="LINK" no COMBOS; vale para os livros do combo que não tiverem vídeo próprio.
"""

def _medidas(m):
    """'altura x largura x comprimento' em cm (altura = grossura do miolo, livro deitado) -> (a, l, c)."""
    if not m: return None
    v = [float(x.strip().replace(",", ".")) for x in m.lower().replace("×", "x").split("x")]
    assert len(v) == 3, f"medidas inválidas: {m!r} (use 'altura x largura x comprimento')"
    return tuple(v)

def B(titulo, autor, preco, qtd, cat, foto, vendido=False, idioma="Português", editora="", cond="", desc="", video="", video_t=0, slug="",
      medidas="", peso=0):
    """medidas: 'A x L x C' em cm (altura = grossura do miolo; largura e comprimento como na foto de referência).
    peso: em gramas."""
    return dict(titulo=titulo, autor=autor, preco=float(preco), qtd=qtd, cat=cat, foto=foto, vendido=vendido,
                idioma=idioma, editora=editora, cond=cond, desc=desc, video=video, video_t=video_t, slug=slug,
                medidas=_medidas(medidas), peso=int(peso))

CIENCIA = "Ciência, Física e Grandes Pensadores"
LIT = "Literatura e Clássicos"
FIN = "Finanças e Negócios"

LIVROS = [
    # ---------- Ciência, Física e Grandes Pensadores (destaque) ----------
    B("Encounters with Einstein: And Other Essays on People, Places, and Particles", "Werner Heisenberg", 49.90, 1, CIENCIA, "heisenberg-encounters",
      idioma="Inglês", editora="Princeton University Press (Princeton Science Library)",
      desc="Ensaios do Nobel de Física Werner Heisenberg sobre Einstein, outros cientistas, lugares e partículas: a física do século XX contada por um de seus protagonistas.", video="https://youtube.com/shorts/4m-eMMlzePw", video_t=54, medidas="1 x 14 x 21,5", peso=240),
    B("Physics and Philosophy: The Revolution in Modern Science", "Werner Heisenberg", 49.90, 1, CIENCIA, "heisenberg-physics-philosophy",
      idioma="Inglês", editora="Harper Perennial (Modern Thought)",
      desc="Clássico de Heisenberg sobre as consequências filosóficas da mecânica quântica. Edição com introdução de David Lindley.", video="https://youtube.com/shorts/4m-eMMlzePw", video_t=0, medidas="2 x 13,5 x 20", peso=210),
    B("The First Three Minutes: A Modern View of the Origin of the Universe", "Steven Weinberg", 49.90, 1, CIENCIA, "weinberg",
      idioma="Inglês", desc="O Nobel de Física de 1979 explica, passo a passo, o que aconteceu nos primeiros minutos do universo. Edição com posfácio do autor.", video="https://youtube.com/shorts/4m-eMMlzePw", video_t=28, medidas="2 x 13,5 x 20", peso=230),
    B("My View of the World", "Erwin Schrödinger", 49.90, 1, CIENCIA, "schrodinger",
      idioma="Inglês", desc="Ensaios filosóficos de Erwin Schrödinger, um dos fundadores da mecânica quântica, sobre consciência, ciência e a natureza da realidade.", video="https://youtube.com/shorts/4m-eMMlzePw", video_t=68, medidas="1 x 14 x 22", peso=185),
    B("As Grandes Equações: A história das fórmulas matemáticas mais importantes e os cientistas que as criaram", "Robert P. Crease", 19.90, 1, CIENCIA, "crease",
      editora="Zahar", desc="Das equações de Newton e Maxwell a E = mc² e à equação de Schrödinger: a história de dez fórmulas que mudaram a ciência e das pessoas por trás delas.",
      medidas="2 x 16 x 23", peso=395),
    B("Quantum Physics: Illusion or Reality? (2nd edition)", "Alastair Rae", 29.90, 1, CIENCIA, "rae",
      idioma="Inglês", editora="Cambridge University Press (Canto)",
      desc="Introdução sem fórmulas aos enigmas da física quântica: medição, não localidade, o gato de Schrödinger e as principais interpretações da teoria.",
      medidas="1 x 14 x 22", peso=230, video="https://youtube.com/shorts/6KuKHV4s2CU", video_t=3),
    B("The Large, the Small and the Human Mind", "Roger Penrose, Abner Shimony, Nancy Cartwright e Stephen Hawking", 49.90, 1, CIENCIA, "penrose",
      idioma="Inglês", editora="Cambridge University Press (Canto)",
      desc="As Tanner Lectures de Roger Penrose sobre cosmologia, física quântica e consciência, seguidas de críticas de Abner Shimony, Nancy Cartwright e Stephen Hawking e da resposta de Penrose.",
      medidas="1,5 x 14 x 22", peso=290, video="https://youtube.com/shorts/6KuKHV4s2CU", video_t=12),
    B("Física Moderna", "Luiz Sergio Coelho de Sampaio", 19.90, 1, CIENCIA, "sampaio",
      editora="H. P. Comunicação Editora",
      desc="Ensaio do filósofo Luiz Sergio Coelho de Sampaio sobre as ideias e o sentido da física moderna.",
      medidas="1,5 x 14 x 21", peso=290),
    B("Big Bang", "Simon Singh", 39.90, 1, CIENCIA, "big-bang",
      desc="Tudo sobre a mais importante descoberta científica de todos os tempos, pelo autor de O Último Teorema de Fermat e O Livro dos Códigos.", video="https://youtube.com/shorts/4m-eMMlzePw", video_t=100, medidas="3 x 16 x 23", peso=790),
    B("O Universo numa Casca de Noz", "Stephen Hawking", 21.90, 1, CIENCIA, "hawking-casca-de-noz", editora="ARX",
      desc="Stephen Hawking apresenta, com muitas ilustrações, as grandes ideias da física moderna: relatividade, buracos negros, tempo e o universo.", video="https://youtube.com/shorts/4m-eMMlzePw", video_t=118, medidas="2 x 19 x 24", peso=630),
    B("The Character of Physical Law", "Richard Feynman", 29.90, 1, CIENCIA, "feynman-character", idioma="Inglês",
      desc="As famosas palestras de Feynman sobre o que as leis da física têm em comum.", medidas="1,5 x 15 x 23", peso=328, video="https://youtube.com/shorts/lyL1FVbah1k", video_t=3),
    B("Sobre as Leis da Física", "Richard Feynman", 29.90, 1, CIENCIA, "feynman-sobre-as-leis", editora="Contraponto / PUC-Rio",
      desc="Tradução de The Character of Physical Law: Feynman explica o que as leis da física têm em comum.", medidas="1 x 14 x 20,5", peso=220, video="https://youtube.com/shorts/lyL1FVbah1k", video_t=39),
    B("Astronomia & Budismo · Uma Jornada Rumo ao Distante Universo", "Ronaldo Rogério de Freitas Mourão e Daisaku Ikeda", 17.90, 1, CIENCIA, "astronomia", medidas="1 x 16 x 23", peso=302),

    # ---------- Literatura e Clássicos ----------
    B("O Estrangeiro", "Albert Camus", 19.90, 1, LIT, "camus-estrangeiro", editora="Record",
      desc="O romance de estreia de Camus, prêmio Nobel de Literatura: Meursault, um homem indiferente às convenções, e o absurdo da existência.",
      medidas="1 x 14 x 21", peso=190, video="https://youtube.com/shorts/Fgo5MXB3cgQ", video_t=55),
    B("O Estrangeiro · capa dura (Mestres da Literatura Contemporânea)", "Albert Camus", 19.90, 1, LIT, "camus-estrangeiro-capa-dura",
      editora="Record/Altaya · coleção Mestres da Literatura Contemporânea", cond="capa dura", slug="o-estrangeiro-camus-capa-dura",
      desc="Edição em capa dura, com letras douradas, da coleção Mestres da Literatura Contemporânea. O romance de estreia de Camus, prêmio Nobel de Literatura: Meursault e o absurdo da existência.",
      medidas="1,5 x 14 x 20", peso=180, video="https://youtube.com/shorts/Fgo5MXB3cgQ", video_t=15),
    B("Noites Brancas e A Árvore de Natal na Casa do Cristo", "Fiódor Dostoiévski", 9.90, 1, LIT, "dostoievski-noites-brancas",
      editora="Ediouro", desc="Duas narrativas curtas de Dostoiévski em edição de bolso: o romance sentimental de um sonhador solitário em São Petersburgo e um conto de Natal.",
      medidas="0,5 x 10 x 15,5", peso=60, video="https://youtube.com/shorts/Fgo5MXB3cgQ", video_t=122),
    B("Sonho de uma Noite de Verão", "William Shakespeare", 19.90, 1, LIT, "sonho-noite-verao",
      editora="L&PM Pocket · tradução de Beatriz Viégas-Faria", slug="shakespeare-sonho-de-uma-noite-de-verao", medidas="1 x 10 x 17", peso=90, video="https://youtube.com/shorts/Fgo5MXB3cgQ", video_t=107),
    B("Hamlet", "William Shakespeare", 19.90, 1, LIT, "hamlet",
      editora="L&PM Pocket · tradução de Millôr Fernandes", slug="shakespeare-hamlet", medidas="1 x 10 x 17", peso=100, video="https://youtube.com/shorts/Fgo5MXB3cgQ", video_t=70),
    B("O Rei Lear", "William Shakespeare", 19.90, 1, LIT, "rei-lear",
      editora="L&PM Pocket · tradução de Millôr Fernandes", slug="shakespeare-o-rei-lear", medidas="1 x 10 x 17", peso=100, video="https://youtube.com/shorts/Fgo5MXB3cgQ", video_t=92),

    # ---------- Finanças e Negócios ----------
    B("Pai Rico, Pai Pobre: O que os Ricos Ensinam a Seus Filhos sobre Dinheiro", "Robert T. Kiyosaki", 24.90, 2, FIN, "pai-rico",
      editora="Alta Books · edição atualizada e ampliada", video="https://youtube.com/shorts/4m-eMMlzePw", video_t=76, medidas="2 x 17,5 x 24", peso=540),
    B("Princípios de Administração Financeira", "Ross, Westerfield e Jordan", 17.90, 1, FIN, "ross-adm-financeira", editora="Atlas", medidas="2,5 x 21,5 x 28", peso=1030),

    # ---------- Catálogo anterior (preservado) ----------
    B("Álgebra Linear e Geometria Analítica", "Antonio dos Santos Machado", 35.90, 1, "Graduação", "machado", medidas="1 x 15 x 21", peso=240),
    B("O Cálculo com Geometria Analítica · Volume 1", "Louis Leithold", 39.90, 1, "Graduação", "leithold-1", editora="Harbra",
      desc="Clássico de cálculo usado em cursos de exatas e engenharia: limites, derivadas, integrais e geometria analítica, com muitos exercícios.",
      medidas="4 x 22 x 28", peso=1130, video="https://youtube.com/shorts/UYsHKHS4F2k", video_t=45),
    B("Cálculo · Volume 1", "James Stewart", 49.90, 1, "Graduação", "stewart", editora="Cengage · tradução da 6ª edição", medidas="3,5 x 21 x 28", peso=1500, video="https://youtube.com/shorts/UYsHKHS4F2k", video_t=9),
    B("Cálculo · Volume 1", "George B. Thomas Jr.", 19.90, 1, "Graduação", "thomas-vol1", medidas="3,5 x 16 x 23", peso=800, video="https://youtube.com/shorts/YmPUQ7VMII8", video_t=48),
    B("Cálculo · Volume 2", "George B. Thomas Jr.", 19.90, 1, "Graduação", "thomas-vol2", medidas="2 x 14 x 20,5", peso=325, video="https://youtube.com/shorts/YmPUQ7VMII8", video_t=84),
    B("Cálculo · Volume 3", "George B. Thomas Jr.", 19.90, 1, "Graduação", "thomas-vol3", medidas="2,5 x 14 x 21", peso=330, video="https://youtube.com/shorts/YmPUQ7VMII8", video_t=113),
    B("Matemática para os Cursos de Economia, Administração e Ciências Contábeis · Vol. 1", "Medeiros", 19.90, 1, "Graduação", "medeiros-vol1", editora="Atlas · 3ª edição", medidas="1,5 x 15 x 21", peso=370, video="https://youtube.com/shorts/YmPUQ7VMII8", video_t=1),
    B("Fundamentos de Matemática Elementar 1 · Conjuntos e Funções", "Iezzi e Murakami", 49.90, 1, "Ensino médio", "fme-novos", True, editora="Atual · edição recente"),
    B("Fundamentos de Matemática Elementar 2 · Logaritmos", "Iezzi, Dolce e Murakami", 49.90, 1, "Ensino médio", "fme-novos", True, editora="Atual · edição recente"),
    B("Fundamentos de Matemática Elementar 3 · Trigonometria", "Gelson Iezzi", 49.90, 1, "Ensino médio", "fme-novos", True, editora="Atual · edição recente"),
    B("Fundamentos de Matemática Elementar 2 · Logaritmos", "Iezzi, Dolce e Murakami", 31.90, 1, "Coleções clássicas", "fme-antigos", True, editora="Edição antiga (anos 80)", slug="fme-2-logaritmos-anos-80"),
    B("Fundamentos de Matemática Elementar 3 · Trigonometria", "Gelson Iezzi", 31.90, 1, "Coleções clássicas", "fme-antigos", True, editora="Edição antiga (anos 80)", slug="fme-3-trigonometria-anos-80"),
    B("Fundamentos de Matemática Elementar 4 · Sequências, Matrizes, Determinantes e Sistemas", "Iezzi e Hazzan", 31.90, 1, "Coleções clássicas", "fme-antigos", True, editora="Edição antiga (anos 80)", slug="fme-4-anos-80"),
    B("Fundamentos de Matemática Elementar 5 · Combinatória e Probabilidade", "Samuel Hazzan", 31.90, 1, "Coleções clássicas", "fme-antigos", True, editora="Edição antiga (anos 80)", slug="fme-5-anos-80"),
    B("Matemática · Segundo Ano Colegial", "Ary Quintella", 26.90, 1, "Coleções clássicas", "quintella-2-colegial", editora="Companhia Editora Nacional", medidas="2 x 14 x 19", peso=323),
    B("Matemática · Terceiro Ano Colegial", "Ary Quintella", 26.90, 1, "Coleções clássicas", "quintella-3-colegial", editora="Companhia Editora Nacional", medidas="2 x 14 x 19", peso=240),
    B("Matemática · 3ª Série Ginasial", "Ary Quintella", 26.90, 1, "Coleções clássicas", "quintella-3-ginasial", editora="Companhia Editora Nacional", medidas="2 x 14 x 19", peso=275),
    B("Matemática · 4ª Série Ginasial", "Ary Quintella", 26.90, 1, "Coleções clássicas", "quintella-4-ginasial", editora="Companhia Editora Nacional", medidas="2,5 x 13,5 x 19", peso=330),
    B("Pitágoras · Matemática II, Livro I: Geometria Plana (1ª parte)", "Coleção Pitágoras", 14.90, 1, "Coleções clássicas", "pitagoras-mat2-livro1", medidas="1 x 16 x 23", peso=180),
    B("Matemática · Box Moderna Plus Vol. 1 (completo)", "Manoel Paiva", 29.90, 1, "Ensino médio", "paiva-box-1", editora="Moderna", medidas="4 x 21 x 28", peso=2030),
    B("Matemática · Box Moderna Plus Vol. 2 (incompleto)", "Manoel Paiva", 19.90, 1, "Ensino médio", "paiva-box-2", editora="Moderna", medidas="4 x 21 x 28", peso=1000),
    B("Matemática · Box Moderna Plus Vol. 3 (completo)", "Manoel Paiva", 29.90, 1, "Ensino médio", "paiva-box-3", editora="Moderna", medidas="4 x 21 x 28", peso=1710),
    B("Minimanual Compacto de Matemática · Ensino Médio", "Editora Rideel", 22.90, 1, "Ensino médio", "minimanual-rideel", editora="Rideel", medidas="3 x 12 x 17", peso=355),
    B("Novo Praticando Matemática · Vol. 2", "Álvaro Andrini e Maria José Vasconcellos", 19.90, 1, "Ensino fundamental", "praticando", editora="Editora do Brasil", medidas="1,5 x 21,5 x 27", peso=580),
    B("Novo Praticando Matemática · Vol. 3", "Álvaro Andrini e Maria José Vasconcellos", 19.90, 1, "Ensino fundamental", "praticando", editora="Editora do Brasil", medidas="1,5 x 21,5 x 27", peso=570),
    B("Novo Praticando Matemática · Vol. 4", "Álvaro Andrini e Maria José Vasconcellos", 19.90, 1, "Ensino fundamental", "praticando", editora="Editora do Brasil", medidas="1,5 x 21,5 x 27", peso=650),
    B("Vivendo a Matemática · A Numeração Indo-Arábica", "Luiz Márcio Imenes", 14.90, 1, "Ensino fundamental", "imenes", editora="Scipione", medidas="0,5 x 13 x 20", peso=65),
    B("Experiências de Ciências para o Ensino Fundamental", "Alberto Gaspar", 18.90, 1, "Ensino fundamental", "gaspar", editora="Ática", medidas="2 x 21,5 x 26", peso=610),
    B("Matemática para Concursos", "Flávio Alcântara", 19.90, 1, "Concursos", "alcantara-concursos", editora="Método · teoria e questões comentadas", medidas="2 x 16 x 23", peso=495),
    B("Matemática Financeira · Série Provas e Concursos", "Benjamin Cesar", 19.90, 1, "Concursos", "benjamin-cesar", editora="Campus/Elsevier · 7ª edição", medidas="2 x 17 x 24", peso=441),
    B("Matemática Básica", "Aref Antar Neto", 17.90, 1, "Concursos", "antar-neto-basica", medidas="2,5 x 16 x 21", peso=482),
    B("Matemática Financeira · Objetiva e Aplicada", "Abelardo de Lima Puccini", 22.90, 1, "Financeira e Estatística", "puccini", editora="Saraiva · 6ª edição", medidas="2,5 x 17 x 24", peso=700),
    B("Matemática Financeira · mais de 600 exercícios resolvidos e propostos", "Washington Franco Mathias e José Maria Gomes", 19.90, 1, "Financeira e Estatística", "mathias-gomes", editora="Atlas", medidas="2 x 14 x 20,5", peso=516),
    B("Curso de Estatística · Elementos", "Ruy Aguiar da Silva Leme", 17.90, 1, "Financeira e Estatística", "estatistica-leme", editora="Ao Livro Técnico", medidas="2 x 14 x 21", peso=350),
    B("The Feynman Lectures on Physics · Vol. III: Quantum Mechanics", "Feynman, Leighton e Sands", 49.90, 1, "Física", "feynman-lectures", idioma="Inglês", editora="New Millennium Edition", medidas="1,5 x 21,5 x 27", peso=880, video="https://youtube.com/shorts/lyL1FVbah1k", video_t=69),
    B("Os Tópicos da Física 2 · Termologia, Ondas e Óptica", "Gualter, Newton e Helou Doca", 24.90, 1, "Física", "topicos-fisica", editora="Saraiva", vendido=True),
    B("Os Tópicos da Física 3 · Eletricidade", "Gualter, Newton e Helou Doca", 24.90, 1, "Física", "topicos-fisica", editora="Saraiva", vendido=True),
    B("Física Básica · Volume Único", "Nicolau, Toledo e Ronaldo", 24.90, 1, "Física", "fisica-basica", editora="Atual", medidas="4 x 20 x 27,5", peso=1500),
    B("La Gaceta de la Real Sociedad Matemática Española · Vol. 21, nº 3 (2018)", "Real Sociedad Matemática Española", 17.90, 1, "Outros", "gaceta", idioma="Espanhol", medidas="1 x 17 x 24", peso=434),
]

CATS = [CIENCIA, LIT, FIN, "Ensino fundamental", "Ensino médio", "Coleções clássicas", "Concursos", "Graduação", "Financeira e Estatística", "Física", "Outros"]

# Combo: livros vendidos juntos com desconto. O desconto vale também quando os itens são adicionados um a um.
COMBOS = [dict(id="shakespeare", nome="Combo Shakespeare", foto="shakespeare-trio", preco=49.90,
               itens=["shakespeare-sonho-de-uma-noite-de-verao", "shakespeare-hamlet", "shakespeare-o-rei-lear"],
               desc="Sonho de uma Noite de Verão, Hamlet e O Rei Lear (L&PM Pocket). Separados saem R$ 59,70.", video="https://youtube.com/shorts/Fgo5MXB3cgQ",
               alt="Os três livros de Shakespeare do combo"),
          dict(id="paiva", nome="Combo Moderna Plus (Manoel Paiva)", foto="paiva", preco=70.90,
               itens=["matematica-box-moderna-plus-vol-1-completo-paiva", "matematica-box-moderna-plus-vol-2-incompleto-paiva",
                      "matematica-box-moderna-plus-vol-3-completo-paiva"],
               desc="Os 3 boxes Matemática Moderna Plus de Manoel Paiva, para o ensino médio (o Vol. 2 está incompleto). Separados saem R$ 79,70.",
               video="", alt="Os três boxes Moderna Plus de Manoel Paiva"),
          dict(id="praticando", nome="Combo Novo Praticando Matemática", foto="praticando", preco=52.90,
               itens=["novo-praticando-matematica-vol-2-andrini", "novo-praticando-matematica-vol-3-andrini",
                      "novo-praticando-matematica-vol-4-andrini"],
               desc="Os volumes 2, 3 e 4 do Novo Praticando Matemática, para o ensino fundamental. Separados saem R$ 59,70.",
               video="", alt="Os volumes 2, 3 e 4 do Novo Praticando Matemática"),
          dict(id="thomas", nome="Combo Cálculo Thomas", foto="thomas", preco=49.90,
               itens=["calculo-volume-1-thomas", "calculo-volume-2-thomas", "calculo-volume-3-thomas"],
               desc="Os 3 volumes de Cálculo de George B. Thomas Jr., coleção completa para a graduação. Separados saem R$ 59,70.",
               video="https://youtube.com/shorts/YmPUQ7VMII8", alt="Os três volumes de Cálculo de George B. Thomas Jr."),
          dict(id="quintella", nome="Combo Ary Quintella", foto="quintella", preco=79.90,
               itens=["matematica-3a-serie-ginasial-quintella", "matematica-4a-serie-ginasial-quintella",
                      "matematica-segundo-ano-colegial-quintella", "matematica-terceiro-ano-colegial-quintella"],
               desc="Os 4 livros de Matemática de Ary Quintella (Companhia Editora Nacional): 3ª e 4ª séries ginasiais, 2º e 3º anos colegiais. Separados saem R$ 107,60.",
               video="", alt="Os quatro livros de Matemática de Ary Quintella")]

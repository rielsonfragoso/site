"""Avaliações de clientes publicadas em /livros/.
SÓ entram aqui avaliações recebidas pelo formulário (ou enviadas pelo cliente) E APROVADAS pelo Rielson.
Campos:
  nome       – nome público que o cliente escolheu
  nota       – 1 a 5
  texto      – comentário (só ajustes de formatação; nunca mudar o sentido)
  livro      – opcional
  data       – "AAAA-MM-DD"
  confirmada – True SOMENTE se o Rielson confirmou que a pessoa tem um pedido pago (não basta a pessoa dizer)
Para remover uma avaliação publicada, apague a linha.
"""
AVALIACOES = [
    dict(nome="Paulo Berndt", nota=5, texto="Ótima experiência de compra! Os livros chegaram muito bem embalados, cuidadosamente protegidos e em excelente estado. A entrega foi rápida e ocorreu dentro do prazo previsto. Destaco o cuidado, a organização e a seriedade em todo o processo. Estou muito satisfeito e recomendo este vendedor!", livro="Cálculo Vol. 1 (Stewart) e Fundamentos de Matemática Elementar 2, 3, 4 e 5 (Iezzi e outros)", data="2026-11-25", confirmada=True),
    dict(nome="Reinaldo Bellini", nota=5, texto="Livro chegou muito rápido, vendedor deu todo apoio. Recomendo. Sobre o livro estava em estado de novo. Muito top, nota 10.", livro="Álgebra Linear e Geometria Analítica", data="2026-11-23", confirmada=True),
    dict(nome="Eugênio", nota=5, texto="Excelente experiência! Os livros foram enviados com muito cuidado, bem embalados e em perfeitas condições. A entrega foi rápida e tudo chegou conforme o esperado. Fiquei muito satisfeito com a organização, o compromisso e a qualidade do atendimento. Recomendo!", livro="Fundamentos de Matemática Elementar 4, 5, 9 e 10", data="2026-11-23", confirmada=True),
    # dict(nome="Tiago", nota=5, texto="...", livro="Fundamentos de Matemática Elementar 1, 2 e 3", data="2026-11-18", confirmada=True),
]

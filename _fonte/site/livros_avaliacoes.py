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
    # dict(nome="Tiago", nota=5, texto="...", livro="Fundamentos de Matemática Elementar 1, 2 e 3", data="2026-11-18", confirmada=True),
]

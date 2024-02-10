#Gerenciamento de Mercado:

'''Vamos criar um sistema orientado a objetos para representar um sistema de mercado seguindo
os requisitos fornecidos:
1- Cada produto pode ter um ou mais fornecedores.
2- O mercado controla apenas o nome, o telefone e o endereço de cada cliente.
3- Cada produto tem um nome, uma lista de categorias às quais pertence e uma quantidade
disponível em estoque.
4- Quando um produto é comprado, sua quantidade disponível em estoque é reduzida.
5- O mercado mantém um registro  de todas as transações realizadas, incluindo detalhes como data
da compra, cliente envolvido e quantidade de produtos comprados.
'''

from datetime import datetime


class Produto:
    def __init__(self, nome, lista_categorias):
        self.nome = nome
        self.lista_categorias = lista_categorias
        self.quantidade = 0

    def entrada(self, quantidade, fornecedor):
        self.quantidade += quantidade
        self.fornecedor = fornecedor
        return self.quantidade, self.fornecedor

    def saida(self, quantidade, cliente):
        hora_venda = datetime.now()
        self.cliente = cliente.nome
        self.quantidade -= quantidade
        return hora_venda, cliente, self.quantidade


class Fornecedor:
    def __init__(self, nome):
        self.nome = nome


class Cliente:
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco


produto_1 = Produto('café em pó', ['café torrado', 'café moído'])
fornecedor_1 = Fornecedor('Armazém tem tudo')
cliente_1 = Cliente('pato donald', '11 11111 1111', 'rua do pato donald')
cliente_2 = Cliente('pateta', '22 22222 2222', 'rua do pateta')

entrada_1 = produto_1.entrada(10, fornecedor_1)
saida_1 = produto_1.saida(1, cliente_1)

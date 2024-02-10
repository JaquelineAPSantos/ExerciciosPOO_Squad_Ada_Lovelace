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
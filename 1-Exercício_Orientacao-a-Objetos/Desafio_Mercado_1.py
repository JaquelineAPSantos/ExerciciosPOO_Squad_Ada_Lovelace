# Gerenciamento de Mercado: 
## Vamos criar um sistema orientado a objetos para representar um sistema de mercado seguindo os requisitos fornecidos: 
### 1. Cada produto pode ter um ou mais fornecedores.
### 2. O mercado controla apenas o nome, o telefone e o endereço de cada cliente.
### 3. Cada produto tem um nome, uma lista de categorias às quais pertence e uma quantidade disponível em estoque.
### 4. Quando um produto é comprado, sua quantidade disponível em estoque é reduzida.
### 5. O mercado mantém um registro de todas as transações realizadas, incluindo detalhes como data da compra,cliente envolvido e quantidade de produtos comprados.

from abc import ABC, abstractmethod
from datetime import datetime

class Pessoa:
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco

class Cliente(Pessoa):
    def __init__(self, nome, telefone, endereco):
        super().__init__(nome, telefone, endereco)

class Fornecedor(Pessoa):
    def __init__(self, nome, telefone, endereco):
        super().__init__(nome, telefone, endereco)

class Produto:
    def __init__(self, nome, categorias, quantidade_estoque):
        self.nome = nome
        self.categorias = categorias
        self.quantidade_estoque = quantidade_estoque

    def comprar(self, quantidade):
        if quantidade <= self.quantidade_estoque:
            self.quantidade_estoque -= quantidade
            return True
        else:
            return False

class Transacao:
    def __init__(self, produto, cliente, quantidade):
        self.data_compra = datetime.now()
        self.produto = produto
        self.cliente = cliente
        self.quantidade = quantidade

class Mercado:
    def __init__(self):
        self.clientes = []
        self.produtos = []
        self.transacoes = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def realizar_compra(self, produto, cliente, quantidade):
        if produto.comprar(quantidade):
            transacao = Transacao(produto, cliente, quantidade)
            self.transacoes.append(transacao)
            return True
        else:
            return False

# Hora de testar:
clienteX = Cliente("Amanda", "125123589", "Rua ABCD")
fornecedorY = Fornecedor("FornecedorY", "89898989", "Rua DCBA")
produtoZ = Produto("ProdutoZ", ["Massa", "Macarrão"], 10)

mercado = Mercado()
mercado.adicionar_cliente(clienteX)
mercado.adicionar_produto(produtoZ)

if mercado.realizar_compra(produtoZ, clienteX, 5):
    print("Compra realizada com sucesso!")
else:
    print("Quantidade indisponível em estoque.")

for transacao in mercado.transacoes:
    print(f"Data: {transacao.data_compra}, Cliente: {transacao.cliente.nome}, Produto: {transacao.produto.nome}, Quantidade: {transacao.quantidade}")
from typing import List, Iterable

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def __str__(self):
        return self.nome, self.preco
    
class Pedido(Produto):
    def __init__(self):
        self.produtos = []
    
    def adicionar_produto(self, id_pedido, produto):
        self.produtos.append(id_pedido, produto)
    
    def valor_total(self):
        return sum(p.preco for p in self.produtos)
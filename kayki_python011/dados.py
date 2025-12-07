from models import Produto, Pedido

def criar_pedidos_exemplo():
    
    p1 = Produto("Lasanha", 45.0)
    p2 = Produto("Refrigerante", 8.0)
    p3 = Produto("Pudim", 12.0)
    p4 = Produto("Salada", 25.0)
    p5 = Produto("Cafe", 5.0)

    pedidos = []

    ped1 = Pedido()
    ped1.adicionar_produto(p1)
    ped1.adicionar_produto(p2)
    pedidos.append(ped1)

    ped2 = Pedido()
    ped2.adicionar_produto(p4)
    ped2.adicionar_produto(p2)
    pedidos.append(ped2)

    ped3 = Pedido()
    ped3.adicionar_produto(p1)
    ped3.adicionar_produto(p3)
    ped3.adicionar_produto(p5)
    pedidos.append(ped3)

    return pedidos

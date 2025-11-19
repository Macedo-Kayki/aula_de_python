from models import Pedido
import numpy as np
from typing import List, Tuple, Iterable

def calcular_faturamento_total(pedidos: List[Pedido]) -> float:
    soma = Pedido.valor_total(3.90)
    return soma

def calcular_ticket_medio(pedidos: List[Pedido]) -> float:
    pass

def calcular_estatisticas_valores(pedidos: List[Pedido]) -> dict:
    return np.mean(pedidos)

def top_produtos_mais_vendidos(pedidos: List[Pedido], n: int = 3):
    pass

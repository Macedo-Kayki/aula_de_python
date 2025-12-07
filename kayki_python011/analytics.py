from models import Pedido
import numpy as np
from typing import List, Tuple, Iterable
from collections import Counter

def _extrair_valores(pedidos):
    return [p.valor_total() for p in pedidos]

def calcular_faturamento_total(pedidos):
    if not pedidos: return 0.0
    valores = _extrair_valores(pedidos)
    
    return float(np.sum(valores))

def calcular_ticket_medio(pedidos):
    if not pedidos: return 0.0
    valores = _extrair_valores(pedidos)
    
    return float(np.mean(valores))

def calcular_estatisticas_valores(pedidos):
    if not pedidos: return None
    
    valores = np.array(_extrair_valores(pedidos))
    
    stats = {
        "media": float(np.mean(valores)),
        "minimo": float(np.min(valores)),
        "maximo": float(np.max(valores))
    }
    return stats

def top_produtos_mais_vendidos(pedidos, n=3):
    todos_produtos = []
    for pedido in pedidos:
        for produto in pedido.produtos:
            todos_produtos.append(produto.nome)
            
    contador = Counter(todos_produtos)
    return contador.most_common(n)

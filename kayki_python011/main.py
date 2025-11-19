import dados as dd
from models import Pedido
import analytics as a

def main():     
    if __name__ == "__main__":
        opc = int(input("===Menu Restaurante Bom Prato===\n1 - Mostrar faturamento total do dia\n2 - Mostrar ticket médio dos pedidos\n3 - Mostrar estatísticas (mínimo, máximo, média dos valores dos pedidos)\n4 - mostrar top 3 produtos mais vendidos\n0 - sair\n"))
    
    return opc

opc = main()
try:
    if opc == 1:
        a.calcular_faturamento_total(dd.criar_pedidos_exemplo())
    if opc == 2:
        a.calcular_estatisticas_valores(dd.criar_pedidos_exemplo())
    if opc == 3:
        a.calcular_faturamento_total(dd.criar_pedidos_exemplo())
except ValueError:
    print("Erro")

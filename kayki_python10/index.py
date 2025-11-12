from typing import Tuple, Iterable

produto = Tuple[str, float]

def filtrar_preco_minimo(produtos: Iterable[produto], minimo: float) -> list[produto]:
    return [(n, p) for (n, p) in produtos if p >= minimo]

def aplicar_desconto(produtos, percentual) -> list[(produto)]:
    fator = 1 - percentual
    return [(n, round(p * fator, 2)) for (n, p) in produtos]

def pipeline(produtos, minimo, desconto):
    return aplicar_desconto(filtrar_preco_minimo(produtos, minimo, desconto))

if __name__ == "__main__":
    produtos = [("A", 10.0), ("B", 5.0), ("C", 12.0)]
    
    filtrados = filtrar_preco_minimo(produtos, 9.0)

    descontados = aplicar_desconto(filtrados, 0.20)

    resultado = pipeline(produtos, minimo=9.0, desconto=0.20)

    print(f"filtro: {filtrados}")
    print(f"descontados: {descontados}")
    print(f"resultado: {resultado}")

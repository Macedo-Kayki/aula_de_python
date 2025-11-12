from typing import Iterable, Tuple
def metricas_sem_builtins(valores: Iterable[float]) -> Tuple[float, float, float, int]:
    if not valores:
        raise ValueError("Não há nenhum valor na lista.")
    
    soma = 0
    min = valores[0]
    max = valores[0]
    media = 0
    acima = 0

    for v in valores:
        if v < min:
            min = v
        if v > max:
            max = v
        soma = soma + v

    media = (soma) / len(valores)

    for v in valores:
        if v > media:
            acima = acima + 1
        
    return min, max, media, acima

valores = [8, 6, 7, 8, 5, 5.60]
metri = metricas_sem_builtins(valores)
print(metri)
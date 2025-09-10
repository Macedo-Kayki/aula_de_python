def media(name: str, n1: float, n2: float) -> None:
    media = (n1 + n2)/2

    if media < 0:
        print("Média inválida, média negativa")
    elif media >= 6:
        print(f"Olá {name}, você está aprovado! Sua média foi de {media}")
    elif media < 6:
        print(f"Olá {name}, infelizmente você foi reprovado! Sua média foi de {media}")
    else:
        print("Média inválida")

def grandeza(v1: int, v2: int, v3: int) -> None:
    if v1 > v2:
        v1, v2 = v2, v1
    if v1 > v3:
        v1, v3 = v3, v1
    if v2 > v3:
        v2, v3 = v3, v2
    print(f"Primeiro número: {v1}")
    print(f"Segundo número: {v2}")
    print(f"Terceiro número: {v3}")

def final():
    opc = int(input("Você deseja permanecer no sistema? (1 = SIM | 0 = NÃO)\n"))

    if opc == 0:
        condition = False
    else:
        condition = True
    return condition

def impidade(idade_txt: str) -> None:
    try:
        idade = int(idade_txt)
        if idade >= 0:
            print(f"Idade registrada: {idade}")
    except ValueError:
        print("Entrada inválida, Tente Novamente")

def menor50(valor: int):
    if not valor>50:
        print(f"\nValor = {valor}")

def contador():
    total, cont, media_turma, soma = 5, 1, 0, 0
    while cont <= total:
        nome=input("Digite seu nome: ")
        n1=float(input("Nota da primeira prova: "))
        n2=float(input("Nota da segunda prova: "))
        media = (n1 + n2)/2
        if media >= 7:
            print(f"O aluno {nome} foi aprovado com média {media}")
        else:
            print(f"O aluno {nome} foi reprovado com média {media}")
        soma += media
        cont += 1
    media_turma = soma / total
    print(f"A média da turma foi de {media_turma}")
    

while True:
    opc = int(input("Digite qual código você quer visualizar\n================================\n1 - Ordem de Grandeza\n================================\n2 - Cálculo de Média\n================================\n3 - Impressão de Números\n================================\n4 - Contador\n================================\n"))
    
    if opc == 1:
        v1 = int(input("Digite o primeiro valor: "))
        v2 = int(input("Digite o segundo valor: "))
        v3 = int(input("Digite o terceiro valor: "))
        grandeza(v1, v2, v3)
        condition = final()
    
    if opc == 2:
        name = input("Digite seu name: ")
        n1 = float(input("Digite sua primeira nota: "))
        n2 = float(input("Digite sua segunda nota: "))
        media(name, n1, n2)
        condition = final()

    if opc == 3:
        idade_txt = input("Digite sua idade: ")
        valor = int(input("Digite um valor menor que 50: "))
        impidade(idade_txt)
        menor50(valor)
        condition = final()
    if opc == 4:
        contador()
        condition = final()

    if not condition:
        break
def repeticao():
    while True:
        name = input("Nome: ")
        if len(name) == 0:
            continue
        if name == "-1":
            break
        n1 = float(input("Nota da primeira prova: "))
        n2 = float(input("Nota da segunda prova: "))
        media = (n1+n2)/2

        if media > 7:
            print(f"O aluno {name} foi aprovado com média {media}")
        else:
            print(f"O aluno {name} foi aprovado com média {media}")

def numero():
    numero = 10

    while numero > 0:
        print(f"valor atual da variável: {numero}")
        numero -= 1
        if numero == 5:
            continue

def forx():
    for x in range(1, 10, 2):
        print(x)

def forchar():
    for letra in 'Kayki':
        if letra == 'y':
            break
        print(f'letra: {letra}')

def matchcase():
    comando = input("Digite a mensagem: ")
    match comando.upper():
        case 'OI':
            print("a")
        case 'TCHAU':
            print("b")
        case _:
            print("dado nao encontrado")

def match2():
    response_code = 404

    match response_code:
        case 400:
            print("Server sem resposta")
        case 401 | 403:
            print("Server se recusa a enviar retorno")
        case 404:
            print("Server não encontrado")

def multas():
    LIMITE_VEL = 80
    MULTA_BASE = 100
    VALOR_KM = 15
    vel = int(input("Qual a velocidade do veículo(em km/h)? "))
    if vel >= LIMITE_VEL:
        subtotal = vel - LIMITE_VEL
        total = (subtotal * VALOR_KM) + MULTA_BASE
        print("O cidadão foi multado!!\n"+"="*19+"Nota Fiscal"+"="*19+f"\nVelocidade: {vel}\n"+"="*50+f"Limite: {LIMITE_VEL}"+"="*50+f"\nPreço por km/h a cima do limite: {MULTA_BASE}\n"+"="*50+f"\nValor a pagar: {total}\n"+"="*50)
    else:
        print("Nenhuma multa aplicada.")

def menu_light():
    print("\nTipos de Instalação:\nR - Residência\n C - Comércio\n I - Indústria\nS - Sair")

def obter_instalacao():
    while True:
        tipo = input("Digite o tipo de instalação (R, C, I, S): ").strip().upper()
        if tipo in ("R", "C", "I", "S"):
            return tipo
        print("Tipo de instalação inválida. Tente Novamente.")

def obter_kwh():
    while True:
        try:
            kwh = int(input("Digite a faixa de kWh consumida."))
            if kwh > 0:
                return kwh
            else:
                print("A quantidade de kWh deve ser maior que zero.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def calcular_preco(tipo, kwh):
    match tipo:
        case "R":
            if kwh <= 500:
                return kwh * 0.40
            else:
                return kwh * 0.65
        case "C":
            if kwh <= 1000:
                return kwh * 0.55
            else:
                return kwh * 0.60
        case "I":
            if kwh <= 5000:
                return kwh * 0.55
            else:
                return kwh * 0.60
        case _:
            return 0.0

def light():
    while True:
        menu_light()
        tipo_instalacao = obter_instalacao()
        
        if tipo_instalacao == "S":
            print("Encerrando o sistema de conta de luz:")
            break

        faixa_kwh = obter_kwh()
        valor = calcular_preco(tipo_instalacao, faixa_kwh)
        print(f"O valor a pagar é: R$ {valor:.2f}")

while True:
    opc = int(input("Digite qual código você quer visualizar\n"+"="*15+"\n1 - teste de while\n"+"="*15+"\n2 - teste de while + continue\n"+"="*15+"\n3 - teste de for\n"+"="*15+"\n4 - teste de for com char\n"+"="*15+"\n5 - switch case\n"+"="*15+"\n6 - switch case com numeros\n"+"="*15+"\n7 - sistema de multas\n"+"="*15+"\n8 - sistema de pagamento de luz\n"+"="*15))
    
    if opc == 1:
        repeticao()
    elif opc == 2:
        numero()
    elif opc == 3:
        forx()
    elif opc == 4:
        forchar()
    elif opc == 5:
        matchcase()
    elif opc == 6:
        match2()
    elif opc == 7:
        multas()
    elif opc == 8:
        light()
    else:
        print("Digite uma opção válida")
    
    perg = input("Deseja continuar no sistema? (sim ou nao)")

    if perg.upper == "NAO":
        break
    continue
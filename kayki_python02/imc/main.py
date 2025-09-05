try:
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))
    imc = peso / (altura ** 2)
    print(f"Seu IMC é: {imc:.2f}")
    if imc < 18.5:
        print("Classificação: Abaixo do Peso")
    elif imc < 24.9:
        print("Classificação: Peso normal")
    elif imc < 29.9:
        print("Classificação: Sobrepeso")
    elif imc < 34.9:
        print("Classificação: Obesidade grau 1")
    elif imc < 39.9:
        print("Classificação: Obesidade grau 2")
    else:
        print("Classificação: Obesidade grau 3")
except ValueError:
    print("Erro: digite valores válidos para o peso e/ou altura ")
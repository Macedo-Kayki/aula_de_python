try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    if num2 == 0:
        print("Erro: não é possível dividir por zero")
    else:
        resultado = num1/num2
        print(f"Resultado da divisão: {resultado}")

except ValueError:
    print("Erro: você deve digitar apenas números inteiros")
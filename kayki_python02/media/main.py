nome = input("\nDigite o nome do aluno: ")
av1 = float(input("Digite a nota da AV1 do Aluno: "))
av2 = float(input("Digite a nota da AV2 do Aluno: "))
media = (av1+av2)/2
if media>=6:
    print(f"O aluno {nome} está aprovado com média igual a {media:.2f}\n")
elif media>=4:
    print(f"O aluno {nome} está aprovado com médial igual a {media:.2f}\n")
else:
    print(f"O aluno {nome} está reprovado com média igual a {media:.2f}\n")


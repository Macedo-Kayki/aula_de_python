
lista = ["laranja", "azul", "verde", "preto"]
def listar():
    val = int(input("Digite qual valor você quer alterar: "))
    txt = input("Qual o novo dado que você deseja printar: ")
    
    listad = ["laranja", "azul", "verde", "preto"]
    listad[val-1] = txt
    exbList(listad)
    remlist(listad)
    
def exbList(listad, lista):
    print(listad)

    for i in range(len(lista)):
        lista[i] = 1 + i

    print(lista)

def remlist(listad):
    while True:
        rem = input("Qual elemento você deseja remover da lista? Caso queira apagar tudo, digite: total")
        if rem != None:
            if rem in listad:
                listad.remove(rem)
            else:
                print("\nEsse elemento não esta presente na lista, por favor tente novamente\n")
                continue
        elif rem.lower() == "total":
            listad.clear()
        else:
            listad.pop()
        print(listad)
        break

def dictionary():
    while True:
        medias = { "Kayki": 10,
                "Robertha": 10,
                "Maria Clara": 9.2,
                "Caetano": 9.5,
                "Rafael": 7,
                "Caua": 10
                }
        nome = input("Informe o nome do aluno: ")
        if nome in medias:
            print(f"Media = {medias[nome]}")
            
            print(f"Outras médias: {medias.values()}")
        else:
            print("\nInsira um nome válido\n")
            continue
        break

opc = input("Escolha um código\n1 - listas\n 2- Dicionários")
if (opc == 1):
    exbList(lista)
    listar()
elif opc == 2:
    dictionary()
else:

    print("insira um valor válido")

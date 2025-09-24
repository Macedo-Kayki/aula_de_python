import math as m
import random as rd
import time 
from datetime import date
from tkinter import Tk

def acima(valor: float) -> float:
    return m.ceil(valor)

def abaixo(valor: float) -> float:
    return m.floor(valor)

def sq(valor: float) -> float:
    return m.sqrt(valor)

def fatorial(valor: int) -> float:
    return m.factorial(valor)

def absoluto(valor: float) -> float:
    return m.fabs(valor)

def exibirval():
    if __name__ == "__main__":
        x = m.pi
        cima = acima(x)
        baixo = abaixo(x)
        sqr = sq(cima)
        fat = fatorial(baixo)
        abs = absoluto(sqr)
        print(f"Arredondando pra cima: {cima}")
        print(f"Arredondando pra baixo: {baixo}")
        print(f"Quadrado: {sqr}")
        print(f"fatorial: {fat}")
        print(f"absoluto: {abs}")

def rpg():
    vida = 100
    boss = 500
    mald = "sem maldição :D"
    while True:
        print("1 - Rola o dado\n2 - Sair")
        if vida < 1:
            print("você perdeu")
            break
        usuario = int(input("O que você deseja: "))
        if usuario == 1:
            numero = rd.randint(0,9)
            if numero == 1:
                mald = "fogo"
                vida = -10
                print(f"Você tenta jogar a maldição mas não tem forças o suficiente e ela volta contra você\n"+"="*10+f"\n-10 de vida ao fim das próximas 3 rodadas\n"+"="*10+f"\nVida atual: {vida}")
                continue
            elif numero == 2:
                print(f"A maldição foi jogada com sucesso, mas o boss é muito resistente\n"+"="*10+f"\no boss perde 10 de vida\n"+"="*10+f"\nVida atual: {boss}")
                continue
            elif numero == 3:
                mald = "zé perna"
                print(f"O boss te joga uma maldição onde você fica paralisado das pernas\n"+"="*10+f"\nmaldição atual {mald}")
            elif numero == 4:
                vida = -100
                print("Você é lançado para longe em um ataque crítico\n"+"="*10+f"\nvida atual: {vida}")
            elif numero == 5:
                print("Você é lançado para longe em um ataque crítico\n"+"="*10+f"\nvida atual: {vida}")
            elif numero == 6:
                print("Você é lançado para longe em um ataque crítico\n"+"="*10+f"\nvida atual: {vida}")
            elif numero == 7:
                print("Você é lançado para longe em um ataque crítico\n"+"="*10+f"\nvida atual: {vida}")
            elif numero == 8:
                print("Você é lançado para longe em um ataque crítico\n"+"="*10+f"\nvida atual: {vida}")
            elif numero == 4:
                print("Você 9 lançado para longe em um ataque crítico\n"+"="*10+f"\nvida atual: {vida}")
            if mald == "fogo":
                if fogo == 3:
                    mald = "sem maldição :D"
                    print("Parabéns, você está curado da maldição de fogo")
                vida = -10
                fogo+= 1
        else:
            break

def exibirtempo():
    x = time.time()
    print(f"Local time: {time.ctime(x)}")
    data = datatual()
    print(data)
    datafmt = dataformatada()
    print(datafmt)
    data2 = datatual2()
    print(data2)
    

def datatual():
    data_atual = date.today()

    return data_atual

def dataformatada():
    datual  = datatual()
    data_formatada = f"{datual.day}/{datual.month}/{datual.year}"

    return data_formatada

def datatual2():
    datual  = datatual()
    data_atual2 = datual.strftime("%d%m%y")

    return data_atual2

def tkin():
    root = Tk()
    width = 600
    height = 300

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)

    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.mainloop()


while True:
    print("1 - Jogar rpg\n2 - Exibir valores\n3 - local time\n4 - tkinter")
    opc = int(input("O que você deseja: "))

    if opc == 1:
        rpg()
    elif opc == 2:
        exibirval()
    elif opc == 3:
        exibirtempo()
    elif opc == 4:
        tkin()
    else:
        break
from Aereo import Aereo
from Terrestre import Terrestre
from Transporte import Transporte
import random as rd

def executar_simulação(frota):
    for transporte in frota:
        transporte.mover()

if __name__ == "__main__":
    transporte = Transporte()
    while True:
        transporte.boas_vindas()
        transp = input("\n"+"="*20+"\nDigite 'Cadastrar' para cadastrar um novo transporte\n"+"="*20+"="*20+"\nDigite 'Listar' para listar os transportes cadastrados\n"+"="*20+"\n"+"Digite 'Simular' para simular o transporte\n"+"="*20+"\n"+"Digite 'Sair' para sair do sistema\n"+"="*20+"\n")
            
        if transp.lower() == "cadastrar":
            tipo = input("Digite o tipo de transporte (Aereo/Terrestre): ")
            if tipo.lower() == "aereo":
                transporte.cadastro_transporte(tipo="a",comp=rd.choice([9001, 9002, 9003, 9004, 9005, 9006, 9007]))
            elif tipo.lower() == "terrestre":
                transporte.cadastro_transporte(tipo="t",comp=rd.choice([1, 2, 3, 4, 5]))
            else:
                print("Tipo de transporte inválido!")
                continue
            continue
        elif transp.lower() == "listar":
            transporte.listar_transporte()
            cont = int(input("Para continuar, digite 1"))
            if cont == 1:
                continue
            else:
                break
        elif transp.lower() == "simular":
            frota = []
            for id, dados in transporte.transport.items():
                if 'rota' in dados:
                    frota.append(Aereo(transporte))
                elif 'abs_nivel' in dados:
                    frota.append(Terrestre(transporte))
            executar_simulação(frota)
            continuar = int(input("Para continuar, digite 1"))
            if continuar == 1:
                continue
            else:
                break

        elif transp.lower() == "sair":
            break
        else:
            print("Digite uma opção válida!")
            continue
        break
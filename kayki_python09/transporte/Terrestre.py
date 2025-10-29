from Transporte import Transporte
import random as rd

class Terrestre(Transporte):
    def __init__(self, transport):
        super().__init__()
        self.transport = transport.transport
        self.distancia = 0
    
    def mover(self):
        for id, dados in self.transport.items():
            if 'abs_nivel' in dados:
                self.combustivel = dados['combustivel']
                self.velocidade = dados['velocidade']
                self.abs_nivel = dados['abs_nivel']
                self.id = id

                if self.combustivel <= 0:
                    print(f"Terrestre com o identificador {id}: Sem combustível para andar.")
                    return

                self.distancia += self.velocidade // 10
                print(
                    f"Terrestre com o identificador {id}: Movendo-se a {self.velocidade} KM/H."
                    f"ABS nível: {self.abs_nivel}, distância total: {self.distancia} KM."
                )
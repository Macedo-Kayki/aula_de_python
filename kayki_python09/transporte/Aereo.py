from Transporte import Transporte
import random as rd

class Aereo(Transporte):
    def __init__(self, transport):
        super().__init__()
        self.transport = transport.transport
        self.altitude = 0
    
    def mover(self):
        for id, dados in self.transport.items():
            if 'rota' in dados:
                self.combustivel = dados['combustivel']
                self.velocidade = dados['velocidade']
                self.rota = dados['rota']
                self.id = id

                if self.combustivel <= 0:
                    print(f"Aéreo com o identificador {id}: Sem combustível para voar.")
                    return

                self.altitude += 1000
                print(
                    f"Aéreo com o identificador {id}: Voando a {self.velocidade} KM/H."
                    f"Rota: {self.rota}, altitude atual: {self.altitude} metros."
                )

                if self.altitude == 0:
                    self.altitude += rd.randint(1000, 5000)
                    print(
                        f"Aéreo com o identificador {id}: Decolando na rota {self.rota}."
                        f"Subindo para {self.altitude} metros a uma velocidade de {self.velocidade} KM/H."
                    )
                else:
                    self.altitude += rd.randint(500, 2000)
                    print(
                        f"Aéreo com o identificador {id}: Em voo na rota {self.rota}."
                        f"Altitude ajustada para {self.altitude} metros a uma velocidade de {self.velocidade} KM/H."
                    )
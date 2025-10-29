class Transporte():
    def __init__ (self):
        self.transport = {}

    def cadastro_transporte(self, comp, tipo):
        self.combustivel = int(input("Combustível(L): "))
        self.velocidade = int(input("Velocidade(KM/H):"))

        if tipo == "a":
            novo_id = max(self.transport.keys(), default=0) + 1
            self.transport[novo_id] = {
                "combustivel": self.combustivel,
                "velocidade": self.velocidade,
                "rota": comp
            }
        elif tipo == "t":
            novo_id = max(self.transport.keys(), default=0) + 1
            self.transport[novo_id] = {
                "combustivel": self.combustivel,
                "velocidade": self.velocidade,
                "abs_nivel": comp
            }
       
    
    def boas_vindas(self):
        print("Seja bem-vindo(a) ao sistema NextTransport\nPara prosseguir, selecione a ação desejada abaixo:")
    
    def listar_transporte(self):
        for id, dados in self.transport.items():
            print("\n"+"="*20+f"\nID: {id}\n"+"="*20+f"\nCombustível: {dados['combustivel']}L\n"+"="*20+f"\nVelocidade: {dados['velocidade']}KM/H\n"+"="*20)
    
    def mover(self):
        print("O método mover() da classe Transporte deve ser sobrescrito nas subclasses.")
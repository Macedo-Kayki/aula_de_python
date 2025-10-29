class Cliente:
    def __init__(self, cpf, nome, endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
    
    def __str__(self):
        return f"Cliente: {self.nome}, CPF: {self.cpf}, Endereço: {self.endereco}"

class Extrato:
    def __init__(self):
        self.movimentos = []
    
    def registrar(self, descricao):
        self.movimentos.append(descricao)

    def mostrar(self):
        print("====EXTRATO====")
        if not self.movimentos:
            print("Não foram realizadas movimentações.")
        else:
            for movimento in self.movimentos:
                print(movimento)
            print("==============")

class Conta:
    def __init__(self, numero, cliente, clientes_iniciais=None):
        self.numero = numero
        self.saldo = 0.0
        if clientes_iniciais is None:
            self.clientes = []
        else:
            self.clientes = list(clientes_iniciais)
        self.extrato = Extrato()
        self.extrato.registrar(
            f"Conta {self.numero} criada com saldo inicial de R$ {self.saldo:.2f}."
        )

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)
        self.extrato.registrar(
            f"Cliente {cliente.nome}, CPF ({cliente.cpf}) vinculado à conta {self.numero}."
        )
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.registrar(
                f"Depósito de R$ {valor:.2f} realizado. Saldo atual: R$ {self.saldo:.2f}."
            )
        else:
            print("Valor de depósito inválido.")
            return
    
    def sacar(self, valor): 
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.extrato.registrar(
                f"Saque de R$ {valor:.2f} realizado. Saldo atual: R$ {self.saldo:.2f}.")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")
            return
    
    def mostrar_dados(self):
        print(f"===Dados da Conta {self.numero}===")
        print(f"Saldo: R$ {self.saldo:.2f}")
        print("Clientes vinculados:")
        for cliente in self.clientes:
            print(cliente)
        print("=================================")
    
    def mostrar_extrato(self):
        self.extrato.mostrar()

if __name__ == "__main__":
    cliente1 = Cliente("123.456.789-00", "Kayki", "Rua A, 123")
    cliente2 = Cliente("987.654.321-00", "Maria", "Rua B, 456") 
    conta = Conta(1, cliente1)
    conta.adicionar_cliente(cliente2)
    for i in range(3):
        conta.depositar(1000)
        conta.sacar(250)
        conta.mostrar_dados()
        conta.mostrar_extrato()
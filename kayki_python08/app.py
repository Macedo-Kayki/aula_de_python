class Conta:
    def __init__(self, saldo=100):
        self.numero = input("Digite o número da conta: ")
        self.titular = input("Digite o nome do titular da conta: ")
        self.saldo = saldo
        print(f"Olá, {self.titular}")
        
    def set_saldo(self):
        print(f"Saldo atual: {self.saldo}")
        self.saldo += float(input("Quanto você deseja depositar?"))
    
    def rem_saldo(self):
        print(f"Saldo atual: {self.saldo}")
        sacou = float(input("Quanto você deseja sacar?"))
        
        if sacou > self.saldo:
            print("Saque falhou: saldo insuficiente")
        else:
            print("Saque realizado com sucesso")
            self.saldo += sacou
    
    def get_saldo(self):
        print(f"Saldo: R${self.saldo:.2f}")

print("Seja Bem-Vindo(a) ao Banco NextEst\nPara Prosseguir, logue em sua conta bancária\n"+"="*60)
contas = Conta()
while True:
    bank = input("Qual ação você deseja realizar?\n"+"="*60+"\nDigite 'Sacar' para realizar um saque\n"+"="*60+"\nDigite 'Depositar' para realizar um deposito\n"+"="*60+"\nDigite 'Conta' para ver seu saldo bancário")
    if bank.lower() == "depositar":
        contas.set_saldo()
    elif bank.lower() == "sacar":
        contas.rem_saldo()
    elif bank.lower() == "conta":
        contas.get_saldo()
    else:
        print("Digite uma opção válida")
        continue
    break
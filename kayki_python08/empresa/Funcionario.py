class Funcionario():
    def __init__(self, nome, idade, email, salario):
        super().__init__(nome, idade, email)
        self.salario = salario
    
    def exibir_detalhes(self):
        return f"{self.exibir_infos()}, Salário: {self.salario}"
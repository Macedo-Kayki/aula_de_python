from empresa import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, idade, email, salario, departamento):
        super().__init__(nome, idade, salario, email)
        self.departamento = departamento
    
    def exibir_details(self):
        return f"{self.exibir_detalhes()}, Departamento: {self.departamento}"
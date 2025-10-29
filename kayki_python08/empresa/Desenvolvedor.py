from empresa import Funcionario

class Desenvolvedor(Funcionario):
    def __init__(self, nome, idade, email, salario, linguagem):
        super().__init__(nome, idade, salario, email)
        linguagem = {}
        self.linguagem = linguagem
    
    def exibicao_det(self):
        return f"{self.exibir_detalhes()}, Linguagem: {self.linguagem}"
    
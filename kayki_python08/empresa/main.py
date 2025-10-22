class Pessoa:
    def __init__(self, nome, idade, time):
        self.nome = nome
        self.__idade = idade
        self._time = time
    
    def exibir_infos(self):
        return f"Nome: {self.nome}, Idade: {self.__idade}"

class Funcionario(Pessoa):
    def __init__(self, nome, idade, time, salario):
        super().__init__(nome, idade, time)
        self.salario = salario
    
    def exibir_detalhes(self):
        return f"{self.exibir_infos()}, Salário: {self.salario}"

class Gerente(Funcionario):
    def __init__(self, nome, idade, time, salario, departamento):
        super().__init__(nome, idade, time)
        self.salario = salario
        self.departamento = departamento
    
    def exibir_details(self):
        return f"{self.exibir_detalhes()}, Departamento: {self.departamento}"

class Desenvolvedor(Funcionario):
    def __init__(self, nome, idade, time, salario, linguagem):
        super().__init__(nome, idade, time)
        linguagem = {}
        self.salario = salario
        self.linguagem = linguagem
    
    def exibicao_det(self):
        return f"{self.exibir_detalhes()}, Linguagem: {self.linguagem}"

funcionario = Gerente("Kayki", 18, "Flamengo", 35000, "R")
print(funcionario.exibir_details())
class Pessoa:
    def __init__(self):
        self.nome = input("Digite o nome da pessoa: ")
        self.__idade = int(input("Digite a idade da pessoa: "))
        
    def get_idade(self):
        return self.__idade
    
    def set_idade(self, nova_idade):
        if nova_idade > 0:
            self.__idade = nova_idade
        else:
            print("Idade inválida!")
        
    def __repr__(self):
        return f"Nome: {self.nome}\nIdade: {self.__idade}"

pessoa = Pessoa()
print(pessoa.nome)
print(pessoa.get_idade())
pessoa.set_idade(30)
print(pessoa.get_idade())
pessoa.set_idade(-5)
print(pessoa)
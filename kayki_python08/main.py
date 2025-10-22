class Aluno:
    uni = "Estácio"
    
    def __init__(self):
        self.nome = input("Digite o nome do aluno: ")
        self.nota = float(input("Digite a nota do aluno: "))
    
    def situacao(self):
        return "Aprovado" if self.nota >= 6 else "Reprovado"

    def __str__(self):
        return f"{self.nome} ({self.nota}) - {self.situacao()}"
    
aluno = Aluno()
print(aluno)
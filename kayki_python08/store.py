produtos = {}

class Produto:
    def __init__(self):
        print("Seja bem-vindo(a) ao sistema NextStore\nPara prosseguir, selecione a ação desejada abaixo:")
        
    def cadastro(self):
        self.nome = input("Digite o nome do produto: ")
        self.preco = float(input("Digite o preço do produto: "))
        self.estoque = int(input("Digite a quantidade de estoque do produto: "))
        
        novo_id = max(produtos.keys(), default=0) + 1
        produtos[novo_id] = {
            "nome": self.nome,
            "preco": self.preco,
            "estoque": self.estoque
        }
    
    def repor(self, id):
        if id in produtos:
            product = produtos[id]
            print(f"Estoque atual: {self.estoque}")
            self.estoque = int(input("Digite o novo estoque do produto: "))
            product['estoque'] = self.estoque
    
    def listar(self):
        for id, dados in produtos.items():
            print("\n"+"="*20+f"\nID: {id}\n"+"="*20+f"\nProduto: {dados['nome']}\n"+"="*20+f"\nPreço: {dados['preco']}\n"+"="*20+f"\nEstoque: {dados['estoque']}\n"+"="*20)

produto = Produto()
while True:
    loja = input("\n"+"="*20+"\nDigite 'Cadastrar' para cadastrar um novo produto\n"+"="*20+"="*20+"\nDigite 'Estoque' para repor o estoque de um produto\n"+"="*20+"\n"+"Digite 'Listar' para listar o estoque de produtos\n"+"="*20+"\n"+"Digite 'Sair' para sair do sistema\n"+"="*20+"\n")
        
    if loja.lower() == "cadastrar":
        produto.cadastro()
        continue
    elif loja.lower() == "estoque":
        id_pd = input("Digite o ID ou Nome do produto que você deseja atualizar o estoque")
        produto.repor(id_pd)
    elif loja.lower() == "listar":
        produto.listar()
        cont = int(input("Para continuar, digite 1"))
        if cont == 1:
            continue
        else:
            break
    elif loja.lower() == "sair":
        break
    else:
        print("Digite uma opção válida!")
        continue
import dados
import analytics

def main():
    pedidos = dados.criar_pedidos_exemplo()
    
    while True:
        print("\n=== Menu Restaurante Bom Prato ===")
        print("1 - Mostrar faturamento total do dia")
        print("2 - Mostrar ticket médio dos pedidos")
        print("3 - Mostrar estatísticas (mínimo, máximo, média)")
        print("4 - Mostrar top 3 produtos mais vendidos")
        print("0 - Sair")
        
        opcao_raw = input("Escolha uma opção: ")

        try:
            opcao = int(opcao_raw)

            if opcao == 0:
                print("Saindo do sistema...")
                break
            
            elif opcao == 1:
                total = analytics.calcular_faturamento_total(pedidos)
                print(f"\n>>> Faturamento Total: R$ {total:.2f}")

            elif opcao == 2:
                try:
                    media = analytics.calcular_ticket_medio(pedidos)
                    if media == 0 and len(pedidos) == 0:
                        raise ZeroDivisionError
                    print(f"\n>>> Ticket Médio: R$ {media:.2f}")
                except ZeroDivisionError:
                    print("\n>>> Erro: Não há pedidos cadastrados para calcular a média.")

            elif opcao == 3:
                stats = analytics.calcular_estatisticas_valores(pedidos)
                if stats:
                    print("\n>>> Estatísticas dos Valores:")
                    print(f"    Mínimo: R$ {stats['minimo']:.2f}")
                    print(f"    Máximo: R$ {stats['maximo']:.2f}")
                    print(f"    Média:  R$ {stats['media']:.2f}")
                else:
                    print("\n>>> Sem dados para estatísticas.")

            elif opcao == 4:
                top = analytics.top_produtos_mais_vendidos(pedidos, n=3)
                print("\n>>> Top 3 Produtos:")
                for i, (nome, qtd) in enumerate(top, 1):
                    print(f"    {i}. {nome} ({qtd} vendas)")

            else:
                print("\n>>> Opção inválida! Por favor, escolha entre 0 e 4.")

        except ValueError:
            print("\n>>> Erro: Entrada inválida! Por favor digite um número inteiro.")
        except Exception as e:
            print(f"\n>>> Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()

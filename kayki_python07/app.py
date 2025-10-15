artilheiros = {
    1: {"nome": "Flaco López", "clube": "Palmeiras", "jogos": 9, "gols": 7, "assistencias": 1},
    2: {"nome": "Adrián Martínez", "clube": "Racing", "jogos": 10, "gols": 7, "assistencias": 2},
    3: {"nome": "Ramiro Vaca", "clube": "Bolivar", "jogos": 4, "gols": 5, "assistencias": 0},
    4: {"nome": "Alan Patrick", "clube": "Internacional", "jogos": 8, "gols": 5, "assistencias": 2},
    5: {"nome": "Maher Carrizo", "clube": "Vélez Sarsfield", "jogos": 10, "gols": 5, "assistencias": 1}
}

def exibir_estatisticas() -> None:
    print("\nEstatísticas dos Artilheiros da Libertadores:\n")
    for id, dados in artilheiros.items():
        print(f"ID {id} - {dados['nome']} ({dados['clube']}): "
              f"Jogos={dados['jogos']}, Gols={dados['gols']}, Assistências={dados['assistencias']}")
    print()

def adicionar_jogador(nome: str, clube: str, jogos: int, gols: int, assistencias:int) -> None:
    novo_id = max(artilheiros.keys(), default=0) + 1
    artilheiros[novo_id] = {
        "nome": nome,
        "clube": clube,
        "jogos": jogos,
        "gols": gols,
        "assistencias": assistencias
    }
    print(f"Jogador '{nome}' adicionado com ID {novo_id}.")


def atualizar_stats(id_jogador: int, jogos: int=None, gols: int=None, assistencias: int=None) -> None:
    if id_jogador in artilheiros:
        jogador = artilheiros[id_jogador]
        if jogos is not None:
            jogador['jogos'] = jogos
        if gols is not None:
            jogador['gols'] = gols
        if assistencias is not None:
            jogador['assistencias'] = assistencias
        print(f"Estatísticas do jogador ID {id_jogador} atualizadas.")
    else:
        print(f"Jogador com ID {id_jogador} não encontrado.")

def remover_jogador(id_jogador: int) -> None:
    if id_jogador in artilheiros:
        nome = artilheiros[id_jogador]['nome']
        del artilheiros[id_jogador]
        print(f"Jogador '{nome}' removido com sucesso.")
    else:
        print(f"ID {id_jogador} não encontrado.")

def encontrar_artilheiro() -> None:
    if not artilheiros:
        print("Nenhum jogador registrado.")
        return
    max_gols = max(jogador['gols'] for jogador in artilheiros.values())
    artilheiros_top = [j for j in artilheiros.values() if j['gols'] == max_gols]
    print(f"\nArtilheiro(s) com {max_gols} gols:")
    for j in artilheiros_top:
        print(f"{j['nome']} ({j['clube']})")

if __name__ == "__main__":
    exibir_estatisticas()
    encontrar_artilheiro()
    adicionar_jogador("Pedro", "Flamengo", 8, 8, 3)
    atualizar_stats(3, gols=6)
    remover_jogador(5)
    exibir_estatisticas()
    encontrar_artilheiro()
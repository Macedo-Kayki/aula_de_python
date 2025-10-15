def transtup():
    x = ["banana", "kiwi", "morango"]
    x[1] = "uva"
    y = tuple(x)

    print(y)

def tupla():
    tupla = (1, 2, 3, "quatro", "cinco")

    primeiro_elemento = tupla[0]
    ultimo_elemento = tupla[-1]
    
    print(primeiro_elemento)
    print(ultimo_elemento)

def planao() -> set:
    planeta_anao = {'Plutão', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
    print("Planetas anões:", planeta_anao)
    print(type(planeta_anao))
    
    return planeta_anao

def planet() -> set:
    planeta = {'Marte', 'Marte', 'Terra', 'Marte'}
    print("Planetas: ", planeta)
    return planeta
    
def exibirplanets():
    planet()
    plana = planao()
    qtd_planet = len(plana)
    print("Quantidade de planetas Anões: ", qtd_planet)
    verify_planet()
    astros()

def verify_planet():
    anao = planao()
    print("Verificação de planetas", anao)
    print("Ceres:", 'Ceres' in anao, "| Lua:", 'Lua' in anao, "| Eris:", 'Eris' not in anao)

def astros():
    anao = planao()
    for astro in anao:
        print(astro.upper(), end = " - ")
        if astro == anao:
            print(astro.upper())
            
  
exibirplanets()
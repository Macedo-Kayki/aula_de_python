def teamum():
    timeum = {"Flamengo", "Vasco", "Botafogo"}
    return timeum

def teamdois():
    timedois = {"Flamengo", "Vasco", "Botafogo", "Paysandu"}
    return timedois

def comp():
    times = teamum()
    times2 = teamdois()
    
    print(times ^ times2)
    print("Time diferente2:", times.symmetric_difference(times2))
    
    print("Time diferente2:", times.isdisjoint(times2))
    
    times |= times2
    print("Tudo junto: ", times)
    testeadc()

def testeadc():
    times = teamum()
    times2 = teamdois()
    
    times.add("Olaria")
    times.add("Flamengo") #teste de item repetido
    
    times.remove("Paysandu")
    
    print(times)

comp()
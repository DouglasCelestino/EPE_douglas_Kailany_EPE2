print ('Atividade EPE2')
def cria_baralho():
    naipes = ['♠','♥','♦','♣']
    termos = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    Baralho = []

    for e in termos:
        juntar1 = e + naipes[0]
        juntar2 = e + naipes[1]
        juntar3 = e + naipes[2]
        juntar4 = e + naipes[3]
        Baralho.append(juntar1)
        Baralho.append(juntar2)
        Baralho.append(juntar3)
        Baralho.append(juntar4)
    return Baralho

def extrai_naipe(carta):
    if carta[0] == '1':
        return(carta[2])
    else:
        return(carta[1])

def extrai_valor (carta):
    if len(carta) == 3:
        return carta[0]+ carta[1]
    return carta[0]
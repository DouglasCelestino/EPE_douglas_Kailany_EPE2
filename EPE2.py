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

def lista_movimentos_possiveis(baralho,ind):
    naipe_carta = extrai_naipe(baralho[ind])
    naipe_anterior = extrai_naipe(baralho[ind-1])
    valor_carta = extrai_valor(baralho[ind])
    valor_anterior = extrai_valor(baralho[ind-1])
    if ind == 0:  
        return []
    elif ind < 3:
        if naipe_carta == naipe_anterior or valor_carta == valor_anterior:
            return [1]
        else:
            return []
    elif ind >= 3:
        naipe_terceiro = extrai_naipe(baralho[ind-3])
        valor_terceiro = extrai_valor(baralho[ind-3])
        if valor_carta == valor_anterior and valor_carta == valor_terceiro:
            return [1, 3]
        elif naipe_carta == naipe_anterior and naipe_carta == naipe_terceiro:
            return [1, 3]
        elif valor_carta == valor_anterior and naipe_carta == naipe_terceiro:
            return [1, 3]
        elif naipe_carta == naipe_anterior and valor_carta == valor_terceiro:
            return [1, 3]
        elif naipe_carta == naipe_anterior or valor_carta == valor_anterior:
            return [1]
        elif valor_carta == valor_terceiro or naipe_carta == naipe_terceiro:
            return [3]
        else:
            return []
    else:
        return []


def empilha (baralho,pI,pF):
    alterada = baralho[pI]
    baralho.remove(baralho[pI])
    baralho[pF] = alterada
    return baralho

def possui_movimentos_possiveis(baralho):
    c = 0
    while c < len(baralho):
        movimento = lista_movimentos_possiveis(baralho, c)
        if movimento != []:
            return True
        c += 1
    return False
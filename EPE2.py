print ("\033[36mQuer se divertir jogando Paciência Acordeão???\033[m")
inicio = input("\033[36mTecle ENTER para proseguir:\033[36m\n")
import random
def cria_baralho():
    naipes = ['♣','♥','♠','♦']
    numeros= ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    cartas_paus = []
    cartas_copas = []
    cartas_espadas = []
    cartas_ouros = []
    for c in numeros:
        conc_paus = c + naipes[0]
        cor_paus = ('\033[47;30m{}\033[m'.format(conc_paus))
        cartas_paus.append(cor_paus)
        conc_copas = c + naipes[1]
        cor_copas = ('\033[47;31m{}\033[m'.format(conc_copas))
        cartas_copas.append(cor_copas)
        conc_espadas = c + naipes[2]
        cor_espadas = ('\033[47;30m{}\033[m'.format(conc_espadas))
        cartas_paus.append(cor_espadas)
        conc_ouros = c + naipes[3]
        cor_ouros = ('\033[47;31m{}\033[m'.format(conc_ouros))
        cartas_copas.append(cor_ouros)
    lista_baralho = cartas_paus+cartas_copas+cartas_espadas+ cartas_ouros
    return lista_baralho

def extrai_naipe(carta):
    if carta[8] == '1':
        return(carta[10])
    else:
        return(carta[9])
    
def extrai_valor(carta):
    if carta[8] == '1':
        return '10'
    else:
        return(carta[8])

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

def empilha(baralho, p0, pf):
    novo = baralho[p0]
    baralho.remove(baralho[p0])
    baralho[pf] = novo
    return baralho
   
def possui_movimentos_possiveis(baralho):
    c = 0
    while c < len(baralho):
        movimento = lista_movimentos_possiveis(baralho, c)
        if movimento != []:
            return True
        c += 1
    return False

#criando o baralho e embaralhando em seguida
baralho = cria_baralho()
embaralhar = random.shuffle(baralho)

#Imprimindo baralho
print('O estado atual do baralho é: ')
i = 0
for c in baralho:
    print('{}.  {}'.format(i, c))
    print("")
    i += 1
# definição para o uso do while
jogada = int(input(('Escolha uma carta (digite um número entre 0 e {}): '.format((len(baralho)-1)))))
if jogada >= 0 and jogada <= 51:
    carta = baralho[jogada]
    verifica_jogada = lista_movimentos_possiveis(baralho, jogada)    
fim = 0
#repetição do jogo
while fim <= 52:
    verificacao = len(baralho) - 1
    if  jogada < 0 or jogada > verificacao:
        print('Posição inválida. Por favor, digite um número entre 0 e {}):'.format(len(baralho) - 1))
    #se não houver jogadas possíveis
    elif verifica_jogada == []:
        carta = baralho[jogada]
        print('A carta {} não pode ser movida. Por favor, digite um número entre 0 e 51): '.format(carta))
    #se houver a possibilidade de empilhar sobre a anterior
    elif verifica_jogada == [1]:
        fim += 1
        empilhar = empilha(baralho, jogada, jogada - 1)
        i = 0
        print('O estado atual do baralho é: ')
        for c in baralho:
            print('{}.  {}'.format(i, c))
            print("")
            i += 1
    #se houver a possibilidade de empilhar sobre a terceira anterior
    elif verifica_jogada == [3]:
        fim += 1
        empilhar = empilha(baralho, jogada, jogada - 3)
        i = 0
        print('O estado atual do baralho é: ')
        for c in baralho:
            print('{}.  {}'.format(i, c))
            print("")
            i += 1
    #se houver duas possibilidades de jogada
    elif verifica_jogada == [1, 3]:
        fim += 1
        carta = baralho[jogada]
        carta_anterior = baralho[jogada - 1]
        carta_terceira = baralho[jogada - 3]
        escolha = 'Sobre qual carta você quer empilhar o {}?'.format(carta)
        opcao1 = ('1. {}'.format(carta_anterior))
        opcao2 = ('2. {}'.format(carta_terceira))
        print(escolha)
        print(opcao1)
        print(opcao2)
        escolhida = int(input(('Escolha 1 ou 2: ')))
        while escolhida >= 3 or escolhida <= 0:
            print('Opção inválida. Sobre qual carta você quer empilhar o {}? '.format(carta))
            escolhida = int(input(('Escolha 1 ou 2: ')))
        #se a escolha for 1, substitua

        if escolhida == 1:
            empilhar = empilha(baralho, jogada, jogada - 1)
            i = 0
            print('O estado atual do baralho é: ')
            for c in baralho:
                print('{}.  {}'.format(i, c))
                print("")
                i += 1

            #se a escolha for 2, substitua
        elif escolhida == 2:
            empilhar = empilha(baralho, jogada, jogada - 3)
            i = 0
            print('O estado atual do baralho é: ')
            for c in baralho:
                print('{}.  {}'.format(i, c))
                print("")
                i += 1

    jogada = int(input(('Escolha uma carta (digite um número entre 0 e {}): '.format(len(baralho)-1))))
    if jogada >= 0 and jogada < verificacao:
        carta = baralho[jogada]
        verifica_jogada = lista_movimentos_possiveis(baralho, jogada)   
    
        #marcador para ver se o usuário perdeu
    perdeu_ganhou = possui_movimentos_possiveis(baralho)
    if perdeu_ganhou == False and len(baralho) != 1:
        print('Você perdeu :(')
        decisao = str(input('Quer jogar novamente? (digite s ou n)'))
        decisao = decisao.lower()
        if decisao == 's':
            print('RODA O CÓDIGO NOVAMENTE FOLGADO!')
        elif decisao == 'n':
            print('Obrigado por jogar com a gente♥')
    
print('Você ganhou')
decisao = str(input('Quer jogar novamente? (digite s ou n)'))
decisao = decisao.lower()
if decisao == 's':
    print('RODA O CÓDIGO NOVAMENTE FOLGADO!')
elif decisao == 'n':
    print('Obrigado por jogar com a gente♥') 
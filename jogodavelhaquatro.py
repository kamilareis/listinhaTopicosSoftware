'''1) Crie uma versão do jogo da velha 4x4. As regras são as mesmas da versão 3x3.'''

'''Utilizando uma matriz os jogadores vão escolher uma linha entre 1 e 4 e uma coluna
entre 1 e 4, se a posição não estiver vazia vai retornar para "Tentar novamente!", ao
preencher uma coluna, linha ou diagonal completa o jogador vence e se for preenchido
todas as posições sem a sequência do X ou O é declarado empate finalizando o jogo.'''


#lista representando o tabuleiro do jogo, inciando com um tabuleiro vazio.
lista = [ [0 for i in range(4)] for j in range(4)]

#função responsável por imprimir o tabuleiro.
def tabuleiro():
    for l in range(4):
        for c in range(4):
            if lista[l][c] == 0:
                print("_ |", end=' ')
            elif lista[l][c] == 1:
                print("X |", end=' ')
            elif lista[l][c] == -1:
                print("O |", end=' ')

        print(" ")

#função principal do jogo, que controla o loop até o jogador ganhar ou empatar, encerrando o jogo.
def jogo():
    jogada = 0
    jogador = "X"

    #loop alterna entre os jogadores, solicita  a linha e coluna e verifica se a jogada é válida.    
    while verifica_ganhador() == 0 and jogada < 16: #após 16 jogadas é declarado empate
        print(f"Vez do {jogador}!")
        tabuleiro()
        linha  = int(input("Escolha uma linha (1-4): "))
        coluna = int(input("Escolha uma coluna (1-4): "))

        #if válida a jogada, se a posição está vazia preenche a posição escolhida pelo jogador.
        if 1 <= linha <= 4 and 1 <= coluna <= 4 and lista[linha-1][coluna-1] == 0:
            if jogador == "X":
                lista[linha-1][coluna-1]=1 #preenche para o jogador X.
            else:
                lista[linha-1][coluna-1]=-1 #preenche para o jogador O.
        else: #se a posição já estiver preenchida imprime "Tente novamente! e retorna para a jogada".
            print("Tente novamente!")
            continue

        if verifica_ganhador(): #verifica se o jogador atual venceu e imprime o tabuleiro final.
            tabuleiro()
            print(f"O jogador {jogador} ganhou!!")
            
        jogada +=1
        jogador = "X" if jogador == "O" else "O"

    #if após terminar o loop e não houver ganhador imprime "Houve empate!".
    if verifica_ganhador() == 0:
        tabuleiro()
        print("Houve empate!")

#função que verifica se teve um ganhador, ela verifica as linhas, colunas e diagonais se estão completas com X ou O e se encontrar retorna 1 para indicar o ganhador, se não retorna 0.
def verifica_ganhador():
    for i in range(4):
        soma = lista[i][0] + lista[i][1] + lista[i][2] + lista[i][3]
        if soma == 4 or soma == -4:
            return 1

    for i in range(4):
        soma = lista[0][i] + lista[1][i] + lista[2][i] + lista[3][i]
        if soma == 4 or soma == -4:
            return 1

    diagonal1 = lista[0][0] + lista[1][1] + lista[2][2] + lista[3][3]
    diagonal2 = lista[0][3] + lista[1][2] + lista[2][1] + lista[3][0]
    if diagonal1 == 4 or diagonal1 == -4 or diagonal2 == 4 or diagonal2 == -4:
        return 1

    return 0
           
jogo()

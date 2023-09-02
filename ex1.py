'''Crie um jogo da velha NxN em que o usuário deve definir as dimensões do
tabuleiro (sempre quadrado).'''


#função que recebe a entrada de um número inteiro digitada pelo usuário. 
tamanho = int(input("Digite o tamanho do tabuleiro: "))
#lista representando o tabuleiro do jogo, inciando com os espaços em branco para representar as posições vazias.
lista = [[' ' for _ in range(tamanho)] for _ in range(tamanho)]
#função responsável por imprimir o tabuleiro.
def tabuleiro():
    for l in range(tamanho): #percorre pelas posições do tabuleiro.
        for c in range(tamanho):
            if lista[l][c] == ' ':
                print("_ |", end = ' ') #se estiver vazia imprime.
            elif lista[l][c] == 1:
                print("X |", end = ' ') #se estiver 1 imprime X.
            elif lista[l][c] == -1:
                print("O |", end = ' ') #se estiver -1 imprime O.
        print(" ")
#função principal do jogo, que controla o loop até o jogador ganhar ou empatar, encerrando o jogo.
def jogo(tamanho):
    jogada = 0
    jogador = 'X'
    
    #loop alterna entre os jogadores, solicita  a linha e coluna e verifica se a jogada é válida.
    #como o tabuleiro é quadrado ele multiplica as linhas pelas colunas e após todos preenchido sem um ganhador é declarado empate.
    while verifica_ganhador(tamanho) == 0 and jogada < tamanho * tamanho:  
        print(f"Vez do Jogador {jogador}")
        tabuleiro()
        linha = int(input(f"Escolha uma linha (1-{tamanho}): "))
        coluna = int(input(f"Escolha uma coluna (1-{tamanho}): "))
        
        #if válida a jogada, se a posição está vazia preenche a posição escolhida pelo jogador.
        if 1 <= linha <= tamanho and 1 <= coluna <= tamanho and lista[linha - 1][coluna - 1] == ' ':
            if jogador == "X":
                lista[linha-1][coluna-1] = 1
            else:
                lista[linha-1][coluna-1] = -1
        else: 
            print("Tente novamente!")
            continue

        if verifica_ganhador(tamanho): 
            tabuleiro()
            print(f"O jogador {jogador} ganhou!!")

        jogador = "X" if jogador == "O" else "O"

    #if após terminar o loop e não houver ganhador imprime "Houve empate!"
    if verifica_ganhador(tamanho) == 0:
        tabuleiro()
        print("Houve empate!")

#função que verifica se teve um ganhador, ela verifica as linhas, colunas e diagonais se estão completas com X ou O e se encontrar retorna 1 para indicar o ganhador, se não retorna 0.
def verifica_ganhador(tamanho):
    for i in range(tamanho):
        soma = sum([1 if lista[i][j] == 1 else -1 if lista[i][j] == -1 else 0 for j in range(tamanho)])
        if soma == tamanho or soma == -tamanho:
            return 1

    for i in range(tamanho):
        soma = sum([1 if lista[j][i] == 1 else -1 if lista[j][i] == -1 else 0 for j in range(tamanho)])
        if soma == tamanho or soma == -tamanho:
            return 1

    diagonal1 = sum([1 if lista[i][i] == 1 else -1 if lista[i][i] == -1 else 0 for i in range(tamanho)])
    diagonal2 = sum([1 if lista[i][tamanho - i - 1] == 1 else -1 if lista[i][tamanho - i - 1] == -1 else 0 for i in range(tamanho)])

    if diagonal1 == tamanho or diagonal1 == -tamanho or diagonal2 == tamanho or diagonal2 == -tamanho:
        return 1

    return 0


jogo(tamanho)





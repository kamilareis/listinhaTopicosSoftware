'''Desenvolver o jogo https://term.ooo/ a partir do arquivo lista_palavras.txt. O jogo deve ser
jogado por meio do terminal, mantendo a lógica do jogo original. Devem aparecer as letras que
já foram descobertas, as letras já tentadas no teclado e assim por diante. Atente-se à
formatação.
'''

arquivo = "lista_palavras.txt"


def le_arquivo(arq):
    """ Lê arquivo especificado e retorna uma lista com todas as linhas """    
    with open(arq, encoding="UTF-8") as f:
        return [linha.strip() for linha in f] # método strip remove o '\n' do final da linha

def gera_lista_n_letras(lista, n):
    return [x for x in lista if len(x) == n]

def imprime_palavra_atual(palavra):
    for l in palavra:
        print(l,end=" ")
    print("")

lista = le_arquivo(arquivo)

print(lista)

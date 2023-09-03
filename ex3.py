'''Desenvolver o jogo https://term.ooo/ a partir do arquivo lista_palavras.txt. O jogo deve ser
jogado por meio do terminal, mantendo a lógica do jogo original. Devem aparecer as letras que
já foram descobertas, as letras já tentadas no teclado e assim por diante. Atente-se à
formatação.
'''
'''Um jogo inspirado no jogo termo, as regras são que tem 6 tentativas de erros para acertar as
letras da palavra sorteada. 
O jogo pede para o usuário o tamanho da palavra, após filtra as palavras pela quantidade de letras,
a partir disso é sorteada uma palavra, após o usuário tem 6 tentativas para acertar a palavra
inserindo uma letra por vez, imprime as letras restantes para palpites até acertar e se todas as
tentativas forem erradas o jogo encerra.'''

import random
import unicodedata

arquivo = "lista_palavras.txt"

#função que trata a acentuação do arquivo.
def remove_acentos(texto):
    return ''.join(ch for ch in unicodedata.normalize('NFKD', texto) if not unicodedata.combining(ch))

#função que trata o arquivo no formato UTF-8.
def le_arquivo(arq):
    """ Lê arquivo especificado e retorna uma lista com todas as linhas """    
    with open(arq, encoding="UTF-8") as f:
        return [linha.strip() for linha in f] 

#função que retorna o numero do comprimento das palvras do arquivo.
def gera_lista_n_letras(lista, n):
    return [x for x in lista if len(x) == n]

#função que iimprime cada letra separada da palvra do arquivo.
def imprime_palavra_atual(palavra):
    for l in palavra:
        print(l, end=" ")
    print("")

#recebe a leitura, processo das palavras, converte as palavras minusculas e usa a função para remover acentos. 
lista = le_arquivo(arquivo)
lista = [remove_acentos(palavra.lower()) for palavra in lista]

qtde = int(input("Escolha quantas letras a palavra tem: ")) #recebe um número inteiro do usuário. 
lista_n = gera_lista_n_letras(lista, qtde) #lista as palavras com o número de letras digitados.

palavra = list(random.choice(lista_n)) #a partir das palavras com o número de letras especiicado é sorteado uma delas e é convertido para uma lista de letras. 


vidas = 6 #tentivas que o jogador tem.
acertos = [] #lista vazia que vai armazernar as letras adivinhadas.
fim_do_jogo = False #define o final do jogo.

#lista de letras dispoiveis para palpites.
alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def jogo():
    erros = 0 #contador de erros.

    while (vidas > 0 and erros < vidas): # o loop ocorre até o número de vidas acabar. 

        tela = " "
        
        for letra in palavra: #percorre as letras para verificar se já foi adivinhada.
            if letra in acertos: #verifica se a letra esta na lista de acertos, se sim imprime e se não imprime vazio.
                tela += f"[{letra}]"
            else:
                tela += "[ ]"
        
        print(tela)
        print(" ")
        #lista as letras ainda disponiveis e pede o próximo palpite.
        print("Letras ainda disponíveis: ") 
        print(alfabeto)
        palpite = input("Escolha uma letra: ") 

        if palpite not in alfabeto: #verifica se a letra já foi.
            print("Essa letra já foi!")
            continue

        if palpite in palavra: #quando acerta a letra adiciona na lista acertos.
            print(f"Acertou a letra {palpite}") 
            acertos.append(palpite)
        else: #se não indica que erros e adiciona jogada no contador.
            print("Errou!")
            erros += 1

        alfabeto.remove(palpite) #remove a letra da lista de letras ainda disponiveis.

        if all(letra in acertos for letra in palavra): #verifica se todas as todos os palpites estão corretos e interrompe o loop, finalizando o jogo. 
            break  

    print("Jogo finalizado!")
    print(f"A palavra do dia é: {''.join(palavra)}, foram {erros} tentativas!")

jogo()

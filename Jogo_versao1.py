
##from thinter import *
##
##menu_inicial = Tk()
##menu_inicial.geometry(500x300)

print ('==' *15)
print('      Jogo da Forca    ')
print ('==' * 15)

import random

palavras = ['banana', 'manga', 'abacaxi', 'cachorro', 'gato','elefante', 'arroz',
            'massa', 'danoninho', 'leite',  'goiabada', 'docinho', 'sorvete', 'boneca', 'jipe']
def desenho(erro):
    if erro == 0:
        print()
        print("|----- ")
        print("|    | ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
        print()
    elif erro == 1:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
        print()
    elif erro == 2:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|    | ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
        print()
    elif  erro == 3:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /| ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
        print()
    elif erro == 4:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\ ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
        print()
    elif erro == 5:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\ ")
        print("|    | ")
        print("|      ")
        print("_      ")
        print()
        print()
    elif erro == 6:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\ ")
        print("|    | ")
        print("|   /  ")
        print("_      ")
        print()
        print()
    elif erro == 7:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\ ")
        print("|    | ")
        print("|   / \ ")
        print("_      ")
        print()
        print()

jogo = True
forca = True
indice_palavra = random.randint(0, len(palavras)-1)
palavra_sorteada = palavras[indice_palavra]
palavra = ['_'] * len(palavra_sorteada)

erro = 0

while jogo :
    desenho(erro)
    tentativa = []
    letra = input('Digite uma letra:  ')
    for i in range(len(palavra_sorteada)):
        if letra == palavra_sorteada[i]:
            palavra[i] = letra
    if ''.join(palavra) == palavra_sorteada:
        print()
        print(palavra_sorteada)
        print()
        print('Muito Bem! Você acertou')
        print()
        print('A palavra é {0} ' .format(palavra_sorteada))
        break

    else:
        print(' '.join(palavra))
    if letra not in(palavra):
        print('Nao há essa letra na palavra!')
        tentativa.append(letra)
        erro +=1
##    if letra in(tentativa):
##        print("Você já tentou com essa letra!")
        

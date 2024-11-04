# Faça um programa que grave uma lista com 15 posições, calcule e mostre:
# a) O maior elemento da lista e em que posição esse elemento se encontra;
# b) O menor elemento da lista e em que posição esse elemento se encontra.
from random import randint

#Função para gravar a lista
def gravarLista():
    maxList = 15
    lista = []
    for i in range(maxList):
        num = randint(1,100)
        lista.append(num)
    return lista

#Função para encontrar o maior elemento da lista e sua posição
def maior(lista):
    maiorNum = lista[0]

    for i in range(len(lista)):
        if lista[i] > maiorNum:
            maiorNum = lista[i]
    
    return f'\nMaior número: {maiorNum}\nPosição: {lista.index(maiorNum)}'

#Função para encontrar o menor elemento da lista e sua posição
def menor(lista):
    menorNum = lista[0]

    for i in range(len(lista)):
        if lista[i] < menorNum:
            menorNum = lista[i]
    
    return f'\nMenor número: {menorNum}\nPosição: {lista.index(menorNum)}'
    pass

#Função principal para executar o programa
def main():
    lista = gravarLista()
    print(f'Lista: {lista}')
    print(maior(lista))
    print(menor(lista))
if __name__ == '__main__':
    main()
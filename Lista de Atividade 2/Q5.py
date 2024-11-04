#Faça um programa que leia duas listas de 10 elementos numéricos cada um e intercale os
#elementos deste em uma outra lista de 20 elementos.

from random import randint

#Função para gravar a lista
def gravarLista():
    maxList = 10
    lista = []
    for i in range(maxList):
        num = randint(1,100)
        lista.append(num)
    return lista

#Função para intercalar as lista
def intercalar(lista1,lista2):
    listaResultado = []

    for i in range(len(lista1)):
        listaResultado.append(lista1[i])
        listaResultado.append(lista2[i])
    
    return listaResultado

#Função Principal
def main():
    lista1 = gravarLista()
    lista2 = gravarLista()
    print(f'Lista 1: {lista1}\nLista2: {lista2}')
    listaIntercalada = intercalar(lista1,lista2)
    print(f'Lista Intercalada: {listaIntercalada}')

if __name__ == '__main__':
    main()
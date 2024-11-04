# Ler uma lista X de 10 elementos inteiros e positivos. Criar uma lista Y da seguinte forma: os
# elementos de Y com índice par receberão os respectivos elementos de X divididos por 2; os
# elementos com índice ímpar receberão os respectivos elementos de X multiplicados por 3.
# Escrever as listas X e Y.
from random import randint

#Função para gravar a lista
def gravarLista():
    maxList = 10
    lista = []
    for i in range(maxList):
        num = randint(1,100)
        lista.append(num)
    return lista

#Função para gerar a nova lista
def novaLista(lista):
    listaNova = []

    for i in range(len(lista)):
        if i % 2 == 0:
            listaNova.append(lista[i] / 2)
        else:
            listaNova.append(lista[i] * 3)
    
    return listaNova

#Função Principal
def main():
    listaX = gravarLista()
    print(f'Lista X: {listaX}')
    listaY = novaLista(listaX)
    print(f'Nova Lista Y: {listaY}')
if __name__ == '__main__':
    main()
# Faça um programa que grave uma lista de 100 elementos numéricos inteiros e:
# a) Mostre a quantidade de números pares;
# b) Grave uma lista somente com os números pares e mostre a lista;
# c) Mostre a quantidade de números ímpares;
# d) Grave uma lista somente com os números ímpares e mostre a lista.

from random import randint

#Função para gravar uma lista somente com os números inteiros
def gravarLista():
    maxList = 100
    lista = []
    for i in range(maxList):
        num = randint(1, 100)
        lista.append(num)
    return lista


#Função para contar os números pares
def pares(lista):
    contador = 0
    for i in range(len(lista)):
        if lista[i]%2 == 0:
            contador += 1
    return contador

#Função para listar os números pares
def paresLista(lista):
    listaPar = []
    for i in range(len(lista)):
        if lista[i]%2 == 0:
            listaPar.append(lista[i])
    return listaPar

#Função para contar os números impares
def impares(lista):
    contador = 0
    for i in range(len(lista)):
        if lista[i]%2 != 0:
            contador += 1
    return contador
    
#Função para listar os números impares
def imparesLista(lista):
    listaImpar = []
    for i in range(len(lista)):
        if lista[i]%2 != 0:
            listaImpar.append(lista[i])
    return listaImpar

#Função Principal
def main():
    print('--------------------------------\n')
    lista = gravarLista()
    print(f'Lista\n{lista}\n')
    print(f'Quantidade de números Pares: {pares(lista)}\n')
    print(f'Números Pares: {paresLista(lista)}\n')
    print(f'Quantidade de números Ìmpares: {impares(lista)}\n')
    print(f'Números Ímpares: {imparesLista(lista)}\n')

if __name__ == '__main__':
    main()
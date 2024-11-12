# Escreva uma função `remover_duplicatas(lista)` que receba uma lista de números e retorne
# uma nova lista sem elementos duplicados. Por exemplo, dado `[1, 2, 3, 1, 4, 2]`, a função deve
# retornar `[1, 2, 3, 4]`.
from random import randint

#Função para gravar uma lista de números aleatorios
def gravarLista():
    maxList = 10
    lista = []
    for i in range(maxList):
        num = randint(-10, 10)
        lista.append(num)
    return lista

#Função para remover elementos duplicados de uma lista
def removerDuplicadas(lista):
    listaNova = []

    for num in lista:
        if lista.count(num) >= 1 or lista.count(num) <= 1:
            if num not in listaNova:
                listaNova.append(num)
    
    return listaNova

#Função Principal

def main():
    lista = gravarLista()
    print(f'Lista Original: {lista}')
    listaModificada = removerDuplicadas(lista)
    print(f'Nova Lista sem Duplicatas: {listaModificada}')

if __name__ == '__main__':
    main()

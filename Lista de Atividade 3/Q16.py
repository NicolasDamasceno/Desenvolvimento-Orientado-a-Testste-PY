# Escreva uma função `agrupa_por_paridade(lista)` que divida uma lista de números em duas
# listas: uma contendo os números pares e outra os ímpares, e retorne uma lista contendo ambas
# as listas.
# **Exemplo:** `lista = [1, 2, 3, 4, 5, 6]` -> `[[2, 4, 6], [1, 3, 5]]`

from random import randint

#Função para gravar uma lista aleatória
def gravarLista():
    maxList = 10
    lista = []
    for i in range(maxList):
        num = randint(0, 15)
        lista.append(num)
    return lista

#Função para agrupar os números por paridade
def agruparPorPariedade(lista):
    listaPar = []
    listaImpar = []

    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            listaPar.append(lista[i])
        else:
            listaImpar.append(lista[i])
    novaLista = [listaPar,listaImpar]
    return novaLista

#Função Principal
def main():
    lista = gravarLista()
    print(f'Lista Original: {lista}')
    listaAgrupada = agruparPorPariedade(lista)
    print(f'Listas Agrupadas: {listaAgrupada}')

if __name__ == '__main__':
    main()
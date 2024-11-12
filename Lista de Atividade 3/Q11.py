# Escreva uma função intercalar_listas(lista1, lista2) que receba duas listas de qualquer
# tamanho e retorne uma nova lista contendo os elementos intercalados de ambas. Se uma lista
# for maior, adicione os elementos restantes ao final da nova lista.
# **Exemplo:** `lista1 = [1, 3, 5]`, `lista2 = [2, 4, 6, 8, 10]` -> `[1, 2, 3, 4, 5, 6, 8, 10]`

from random import randint

#Função para gravar uma lista aleatoria
def gravarLista(maxList):
    lista = []
    for i in range(maxList):
        num = randint(1, 100)
        lista.append(num)
    return lista

#Função	para gerar uma lista intercalada
def intercalarListas(lista1, lista2):
    novaLista = []
    if len(lista1) == len(lista2):
        for i in range(len(lista1)):
            novaLista.append(lista1[i])
            novaLista.append(lista2[i])
    elif len(lista1) > len(lista2):
        for i in range(len(lista2)):
            novaLista.append(lista1[i])
            novaLista.append(lista2[i])
        for i in range(len(lista2), len(lista1)):
            novaLista.append(lista1[i])
    else:
        for i in range(len(lista1)):
            novaLista.append(lista1[i])
            novaLista.append(lista2[i])
        for i in range(len(lista1), len(lista2)):
            novaLista.append(lista2[i])
    return novaLista

#Função Principal
def main():
    lista1 = gravarLista(5)
    lista2 = gravarLista(7)
    print(f'Lista 1: {lista1}')
    print(f'Lista 2: {lista2}')
    listaIntercalada = intercalarListas(lista1, lista2)
    print(f'Nova lista intercalada: {listaIntercalada}')
if __name__ == '__main__':
    main()
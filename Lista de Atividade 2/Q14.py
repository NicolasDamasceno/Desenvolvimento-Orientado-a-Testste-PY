# Ler uma lista C de 10 elementos inteiros, trocar todos os valores negativos da lista C por 0.
# Escrever a lista C modificada.
from random import randint

# Função para gravar a lista C
def gravarLista():
    maxList = 10
    lista = []
    for i in range(maxList):
        num = randint(-100, 100)
        lista.append(num)
    return lista

#Função para modificar a lista C e trocar os números negativos
def modificarLista(lista):
    listaModificada = []

    for i in range(len(lista)):
        if lista[i] < 0:
            listaModificada.append(0)
        else:
            listaModificada.append(lista[i])

    return listaModificada

#Função Principal
def main():
    lista = gravarLista()
    print(f'Lista Original: {lista}')
    listaModificada = modificarLista(lista)
    print(f'Lista Modificada: {listaModificada}')

if __name__ == '__main__':
    main()
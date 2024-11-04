# Ler uma lista X de 10 elementos. A seguir copiar todos os valores negativos da lista X para
# uma lista R, sem deixar elementos vazios entre os valores copiados. Escrever as listas X e R.

from random import randint

#Função para gravar lista com valores positivos e negativos
def gravarLista():
    maxList = 10
    lista =[]
    for i in range(maxList):
        num = randint(-10,10)
        lista.append(num)
    return lista

#Função para copiar valores negativos para uma nova lista
def novaLista(lista):
    listaNegativa = []
    for i in range(len(lista)):
        if lista[i] < 0:
            listaNegativa.append(lista[i])
    return listaNegativa


#Função Principal
def main():
    listaX = gravarLista()
    print(f'Lista Original: {listaX}')

    listaR = novaLista(listaX)
    print(f'Nova Lista Negativa: {listaR}')

if __name__ == '__main__':
    main()
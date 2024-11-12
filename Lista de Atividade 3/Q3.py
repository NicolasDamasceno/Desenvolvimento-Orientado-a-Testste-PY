# Escreva um programa que receba uma lista de números e retorne outra lista com os números
# elevados ao quadrado. Por exemplo, dado `[2, 3, 4]`, o código deve retornar `[4, 9, 16]`.
from random import randint

#Função para gerar lista númerica
def gerarLista():
    maxList = 6
    lista = []
    for i in range(maxList):
        num = randint(0,10)
        lista.append(num)
    return lista

#Função paa gerar uma lista ao quadrado de uma lista posterior
def gerarListaQuadrada(lista):
    listaQuadrada = []
    for num in lista:
        listaQuadrada.append(num**2)
    return listaQuadrada

#Função principal
def main():
    lista = gerarLista()
    print(f'Lista: {lista}')
    listaQuadrada = gerarListaQuadrada(lista)
    print(f'Lista elevada ao quadrado: {listaQuadrada}')
if __name__ == '__main__':
    main()
    
    

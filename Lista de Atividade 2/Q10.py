# vFaça um programa que grave uma lista com 15 posições, calcule e mostre:
# a) O maior elemento da lista e em que posição esse elemento se encontra;
# b) O menor elemento da lista e em que posição esse elemento se encontra.

from random import randint

#Função para gravar a lista

def gravar_lista():
    max_list = 15
    lista = []
    for i in range(max_list):
        num = randint(1,100)
        lista.append(num)
    
    return lista 

# Função para encontrar o maior elemento da lista e sua posição
def maior(lista):
    maiorNum = lista[0]
    maiorPos = 0
    for i in range(len(lista)):
        if lista[i] > maiorNum:
            maiorNum = lista[i]
            maiorPos = i 
    
    return f'Maior Número da lista: {maiorNum}\nPosição: {maiorPos}'

# Função para encontrar o menor elemento da lista e sua posição
def menor(lista):
    menorNum = lista[0]
    menorPos = 0
    for i in range(len(lista)):
        if lista[i] < menorNum:
            menorNum = lista[i]
            menorPos = i 
    
    return f'Menor Número da lista: {menorNum}\nPosição: {menorPos}'

#Função principal para executar o programa
def main():
    lista = gravar_lista()
    print(f'Lista Gerada: {lista}\n')
    print(maior(lista))
    print(menor(lista))

if __name__ == '__main__':
    main()
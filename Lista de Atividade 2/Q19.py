# Ler duas listas: R de 5 elementos e S de 10 elementos. Gerar uma lista X de 15 elementos
# cujas 5 primeiras posições contenham os elementos de R e as 10 últimas posições, os elementos
# de S. Escrever a lista X.
from random import randint

#Função para gravar a lista R
def gravarR():
    maxList = 5
    lista =[]
    for i in range(maxList):
        num = randint(0,10)
        lista.append(num)
    return lista

#Função para gravar a lista S
def gravarS():
    maxList = 10
    lista =[]
    for i in range(maxList):
        num = randint(0,20)
        lista.append(num)
    return lista

#Função para intercalar as listas R e S
def intercalar(listaR, listaS):
    listaX = listaR[:5] + listaS[-10:]
    return listaX

#Função principal
def main():
    listaR = gravarR()
    print(f'Lista R: {listaR}')
    listaS = gravarS()
    print(f'Lista S: {listaS}')
    listaX = intercalar(listaR, listaS)
    print(f'Lista X: {listaX}')
if __name__ == "__main__":
    main()
#Ler uma lista D de 10 elementos. Criar uma lista E, com todos os elementos de D na ordem
#inversa, ou seja, o último elemento passará a ser o primeiro, o penúltimo será o segundo e assim
#por diante. Escrever todo a lista D e todo a lista E.
from random import randint

#Função para gravar a lista com 10 números
def gravarLista():
    maxList = 10
    lista = []
    for i in range(maxList):
        num = randint(1, 100)
        lista.append(num)
    return lista

#Função para gravar a lista com elementos invertidos
def inverter(lista):

    listaInvertida = []

    for i in range(len(lista)):
        listaInvertida.insert(0, lista[i])

    return listaInvertida  

#Função Principal  
def main():
    lista = gravarLista()
    print(f'Lista D: {lista}')
    listaInvertida = inverter(lista)
    print(f'Lista E: {listaInvertida}')
if __name__ == '__main__':
    main()
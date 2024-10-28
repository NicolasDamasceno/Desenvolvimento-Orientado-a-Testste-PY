#Faça um programa que dada uma seqüência de n números, imprimi-la na ordem inversa à da
#leitura.
from random import randint
#Função para inveter os números da lista
def inveterLista(lista):
    listaInversa = []
    for i in range(len(lista)):
        listaInversa.insert(0,lista[i])
    return listaInversa

#Função para gravar a lista com N números
def gravarLista(n):
    lista = []
    for i in range(n):
        num = randint(1, n)
        lista.append(num)
    return lista

#Função Principal
def main():
    try:
        n = int(input('Digite uma quantidade inteira de números que serão gravados: '))
        lista = gravarLista(n)
        print(f'Lista Gerada: {lista}')
        print(f'Lista Inversa: {inveterLista(lista)}')
    except ValueError:
        print('Por favor, insira um número inteiro.')

if __name__=='__main__':
    main()
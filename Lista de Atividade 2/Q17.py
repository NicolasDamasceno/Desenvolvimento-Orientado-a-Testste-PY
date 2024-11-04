# Ler uma lista W de 10 elementos, depois ler um valor V. Contar e escrever quantas vezes o
# valor V ocorre na lista W e escrever também em que posições (índices) da lista W o valor V
# aparece.
# Caso o valor V não ocorra nenhuma vez na lista W, escrever uma mensagem informando isto.
from random import randint

#Função para gravar a nossa lista W
def gravarLista():
    maxList = 10
    lista =[]
    for i in range(maxList):
        num = randint(1,30)
        lista.append(num)
    return lista

#Função para verificar a ocorrência do valor V na lista W
def verificarLista(lista, num):
    contador = 0
    posicoes = []
    for i in range(len(lista)):
        if lista[i] == num:
            contador += 1
            posicoes.append(i)

    if contador == 0:
        print(f'O número {num} não ocorre na lista W.')

    else:
        print(f'O número {num} ocorre {contador} vezes na lista W.')
        print(f'Ele aparece nas posições: {posicoes}')

#Função principal
def main():
    listaW = gravarLista()
    try:
        num = int(input('Digite um número para ver quantas vezes elke aparece na lista W: '))
        verificarLista(listaW, num)
        print(f'Lista W: {listaW}')
    except ValueError:
        print('Por favor, digite um número inteiro.')
        return

if __name__ == '__main__':
    main()
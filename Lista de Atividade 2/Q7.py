#Dada uma lista contendo 10 elementos numéricos, elabore um programa que verifique se um
#outro valor dado pertence ou não à lista.
from random import randint

#Função para gravar a lista
def gravarLista():
    maxList = 10
    lista = []
    for i in range(maxList):
        num = randint(1,30)
        lista.append(num)

    return lista

#Função Principal
def main():
    while True:
        lista = gravarLista()
        try:
            print('Digite 0 para finalizar o programa')
            num = int(input('Digite um número para verificar se ele pertence a lista: '))
            if num in lista:
                print(f'O número {num} está na lista!\n')
            elif num == 0:
                print('\nPrograma finalizado')
                break
            else:
                print('Esse número não está na lista.\n')
        except ValueError:
            print('Caractere inválido!')

if __name__ == '__main__':
    main()
# Dada uma lista X numérica contendo 5 elementos, fazer um programa que crie e exiba na tela
# uma lista Y. A lista Y deverá conter o mesmo conteúdo da lista X na ordem inversa.


def inverter(listaOriginal):
    listaInvertida = []
    for i in range(len(listaOriginal)):
        listaInvertida.insert(0, listaOriginal[i])
    
    return listaInvertida

#Função Principal
def main():

    try:
        lista =  []
        for i in range(5):
            numero = float(input(f'{i+1} - Digite uma série de 5 números qualquer: '))
            lista.append(numero)
        
        print(f'\nLista orignal: {lista}')
        print(f'Lista invertida: {inverter(lista)}')

    except ValueError:
        print('Por favor, insira um número real.')

if __name__ == '__main__':
    main()
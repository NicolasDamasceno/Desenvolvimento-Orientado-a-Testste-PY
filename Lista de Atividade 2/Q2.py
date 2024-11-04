# Faça um programa que grave uma lista com dez números reais, calcule e mostre a quantidade
# de números negativos e a soma dos números positivos dessa lista.

#Função para mostrar a quantidade de números negativos
def negativos(lista):
    listaNegativos = []
    for i in range(len(lista)):
        if lista[i] < 0:
            listaNegativos.append(lista[i])
    return listaNegativos

#Função para calcular a soma dos números positivos
def somaPositivos(lista):
    soma = 0
    for i in range(len(lista)):
        if lista[i] > 0:
            soma += lista[i]
    return soma
#Função Principal
def main():
    try:
        lista = []
        for i in range(10):
            numero = float(input(f'Digite o {i+1}º número real: '))
            lista.append(numero)
        print(f'\nLista com os números negativos: {negativos(lista)}')
        print(f'Soma dos números positivos: {somaPositivos(lista)}')
    except ValueError:
        print('Por favor, insira um número real.')
        return
if __name__ == '__main__':
    main()
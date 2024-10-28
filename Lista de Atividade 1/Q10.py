# Escreva um programa composto de uma função Max e o programa principal como segue:
# a) A função Max recebe como parâmetros de entrada dois números inteiros e retorna o maior. Se forem iguais retorna qualquer um
# deles;
# b) O programa principal lê 4 séries de 4 números a, b. Para cada série lida imprime o maior dos quatro números usando a função
# Max

# Funçao Máxima
def maxima(lista_numeros):
    maior = lista_numeros[0]  # Começamos assumindo que o primeiro elemento é o maior
    for numero in lista_numeros:
        if numero > maior:    # Se encontramos um número maior, atualizamos a variável
            maior = numero
    return maior

#Função Principal
def main():
    try:
        serieMaior = []
        for i in range(4):
            a = int(input(f'Digite o primeiro número da série {i+1}: '))
            b = int(input(f'Digite o segundo número da série {i+1}: '))
            c = int(input(f'Digite o terceiro número da série {i+1}: '))
            d = int(input(f'Digite o quarto número da série {i+1}: '))

            maior = maxima([a,b,c,d])
            serieMaior.append(maior)
            print(f'O maior número da série {i+1} é {maior}')
        print(f'O maior número das séries é: {maxima(serieMaior)}')
    except ValueError:
        print('Você digitou um valor inválido. Por favor, digite um número inteiro.')

if __name__ == "__main__":
    main()
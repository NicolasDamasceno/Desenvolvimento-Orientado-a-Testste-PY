# Escreva uma função que recebe 2 números inteiros n1 e n2 como entrada e retorna a soma de todos os números inteiros contidos
# no intervalo [n1,n2]. Use esta função em um programa que lê n1 e n2 do usuário e imprime a soma

#Função para calcular a soma do intervalo [n1,n2]
def intervalo(n1,n2):
    soma = 0
    for i in range(n1,n2+1):
        soma += i
    return soma

#Função Principal
def main():
    try:
        n1 = int(input('Digite o primeiro número do intervalo: '))

        n2 = int(input('Digite o segundo número do intervalo: '))

        print(f'A soma dos números inteiros no intervalo [{n1}, {n2}] é: {intervalo(n1, n2)}')
    except ValueError:
        print('Por favor, digite apenas números inteiros.')
if __name__ == '__main__':
    main()
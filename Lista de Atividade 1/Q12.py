#Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o somatório desse valor

#Função para calcular o somatorio do número
def somatorio(num):
    soma = 0
    for i in range(1, num+1):
        soma += i
    return soma

#Funçaõ Principal
def main():
    try:
        num = int(input('Digite um número inteiro: '))

        print(f'O somatório de 1 a {num} é {somatorio(num)}')
    except ValueError:
        print('Por favor, digite um número inteiro.')
if __name__ == '__main__':
    main()
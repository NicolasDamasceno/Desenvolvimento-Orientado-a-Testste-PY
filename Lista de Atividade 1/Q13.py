# Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
# S = 1 + ½ + 1/3 + ¼ + 1/5 + 1/N.

#Função para calcluar o somatório
def somatorio(num):
    soma = 0
    for i in range(1, num+1):
        soma += 1/i
    return soma

#Função Principal
def main():
    try:
        numero = int(input('Digite um número inteiro: '))

        print(f'O valor de S é: {somatorio(numero):.2f}')
    except ValueError:
        print('O valor digitado não é um número inteiro.')

if __name__ == '__main__':
    main()
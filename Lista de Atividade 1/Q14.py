# Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
# S = 1 + 1/1! + ½! + 1/3! + 1 /N!

#Função para calcular o Somatório
def somatorio(num):
    soma = 1
    fatorial = 1
    for i in range(1, num+1):
        fatorial *= i
        soma += 1/fatorial
    return soma

#Função Principal
def main():
    try:
        numero = int(input('Digite um número inteiro: '))

        print(f'O valor S é: {somatorio(numero):0.2f}')
    except ValueError:
        print('Por favor, insira um número inteiro.')
if __name__ == '__main__':
    main()
# Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
# S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(t^2+1)/(t+3)

#Função para calcular o Somatório
def somatorio(num):
    soma = 0
    for i in range(1, num+1):
        soma += (i**2 + 1) / (i + 3)
    return soma

#Função Principal
def main():
    numero = int(input('Digite um número interio: '))

    print(f'O valor de S é {somatorio(numero):0.2f}')
if __name__ == '__main__':
    main()
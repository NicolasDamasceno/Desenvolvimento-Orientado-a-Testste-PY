# Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor.+

#Função para calcular o número de divisores do valor passado
def divisores(num):
    quantidade = 0
    for i in range(1, num + 1):
        if num % i == 0:
            quantidade += 1
    return quantidade

#Função Principal
def main():
    try:
        num = int(input('Digite um número inteiro: '))

        print(f'O número {num} possui {divisores(num)} divisores.')
    except ValueError:
        print('Por favor, digite um número inteiro.')
if __name__=='__main__':
    main()
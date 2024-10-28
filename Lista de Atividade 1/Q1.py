#Faça uma função que recebe um número inteiro por parâmetro e retorna verdadeiro se ele for par e falso se for ímpar.
#Função para validar número
def validar(num):
    if num % 2 == 0:
        return print('Par')
    else:
         return print('Ímpar')

#Função principal
def main():
    try:
        num = int(input('Digite um número inteiro para saber se ele é par ou ímpar: '))
        validar(num)
    except ValueError:
        print('Digite um número inteiro válido.')

if __name__ == '__main__':
    main()
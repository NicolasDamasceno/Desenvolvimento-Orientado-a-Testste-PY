#Escreva um programa que leia o raio de um círculo e faça duas funções: uma função chamada área que calcula e retorna a área do círculo e outra função chamada perímetro que calcula e retorna o perímetro do círculo.
# Área = PI * r2; Perímetro = PI * 2 * r;

#Função para calclar a área do círculo
def area(raio):
    a = (3,14 * raio**2)
    return f'Área: {a:0.2f}'

#Função para calcular o perímetro do círculo
def perimetro(raio):
    p = (3,14 * 2 * raio)
    return f'Perímetro: {p:0.2f}'

#Função principal
def main():
    try: 
        raio = int(input('Digite o raio de um círculo para calcular a sua área e perímetro: '))

        print(area(raio))
        print(perimetro(raio))
    except ValueError:
        print('Digite um inteiro válido.')
if __name__ == '__main__':
    main()
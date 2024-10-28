# Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Faça um procedimento
# que receba como parâmetro o número de lados e a medida do lado deste polígono e calcule e imprima o seguinte:
# - Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu perímetro.
# - Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
# - Se o número de lados for igual a 5, escrever PENTÁGONO.

#Função para calcular o perímetro do triângulo
def perimetro_triangulo(lado):
    perimetro = 3 * lado
    return f'Perímetro do triângulo: {perimetro}'

#Função para calcular a área do quadrado
def area_quadrado(lado):
    area = lado ** 2
    return f'Área do quadrado: {area}'

#Função para escrever o nome do polígono Pentágulo
def pentagono():
    return f'PENTÁGONO'

#Função Principal
def main():
    try:
        lado = int(input('Digite uma quantidade de lado: '))

        if lado == 3:
            print(perimetro_triangulo(lado))

        elif lado == 4:
            print(area_quadrado(lado))

        elif lado == 5:
            print(pentagono())
    except ValueError:
        print('Por favor, digite um número inteiro.')

#Escreva um programa para ler uma temperatura em graus Fahrenheit. Faça uma função chamada celsius para calcular e retornar o valor correspondente em graus Celsius.
#Fórmula: C = ((F-32)/9)*5

#Função para calcular a transformação de Fahrenheit para Celsius
def celsius(fahrenheit):
    celsius = ((fahrenheit - 32) / 9) * 5
    return f'Celsius: {celsius:0.2f} Celsius'

#Função Principal:
def main():
    try:
        fahrenheit = float(input('Digite a temperatura em graus Fahrenheit: '))

        print(celsius(fahrenheit))
    
    except ValueError:
        print('Digite um caractere válido.')

if __name__ == '__main__':
    main()
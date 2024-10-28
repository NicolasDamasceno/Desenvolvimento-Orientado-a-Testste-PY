# Faça um programa para calcular o Fatorial de um número. Para o cálculo do fatorial, sabemos que N! depende de (N-1)!; este por
# sua vez depende de (N-2)!; e, assim por diante, até que N seja 1, quando então tem-se que fatorial de 1 é igual a 1 mesmo. Utilize
# uma função que recebe como parâmetro de entrada o número a ser calculado o fatorial, do tipo inteiro, e retorna o fatorial deste
# número, também do tipo inteiro. 

# Função para calcular o fatorial de um número
def fatorial(num):
    if num == 1:
        return 1
    else:
        return num * fatorial(num - 1)  # Recursão para calcular o fatorial

#Função Principal
def main():
    try:
        numero = int(input('Digite o número a ser fatorado: '))
        print(f'O fatorial de {numero} é {fatorial(numero)}')
    except ValueError:
        print('Entrada inválida. Digite um número inteiro.')

if __name__ == '__main__':
    main()
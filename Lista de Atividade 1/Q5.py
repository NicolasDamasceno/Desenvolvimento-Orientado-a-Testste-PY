# Faça um programa que leia a altura e o sexo (codificado da seguinte forma:
# 1:feminino 2:masculino) de uma pessoa. Depois faça uma função chamada peso ideal que receba a altura e o sexo via parâmetro e
# que calcule e retorne seu peso ideal, utilizando as seguintes fórmulas:
# - para homens : (72.7 * h) – 58
# - para mulheres : (62.1 * h) – 44.7
#  Observação: Altura = h (na fórmula acima)

#Função para calcular o peso ideal
def peso_ideal(altura, tipo):
    if tipo == 1:
        peso = (72.7 * altura) - 58
        return f'O peso ideal é {peso:0.2f}KG'
    elif tipo == 2:
        peso = (62.1 * altura) - 44.7
        return f'O peso ideal é {peso:0.2f}KG'

#Função Principal
def main(): 
    try:
        altura = float(input('Digite a altura: '))
            
        tipo = int(input('Digite o tipo (1:feminino 2:masculino): '))

        print(peso_ideal(altura, tipo))
    except ValueError:
        print('Valor inválido. Insira um número.')
if __name__ == '__main__':
    main()
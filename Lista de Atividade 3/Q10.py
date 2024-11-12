# Crie uma lista `notas = [7.5, 8.0, 9.0, 4.5, 6.0, 10.0, 5.0]` e escreva um programa que
# identifique a nota mais alta e a nota mais baixa da lista sem usar as funções `max` e `min`.
# Exiba ambas ao final.

#Função para indetificar a maior nota
def maiorNota(notas):
    maior = notas[0]
    for i in range(len(notas)):
        if notas[i] > maior:
            maior = notas[i]
    
    return maior

#Função para identificar a menor nota
def menorNota(notas):
    menor = notas[0]
    for i in range(len(notas)):
        if notas[i] < menor:
            menor = notas[i]
    
    return menor

#Função Principal
def main():
    notas = [7.5, 8.0, 9.0, 4.5, 6.0, 10.0, 5.0]
    print(f'Notas da lista: {notas}')
    print(f'Nota mais alta: {maiorNota(notas)}')
    print(f'Nota mais baixa: {menorNota(notas)}')

if __name__ == '__main__':
    main()

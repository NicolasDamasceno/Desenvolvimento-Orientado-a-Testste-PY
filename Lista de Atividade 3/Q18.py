# Crie uma função `menor_maior_diferenca(lista)` que receba uma lista de números e retorne a
# diferença entre o maior e o menor número da lista sem usar as funções `max` e `min`.

from random import randint

#Função para gravar uma lista aleatória
def gravarLista():
    maxList = 5
    lista = []
    for i in range(maxList):
        num = randint(0, 15)
        lista.append(num)
    return lista

#Função para encontrar o maior e o menor número da lista e fazer a diferança
def encontrarDiferancao(lista):
    maior = lista[0]
    menor = lista[0]

    for num in lista:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    
    return maior - menor

#Função Principal
def main():
    lista = gravarLista()
    print(f'Lista Original: {lista}')
    print(f'Diferença entre o maior e o menor número: {encontrarDiferancao(lista)}')

if __name__ == '__main__':
    main()
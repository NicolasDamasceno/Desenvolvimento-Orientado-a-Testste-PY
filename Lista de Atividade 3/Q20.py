# Escreva uma função que receba uma lista de números e retorne uma nova lista onde cada
# elemento é o produto de todos os outros números na lista, exceto ele mesmo (sem usar divisão).
# **Exemplo:** Para `[1, 2, 3, 4]`, a função deve retornar `[24, 12, 8, 6]`.

from random import randint

#Função para gravar uma lista aleatória
def gravarLista():
    maxList = 4
    lista = []
    for i in range(maxList):
        num = randint(1, 10)
        lista.append(num)
    return lista

#Função para calcular o produto de todos os outros elementos
def calcularProduto(lista):
    novaLista = []

    for i in range(len(lista)):
        produto = 1
        for j in range(len(lista)):
            if i!= j:
                produto *= lista[j]
        novaLista.append(produto)
    return novaLista

#Função Principal
def main():
    lista = gravarLista()
    print(f'Original Lista: {lista}')
    produto = calcularProduto(lista)
    print(f'Nova Lista: {produto}')
if __name__ == '__main__':
    main()
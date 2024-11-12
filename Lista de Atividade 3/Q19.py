# Dada uma lista de números, escreva um programa que retorne todos os pares de elementos que
# somam um valor específico `k`.
# **Exemplo:** Para `lista = [1, 2, 3, 4, 5]` e `k = 6`, o programa deve retornar `[(1, 5), (2, 4)]`.

from random import randint

#Função para gravar uma lista aleatória
def gravarLista():
    maxList = 8
    lista = []
    for i in range(maxList):
        num = randint(0, 15)
        lista.append(num)
    return lista

#Função para encontrar os pares de elementos que somam um valor específico k
def paresK(lista,k):
    novaLista = []

    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i] + lista[j] == k:
                novaLista.append((lista[i], lista[j]))

    return novaLista

#Função Principal
def main():
    lista = gravarLista()
    k = randint(1,6)
    print(f'Lista: {lista}')
    print(f'Valor de k: {k}')
    pares = paresK(lista, k)
    print(f'Pares de elementos que somam {k}: {pares}')
if __name__ == '__main__':
    main()
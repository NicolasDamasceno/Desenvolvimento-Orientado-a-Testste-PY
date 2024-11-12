# Escreva uma função `rotacionar_lista(lista, n)` que rotacione os elementos de uma lista `n`
# vezes para a direita.
# **Exemplo:** `rotacionar_lista([1, 2, 3, 4, 5], 2)` -> `[4, 5, 1, 2, 3]`

from random import randint

#Função para rotacionar a lista para a direita
def rotacionarLista(lista, n):
    n = n % len(lista)
    return lista[-n:] + lista[:-n]

#Gerando lista aleatória
def gravarLista():
    maxList = 5
    lista = []
    for i in range(maxList):
        num = randint(1, 100)
        lista.append(num)
    return lista

#Função Principal
def main():
    lista = gravarLista()
    rotacao = randint(1, 5)
    print(f"Antes da rotação: {lista}")
    print(f"Rotacionando {rotacao} vezes")
    print(f"Depois da rotação: {rotacionarLista(lista, rotacao)}")

if __name__ == "__main__":
    main()

# Crie uma função que receba uma lista de números e retorne uma nova lista contendo apenas
# os números que são a soma de dois outros números distintos na mesma lista.
# **Exemplo:** `lista = [3, 5, 7, 10, 15]` -> `[10, 15]` (pois 10 = 3 + 7 e 15 = 5 + 10)

from random import randint

# Função para gravar uma lista aleatória
def gravarLista():
    maxList = 5
    lista = []
    for i in range(maxList):
        num = randint(1, 100)
        lista.append(num)
    return lista

#Função para gravar uma lista sendo seus elementos a soma de dois números distintos
def listaSomaDistintos(lista):
    novaLista = []
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] + lista[j] not in novaLista:
                novaLista.append(lista[i] + lista[j])
    
    return novaLista

# Função principal
def main():
    lista = gravarLista()
    print(f'Lista Original: {lista}')
    listaSoma = listaSomaDistintos(lista)
    print(f'Nova Lista: {listaSoma}')

if __name__ == '__main__':
    main()

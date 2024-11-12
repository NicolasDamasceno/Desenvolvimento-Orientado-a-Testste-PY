# Crie uma lista `idades` com as idades de 10 pessoas. Escreva um código que divida essa lista
# em duas listas: uma com idades menores que 18 anos e outra com idades maiores ou iguais a
# 18 anos.
from random import randint
#Função para gerar a lista com as idades
def gerarLista():
    maxList = 10
    lista = []
    for i in range(maxList):
        num = randint(1,80)
        lista.append(num)
    return lista

def main():
    idades = gerarLista()
    print(f'Idades: {idades}')
if __name__ == "__main__":
    main()
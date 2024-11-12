# Crie uma lista com números inteiros de 1 a 10. Em seguida, use um loop para encontrar a soma
# de todos os números pares dessa lista.

#Função para criar a lista de números 10
def criarLista():
    return list(range(1, 11))

#Função para retornar a soma dos números pares
def somaPar(lista):
    contador = 0
    for num in range(len(lista)):
        if (lista[num] % 2) == 0:
            contador += lista[num]
    return contador
    
#Função Principal
def main():
    lista = criarLista()
    print(f'Lista: {lista}')
    soma = somaPar(lista)
    print(f'Soma dos números pares: {soma}')
    
if __name__ == '__main__':
    main()
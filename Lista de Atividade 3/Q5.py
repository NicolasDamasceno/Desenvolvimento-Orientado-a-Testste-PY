# Dada uma lista de números inteiros `numeros = [3, 6, 9, 12, 15, 18]`, escreva um código para
# encontrar e remover o maior número da lista sem usar a função `max`.

#Função para achar o maior número da lista sem usar a função Max
def maiorNum(lista):
    num = 0

    for i in range(len(lista)):
        if lista[i] > num:
            num = lista[i]
    
    return num

#Função Principal
def main():
    lista = [3, 6, 9, 12, 15, 18]
    print(f'Lista: {lista}')
    maior = maiorNum(lista)
    print(f'Maior número da lista: {maior}')

if __name__ == '__main__':
    main()
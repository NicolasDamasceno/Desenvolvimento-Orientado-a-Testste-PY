# Escreva um programa que receba duas listas de números de mesmo tamanho e retorne uma
# nova lista onde cada elemento é a soma dos elementos nas mesmas posições nas listas originais.
# Exemplo: se `lista1 = [1, 2, 3]` e `lista2 = [4, 5, 6]`, o código deve retornar `[5, 7, 9]`.

#Função para gravar a lista 3 como soma das lista 1 e lista 2
def gravarLista(lista1, lista2):
    lista3 = []
    if len(lista1) == len(lista2):
        for i in range(len(lista1)):
            lista3.append(lista1[i] + lista2[i])
        return lista3
    else:
        return False

#Função Principal
def main():
    lista1 = [1, 2, 3]
    lista2 = [4, 5, 6]
    novaLista = gravarLista(lista1, lista2)
    if novaLista:
        print(f'Lista 1: {lista1}')
        print(f'Lista 2: {lista2}')
        print(f'Nova lista: {novaLista}')
    else:
        print('As listas devem ter o mesmo tamanho.')
if __name__ == '__main__':
    main()
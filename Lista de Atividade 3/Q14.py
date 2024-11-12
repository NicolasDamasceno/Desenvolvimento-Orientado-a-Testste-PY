# Escreva um programa que receba uma lista de listas (matriz) e calcule a soma de todos os
# elementos em cada linha, retornando uma nova lista com essas somas.
# **Exemplo:** `matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]` -> `[6, 15, 24]`

#Função para criar a lista a partir de uma matriz, lista de listas
def listaMatiz(matriz):
    lista = []
    for i in range(len(matriz)):
        soma = 0
        for j in range(len(matriz[i])):
            soma += matriz[i][j]
        lista.append(soma)
    return lista


#Função Principal
def main():
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f'Matriz: {matriz}')
    listaSoma = listaMatiz(matriz)
    print(f'Soma de cada linha: {listaSoma}')

if __name__ == '__main__':
    main()
# Escreva um programa que, dada uma lista de listas (matriz), retorne outra matriz que seja a
# transposta da original.
# **Exemplo:** `matriz = [[1, 2, 3], [4, 5, 6]]` -> `[[1, 4], [2, 5], [3, 6]]`

#Função para transpor a matriz
def transporMatriz(matriz):
    transposta = []
    for coluna in range(len(matriz[0])):
        transpostaColuna = []
        for linha in range(len(matriz)):
            transpostaColuna.append(matriz[linha][coluna])
        transposta.append(transpostaColuna)
    return transposta

#Função Principal
def main():
    matriz = [[1, 2, 3], [4, 5, 6]]
    print(f'Matriz original: {matriz}')
    transposta = transporMatriz(matriz)
    print(f'Matriz transposta: {transposta}')

if __name__ == '__main__':
    main()
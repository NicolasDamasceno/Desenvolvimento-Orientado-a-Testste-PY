# Faça uma função que lê 50 valores inteiros e retorna o maior e o menor deles.

def maximoMinimo(numeros):
    if type(numeros) != list or len(numeros) != 50:
        return Exception
    for numero in numeros:
        if type(numero) != int:
            return Exception
    
    maiorNum = menorNum = 0
    for numero in numeros:
        if numero > maiorNum:
            maiorNum = numero
        if numero < menorNum:
            menorNum = numero

    return [maiorNum, menorNum]

# Valores Inválidos
assert maximoMinimo([-45, 12, -7, 25, -19, 33, -2, 8, -50, 14, 27, -36, 9, -11, 4, -18, 21, -3, 0, 42, -23, 6, -8, 37, -30, 16, -4, 29, -41, 5, -22, 48, -12, 18, -6, 31, -35, 2, -9, 15]) == Exception
assert maximoMinimo([-45, 12, -7, 25, 'TDs', 33, -2, 8, -50, 14, 27, -36, 9, -11, 4, -18, 21, -3, 0, 42, -23, 6, -8, 37, -30, 16, -4, 29, -41, 5, -22, 48, -12, 18, -6, 31, -35, 2, -9, 15, -13, 20, -40, 7, -1, 22, -28, 10, -32, 39]) == Exception
assert maximoMinimo([-45, 12, -7, 25.5, -19, 33, -2, 8, -50, 14, 27, -36, 9, -11, 4, -18, 21, -3, 0, 42, -23, 6, -8, 37, -30, 16, -4, 29, -41, 5, -22, 48, -12, 18, -6, 31, -35, 2, -9, 15, -13, 20, -40, 7, -1, 22, -28, 10, -32, 39]) == Exception

# Valores válidos
assert maximoMinimo([-45, 12, -7, 25, -19, 33, -2, 8, -50, 14, 27, -36, 9, -11, 4, -18, 21, -3, 0, 42, -23, 6, -8, 37, -30, 16, -4, 29, -41, 5, -22, 48, -12, 18, -6, 31, -35, 2, -9, 15, -13, 20, -40, 7, -1, 22, -28, 10, -32, 39]) == [48, -50]

print('Gotcha! Testes okay')
# Escreva uma função que recebe uma lista com n números inteiros, e determina a
# maior soma dos números que se repetem da lista. Ex: [5, -2, -2, 5, 3, 5, 10, -2, 3,
# 10, 3, 1] = 20

def somaRepitidos(lista):
    if type(lista) != list or len(lista) == 0:
        return Exception
    
    for num in lista:
        if type(num) != int:
            return Exception
    
    somaAtual = 0
    maiorSoma = 0

    for i in lista:
        somaAtual = i * lista.count(i)
        if somaAtual >= maiorSoma:
            maiorSoma = somaAtual

    return maiorSoma

# Valores Inválidos 
assert somaRepitidos([]) == Exception
assert somaRepitidos([1.1,1.1,2,2]) == Exception
assert somaRepitidos(['tds',5, 2, 5]) == Exception

# Valores Válidos
assert somaRepitidos([5, -2, -2, 5, 3, 5, 10, -2, 3, 10, 3, 1]) == 20
assert somaRepitidos([-1, -1, -3, -3]) == 0
assert somaRepitidos([5, 5, 2, 1, 1, 1, 1]) == 10

print('Gotcha! Testes okay')
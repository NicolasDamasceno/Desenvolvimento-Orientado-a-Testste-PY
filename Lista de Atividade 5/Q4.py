# Escreva uma função que recebe uma lista com n números inteiros, e determina a
# maior soma de qualquer seguimento da lista. Ex: Ex: [5, -2, -2, -7, 3, 15, 10, -3, 9,
# -6, 4, 1] = 34

def somaSegmento(lista):
    if type(lista) != list or len(lista) == 0:
        return Exception
    
    for num in lista:
        if type(num) != int:
            return Exception

    maiorSoma = 0
    somaAtual = 0

    for i in lista:
        somaAtual = max(i, somaAtual + i)
        maiorSoma = max(maiorSoma, somaAtual)
    
    return maiorSoma

# Valores Inválidos
assert somaSegmento([-2,5,2.5]) == Exception
assert somaSegmento([]) == Exception
assert somaSegmento(['tds',3,4,5]) == Exception

# Valores Válidos
assert somaSegmento([5,2,1,7,-3]) == 15
assert somaSegmento([1,-5,4,3,6]) == 13
assert somaSegmento([1,4]) == 5

print('Gotcha! Testes okay')
# Escreva uma função que recebe uma lista com n números inteiros, e determina a
# maior soma de um segmento com 2 valores. Ex: [5, -2, -2, -7, 3, 15, 10, -3, 9, -6,
# 4, 1] = 25

def maiorSoma(lista):
    if type(lista) != list or len(lista) == 0:
        return Exception
    
    for num in lista:
        if type(num) != int:
            return Exception
    
    maior_soma = 0
    for i in range(len(lista) - 1):
        soma = lista[i] + lista[i + 1]
        if soma > maior_soma:
            maior_soma = soma
    
    return soma

# Valores inválidos
assert maiorSoma([1,2.1,3]) == Exception
assert maiorSoma([]) == Exception
assert maiorSoma(['tds', 5, 2]) == Exception

# Valores válidos
assert maiorSoma([1,3,4,4,4]) == 8
assert maiorSoma([-1,5,2,-3,1]) == -2

print('Gotcha! Testes okay')
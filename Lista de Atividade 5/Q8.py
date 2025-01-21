# Escreva uma função que recebe uma lista com n números inteiros, e retorna o valor
# mais próximo da média de valores da lista. Ex [2.5, 7.5, 10.0, 4.0] = 7.5

def media(lista):
    if type(lista) != list or len(lista) == 0:
        return Exception
    
    for num in lista:
        if type(num) == str:
            return Exception
        
    soma = sum(lista)
    tamanho = len(lista)

    media = soma / tamanho
    valorProximo = lista[0]
    menorDiferenca = abs(lista[0] - media)

    for i in lista:
        diferenca = abs(i - media)
        if diferenca < menorDiferenca:
            menorDiferenca = diferenca
            valorProximo = i
    
    return valorProximo

# Valores Inválidos
assert media(['tds', 2, 3]) == Exception
assert media([]) == Exception

# Valores Válidos
assert media([2.5, 7.5, 10.0, 4.0]) == 7.5
assert media([5.1, 4, 6, 8.1]) == 6
assert media([2,8,3]) == 3

print('Gotcha! Testes okay')
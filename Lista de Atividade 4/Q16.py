# Faça uma função que leia um número não determinado de valores positivos
# e retorna a média aritmética dos mesmos.

def media(numeros):
    if type(numeros) != list:
        return Exception
    for numero in numeros:
        if type(numero) == str or numero < 0:
            return Exception
    
    mediaAritmetica = sum(numeros)/len(numeros)
    return round(mediaAritmetica,2)

# Valores Inválidos
assert media((2,7,8)) == Exception
assert media({9:0}) == Exception
assert media([2,5,'TDS']) == Exception
assert media([0,34,-9]) == Exception

# Valores Válidos
assert media([7,8,6]) == 7.0
assert media([1.5,6,8.9]) == 5.47

print('Gotcha! Testes okay')
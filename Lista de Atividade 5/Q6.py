# Escreva uma função que recebe uma lista com n números inteiros, e retorna True
# caso a lista esteja ordenada em ordem ascendente ou False caso não esteja
# ordenada. Ex [1, 2, 3] = True. Ex. [3, 7, 2] = False

def ordenada(lista):
    if type(lista) != list or len(lista) == 0:
        return Exception
    
    for num in lista:
        if type(num) != int:
            return Exception
        

    ordenada = bool
    for i in range(len(lista) - 1):
        if lista[i] <= lista[i+1]:
            ordenada = True
        else:
            ordenada = False
            break

    return ordenada

# Valores Inválidos
assert ordenada([1,2,5,6.7]) == Exception
assert ordenada([]) == Exception
assert ordenada([5,8,7,'tds']) == Exception
assert ordenada((4,5,6)) == Exception

# Valores Válidos
assert ordenada([1,2,3,4]) == True
assert ordenada([6,7,8]) == True
assert ordenada([2,1,8]) == False
assert ordenada([-1,0,1]) == True

print('Gotcha! Testes okay')
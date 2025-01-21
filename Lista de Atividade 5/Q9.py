# Escreva uma função que recebe uma lista com n números inteiros, retornar uma
# lista eliminando todas as ocorrências de valores repetidos. Ex: [5, 4, 5, 7, 3, 4] =
# [7, 3]

def filtro(lista):
    if type(lista) != list or len(lista) == 0:
        return Exception
    
    for num in lista:
        if type(num) != int:
            return Exception

    novaLista = []
    for i in lista:
        if lista.count(i) == 1:
            novaLista.append(i)

    return novaLista

# Valores Inválidos
assert filtro([]) == Exception
assert filtro([2.1,10,5,5.1]) == Exception
assert filtro([5,'tds',8]) == Exception

# Valores Válidos
assert filtro([5, 4, 5, 7, 3, 4]) == [7,3]
assert filtro([-1,2,2,1,1,5,6]) == [-1,5,6]

print('Gotcha! Testes okay')
# Escreva uma função que recebe uma lista com n números inteiros, e retorna uma
# lista com a soma cumulativa dos elementos da lista original onde o i-ésimo
# elemento é a soma dos primeiros i+1 elementos da lista original. Ex: [1,2,3] =
# [1,3,6]

def somaCulmulativa(lista):
    if type(lista) != list or len(lista) == 0:
        return Exception
    
    for num in lista:
        if type(num) != int:
            return Exception
        
    novaLista = []
    soma = 0
    for i in lista:
        soma += i
        novaLista.append(soma)
    
    return novaLista

# Valores Inválidos
assert somaCulmulativa([2,5,6.1,4]) == Exception
assert somaCulmulativa([]) == Exception
assert somaCulmulativa([5,1,3,'tds']) == Exception

# Valores Válidos
assert somaCulmulativa([1,3,4]) == [1,4,8]
assert somaCulmulativa([4,1,2,3]) == [4,5,7,10]

print('Gotcha! Testes okay')
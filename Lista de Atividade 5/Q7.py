# Escreva uma função que recebe uma lista com n números inteiros, e retorna True
# caso algum elemento apareça mais de uma vez ou False caso nenhum elemento
# apareça mais de uma vez. Ex [1, 2, 3, 1] = True. Ex. [3, 7, 2, 4] = False

def repeticao(lista):
    if type(lista) != list or len(lista) == 0:
        return Exception
    
    for num in lista:
        if type(num) != int:
            return Exception
        
    for i in lista:
        if lista.count(i) > 1:
            return True
        else:
            return False

# Valores Inválidos
assert repeticao([]) == Exception
assert repeticao((1,2,3)) == Exception
assert repeticao(['tds',1,2]) == Exception
assert repeticao([5,1,2,2.5]) == Exception

# Valores Válidos
assert repeticao([1,2,3,1,1]) == True
assert repeticao([1,5,6,8]) == False
assert repeticao([-1,-1,-5,2]) == True

print('Gotcha! Testes okay')
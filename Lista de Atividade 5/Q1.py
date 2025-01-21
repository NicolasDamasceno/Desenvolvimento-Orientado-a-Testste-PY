# Escreva uma função que recebe uma lista com n números inteiros, retornar uma
# lista eliminando as repetições. Ex: [5, 4, 5, 7, 3, 4] = [5, 4, 7, 3]

# Criando uma função para elimiar as repetição de uma lista
def filtrarLista(lista):
    if type(lista) == list and len(lista) > 0:
        for i in range(len(lista)):
            if type(lista[i]) != int:
                return Exception
            
        novaLista = []
        for num in range(len(lista)):
            if lista[num] not in novaLista:
                novaLista.append(lista[num])
        
        return novaLista
    
    else:
        return Exception

# Verificando valores inválidos
assert filtrarLista([]) == Exception
assert filtrarLista('tds') == Exception
assert filtrarLista(90) == Exception
assert filtrarLista([1, 2, 3, 3.2]) == Exception
assert filtrarLista([1, 2, 3, 'tds']) == Exception

# Verificando valores válidos
assert filtrarLista([1,1,1,2,3]) == [1, 2, 3]

print('Gotcha! Testes okay')
# Escreva uma função que recebe uma lista com n números inteiros, conta e imprime
# o número de vezes que cada número ocorre na sequência.

# Função para contar quantas vezes que cada número ocorre na sequência
def contadora(lista):
    if type(lista) == list and len(lista) > 0:
        for i in range(len(lista)):
            if type(lista[i]) != int:
                return Exception
        
        contagem = {}
        for num in lista:
            if num not in contagem:
                contagem[num] = 1
            else:
                contagem[num] += 1
        
        return contagem
    
    else: 
        return Exception
    
# Verificando valores inválidos
assert contadora([]) == Exception
assert contadora('teste') == Exception
assert contadora(30) == Exception
assert contadora([1, 1, 1, 6.5, 6])
assert contadora([1, 1, 2, 2, 'tds']) == Exception

# Verificando valores válidos
assert contadora([1, 1, 1, 2, 2, 3, 3, 3]) == {1 : 3, 2 : 2, 3 : 3}

print('Gotcha! Testes okay')
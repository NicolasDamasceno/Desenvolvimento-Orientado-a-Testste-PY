# Faça uma função que recebe 2 valores inteiros por parâmetro e retorna-os
# ordenados em ordem crescente.

def crescente(num1,num2):
    if type(num1) != int or type(num2) != int:
        return Exception
    
    if num1 < num2 or num2 > num1:
        return [num1,num2]
    
    elif num2 < num1 or num1 > num2:
        return [num2,num1]
    
    elif num1 == num2:
        return [num1,num2]

# Valores Inválidos
assert crescente(2.5, -8) == Exception
assert crescente(3, 0.2) == Exception
assert crescente('TDS', 8) == Exception
assert crescente(0, 'TDs') == Exception

# Valores Válidos
assert crescente(8,5) == [5, 8]
assert crescente(7,10) == [7, 10]
assert crescente(0,-5) == [-5, 0]
assert crescente(-2,-4) == [-4, -2]

print('Gotcha! Testes okay')
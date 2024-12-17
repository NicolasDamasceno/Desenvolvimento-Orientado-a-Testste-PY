# Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e
# retorna o número de divisores desse valor.
def divisores(num):
    if type(num) != int or num <= 0:
        return Exception
    
    totalDivisores = 0
    for divisor in range(1, num + 1):
        if num % divisor == 0:
            totalDivisores += 1
    
    return totalDivisores

# Valores Inválidos
assert divisores(2.4) == Exception
assert divisores('tds') == Exception
assert divisores(-3) == Exception
assert divisores(0) == Exception

# Valores Válidos
assert divisores(2) == 2
assert divisores(8) == 4

print('Gotcha! Testes okay')
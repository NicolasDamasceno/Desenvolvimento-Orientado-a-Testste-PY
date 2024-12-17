# Escreva uma função que recebe por parâmetro um valor inteiro e positivo N
# e retorna o valor de S.
# S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(n2+1)/(n+3)

def somatorio(num):
    if type(num) != int or num <= 0:
        return Exception
    
    soma = 0
    for i in range(1, num + 1):
        soma += (i**2 + 1)/(i+3)

    return round(soma,2)

# Valores Inválidos
assert somatorio('tds') == Exception
assert somatorio(9.3) == Exception
assert somatorio(-9) == Exception
assert somatorio(0) == Exception

# Valores Válidos
assert somatorio(3) == 3.17
assert somatorio(10) == 38.47

print('Gotcha! Testes okay')
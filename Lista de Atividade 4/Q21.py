# Escreva uma função que recebe por parâmetro um valor inteiro e positivo N
# e retorna o valor de S.

# S = 1 + 1⁄2 + 1/3 + 1⁄4 + 1/5 + 1/N.

def somatorio(num):
    if type(num) != int or num <= 0:
        return Exception
    
    soma = 0
    for i in range(1, num + 1):
        soma += 1/i
    return round(soma,2)

# Valores Inválidos
assert somatorio('tds') == Exception
assert somatorio(9.3) == Exception
assert somatorio(-9) == Exception
assert somatorio(0) == Exception

# Valores Válidos
assert (somatorio(4)) == 2.08
assert (somatorio(7)) == 2.59
assert somatorio(10) == 2.93

print('Gotcha! Testes okay')
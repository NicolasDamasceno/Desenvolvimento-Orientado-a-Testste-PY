# Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e
# retorna o somatório desse valor.

def somatorio(num):
    if type(num) != int or num <= 0:
        return Exception
    
    soma = 0
    for i in range(1,num+1):
        soma += i
    return soma

# Valores Inválido
assert somatorio('tds') == Exception
assert somatorio(9.3) == Exception
assert somatorio(-9) == Exception
assert somatorio(0) == Exception

# Valores Válidos
assert somatorio(4) == 10
assert somatorio(8) == 36

print('Gotcha! Testes okay')
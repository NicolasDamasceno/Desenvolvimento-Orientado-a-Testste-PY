# Faça uma função que recebe, por parâmetro, um valor N e calcula e escreve
# a tabuada de 1 até N. Mostre a tabuada na forma:
# 1 x N = N
# 2 x N = 2N
# ...
# N x N = N2

def tabuada(num):
    if type(num) != int or num <= 0:
        return Exception
    
    resultado = []
    for i in range(1, num + 1):
        resultado.append(f'{i} x {num} = {i*num}')
    return resultado

# Valores Inválidos
assert tabuada('tds') == Exception
assert tabuada(0) == Exception
assert tabuada(-2) == Exception
assert tabuada(8.7) == Exception

# Valores Válidos
assert tabuada(3) == ['1 x 3 = 3', '2 x 3 = 6', '3 x 3 = 9']
assert tabuada(2) == ['1 x 2 = 2', '2 x 2 = 4']

print('Gotcha! Testes okay')
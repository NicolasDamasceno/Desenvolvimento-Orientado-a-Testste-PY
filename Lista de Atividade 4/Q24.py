# Escreva uma função que recebe, por parâmetro, dois valores X e Z e calcula
# e retorna Xz

# . (sem utilizar funções ou operadores de potência prontos)

def potencia(x,z):
    if type(x) != int or type(z) != int:
        return Exception
    
    if z == 0:
        return 1
    
    resultado = 1
    for i in range(1,z+1):
        resultado *= x
    
    return resultado

# Valores Inválidos
assert potencia('tds', 2) == Exception
assert potencia(2, 'tds') == Exception
assert potencia(4.4, 2) == Exception
assert potencia(2, 3.1) == Exception

# Valores Válidos
assert potencia(2,0) == 1
assert potencia(5,4) == 625

print('Gotcha! Testes okay')
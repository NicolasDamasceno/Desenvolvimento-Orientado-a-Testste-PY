# Escreva uma função que recebe, por parâmetro um valor inteiro e retorna o
# seu fatorial.

def fatorial(num):
    if type(num) != int or num <= 0:
        return Exception
    
    fator = 1
    for i in range(1,num+1):
        fator *=  i

    return fator

# Valores Inválidos
assert fatorial(-1) == Exception
assert fatorial(3.5) == Exception
assert fatorial('tds') == Exception 

# Valores Válidos
assert fatorial(3) == 6
assert fatorial(5) == 120

print('Gotcha! Testes okay')
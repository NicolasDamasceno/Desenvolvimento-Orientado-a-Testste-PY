# Faça uma função que recebe um valor inteiro e verifica se o valor é positivo
# ou negativo. A função deve retornar um valor booleano.

def trueFalse(num):
    if type(num) != int or num == 0:
        return Exception
    
    # Para números positivos retorna True
    if num > 0:
        return True
    
    # Para números negativos retorna False
    elif num < 0:
        return False
    
# Valores Inválidos
assert trueFalse('TDS') == Exception
assert trueFalse(0) == Exception
assert trueFalse(2.5) == Exception
assert trueFalse(-0.9) == Exception

# Valores Válidos
assert trueFalse(20) == True
assert trueFalse(-1) == False

print('Gotcha! Testes okay')

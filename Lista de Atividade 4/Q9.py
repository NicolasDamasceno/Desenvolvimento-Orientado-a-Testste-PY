# Faça uma função que recebe um valor inteiro e verifica se o valor é par ou
# ímpar. A função deve retornar um valor booleano.

def trueFalse(num):
    if type(num) != int or num < 0:
        return Exception
    
    # Para números igual a 0 ou com resto 0, retorna True (Par)
    if num == 0 or (num % 2 == 0):
        return True
    
    # Para números com resto diferente de 0, retorna False (Impar)
    else:
        return False
    
# Valores Inválidos
assert trueFalse(-2) == Exception
assert trueFalse(6.85) == Exception
assert trueFalse('TDS') == Exception

# Valores Válidos
assert trueFalse(0) == True
assert trueFalse(8) == True
assert trueFalse(3) == False
assert trueFalse(5) == False

print('Gotcha! Testes okay')
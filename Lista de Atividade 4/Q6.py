# Faça uma função que verifique se um valor é perfeito ou não. Um valor é dito
# perfeito quando ele é igual à soma dos seus divisores excetuando ele próprio.
# (Ex: 6 é perfeito, 6 = 1 + 2 + 3, que são seus divisores). A função deve retornar
# um valor booleano.

def perfeito(num):
    if type(num) != int:
        return Exception
    
    if num < 0: 
        return Exception
    
    divisores = 0
    for i in range(num):
        if i < num and i > 0 :
            if num % i == 0:
                divisores += i
    
    if divisores == num:
        return True
    
    return False

# Valores Inválidos
assert perfeito('TDS') == Exception
assert perfeito(2.5) == Exception
assert perfeito(-2) == Exception

# Valores Válidos
assert perfeito(6) == True
assert perfeito(28) == True
assert perfeito(4) == False

print('Gotcha! Testes okay')
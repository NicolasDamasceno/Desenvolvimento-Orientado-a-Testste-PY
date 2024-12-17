# Faça uma função que recebe por parâmetro um valor inteiro e positivo e
# retorna o valor lógico Verdadeiro caso o valor seja primo e Falso em caso
# contrário.

# Função para indentificar os números primos
def primos(n):
    if type(n) != int or n <= 0:
        return Exception
    
    elif n == 1:
        return False
    
    for i in range(2,n):
        if n % i == 0:
            return False

    return True
    
# Valores inválidos 
assert primos('tds') == Exception
assert primos(0) == Exception
assert primos(-2) == Exception
assert primos(2.5) == Exception

#Valores válidos
assert primos(1) == False
assert primos(4) == False
assert primos(3) == True

print('Gotcha! Testes okay')
# Escreva uma função que recebe por parâmetro um valor inteiro e positivo N
# e retorna o valor de S.

# S = 1 + 1/1! + 1⁄2! + 1/3! + 1 /N!

def somatorio(num):
    if type(num) != int or num <= 0:
        return Exception
    
    def fatorial(n):
        fator = 0
        if n == 1 or n == 0:
            return 1
        fator = 1
        for x in (1, n+1):
            fator *= i
        return fator

    soma = 0

    for i in range(num+1):
        soma += (1/fatorial(i))
    
    return round(soma,2)

# Valores Válidos
assert somatorio(5) == 2.46
assert somatorio(6) == 2.49

print('Gotcha! Testes okay')
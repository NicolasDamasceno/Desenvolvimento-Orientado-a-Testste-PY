# Escreva uma função que recebes 3 valores reais X, Y e Z e que verifique se
# esses valores podem ser os comprimentos dos lados de um triângulo e, neste
# caso, retornar qual o tipo de triângulo formado. Para que X, Y e Z formem um
# triângulo é necessário que a seguinte propriedade seja satisfeita: o comprimento
# de cada lado de um triângulo é menor do que a soma do comprimento dos outros
# dois lados. O procedimento deve identificar o tipo de triângulo formado
# observando as seguintes definições:

# o Triângulo Equilátero: os comprimentos dos 3 lados são iguais.
# o Triângulo Isósceles: os comprimentos de 2 lados são iguais.
# o Triângulo Escaleno: os comprimentos dos 3 lados são diferentes.

def triangulo(l1,l2,l3):
    if type(l1) == str or type(l2) == str or type(l3) == str:
        return Exception
    
    if l1 <= 0 or l2 <= 0 or l3 <= 0:
        return Exception
    
    if l1 >= (l2 + l3) or l2 >= (l1 + l3) or l3 >= (l1 + l2):
        return Exception
    
    if (l1 == l2) and (l2 == l3) and (l1 == l3):
        return 'Triângulo Equilátero'
    
    elif (l1 == l2) or (l3 == l1) or (l3 == l2):
        return 'Triângulo Isósceles'
    
    elif (l1 != l2) and (l1 != l3) and (l3 != l2):
        return 'Triângulo Escaleno'
    
# Valores Inválidos
assert triangulo('TDs',4,5) == Exception
assert triangulo(3,'TDs',5) == Exception
assert triangulo(3,4,'TDs') == Exception
assert triangulo(0,4,5) == Exception
assert triangulo(3,0,5) == Exception
assert triangulo(3,4,0) == Exception
assert triangulo(-1,4,5) == Exception
assert triangulo(4,3,7) == Exception

# Valores válidos
assert triangulo(3,3,3) == 'Triângulo Equilátero'
assert triangulo(9,5,5) == 'Triângulo Isósceles'
assert triangulo(3,4,5) == 'Triângulo Escaleno'

print('Gotcha! Testes okay')
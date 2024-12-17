# Faça uma função que recebe, por parâmetro, a altura e o sexo de uma
# pessoa e retorna o seu peso ideal. Para homens, calcular o peso ideal usando a
# fórmula peso ideal = 72.7 * altura - 58 e, para mulheres, peso ideal = 62.1 * altura
# - 44.7.

# A altura será calculado em m
# Para a escolha será usado 1 - Para Massculino e 2 - para Feminino
def pesoIdeal(altura,escolha):
    if type(altura) == str or altura <= 0:
        return Exception

    if type(escolha) != int or escolha not in [1,2]:
        return Exception

    if escolha == 1:
        peso = (72.7 * altura) - 58    
        return round(peso,1)
    
    elif escolha == 2:
        peso = (62.1 * altura) - 44.7
        return round(peso,1)
    
# Valores Inválidos
assert pesoIdeal('TDS', 1) == Exception
assert pesoIdeal(0, 2) == Exception
assert pesoIdeal(-2.5, 1) == Exception
assert pesoIdeal(1.70, 1.1) == Exception
assert pesoIdeal(1.65, 4) == Exception
assert pesoIdeal(1.40, 'Tds') == Exception

# Valores Válidos
assert pesoIdeal(1.60,1) == 58.3
assert pesoIdeal(1.85,2) == 70.2

print('Gotcha! Testes okay')
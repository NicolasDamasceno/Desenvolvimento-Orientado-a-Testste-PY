# Faça uma função que recebe a idade de um nadador por parâmetro e retorna
# a categoria desse nadador de acordo com a tabela abaixo:

# Idade         Categoria
# 5 a 7 anos     Infantil A
# 8 a 10 anos    Infantil B
# 11-13 anos     Juvenil A
# 14-17 anos     Juvenil B
# Maiores de      Adulto
# 18 anos 
# (inclusive)

def idade(anos):
    if type(anos) != int or anos < 5:
        return Exception
    
    if 5 <= anos <= 7:
        return 'Infantil A'

    elif 8 <= anos <= 10:
        return 'Infantil B'

    elif 11 <= anos <= 13:
        return 'Juvenil A'

    elif 14 <= anos <= 17:
        return 'Juvenil B'

    elif anos >= 18:
        return 'Adulto'

# Valores Inválidos
assert idade('TDS') == Exception
assert idade(2.5) == Exception
assert idade(3) == Exception
assert idade(-10) == Exception

# Valores Válidos
assert idade(6) == 'Infantil A'
assert idade(10) == 'Infantil B'
assert idade(12) == 'Juvenil A'
assert idade(14) == 'Juvenil B'
assert idade(18) == 'Adulto'

print('Gotcha! Testes okay')

# Faça uma função que recebe a média final de um aluno por parâmetro e
# retorna o seu conceito, conforme a tabela abaixo:
# Nota           Conceito
# de 0,0 a 4,9      D
# de 5,0 a 6,9      C
# de 7,0 a 8,9      B
# de 9,0 a 10,0     A

def conceito(media):
    if type(media) == str or media < 0 or media > 10:
        return Exception
    
    if 0 <= media <= 4.9:
        return 'D'

    elif 5 <= media <= 6.9:
        return 'C'
    
    elif 7 <= media <= 8.9:
        return 'B'
    
    elif 9 <= media <= 10:
        return 'A'

# Valores Inválidos
assert conceito(-1) == Exception
assert conceito(11) == Exception
assert conceito('TDS') == Exception

# Valores Válidos
assert conceito(10.0) == 'A'
assert conceito(8) == 'B'
assert conceito(6.2) == 'C'
assert conceito(4.9) == 'D'

print('Gotcha! Testes okay')
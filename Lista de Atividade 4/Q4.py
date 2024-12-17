# Faça uma função que recebe por parâmetro o tempo de duração de um
# processo em uma fábrica expressa em segundos e retorna também por
# parâmetro esse tempo em horas, minutos e segundos.

def tempo(s):
    if type(s) != int or s <= 0:
        return Exception
    
    hora = s // 3600
    s = s % 3600
    min = s // 60
    seg = s % 60
    return f'{hora}h {min}m {seg}s'

# Valores inválidos
assert tempo('tds') == Exception
assert tempo(4.5) == Exception
assert tempo(-12) == Exception

# Valores válidos
assert tempo(360) == f'{0}h {6}m {0}s'

print('Gotcha! Testes okay')
   
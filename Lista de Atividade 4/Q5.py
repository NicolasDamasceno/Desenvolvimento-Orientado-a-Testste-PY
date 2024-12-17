# Faça uma função que recebe a idade de uma pessoa em anos, meses e dias
# e retorna essa idade expressa em dias.

def idade(ano,mes,dia):
    idadeDias = 0
    if type(ano) != int or type(mes) != int or type(dia) != int:
        return Exception 

    if ano < 0:
        return Exception

    elif mes > 12 or mes < 0:
        return Exception

    elif dia > 30 or dia < 0:
        return Exception 
    
    idadeDias = (ano*365) + (mes*30) + (dia)
    return idadeDias

# Valores Inválidos
assert idade('TDS',10,25) == Exception
assert idade(25,'TDs',10) == Exception
assert idade(20,2,'Tds') == Exception
assert idade(20.12,10,30) == Exception
assert idade(40,8.5,20) == Exception
assert idade(80,4,2.2) == Exception
assert idade(60,14,8) == Exception
assert idade(22,10,35) == Exception
assert idade(-2,10,30) == Exception

#Valores válidos
assert idade(20,9,15) == 7585
assert idade(55,7,25) == 20310

print('Gotcha! Testes okay')
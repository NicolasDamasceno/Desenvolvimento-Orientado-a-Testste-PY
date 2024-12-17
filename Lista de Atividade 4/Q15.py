# A prefeitura de uma cidade fez uma pesquisa entre os seus habitantes,
# coletando dados sobre o salário e número de filhos. Faça uma função que leia
# esses dados para um número não determinado de pessoas e retorne a média de
# salário da população, a média do número de filhos, o maior salário e o percentual
# de pessoas com salário até R$ 350,00.

def pesquisa(salarios,filhos):
    if type(salarios) != list or type(filhos) != list:
        return Exception
    
    if len(salarios) != len(filhos) or len(salarios) == 0:
        return Exception
    
    for salario in salarios:
        if type(salario) == str or salario < 0:
            return Exception

    for filho in filhos:
        if type(filho) != int or filho < 0:
            return Exception
    
    totalPessoas = len(salarios)
    totalFilhos = sum(filhos)
    totalSalario = sum(salarios)
    mediaSalario = totalSalario / totalPessoas
    mediaFilhos = totalFilhos / totalPessoas
    maxSalario = max(salarios)
    quantidadePercentualSalario = 0
    for salario in salarios:
        if salario <= 350:
            quantidadePercentualSalario += 1
    percentual = (quantidadePercentualSalario/totalPessoas)*100

    return round(mediaSalario,2), round(mediaFilhos,2), round(maxSalario,2), round(percentual,2)

# Valores Inválidos
assert pesquisa((200, 300, 400),[2,1,0]) == Exception
assert pesquisa([350,500,600],{1,2,3}) == Exception
assert pesquisa([350,400,'tds'],[1,2,3]) == Exception
assert pesquisa([500,400,700],[1,2,'tds']) == Exception
assert pesquisa([-200,350],[1,2]) == Exception
assert pesquisa([450,600,150],[1,2,-3]) == Exception
assert pesquisa([500.50,600,700],[1,2,3.5]) == Exception

# Valores Válidos
assert pesquisa([1000,350,250],[1,2,3]) == (533.33, 2.0, 1000, 66.67)
assert pesquisa([200.10,360,700],[2,1,4]) == (420.03, 2.33, 700, 33.33)
assert pesquisa([505,670,880],[0,2,4]) == (685.0, 2.0, 880, 0.0)

print('Gotcha! Testes okay')
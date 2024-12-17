# Escreva uma função que recebe as 3 notas de um aluno por parâmetro e uma
# letra. Se a letra for A o procedimento calcula a média aritmética das notas do
# aluno, se for P, a sua média ponderada (pesos: 5, 3 e 2). A função deve retornar
# a média calculada.

# Função para calcular a média aritmétrica ou ponderada
def calcularMedia(n1,n2,n3,letra):
    if type(n1) == str or type(n2) == str or type(n3) == str:
        return Exception
    
    elif(n1 < 0 or n1 > 10) or (n2 < 0 or n2 > 10) or (n3 < 0 or n3 > 10):
        return Exception
    
    elif letra not in ['A', 'P']:
        return Exception
    
    if letra.upper() == 'A':
        return round((n1+n2+n3) / 3,2)
    
    elif letra.upper() == 'P':
        return round(((n1*5) + (n2*3) + (n3*2))/10,2)
    
# Testando a função de média
# Valores inválidos
assert calcularMedia('tds', 4, 5, 'A') == Exception
assert calcularMedia(6, 'tds', 9, 'P') == Exception
assert calcularMedia(8, 7, 'tds', 'A') == Exception
assert calcularMedia(0, 10, 7, 0) == Exception
assert calcularMedia(5, 10, 9, 'I') == Exception
assert calcularMedia(-1, 1, 2, 'A') == Exception 
assert calcularMedia(3, -2, 5, 'P') == Exception 
assert calcularMedia(4, 9, -1, 'P') == Exception 
assert calcularMedia(11, 1, 9, 'A') == Exception
assert calcularMedia(5, 13, 4, 'P') == Exception
assert calcularMedia(9, 7, 14, 'A') == Exception 

# Valores válidos
assert calcularMedia(4, 9, 10, 'A') == 7.67
assert calcularMedia(7.8, 9.2, 10, 'P') == 8.66

print('Gotcha! Testes okay')
# Faça uma função que recebe por parâmetro o raio de uma esfera e calcula o
# seu volume (v = 4/3 * PI * R**3).

# Criando a variavel constante PI
PI = 3.14

# Função para calcular o raio de uma esfera
def volume(raio):
    if type(raio) == str:
        return Exception
    if raio <= 0: 
        return Exception
    
    return round(4/3*PI*raio,2)

# Iniciando os testes da função
assert volume(0) == Exception # Testando o raio igual a 0
assert volume(-1) == Exception # Testando para valores menores de 0
assert volume('tds') == Exception # Testando para strings

assert volume(1.0) == 4.19 #Testando para valor válido
assert volume(3) == 12.56 #Testando para um valor inteiro válido

print('Gotcha! Testes okay')
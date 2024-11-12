# Crie uma lista `temperaturas = [23.5, 18.6, 30.2, 15.9, 25.1, 29.8]` e escreva um código para
# encontrar a média das temperaturas. Imprima a média ao final.

#Função para calcular a médias das temperaturas
def mediaTemperaturas(temperaturas):
    soma = 0
    quantidade = 0 
    for i in range(len(temperaturas)):
        soma += temperaturas[i]
        quantidade += 1
    media = soma / quantidade
    return media

#Função Principal
def main():
    temperaturas = [23.5, 18.6, 30.2, 15.9, 25.1, 29.8]
    print(f'Temperaturas: {temperaturas}')
    print(f'Média das temperaturas: {mediaTemperaturas(temperaturas):0.2f}°C')
if __name__ == '__main__':
    main()
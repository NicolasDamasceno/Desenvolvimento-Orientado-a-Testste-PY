# Dadas duas listas, uma contendo a quantidade e a outra o preço de 20 produtos, elabore um
# programa que calcule e exiba o faturamento que é igual a quantidade x preço. Calcule e exiba
# também o faturamento total que é o somatório de todos os faturamentos, a média dos faturamentos
# e quantos faturamentos estão abaixo da média.

from random import randint

#Função para gravar a lista
def gravarLista():
    maxList = 20
    lista = []
    for i in range(maxList):
        num = randint(1,30)
        lista.append(num)
    return lista

#Função para calcular o faturamento total
def faturamentoTotal(quntidade,preco):
    total = 0
    for i in range(len(quntidade)):
        total += quntidade[i]*preco[i]
    
    return total

#Função para calcular a média do faturamento total
def calcularMedia(total):
    media = total/20
    return media

#Função para calcular quantos faturamentos estão abaixo da média
def abaixoMedia(media,quantidade,preco):
    contador = 0
    for i in range(len(quantidade)):
        if ((preco[i]*preco[i]) < media):
            contador += 1
    return contador
#Função Principal
def main():
    quantidade = gravarLista()
    preco = gravarLista()
    print(f'Quantidade de cada produto: {quantidade}\nPreço respectivamente: {preco}')
    total = faturamentoTotal(quantidade,preco)
    print(f'\nFaturamento total: R${total},00')
    media = calcularMedia(total)
    print(f'Média dos faturamentos: R${media:0.2f}')
    abaixo = abaixoMedia(media,quantidade,preco)
    print(f'Quantidades de faturamentos abaixo da Média: {abaixo}')
if __name__== '__main__':
    main()
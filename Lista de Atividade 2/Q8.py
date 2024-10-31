# Dada uma lista contendo letras do alfabeto, elabore um programa para verificar quantas vezes
# ocorreu a letra ‘A’.
# OBS: Fazer crítica na entrada do caractere para aceitar somente letras.

#Função para verificar os caracters da frase

def verficarCaracteres(fraseOriginal):
    fraseCorreta = list(range(len(fraseOriginal)))
    for i in range(len(fraseOriginal)):
        fraseCorreta[i] = fraseOriginal[i]
        while (fraseCorreta[i]< "A" or fraseCorreta[i]> 'Z' or type(fraseCorreta[i]) != str):
            print(f'\nCaractere digitado não é uma letra: {fraseCorreta[i]}')
            fraseCorreta[i] = input(f'Digite novamente a letra: ').upper()

    return fraseCorreta

#Função para contar a ocorrência da letra 'A'

def contarA(frase):
    contador = 0
    for i in range(len(frase)):
        if frase[i] == 'A':
            contador += 1
    
    return contador

#Função Principal

def main():

    frase = input('\nDigite uma sequência qualquer de letras: ').upper()
    frase = verficarCaracteres(frase)
    print(f'\nA letra "A" apareceu {contarA(frase)} vezes.')

if __name__ == "__main__":
    main()
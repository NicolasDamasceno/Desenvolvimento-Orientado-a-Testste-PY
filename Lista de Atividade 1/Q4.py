#4. Escreva um programa para ler as notas das duas avaliações de um aluno no semestre. Faça um procedimento que receba as duas
# notas por parâmetro e calcule e escreva a média semestral e a mensagem “PARABÉNS! Você foi aprovado!” somente se o aluno
# foi aprovado (considere 6.0 a média mínima para aprovação)

#Função para calcular a média das notas
def media(nota1, nota2):
    media_semestral = (nota1 + nota2) / 2
    if media_semestral >= 6:
        return print("PARABÉNS! Você foi aprovado!")
    else:
        return print("Você não foi aprovado.")
 
#Função Principal
def main():
    try:
        nota1 = float(input('Digite a nota 1: '))
        nota2 = float(input('Digite a nota 2: '))

        media(nota1, nota2)
    
    except ValueError:
        print('Por favor, insira valores numéricos.')

if __name__ == '__main__':
    main()
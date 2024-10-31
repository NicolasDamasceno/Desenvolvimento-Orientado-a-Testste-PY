# Deseja-se publicar o número de acertos de cada aluno em uma prova em forma de testes. A
# prova consta de 30 questões, cada uma com cinco alternativas identificadas por A, B, C, D e E.
# Para isso são dados:
# o cartão gabarito;
# o número de alunos da turma;
# o cartão de respostas para cada aluno, contendo o seu número e suas respostas.
from random import randint

# Criando limetes do gabarito e alunos e as alternatives
alternativas = ['A', 'B', 'C', 'D', 'E']
maxList = 30
alunos = 10

# Função para gerar o Gabarito
def gerarGabarito(maxList):
    gabarito = []
    for i in range(maxList):
        gabarito.append(alternativas[randint(0, 4)])
    return gabarito

# Função para gerar o Cartao Resposta
def gerarCartaoResposta(maxList):
    cartao = []
    for i in range(maxList):
        cartao.append(alternativas[randint(0,4)])
    return cartao

#Função para contar os acertos dos alunos
def acertos(gabarito, cartao):
    acertos = 0
    for i in range(maxList):
        if gabarito[i] == cartao[i]:
            acertos += 1
    return acertos

#Função Principal
def main():
    print(f'Gabarito:')
    gabarito = gerarGabarito(maxList)
    print(gabarito)
    print('\n')
    print('-'*30)
    for aluno in range(alunos):
        print(f'Aluno {aluno+1}:')
        cartaoResposta = gerarCartaoResposta(maxList)
        print(f'Cartão de Resposta do aluno {aluno+1}: \n{cartaoResposta}')
        print(f'Número de acertos do aluno {aluno+1}: {acertos(gabarito, cartaoResposta)}')
        print('-'*30)
        print('\n')

if __name__ == '__main__':
    main()
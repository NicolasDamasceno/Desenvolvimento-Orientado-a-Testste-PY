# Tentando descobrir se um dado era viciado, um dono de cassino honesto (ha! ha! ha! ha!) o
# lançou n vezes. Dados os n resultados dos lançamentos, determinar o número de ocorrências de
# cada face.
from random import randint

#Função para realizar o lançamento, o indíce da lista equivale a uma face do dado
def lancamento(n):
    faces = [0,0,0,0,0,0]

    for i in range(n):
        face = randint(1, 6)
        faces[face-1] += 1
    return faces

#Função para imprimir o número de ocorrências de cada face do dado
def imprime_ocorrencias(faces):
    print('Ocorrências de cada face:')
    for q in range(len(faces)):
        print(f'Face {q+1}: {faces[q]} ocorrências')

#Função principal para testar a função
def main():
    try:
        n = int(input('Digite quantas vezes o dado será jogado: '))
        faces = lancamento(n)
        print(f'Lançamentos: {faces}')
        imprime_ocorrencias(faces)
    except ValueError:
        print('Por favor, digite um número inteiro.')
        return
if __name__ == '__main__':
    main()
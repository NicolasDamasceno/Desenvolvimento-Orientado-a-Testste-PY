#Faça um programa que alimente uma lista com um número de posições definidas pelo
#usuário.
#Esta lista deverá armazenar um conjunto de nomes em diferentes posições.
#Crie um mecanismo para alimentar elementos da lista e pesquisar por um valor existente.
#==== =MENU========
#1)Cadastar nome
#2)Pesquisar nome
#3)Listar todos os nome
#0) Sair do programa
#——————–
#Digite sua escolha:_

#Função para pesquisar um nome especifico
def pesquisarNome(lista, nome):
    for i in range(len(lista)):
        if lista[i] == nome:
            return 'foi encontrado!'

    return 'não foi encontrado'

#Função principal
def main():
    nomes = []
    while True:
        print("\n==== MENU========\n1) Cadastrar nome\n2) Pesquisar nome\n3) Listar todos os nomes\n0) Sair do programa\n——————–")
        escolha = int(input("Digite sua escolha: "))
        if escolha == 1:
            nome = input("Digite um nome: ")
            nomes.append(nome)
        elif escolha == 2:
            nome = input("Digite um nome para pesquisar: ")
            print(f'O nome pesquisado {nome} {pesquisarNome(nomes, nome)}')
        elif escolha == 3:
            print("Todos os nomes na lista:")
            for nome in nomes:
                print(f'\n{nome}')
        elif escolha == 0:
            print("Programa finalizado.")
            break
        else:
            print("Escolha inválida!")
    
if __name__ == "__main__":
    main()
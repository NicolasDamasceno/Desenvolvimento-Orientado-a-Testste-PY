# Faça um programa que alimente uma lista com um número de posições definidas pelo
# usuário.
# Esta lista deverá armazenar um conjunto de nomes em diferentes posições.
# Crie um mecanismo para alimentar elementos da lista e pesquisar por um valor existente.
# ==== =MENU========
# 1)Cadastar nome
# 2)Pesquisar nome
# 3)Listar todos os nome
# 4)Excluir nome
# 5)Alterar nome
# 0) Sair do programa
# ——————–
# Digite sua escolha:_

def quantidadeDefinida():
    global maxList
    while True:
        try:
            quantidade = int(input('\nDigite a quantidade de elementos da lista: '))
            while quantidade <= 0:
                quantidade = int(input('\nDigite a quantidade de elementos da lista: '))
            maxList = quantidade
            break
        except ValueError:
            print('\nQuantidade inválida. Digite novamente')
            
#Função para pesquisar um nome especifico
def pesquisarNome(lista):
    while True:
        if len(lista) != 0:
            nomePesquisado = input('Digite o nome que deseja pesquisar: ')
            for i in range(len(lista)):
                if lista[i] == nomePesquisado:
                    print(f'O {nomePesquisado} foi encontrado na lista!')
                    
            return print(f'O {nomePesquisado} não foi encontrado...')
        else:
            print('A lista está vazia!')

#Função para adicionar um nome na lista
def adicionarNome(lista):
    if len(lista) < maxList:
        while True:
            try:
                nome = input("Digite o nome: ")
                lista.append(nome)
                print(f'Nome {nome} adicionado com sucesso!')
                break
            except ValueError:
                print('Nome inválido. Digite novamente')
    else:
        print('A lista já está cheia!')
   
#Função para listar todos os nomes
def listarNomes(lista):
    if len(lista) != 0:
        for nome in lista:
            print(nome)
    else:
        print('A lista está vazia!')

#Função para excluir um nome da lista
def excluirNome(lista):
    if len(lista)!= 0:
        while True:
            try:
                nomeExcluir = input('Digite o nome para excluir: ')
                if nomeExcluir in lista:
                    print(f'Nome encontrado!')
                    lista.remove(nomeExcluir)
                    print(f'Nome {nomeExcluir} excluído com sucesso!')
                    break
                else:
                    print(f'Nome {nomeExcluir} não foi encontrado.')
                    break
            except ValueError:
                print('Nome inválido. Digite novamente')
    else:
        print('A lista está vazia!')

#Função para alterar um dos nomes da lista
def alterarNome(lista):
    if len(lista)!= 0:
        while True:
            try:
                nomeAlterar = input('Digite um nome para alterar: ')
                if nomeAlterar in lista:
                    print(f'Nome encontrado!')         
                    novoNome = input('Digite o novo nome: ')
                    lista[lista.index(nomeAlterar)] = novoNome
                    print(f'Nome {nomeAlterar} alterado com sucesso para {novoNome}!')
                    break 
                else:
                    print(f'Nome {nomeAlterar} não foi encontrado.')
                    break
            except ValueError:
                print('Nome inválido. Digite novamente')
    else:
        print('A lista está vazia!')
        
#Função principal
def main():
    nomes = []
    quantidadeDefinida()
    while True:
        try:
            print("\n==== MENU========\n1) Cadastrar nome\n2) Pesquisar nome\n3) Listar todos os nomes\n4) Excluir um nome\n5) Alterar um nome\n0) Sair do programa\n——————–")
            escolha = int(input("Digite sua escolha: "))
            if escolha == 1:
                adicionarNome(nomes)
            elif escolha == 2:
                pesquisarNome(nomes)
            elif escolha == 3:
                listarNomes(nomes)
        
            elif escolha == 4:
                excluirNome(nomes)
                
            elif escolha == 5:
                alterarNome(nomes)

            elif escolha == 0:
                print("Programa finalizado.")
                break
            else:
                print("Escolha inválida!")
        except ValueError:
            print('Caractere Inválido')
if __name__ == "__main__":
    main()
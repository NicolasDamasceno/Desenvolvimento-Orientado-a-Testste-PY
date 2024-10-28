# Escreva uma função que lê um caractere digitado pelo usuário e retorna este caractere somente se ele for igual a 'S' ou 'N'. Se o
# caractere não for nem 'S' nem 'N', a função imprime a mensagem 'Caractere inválido. Digite novamente'. Use esta função em um
# programa que fica lendo do usuário um número qualquer e imprime este número ao cubo na tela. O programa deve ficar lendo os
# números até o usuário responder 'N' à pergunta se ele deseja continuar ou não

# Função para ler um caractere do usuário e retornar 'S' ou 'N'
def ler_caractere():
    while True:
        caractere = input("Deseja continuar? (S/N): ").upper() 
        if caractere == 'S' or caractere == 'N':
            return caractere
        else:
            print("Caractere inválido. Digite novamente.")

#Função Principal
def main():
    while True:
        try:
            numero = float(input("Digite um número: "))
            
            cubo = numero ** 3
            print(f"O cubo de {numero} é {cubo:.2f}")
            
            continuar = ler_caractere()
            if continuar == 'N':
                print("Programa finalizado.")
                break
        except ValueError:
            print("Valor inválido. Digite um número.")

if __name__ == "__main__":
    main()
# Dada uma lista `nomes = ["Ana", "Beatriz", "Carlos", "Daniel", "Eduarda", "Fabio"]`, escreva
# um código para contar quantos nomes têm mais de cinco letras.

#Função para contar quantos nmes tem mais de 5 letras
def contarNomes(nomes):
    contador = 0
    for nome in nomes:
        if len(nome) > 5:
            contador += 1
    return contador

#Função Principal
def main():
    nomes = ["Ana", "Beatriz", "Carlos", "Daniel", "Eduarda", "Fabio"]
    print(nomes)
    print(f'Quantidade de nomes com 5 letras = {contarNomes(nomes)}')    
if __name__ == "__main__":
    main()
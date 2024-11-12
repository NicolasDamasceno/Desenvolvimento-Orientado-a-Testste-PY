# Dada uma lista de palavras, escreva um programa que retorne uma nova lista contendo apenas
# as palavras que começam com uma vogal. Exemplo: se `palavras = ["gato", "elefante", "urso",
# "abelha", "cobra"]`, o programa deve retornar `["elefante", "urso", "abelha"]`.

#Função que cria uma lista de palavras que apenas começam com vogal
def listaVogais(lista):
    vogais = ['a', 'e', 'o', 'u', 'i']
    novaLista = []
    for palavra in lista:
        if palavra[0].lower() in vogais:
            novaLista.append(palavra)
    
    return novaLista

#Função Principal
def main():
    palavras = ["gato", "elefante", "urso", "abelha", "cavalo", "ema"]
    print(f'Lista de Palavras: {palavras}')
    print(f'Lista de palvaras que començam com vogal: {listaVogais(palavras)}')

if __name__=='__main__':
    main()

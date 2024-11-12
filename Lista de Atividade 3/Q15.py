# Crie uma função que receba uma lista de números e retorne uma lista de tuplas, onde cada
# tupla contenha um número e sua frequência na lista. Ordene a lista de tuplas por frequência em
# ordem decrescente.
# **Exemplo:** `lista = [4, 4, 3, 2, 4, 3]` -> `[(4, 3), (3, 2), (2, 1)]`

#Função para criar a lista de tuplas
def listaTuplas(lista):
    tuplas = []
    for i in range(len(lista)):
       if (lista[i], lista.count(lista[i])) not in tuplas:
            tuplas.append((lista[i], lista.count(lista[i])))
    
    tuplas.sort(key=lambda x: x[1], reverse=True)
    return tuplas

#Função Principal
def main():
    lista = [4, 4, 3, 2, 4, 3]
    print(f'Original Lista: {lista}')
    listaNovaTuplas = listaTuplas(lista)
    print(f'Nova Lista de Tuplas: {listaNovaTuplas}')


if __name__ == '__main__':
    main()

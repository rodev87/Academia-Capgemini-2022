# Função que analisa o vetor recebido, buscando por
# pares cuja diferença resulte no valor de x.
def compara_itens(n):
    lista = []

    # Estrutura de repetição aninhada para
    # comparação dos itens do vetor
    for i in range(len(n)):
        for j in range(len(n)-1, i, -1):

            # Estrutura de seleção que verifica se
            # o valor de x é positivo ou negativo
            # e chama a função correspondente:
            if x >= 0:

                # Se a função de verificação retornar verdadeiro,
                # os pares serão incluídos na variável local lista.
                # Ao final da execução, a função devolverá o lenght de
                # lista, que é a quantidade de pares identificados:
                if verifica_xpositivo(n[i], n[j]):
                    lista.append([n[i], n[j]])
            else:
                if verifica_xnegativo(n[i], n[j]):
                    lista.append([n[i], n[j]])
    return len(lista)


# Verifica se o resultado da subtração
# de um item pelo outro é igual a x,
# devolvendo um booleano:
def verifica_xpositivo(a, b):
    if a >= b:
        return a - b == x
    else:
        return b - a == x


def verifica_xnegativo(a, b):
    if a < b:
        return a - b == x
    else:
        return b - a == x


# Teste 1
print(f"{'-='*8}Teste 1{'=-'*8}\nEntrada:\nn = [1, 5, 3, 4, 2]\nx = 2\n")

n = [1, 5, 3, 4, 2]
x = 2
pares = compara_itens(n)
print(f'Saída:\n{pares}')

# Teste 2
print(f"{'-='*8}Teste 2{'=-'*8}\nEntrada:\nn = [9, 2, 1, 4, 6]\nx = -3\n")

n = [9, 2, 1, 4, 6]
x = -3
pares = compara_itens(n)
print(f'Saída:\n{pares}')
print(f"{'_'*39}\n")

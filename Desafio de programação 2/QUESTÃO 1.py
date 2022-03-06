# Função que ordena a lista recebida,
# calcula e devolve a sua mediana.
def calc_mediana(arr):
    # Ordenação da lista "arr" com o método embutido sort():
    arr.sort()

    # Calcula a divisão inteira de lenght de "arr" por 2,
    # atribuindo o resultado à variável local i, que servirá de índice:
    i = len(arr)//2

    # A função devolve o valor armazenado no índice i de "arr":
    return arr[i]


print(f"{'-='*8}Teste 1{'=-'*8}\nEntrada:\narr = [7, 3, 1, 9, 6, 101, 33, 20, 2]\n")

arr = [7, 3, 1, 9, 6, 101, 33, 20, 2]
mediana = calc_mediana(arr)
print(f'Saída:\n{mediana}')


print(f"{'-='*8}Teste 2{'=-'*8}\nEntrada:\narr = [9, 2, 1, 4, 6]\n")

arr = [9, 2, 1, 4, 6]
mediana = calc_mediana(arr)
print(f'Saída:\n{mediana}')


print(f"{'-='*8}Teste 3{'=-'*8}\nEntrada:\narr = [1, 5, 3, 6, 2, 10, 7]\n")

arr = [1, 5, 3, 6, 2, 10, 7]
mediana = calc_mediana(arr)
print(f'Saída:\n{mediana}')

print(f"{'_'*39}\n")

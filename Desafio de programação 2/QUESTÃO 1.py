def calc_mediana(arr):
    arr.sort()
    i = len(arr)//2
    return arr[i]


print('Teste 1\n\nEntrada:\narr = [7, 3, 1, 9, 6, 101, 33, 20, 2]\n')
arr = [7, 3, 1, 9, 6, 101, 33, 20, 2]
mediana = calc_mediana(arr)
print(f'Saída:\n{mediana}')
print('-------------------------------------\n')

print('Teste 2\n\nEntrada:\narr = [9, 2, 1, 4, 6]\n')
arr = [9, 2, 1, 4, 6]
mediana = calc_mediana(arr)
print(f'Saída:\n{mediana}')
print('-------------------------------------\n')

print('Teste 3\n\nEntrada:\narr = [1, 5, 3, 4, 2]\n')
arr = [1, 5, 3, 4, 2]
mediana = calc_mediana(arr)
print(f'Saída:\n{mediana}')
print('-------------------------------------\n')

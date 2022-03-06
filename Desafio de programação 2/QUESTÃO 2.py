def analisa_vetor(n, x):
    lista = []
    for i in range(len(n)):
        for j in range(len(n)-1, i, -1):
            if n[i] >= n[j]:
                if n[i] - n[j] == x:
                    lista.append([n[i], n[j]])
            else:
                if n[j] - n[i] == x:
                    lista.append([n[j], n[i]])
    return lista


# Testes:
print(f"{'-='*8}Teste 1{'=-'*8}\nEntrada:\nn = [1, 5, 3, 4, 2]\nx = 2\n")

n = [1, 5, 3, 4, 2]
x = 2
pares = analisa_vetor(n, x)
print(f'Saída:\n{len(pares)}')

print(f"{'-='*8}Teste 2{'=-'*8}\nEntrada:\nn = [9, 2, 1, 4, 6]\nx = 3\n")

n = [9, 2, 1, 4, 6]
x = 3
pares = analisa_vetor(n, x)
print(f'Saída:\n{len(pares)}')
print(f"{'_'*39}\n")

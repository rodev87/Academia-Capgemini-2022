# https://docs.google.com/document/d/e/2PACX-1vRrSJORROEeHhNOmTuKxwlnC9APumr1C_k365WH3zVlryBy3KnvvZPnSmulijLktw/pub

def analisa_vetor(vetor, x):
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


n = []
continua = 's'
while continua != 'n':
    a = int(input('Por favor, digite um número para incluir no vetor: '))
    n.append(a)
    continua = input("Deseja incluir mais números? (s/n): ")

x = int(input('Por favor, defina um valor para x: '))
pares = analisa_vetor(n, x)

print(len(pares))
print(pares)

import math

s = input('Digite a frase que deseja encriptar: ')

t = s.replace(" ", "")
passo = math.ceil(math.sqrt(len(t)))
tamanho = len(t)
grid = []
for i in range(passo):
    lista = []
    for j in range(i, len(t), passo):
        lista.append(t[j])
    grid.append("".join(lista))

print(*grid)

from math import sqrt, ceil


def encript(s):
    t = s.replace(" ", "")
    raiz_de_t = ceil(sqrt(len(t)))
    matriz = []
    for i in range(raiz_de_t):
        linha = []
        for j in range(i, len(t), raiz_de_t):
            linha.append(t[j])
        matriz.append("".join(linha))
    return matriz


print('Teste 1: tenha um bom dia')
s = 'tenha um bom dia'
print(*encript(s))

print('--------------------------')

print('Teste 2: ola mundo')
s = 'ola mundo'
print(*encript(s))

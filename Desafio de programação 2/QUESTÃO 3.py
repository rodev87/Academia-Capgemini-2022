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


print('Teste 1\n\nEntrada:\ns = tenha um bom dia\n')
s = 'tenha um bom dia'
print('Saída:')
print(*encript(s))
print('---------------------------\n')

print('Teste 2\n\nEntrada:\ns = ola mundo\n')
s = 'ola mundo'
print('Saída:')
print(*encript(s))
print('---------------------------\n')

print('Teste 3\n\nEntrada:\ns = Academia Capgemini 2022\n')
s = 'Academia Capgemini 2022'
print('Saída:')
print(*encript(s))
print('---------------------------\n')

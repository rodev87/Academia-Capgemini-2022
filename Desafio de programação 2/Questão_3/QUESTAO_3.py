# Importação das funções sqrt e ceil, que
# fazem parte do módulo de matemática do Python.
from math import sqrt, ceil


def encript(s):
    # Remove os espaços da string "s" com o método replace()
    # O texto assim obtido é armazenado na variável "t":
    t = s.replace(" ", "")

    # Calcula a raíz quadrada de length de "t" com a função sqrt(),
    # e arredonda o resultado para cima com a função ceil():
    raiz_de_t = ceil(sqrt(len(t)))

    matriz = []

# Seleciona uma coluna:
    for i in range(raiz_de_t):
        coluna = []

        # Percorre a coluna selecionada, armazenando seus itens em listas.
        for j in range(i, len(t), raiz_de_t):
            coluna.append(t[j])

        # Com o método join(), cada lista é transformada em uma string.
        # As strings criadas são armazenadas na matriz,
        # que será devolvida pela função ao final da execução:
        matriz.append("".join(coluna))
    return matriz


# Testes:
print(f"{'-='*8}Teste 1{'=-'*8}\nEntrada:\ns = tenha um bom dia\n")
s = 'tenha um bom dia'
print('Saída:')
print(*encript(s))


print(f"{'-='*8}Teste 2{'=-'*8}\nEntrada:\ns = ola mundo\n")
s = 'ola mundo'
print('Saída:')
print(*encript(s))


print(f"{'-='*8}Teste 3{'=-'*8}\nEntrada:\ns = Academia Capgemini 2022\n")
s = 'Academia Capgemini 2022'
print('Saída:')
print(*encript(s))
print(f"{'_'*39}\n")

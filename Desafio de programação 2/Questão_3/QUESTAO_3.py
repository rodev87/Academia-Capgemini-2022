# Importação das funções sqrt e ceil,
# do módulo de matemática do Python.
from math import sqrt, ceil



def encript(s):
    # Remove os espaços da string "s" com o método replace()
    # O texto assim obtido é armazenado na variável "t":
    t = s.replace(" ", "")

    # Calcula a raíz quadrada de length de "t" com a função sqrt(),
    # e arredonda o resultado para cima com a função ceil():
    raiz_de_t = ceil(sqrt(len(t)))

    matriz = []

    # Percorre a string "t" por meio de uma estrutura de repetição aninhada cujo
    # passo é "raiz_de_t", agrupando assim os itens de "t" em listas que
    # irão representar as colunas do grid descrito no enunciado:
    for i in range(raiz_de_t):
        coluna = []
        for j in range(i, len(t), raiz_de_t):
            coluna.append(t[j])

        # Com o método join(), cada lista é transformada em uma string.
        # As strings criadas são armazenadas na variável matriz,
        # que será devolvida pela função ao final da execução:
        matriz.append("".join(coluna))
    return matriz


# Teste 1:
print(f"{'-='*8}Teste 1{'=-'*8}\nEntrada:\ns = tenha um bom dia\n")
s = 'tenha um bom dia'
print('Saída:')
print(*encript(s))

# Teste 2:
print(f"{'-='*8}Teste 2{'=-'*8}\nEntrada:\ns = ola mundo\n")
s = 'ola mundo'
print('Saída:')
print(*encript(s))

# Teste 3:
print(f"{'-='*8}Teste 3{'=-'*8}\nEntrada:\ns = Academia Capgemini 2022\n")
s = 'Academia Capgemini 2022'
print('Saída:')
print(*encript(s))
print(f"{'_'*39}\n")

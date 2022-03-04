def fatiamento(string):
    lista_fatias = []
    fim = 1
    while fim <= len(string):
        for inicio in range(len(string)):
            if inicio < fim:
                fatia = string[inicio:fim]
                if fatia != string and fatia not in lista_fatias:
                    lista_fatias.append(fatia)
        fim += 1
    return lista_fatias


def agrupa(substrings):
    agrupa_subs = []
    for substring in substrings:
        qtd_ocorrencias = 0
        area = len(substring)
        for i in range(len(palavra)):
            qtd_ocorrencias += palavra.count(substring, i, area)
            area += 1
        if qtd_ocorrencias > 1:
            agrupa_subs.append([substring]*qtd_ocorrencias)
    return agrupa_subs


def compara_substrings(a, b):
    cont = 0
    for i in range(len(a)):
        if a.count(a[i]) == b.count(a[i]):
            cont += 1
    return len(a) == cont


def busca_anagramas(substrings):
    for i in range(len(substrings)):
        a = substrings[i]
        for j in range(len(substrings)-1, i, -1):
            b = substrings[j]
            if a != b and len(a) == len(b) and [b, a] not in anagramas:
                if compara_substrings(a, b):
                    anagramas.append([a, b])


palavra = input('Digite uma palavra: ')
substrings = fatiamento(palavra)
anagramas = agrupa(substrings)
busca_anagramas(substrings)

print(len(anagramas))

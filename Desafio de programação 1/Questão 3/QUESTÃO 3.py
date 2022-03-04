def fatiamento(string):
    lista_fatias = []
    for i in range(len(string)):
        for j in range(len(string), i, -1):
            if string[i:j] != string and string[i:j] not in lista_fatias:
                lista_fatias.append(string[i:j])
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
        for j in range(len(substrings)-1, i, -1):
            if len(substrings[i]) == len(substrings[j]):
                if compara_substrings(substrings[i], substrings[j]):
                    anagramas.append([substrings[i], substrings[j]])


palavra = input('Digite uma palavra: ')
substrings = fatiamento(palavra)
anagramas = agrupa(substrings)
busca_anagramas(substrings)

print(len(anagramas))

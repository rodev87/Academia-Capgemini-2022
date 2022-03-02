def cont_caracteres(n):
    return 6-n


senha = input('Digite sua senha: ')
if len(senha) < 6:
    print(cont_caracteres(len(senha)))

<h1>Questão 02</h1>

Algoritmo criado em Python para solucionar o problema abaixo:

<i>"Dado um vetor de inteiros n e um inteiro qualquer x. Construa um algoritmo que determine o número de elementos pares do vetor que tem uma diferença igual ao valor de x."</i>


<h2>Proposta de solução</h2>


Para solucionar o problema, criamos a função compara_itens( ), que recebe uma lista de números inteiros como parâmetro. Dentro da função, uma estrutura de repetição aninhada é responsável por selecionar pares de itens para verificação. Uma estrutura de seleção verifica se o valor de x é positivo ou negativo, e chama a função de verificação correspondente.

```Python
def compara_itens(n):
    lista = []
    for i in range(len(n)):
        for j in range(len(n)-1, i, -1):
            if x >= 0:
                if verifica_xpositivo(n[i], n[j]):
                    lista.append([n[i], n[j]])
            else:
                if verifica_xnegativo(n[i], n[j]):
                    lista.append([n[i], n[j]])
    return len(lista)
```

Se a função de verificação retornar verdadeiro, os pares serão incluídos na variável local lista. Ao final da execução, a função devolverá o lenght de lista, que é a quantidade de pares identificados.


```Python
def verifica_xpositivo(a, b):
    if a >= b:
        return a - b == x
    else:
        return b - a == x

def verifica_xnegativo(a, b):
    if a < b:
        return a - b == x
    else:
        return b - a == x
```
Para a realização dos testes, foram criadas no escopo global a variável "n", que armazena a lista de números, a variável x, e a variável "pares", responsável por chamar a função compara_itens( ), bem como armazenar o valor devolvido pela função. Por fim, a função print( ) exibe a quantidade de pares encontrados: 


```Python
# Teste 1
n = [1, 5, 3, 4, 2]
x = 2
pares = compara_itens(n)
print(f'Saída:\n{pares}')
```


<h2>Para rodar a aplicação, siga as instruções abaixo:</h2>
<ol>
    <li>Instale a última versão do Python;</li>
    <li>Baixe o arquivo com a extensão .py;</li>
    <li>Clique com o botão direito do mouse no arquivo baixado e selecione a opção "Edit with IDLE";</li>
    <li>Com o IDLE aberto, pressione a tecla F5 para rodar a aplicação.</li>
</ol>
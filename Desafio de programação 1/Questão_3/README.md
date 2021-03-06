<h1>Questão 03</h1>

Algoritmo criado em Python para solucionar o problema abaixo:

<i>"Duas palavras podem ser consideradas anagramas de si mesmas se as letras de uma palavra podem ser realocadas para formar a outra palavra. Dada uma string qualquer, desenvolva um algoritmo que encontre o número de pares de substrings que são anagramas."</i>

    Exemplo 2)

    Entrada:
    ifailuhkqq

    Saída:
    3
    Explicação:
    
    A lista de todos os anagramas pares são: [i, i], [q, q] e [ifa, fai] que estão nas posições [[0],
    [3]], [[8], [9]] e [[0, 1, 2], [1, 2, 3]].

<h2>Proposta de solução</h2>

Após ler uma sequência de caracteres digitada pelo usuário, e armazená-la na variável global "palavra", a função "fatiamento(string)" é chamada. Nela é operado o fatiamento da string original em todas as suas substrings, e que ficarão armazenadas em formato de lista na variável global "substrings".

```Python
def fatiamento(string):
    lista_fatias = []
    for i in range(len(string)):
        for j in range(len(string), i, -1):
            if string[i:j] != string and string[i:j] not in lista_fatias:
                lista_fatias.append(string[i:j])
    return lista_fatias
```

 Em seguida, a função "agrupa(substrings)" é chamada para percorrer a string original "palavra" e verificar a quantidade de ocorrências de cada substring ao longo da sequência. A sequência é percorrida respeitando o tamanho de cada substring (armazenado na variável "area"), possibilitando identificar possíveis interseções de substrings. Por exemplo, na string "banana", a substring "ana" aparece duas vezes. O último caractere "a" da primeira ocorrência de "ana" também é o primeiro caractere "a" da segunda ocorrência.
 
 As substrings com mais de uma ocorrência serão agrupadas com seus pares e armazenadas em formato de lista na variável local "agrupa_subs", que é devolvida pela função e armazenada na variável global "anagramas".

```Python
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
```
 
 Em seguida, a função "busca_anagramas(substrings)" é chamada para identificar substrings de mesmo tamanho, mas diferentes entre si. Uma estrutura de repetição encadeada busca pelas substrings de mesmo tamanho e chama a função "compara_substrings(a, b)", que irá comparar as quantidades de ocorrências de cada item do par de substrings. Se os itens aparecerem de forma proporcional em ambas as substrings, isto significa que são anagramas, e serão armazenadas em pares na lista da variável global "anagramas".

```Python
def busca_anagramas(substrings):
    for i in range(len(substrings)):
        for j in range(len(substrings)-1, i, -1):
            if len(substrings[i]) == len(substrings[j]):
                if compara_substrings(substrings[i], substrings[j]):
                    anagramas.append([substrings[i], substrings[j]])


def compara_substrings(a, b):
    cont = 0
    for i in range(len(a)):
        if a.count(a[i]) == b.count(a[i]):
            cont += 1
    return len(a) == cont
```

 Por fim, com uma combinação de duas funções embutidas do Python, é exibido na tela o número de pares de substrings que são anagramas.

 ```Python
 print(len(anagramas))
 ```


<h2>Para rodar a aplicação, siga as instruções abaixo:</h2>
<ol>
    <li>Instale a última versão do Python;</li>
    <li>Baixe o arquivo com a extensão .py;</li>
    <li>Clique com o botão direito do mouse no arquivo baixado e selecione a opção "Edit with IDLE";</li>
    <li>Com o IDLE aberto, pressione a tecla F5 para rodar a aplicação.</li>
</ol>
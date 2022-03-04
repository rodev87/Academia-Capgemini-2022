Algoritmo criado em Python para solucionar o problema abaixo:

"Questão 03 - Duas palavras podem ser consideradas anagramas de si mesmas se as letras de uma palavra podem ser realocadas para formar a outra palavra. Dada uma string qualquer, desenvolva um algoritmo que encontre o número de pares de substrings que são anagramas."


<h2>Proposta de solução</h2>

Após ler uma sequência de caracteres digitada pelo usuário, e armazená-la na variável global "palavra", a função "fatiamento(string)" é chamada. Nela é operado o fatiamento da string original em todas as suas substrings, e que ficarão armazenadas em formato de lista na variável global "substrings".

 Em seguida, a função "agrupa(substrings)" é chamada para percorrer a string original "palavra" e verificar a quantidade de ocorrências de cada substring ao longo da sequência. A sequência é percorrida respeitando o tamanho de cada substring (armazenado na variável "area"), possibilitando identificar possíveis interseções de substrings. Por exemplo, na string "banana", a substring "ana" aparece duas vezes. O último caractere "a" da primeira ocorrência de "ana" também é o primeiro caractere "a" da segunda ocorrência.
 
 As substrings com mais de uma ocorrência serão agrupadas com seus pares e armazenadas em formato de lista na variável local "agrupa_subs", que é devolvida pela função e armazenada na variável global "anagramas".
 
 Em seguida, a função "busca_anagramas(substrings)" é chamada para identificar substrings de mesmo tamanho, mas diferentes entre si. Uma estrutura de repetição encadeada busca pelas substrings de mesmo tamanho e chama a função "compara_substrings(a, b)", que irá comparar as quantidades de ocorrências de cada item do par de substrings. Se os itens aparecerem de forma proporcional em ambas as substrings, isto significa que são anagramas, e serão armazenadas em pares na lista da variável global "anagramas".

 Finalmente, com uma combinação de duas funções embutidas do Python "print(len(anagramas))" é exibido na tela o número de pares de substrings que são anagramas.


<h2>Para rodar a aplicação, siga a instruções abaixo:</h2>
<ol>
    <li>Instale a última versão do Python;</li>
    <li>Baixe o arquivo com o nosso algoritmo;</li>
    <li>Clique com o botão direito do mouse no arquivo baixado e selecione a opção "Edit with IDLE";</li>
    <li>Com o IDLE aberto, pressione a tecla F5 para rodar a aplicação.</li>
</ol>
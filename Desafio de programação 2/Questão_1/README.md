<h1>Questão 01</h1>

Algoritmo criado em Python para solucionar o problema abaixo:

<i>"A mediana de uma lista de números é basicamente o elemento que se encontra no meio da lista após a ordenação. Dada uma lista de números com um número ímpar de elementos, desenvolva um algoritmo que encontre a mediana."</i>


<h2>Proposta de solução</h2>


Para solucionar o problema, criamos a função calc_mediana( ), que ao receber uma lista de elementos numéricos como parâmetro:
<ul>
    <li>ordena a lista utilizando o método embutido list.sort(); </li>
    <li>calcula a divisão inteira de lenght de lista por 2, atribuindo o resultado à variável local i, que servirá de índice; </li>
    <li>e devolve o valor armazenado no índice i da lista (que é a mediana).</li>
 </ul>


```Python
def calc_mediana(arr):
    arr.sort()
    i = len(arr)//2
    return arr[i]
```
Para a realização dos testes, foram criadas no escopo global a variável "arr", que armazena a lista de números, e a variável "mediana", responsável por chamar a função calc_mediana( ) e armazenar o valor devolvido. Por fim, a função print imprime a mediana:


```Python
# Teste 1
arr = [7, 3, 1, 9, 6, 101, 33, 20, 2]
mediana = calc_mediana(arr)
print(f'Saída:\n{mediana}')
```


<h2>Para rodar a aplicação, siga a instruções abaixo:</h2>
<ol>
    <li>Instale a última versão do Python;</li>
    <li>Baixe o arquivo com o nosso algoritmo;</li>
    <li>Clique com o botão direito do mouse no arquivo baixado e selecione a opção "Edit with IDLE";</li>
    <li>Com o IDLE aberto, pressione a tecla F5 para rodar a aplicação.</li>
</ol>
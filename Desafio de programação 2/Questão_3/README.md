<h1>Questão 03</h1>

Algoritmo criado em Python para solucionar o problema abaixo:

<i>"Um texto precisa ser encriptado usando o seguinte esquema. Primeiro, os espaços são removidos do texto. Então, os caracteres são escritos em um grid, no qual as linhas e colunas tem as seguintes regras: Considere T, como o tamanho do texto. Se certifique de que linhas x colunas >= T. Se múltiplos grids satisfazem as condições, escolha aquele com a menor área. Escreva um algoritmo que ao receber uma string s, mostre a mensagem encriptada de acordo com as regras descritas."</i>

    Exemplo 1)

    Entrada:
    s = tenha um bom dia

    Saída:
    taoa eum nmd hbi

    Explicação:
    Depois de remover os espaços, a string tem 13 caracteres. [A raíz quadrada de 13] está entre 3 e 4, então a string é rescrita na forma de um grid com 4 linhas e 4 colunas:

    tenh
    aumb
    omdi
    a

    O resultado é obtido ao mostrar os caracteres de cada coluna, com um espaço entre as colunas de texto. A mensagem encriptada é obtida ao mostrar os caracteres de cada linha com um espaço entre as colunas.


<h2>Proposta de solução</h2>

Para solucionar o problema, criamos a função encript( ), que ao receber uma string como parâmetro:
<ul>
    <li>remove os espaços existentes na string com o método embutido replace( ), armazenando a nova string sem espaços na variável local "t";</li>
    <li>calcula a raíz quadrada do comprimento de "t" utilizando a função sqrt( ) do módulo de matemática integrado do Python, e arredonda o resultado para cima com a função ceil( ) (também do módulo math), armazenando o valor na variável local "raiz_de_t";</li>
    <li>percorre a string "t" por meio de uma estrutura de repetição aninhada cujo passo é "raiz_de_t", agrupando assim os itens de "t" em listas que irão representar as colunas do grid descrito no enunciado, mas sem a necessidade de criá-lo na memória;</li>
    <li>converte para string cada uma das listas criadas ao longo das iterações, com o método embutido join( );</li>
    <li>e, por fim, armazena as strings obtidas em uma variável local (matriz), que será devolvida pela função ao final da execução.</li>
 </ul>


```Python
def encript(s):
    t = s.replace(" ", "")
    raiz_de_t = ceil(sqrt(len(t)))
    matriz = []
    for i in range(raiz_de_t):
        coluna = []
        for j in range(i, len(t), raiz_de_t):
            coluna.append(t[j])
        matriz.append("".join(coluna))
    return matriz
```

No escopo local, a função print( ) é responsável por chamar a função encript( ). E, com um asterisco adicional, a própria função print( ) realiza o desempacotamento da lista de strings devolvida pela função encript( ), exibindo a menssagem encriptada na tela:

```Python
print(*encript(s))
```

Para a realização dos testes, foi criada no escopo global a variável "s", que armazena a string a ser encriptada, e que será o argumento para a chamada da função encript( ).

```Python
# Teste 1:
s = 'tenha um bom dia'
print(*encript(s))
```


<h2>Para rodar a aplicação, siga as instruções abaixo:</h2>
<ol>
    <li>Instale a última versão do Python;</li>
    <li>Baixe o arquivo com a extensão .py;</li>
    <li>Clique com o botão direito do mouse no arquivo baixado e selecione a opção "Edit with IDLE";</li>
    <li>Com o IDLE aberto, pressione a tecla F5 para rodar a aplicação.</li>
</ol>
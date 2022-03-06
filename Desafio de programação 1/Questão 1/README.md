<h1>Questão 01</h1>

Algoritmo criado em Python para solucionar o problema abaixo:

"Escreva um algoritmo que mostre na tela uma escada de tamanho n utilizando o caractere * e espaços. A base e altura da escada devem ser iguais ao valor de n. A última linha não deve conter nenhum espaço."


<h2>Proposta de solução</h2>

Após ler um número inteiro (n) digitado pelo usuário, uma estrutura de repetição percorre o intervalo de 1 a n, imprimindo a cada iteração o caractere '*' vezes o número atual (i), concatenado ao espaço (' ') vezes o resultado da expressão n - i:

```Python
n = int(input('Digite um número inteiro: '))

for i in range(1, n + 1):
    print(f"{(n - i) * ' ' + i * '*'}")
```

<h2>Para rodar a aplicação, siga a instruções abaixo:</h2>
<ol>
    <li>Instale a última versão do Python;</li>
    <li>Baixe o arquivo com o nosso algoritmo;</li>
    <li>Clique com o botão direito do mouse no arquivo baixado e selecione a opção "Edit with IDLE";</li>
    <li>Com o IDLE aberto, pressione a tecla F5 para rodar a aplicação.</li>
</ol>
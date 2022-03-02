Algoritmo criado em Python para solucionar o problema abaixo:

"Questão 02 - Débora se inscreveu em uma rede social para se manter em contato com seus amigos. A página de cadastro exigia o preenchimento dos campos de nome e senha, porém a senha precisa ser forte. O site considera uma senha forte quando ela satisfaz os seguintes critérios:
● Possui no mínimo 6 caracteres.
● Contém no mínimo 1 digito.
● Contém no mínimo 1 letra em minúsculo.
● Contém no mínimo 1 letra em maiúsculo.
● Contém no mínimo 1 caractere especial. Os caracteres especiais são: !@#$%^&*()-+

Débora digitou uma string aleatória no campo de senha, porém ela não tem certeza se é uma senha forte. Para ajudar Débora, construa um algoritmo que informe qual é o número mínimo de caracteres que devem ser adicionados para uma string qualquer ser considerada segura."


<h2>Proposta de solução</h2>

Após ler a sequência de caracteres digitada pela usuária, e armazená-la na variável "senha", uma estrutura condicional verifica se a sequência possui quantidade insuficiente de caracteres para ser considerada uma senha forte (no mínimo 6 caracteres). Se a verificação resultar em verdadeiro, a função "cont_caracteres(n)" é chamada, e retorna quantos caracteres faltam para que a senha seja considerada segura quanto ao número mínimo de caracteres.


<h2>Para rodar a aplicação, siga a instruções abaixo:</h2>
<ol>
    <li>Instale a última versão do Python;</li>
    <li>Baixe o arquivo com o nosso algoritmo;</li>
    <li>Clique com o botão direito do mouse no arquivo baixado e selecione a opção "Edit with IDLE";</li>
    <li>Com o IDLE aberto, pressione a tecla F5 para rodar a aplicação.</li>
</ol>
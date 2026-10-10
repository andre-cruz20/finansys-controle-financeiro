FinanSys — Sistema de Controle Financeiro Pessoal

1. Sobre o projeto

O FinanSys é um sistema de controle financeiro pessoal desenvolvido para fins acadêmicos. Seu objetivo é permitir que os usuários registrem e acompanhem suas receitas e despesas de maneira simples e organizada.

O projeto será utilizado como estudo de caso na disciplina de Arquitetura de Software e Computação em Nuvem, com foco na organização dos componentes, na manutenção e na evolução arquitetural.

2. Funcionalidades previstas

- Cadastro de receitas e despesas.
- Registro de descrição, valor, categoria, data e tipo de movimentação.
- Consulta do histórico financeiro.
- Cálculo automático do saldo geral.
- Consulta de receitas, despesas e saldo mensal.
- Exclusão de movimentações.
- Armazenamento persistente dos dados.

3. Tecnologias previstas

- Python: linguagem de programação.
- Flask: framework para a aplicação web.
- HTML: estrutura das páginas.
- CSS: estilização da interface.
- SQLite: armazenamento dos dados.
- Git e GitHub: controle de versões e hospedagem do código.

4. Organização planejada

O sistema será organizado em componentes responsáveis pela interface web, pelas regras de negócio e pelo acesso ao banco de dados.

Essa separação tem como objetivo facilitar a manutenção, os testes e futuras melhorias no sistema.

5. Integrantes

- André Cruz
- Adison Teixeira
- Filipe Carvalho

6. Situação do projeto

O repositório está sendo preparado para o desenvolvimento da primeira versão do FinanSys. As funcionalidades e a documentação serão atualizadas conforme a implementação avançar.

7. Execução

As instruções de instalação e execução serão adicionadas após a implementação e os testes da aplicação.


Como executar o projeto

Requisitos

- Python 3.10 ou superior
- Pip para instalação de bibliotecas

Instalação

1. Clone ou baixe este repositório.
2. Abra o terminal na pasta do projeto.
3. Instale a dependência com o comando:

pip install -r requirements.txt

Execução

Execute o comando:

python app.py

Depois, abra no navegador o endereço indicado no terminal, normalmente "http://127.0.0.1:5000".

Arquitetura atual

A versão inicial utiliza Python com Flask para receber as requisições e apresentar a interface HTML. As transações são armazenadas em um banco SQLite, criado automaticamente na primeira execução.

O código está concentrado inicialmente no arquivo "app.py", para facilitar a implementação da versão acadêmica inicial. Uma evolução futura poderá separar as rotas, as regras de negócio e o acesso aos dados em módulos independentes.

Limitações da versão inicial

- O sistema ainda precisa ser executado e testado em ambiente local.
- Não possui autenticação de usuários.
- O banco de dados é local, adequado para fins didáticos e uso individual.

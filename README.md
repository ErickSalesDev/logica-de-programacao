🏦 Sistemas Bancários em Python

Repositório de estudos de lógica de programação com foco em variáveis e condicionais, desenvolvido durante minha jornada como programador backend iniciante.


👨‍💻 Sobre este repositório
Este repositório reúne projetos práticos criados para consolidar os fundamentos da programação em Python. Cada projeto simula um problema real do mundo bancário, aplicando os conceitos de variáveis, condicionais e pensamento algorítmico.
Os projetos foram desenvolvidos de forma progressiva, aumentando a complexidade a cada etapa.

🛠️ Tecnologias utilizadas

Python 3


📁 Projetos
1. sistema_saque.py — Sistema de Saque
Simula o processo de saque em um caixa eletrônico.
Regras implementadas:

Verifica se a conta está bloqueada antes de prosseguir
Verifica se o saldo é suficiente para o saque
Exibe o novo saldo após o saque aprovado

Conceitos praticados: condicionais aninhadas, operações com float, ordem lógica das verificações

2. sistema_de_score.py — Aprovação de Empréstimo
Simula a análise de crédito para concessão de empréstimo bancário.
Regras implementadas:

Nega o empréstimo se o score for abaixo de 300
Aplica juros de 2% para score acima de 700
Aplica juros de 5% para score entre 300 e 700
Nega o empréstimo se o salário for insuficiente para cobrir a parcela mensal

Conceitos praticados: cálculo de juros, divisão em parcelas, múltiplas condicionais

3. transferencia_bancaria.py — Transferência Bancária
Simula o processamento de uma transferência entre contas.
Regras implementadas:

Verifica se a conta está bloqueada
Verifica se o saldo é suficiente
Exige senha especial para transferências acima de R$ 5.000,00
Exibe o novo saldo após a transferência aprovada

Conceitos praticados: condicionais aninhadas em vários níveis, comparação de strings, controle de fluxo

4. sistema-conta-bancaria.py — Abertura de Conta
Simula a avaliação de abertura de conta para novos clientes.
Regras implementadas:

Verifica a idade do cliente (menores precisam de responsável)
Valida o CPF (mínimo de 11 dígitos)
Define o tipo de conta com base na renda mensal (corrente ou poupança)
Aprova conta juvenil para menores acompanhados de responsável

Conceitos praticados: len() para validação de strings, condicionais com int() e str(), fluxos diferentes para perfis diferentes

📚 Conceitos aplicados

Variáveis e tipos de dados (str, int, float)
Entrada de dados com input()
Conversão de tipos (int(), float(), str())
Condicionais if, elif, else
Condicionais aninhadas
Operadores lógicos (and, or)
Operadores de comparação (<, >, <=, >=, ==)
Funções nativas: len(), round()
Pensamento algorítmico e ordem lógica das verificações


🚀 Como executar

Certifique-se de ter o Python 3 instalado. No terminal, navegue até a pasta do projeto e execute:
bashpython nome_do_arquivo.py
Exemplo:
bashpython sistema_saque.py

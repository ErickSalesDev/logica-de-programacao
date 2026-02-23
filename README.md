# 🏦 Sistemas Bancários em Python

Repositório de estudos de **lógica de programação** com foco em variáveis e condicionais, desenvolvido durante minha jornada como programador backend iniciante.

---

## 👨‍💻 Sobre o repositório

Este repositório reúne projetos práticos criados para consolidar os fundamentos da programação em Python.

Cada projeto simula situações inspiradas no contexto bancário, aplicando:

- Variáveis
- Estruturas condicionais
- Conversão de tipos
- Validação de dados
- Pensamento algorítmico

Os projetos foram desenvolvidos de forma progressiva, aumentando a complexidade a cada etapa.

---

## 🛠️ Tecnologias utilizadas

- Python 3

---

## 📁 Projetos

### 1️⃣ `sistema_saque.py` — Sistema de Saque

Simula o processo de saque em um caixa eletrônico.

**Regras implementadas:**

- Verifica se a conta está bloqueada
- Verifica se o saldo é suficiente
- Atualiza e exibe o novo saldo após saque aprovado

**Conceitos praticados:**

- Condicionais aninhadas  
- Operações com `float`  
- Ordem lógica das verificações  

---

### 2️⃣ `sistema_de_score.py` — Aprovação de Empréstimo

Simula a análise de crédito para concessão de empréstimo.

**Regras implementadas:**

- Score abaixo de 300 → empréstimo negado  
- Score acima de 700 → juros de 2%  
- Score entre 300 e 700 → juros de 5%  
- Empréstimo negado se salário não cobrir a parcela mensal  

**Conceitos praticados:**

- Cálculo de juros  
- Divisão em parcelas  
- Múltiplas condicionais  
- Comparação entre valores  

---

### 3️⃣ `transferencia_bancaria.py` — Transferência Bancária

Simula o processamento de uma transferência entre contas.

**Regras implementadas:**

- Verifica se a conta está bloqueada  
- Verifica se há saldo suficiente  
- Exige senha para transferências acima de R$ 5.000,00  
- Atualiza saldo após aprovação  

**Conceitos praticados:**

- Condicionais aninhadas em múltiplos níveis  
- Comparação de strings  
- Controle de fluxo  

---

### 4️⃣ `sistema-conta-bancaria.py` — Abertura de Conta

Simula a análise para abertura de conta bancária.

**Regras implementadas:**

- Menores de 18 anos precisam de responsável  
- CPF deve ter no mínimo 11 dígitos  
- Renda define tipo de conta (corrente ou poupança)  
- Conta juvenil aprovada apenas com responsável  

**Conceitos praticados:**

- `len()` para validação de strings  
- Conversão de tipos com `int()` e `float()`  
- Estruturas condicionais aninhadas  
- Separação de fluxos por perfil de cliente  

---

## 📚 Conceitos aplicados

- Variáveis e tipos de dados (`str`, `int`, `float`)  
- Entrada de dados com `input()`  
- Conversão de tipos  
- Condicionais `if`, `elif`, `else`  
- Condicionais aninhadas  
- Operadores lógicos (`and`, `or`)  
- Operadores de comparação (`<`, `>`, `<=`, `>=`, `==`)  
- Funções nativas: `len()`, `round()`  
- Organização de fluxo e raciocínio lógico  

---

## 🚀 Como executar

Certifique-se de ter o **Python 3** instalado.

No terminal, navegue até a pasta do projeto e execute:

```bash
python nome_do_arquivo.py

# SISTEMA-DE-GEST-O-DE-NOTAS-E-FALTAS-GradeSystem

## Descrição

O Sistema de Gestão de Notas e Faltas foi desenvolvido em Python com o objetivo de simular o controle acadêmico de estudantes da Educação Básica.

O sistema permite cadastrar informações acadêmicas, registrar notas e faltas, calcular automaticamente a nota final e a frequência do estudante, determinar sua situação acadêmica e gerar um relatório final completo.

Este projeto foi desenvolvido como atividade avaliativa da disciplina de Programação.

---

## Objetivo

Desenvolver um sistema capaz de:

* Cadastrar estudantes;
* Selecionar o nível da educação básica;
* Registrar notas das disciplinas;
* Registrar faltas;
* Calcular a nota final;
* Calcular a frequência escolar;
* Determinar a situação final do estudante;
* Gerar relatório acadêmico.

---

## Funcionalidades

### Cadastro do estudante

O sistema solicita o nome do estudante e o nível de ensino.

### Níveis da Educação Básica

* Educação Infantil
* Ensino Fundamental I
* Ensino Fundamental II
* Ensino Médio

### Disciplinas por segmento

#### Educação Infantil

* Linguagem
* Matemática Básica
* Artes

#### Ensino Fundamental I

* Português
* Matemática
* Ciências

#### Ensino Fundamental II

* Português
* Matemática
* História
* Geografia
* Ciências

#### Ensino Médio

* Português
* Matemática
* Física
* Química
* Biologia

### Registro de Notas

Para cada disciplina são registradas:

* Nota da Prova 1
* Nota da Prova 2
* Nota do Trabalho

### Registro de Frequência

O sistema solicita:

* Quantidade de faltas
* Total de aulas

Com essas informações é calculado o percentual de frequência.

---

## Regras de Negócio

### Nota Final

A nota final é calculada pela soma das avaliações:

Nota Final = Prova 1 + Prova 2 + Trabalho

### Frequência

A frequência é calculada pela fórmula:

Frequência (%) = ((Total de Aulas - Faltas) / Total de Aulas) × 100

### Critérios de Aprovação

#### Aprovado

* Nota final maior ou igual a 6;
* Frequência maior ou igual a 75%.

#### Reprovado por Nota

* Nota final menor que 6;
* Frequência maior ou igual a 75%.

#### Reprovado por Falta

* Frequência menor que 75%, independentemente da nota.

---

## Relatório Final

Ao final da execução o sistema apresenta:

* Nome do estudante;
* Nível da educação básica;
* Nome da disciplina;
* Nota final calculada;
* Total de faltas;
* Percentual de frequência;
* Situação final.

Também é exibido um resumo contendo:

* Quantidade de disciplinas aprovadas;
* Quantidade de disciplinas reprovadas por nota;
* Quantidade de disciplinas reprovadas por falta.

---

## Tecnologias Utilizadas

* Python 3

---

## Conceitos Aplicados

Durante o desenvolvimento foram utilizados os seguintes conceitos:

* Variáveis;
* Entrada e saída de dados;
* Estruturas condicionais (if, elif e else);
* Estruturas de repetição (for);
* Funções;
* Listas;
* Dicionários;
* Modularização do código.

---

## Integrantes

* Nome do Integrante 1
* Nome do Integrante 2
* Nome do Integrante 3
* Nome do Integrante 4
* Nome do Integrante 5

---

## Disciplina

Programação de Computadores

## Instituição

Centro Universitário do Distrito Federal – UDF

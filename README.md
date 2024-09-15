# 🧮 Operações Matemáticas com Funções Lambda em Python

Este repositório contém um código simples que demonstra o uso de **funções lambda** para realizar operações matemáticas básicas em Python. As operações implementadas são:

- Soma
- Subtração
- Multiplicação
- Divisão
- Módulo


## Descrição

As funções lambda são funções anônimas em Python, definidas com a palavra-chave `lambda`. Elas são úteis para criar funções simples de forma concisa. Neste exemplo, usamos lambdas para realizar cinco operações matemáticas básicas.

## Código

```python
# Variáveis com lambdas para operações matemáticas
soma = lambda a, b: a + b
subtracao = lambda a, b: a - b
multiplicacao = lambda a, b: a * b
divisao = lambda a, b: a / b if b != 0 else 'Divisão por zero não permitida'
modulo = lambda a, b: a % b
```

## Exemplo de Uso

Suponha que `a = 10` e `b = 5`. Para realizar as operações, usamos as funções lambdas definidas:

```python
a, b = 10, 5
print(f"Soma: {soma(a, b)}")            
print(f"Subtração: {subtracao(a, b)}") 
print(f"Multiplicação: {multiplicacao(a, b)}")
print(f"Divisão: {divisao(a, b)}")
print(f"Módulo: {modulo(a, b)}")
```

## Resultado

A saída das operações será:

```markdown
Soma: 15
Subtração: 5
Multiplicação: 50
Divisão: 2.0
Módulo: 0
```

Para o caso de divisão por zero:

```python
a, b = 10, 0
print(f"Divisão: {divisao(a, b)}")
```

A saída será: `Divisão por zero não permitida`.

"""
Este programa executa operações matemáticas básicas usando funções lambda em Python.

Autor: Prof. Sauer
Versão: 1.97
Site: www.sauer.pro.br
Email: sauer@simplificatreinamentos.com.br
Instagram: https://www.instagram.com/prof.alesauer/
Facebook: https://www.facebook.com/prof.alesauer/
YouTube:  https://www.youtube.com/@prof.alesauer
LinkedIn: www.linkedin.com/in/alesauer
"""

# Variáveis com lambdas para operações matemáticas
soma = lambda a, b: a + b
subtracao = lambda a, b: a - b
multiplicacao = lambda a, b: a * b
divisao = lambda a, b: a / b if b != 0 else 'Divisão por zero não permitida'
modulo = lambda a, b: a % b

# Testando as funções
a, b = 10, 5
print(f"Soma: {soma(a, b)}")            
print(f"Subtração: {subtracao(a, b)}") 
print(f"Multiplicação: {multiplicacao(a, b)}")
print(f"Divisão: {divisao(a, b)}")
print(f"Módulo: {modulo(a, b)}")

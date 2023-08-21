"""
Desenvolver um programa que apresente os resultados de uma tabela de um número qualquer. Ela deve ser
impressa no seguinte formato:

considerando como exemplo o fornecimento do número 2
2 . 1 = 2
2 . 2 = 4
2 . 3 = 6
2 . 4 = 8
2 . 5 = 10
(...)
2 . 10 = 20
"""

numero = int(input("Digite um número: "))
i = 1

while (i <= 10):
    resultado = numero * i
    print(f"{numero} . {i} = {resultado}")
    i += 1
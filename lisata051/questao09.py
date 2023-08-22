"""
Elaborar um programa que apresente no final a soma dos valores pares existentes na faixa de 0 até 500. Utilize
um laço que efetue a variação de 2 em 2
"""

soma = 0
numero = 0

while (numero <= 500):
    soma += numero
    numero += 2

print("A soma dos valores pares de 0 a 500 é:", soma)
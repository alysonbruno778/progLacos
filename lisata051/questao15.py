"""
Desenvolver um programa que apresente a série de Fibonacci até o décimo quinto termo. A série de Fibonacci é
formada pela sequência 1,1,2,3,5,8,13,21,34, ... etc. Ela se caracteriza pela soma de um termo posterior com seu
anterior subsequente
"""

termo_anterior = 1
termo_atual = 1

print(termo_anterior)
print(termo_atual)

contador = 0
while contador < 13:  # Vamos calcular até o décimo quinto termo (já imprimimos os dois primeiros)
    proximo_termo = termo_anterior + termo_atual
    print(proximo_termo)

    termo_anterior = termo_atual
    termo_atual = proximo_termo

    contador += 1
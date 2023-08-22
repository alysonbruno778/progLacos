"""
Desenvolver um programa que peça ao usuário para digitar diversos números reais, e ao final, exibir o maior e o
menor número que foram digitados, além da média entre TODOS os números digitados pelo usuário. A inserção
de números deve parar quando o usuário digitar o número -1, e este número -1 não deve ser considerado nem
como maior, nem como menor, e nem na contagem da média
"""

num = float(input("Digite um número (-1 encerra o prograna): "))
maior = num
menor = num
total_respostas = 0
soma = 0

while ( num != -1 ):
    total_respostas = total_respostas + 1
    if ( maior < num ):
        maior = num

    if ( maior > num ):
        maior = num

    num = float(input("Digite outro número (-1 encerra o prograna): "))

if ( maior == -1):
    print("Você inseriu -1 na primeira resposta.\nPROGRAMA ENCERRADO! ")
print(f"Maior valor inserido: {maior}")
print(f"Menor valor inserido: {menor}")
print(f"Média dos valores inseridos: {soma/total_respostas}")
print("FIM DO PROGRAMA")


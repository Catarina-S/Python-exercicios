# faça um algoritmo que solicite ao usuário números e os armazene em um vetor de 6 posições.
# O usuário deverá inserir valores positivos e negativos.
# Substitua todas as ocorrência de valores positivos por 1 e todos os valores negativos por 0.

vet = [0]*6
cont = 0

for cont in range(0,6,1):
    vet[cont] = int(input(f"Insira um número positivo ou negativo na posição {cont}: "))

    if (vet[cont] > 0):
        vet[cont] = 1
        print("O valor que você digitou foi transformado em ",vet[cont])
    else:
        if (vet[cont] < 0):
            vet[cont] = 0
            print("O valor que você digitou foi transformado em ",vet[cont])
    
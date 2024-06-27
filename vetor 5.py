# faça um algoritmo que solicite ao usuário números e os armazene em um vetor de 30 posições.
# Crie uma função que recebe o vetor preenchido e substitua todas as
# ocorrências de valores positivos por 1 e todos os valores negativos por 0.

vet = [0] * 3
i = 0

for i in range(0,3,1):
    vet[i] = int(input(f"Digite o número para a posição {i}: "))

    if (vet[i] > 0):
        vet[i] = 1
    else:
        vet[i] = 0

    print(f"Substituindo o valor por: {vet[i]}")

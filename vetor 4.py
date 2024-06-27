# Faça um algoritmo que leia 50 valores reais e armazene em um vetor.
# Modifique o vetor de modo que os valores das posições impares sejam
# aumentados em 5%, e os das posições pares sejam aumentados em 2%.
# Imprima depois o vetor resultante

vet = [0]*50
i = 0

for i in range(0,50,1):
    vet[i] = float(input(f"Informe um valor na posição {i}: "))

    if (vet[i] % 2 == 0):
        vet[i] = vet[i] * 1.02
    else:
        vet[i] = vet[i] * 1.05


print("Vetor resultante: ")
for i in range(0,50,1):
    print(f"{vet[i]}")
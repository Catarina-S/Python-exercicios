#crie um algoritmo que crie e leia um vetor com 6 posições e a partir disso faça: 
#-  percorra cada elemento do vetor fazendo:
#    -  se for um valor negativo, mostre o módulo (valor sem sinal) do valor; 
#    -  se for um valor maior do que 10, solicite outro valor e mostre a diferença entre eles;
#    -  Caso o valor não seja de nenhuma condição anterior, mostre o valor dividido por 5.

vet = [0]*6
cont = 0

for cont in range(0,6,1):
    vet[cont] = int(input(f"Digite um valor para a posição {cont}: "))

    if (vet[cont] < 0):
        print(vet[cont] * -1)
    else:
        if (vet[cont] > 10):
            valor = int(input("Digite um valor: "))
            print(vet[cont] - valor)
        else:
            print(vet[cont] / 5)

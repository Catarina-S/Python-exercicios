# Criar uma matriz 3x4 de números inteiros, solicite números para preencher essa matriz e 
# depois mostre a mesma na tela.

mat = [[0]*4, [0]*4, [0]*4]
linha = 0
coluna = 0

for linha in range(0,3,1):
    for coluna in range(0,4,1):
        mat[linha][coluna] = int(input(f"Informe um número para a linha {linha} e coluna {coluna}: "))

for linha in range(0,3,1):
    for coluna in range(0,4,1):
        print(f"[{mat[linha][coluna]}]", end='')
        print()

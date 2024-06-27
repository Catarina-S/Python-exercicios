# Criar um algoritmo que leia os elementos de uma matriz
# inteira 5 x 5 e escreva os elementos da diagonal principal

linha = 0
coluna = 0
mat = [[0]*5, [0]*5, [0]*5, [0]*5, [0]*5]

for linha in range(0,5,1):
    for coluna in range(0,5,1):
        mat[linha][coluna] = int(input(f"Informe um numero para linha {linha} e coluna {coluna}: "))

print("DIAGONAL PRINCIPAL: ")
for linha in range(0,5,1):
    for coluna in range(0,5,1):
        if(linha == coluna):
            print(f"[{mat[linha][coluna]}]", end='')

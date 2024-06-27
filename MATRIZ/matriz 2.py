# Faça um algoritmo que leia uma matriz 2 x 3 real
# e depois imprima a matriz original e depois gere e
# imprima sua matriz transposta (matriz 3 x 2 equivalente)


linha = 0
coluna = 0
mat =  [[0]*3, [0]*3] 
mat_trans = [[0]*2, [0]*2, [0]*2]

for linha in range(0,2,1):
  for coluna in range(0,3,1):
    mat[linha][coluna] = int(input(f"Informe o número para a posição {linha} {coluna}: "))

print("Matriz horiginal: ")
for linha in range(0,2,1):
  for coluna in range(0,3,1):
    print(f"[{mat[linha][coluna]}]", end='')

for linha in range(0,3,1):
    for coluna in range(0,2,1):
        mat_trans[linha][coluna] = int(input(f"Informe um numero para a linha {linha} e coluna {coluna}: "))


print("Matriz Transposta: ")
for linha in range(0,3,1):
    for coluna in range(0,2,1):
        print(f"[{mat_trans[linha][coluna]}]", end='')

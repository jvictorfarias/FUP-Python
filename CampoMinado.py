linhas_colunas = raw_input()
linhas_colunas = linhas_colunas.split(' ')
linhas = int(linhas_colunas[0])
colunas = int(linhas_colunas[1])
aux = ''


def criaMatriz(n_linhas, n_colunas):  # Function to create the  matrix
    matriz = []
    for i in range(n_linhas):
        linha = raw_input()
        matriz.append(list(linha))
    return matriz


def contaBombas(linha, coluna, matrix):
    bomb_count = 0
    # Cima
    if linha == 0:
        pass
    else:
        if matrix[linha - 1][coluna] == '*':
            bomb_count += 1
    # Baixo
    if linha == linhas - 1:
        pass
    else:
        if matrix[linha + 1][coluna] == '*':
            bomb_count += 1
    # Direita
    if coluna == colunas - 1:
        pass
    else:
        if matrix[linha][coluna + 1] == '*':
            bomb_count += 1
    # Esquerda
    if coluna == 0:
        pass
    else:
        if matrix[linha][coluna - 1] == '*':
            bomb_count += 1
    # Diagonal superior Direita
    if linha == 0 or coluna == colunas - 1:
        pass
    else:
        if matrix[linha - 1][coluna + 1] == '*':
            bomb_count += 1
    # Diagonal superior Esquerda
    if linha == 0 or coluna == 0:
        pass
    else:
        if matrix[linha - 1][coluna - 1] == '*':
            bomb_count += 1
    # Diagonal inferior Direita
    if linha == linhas - 1 or coluna == colunas - 1:
        pass
    else:
        if matrix[linha + 1][coluna + 1] == '*':
            bomb_count += 1
    # Diagonal inferior Esquerda
    if linha == linhas - 1 or coluna == 0:
        pass
    else:
        if matrix[linha + 1][coluna - 1] == '*':
            bomb_count += 1
    if bomb_count:
        return str(bomb_count)
    else:
        return '-'


matrix = criaMatriz(linhas, colunas)

for i in range(linhas):
    for j in range(colunas):
        if matrix[i][j] != '*':
            matrix[i][j] = contaBombas(i, j, matrix)
for i in range(linhas):
    for j in range(colunas):
        aux += str(matrix[i][j])
    print(''.join(aux))
    aux = ''

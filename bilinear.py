import numpy as np

def bilinear_interpolation_reduce(matrix):
    old_height = len(matrix)
    old_width = len(matrix[0])

    # Redução pela metade (divide por 2)
    new_height = old_height // 2
    new_width = old_width // 2

    # Cria uma nova matriz com as novas dimensões
    new_matrix = np.zeros((new_height, new_width))

    for i in range(new_height):
        for j in range(new_width):
            # Pixels vizinhos no bloco 2x2 da matriz original
            top_left = matrix[i*2][j*2]
            top_right = matrix[i*2][j*2 + 1]
            bottom_left = matrix[i*2 + 1][j*2]
            bottom_right = matrix[i*2 + 1][j*2 + 1]

            # Média dos 4 pixels
            new_matrix[i][j] = round((top_left + top_right + bottom_left + bottom_right) / 4)

    return new_matrix


#  ampliar a imagem por interpolação bilinear

def bilinear_interpolation_expand(matrix):
    old_height, old_width = len(matrix), len(matrix[0])
    
    new_height = 2 * old_height - 1
    new_width = 2 * old_width - 1
    
    new_matrix = np.zeros((new_height, new_width))
    
    # Preenche os pixels originais e interpolados
    for i in range(old_height - 1):
        for j in range(old_width - 1):
            # Os valores originais f(i,j), f(i+1,j), f(i,j+1), f(i+1,j+1)
            f_ij = matrix[i][j]
            f_ij1 = matrix[i][j+1]
            f_i1j = matrix[i+1][j]
            f_i1j1 = matrix[i+1][j+1]

            new_matrix[2 * i][2 * j] = f_ij

            # a = f(i,j) + f(i,j+1)) / 2
            new_matrix[2 * i][2 * j + 1] = round ((f_ij + f_ij1) / 2)
            
            # b = (f(i,j) + f(i+1,j)) / 2
            new_matrix[2 * i + 1][2 * j] = round((f_ij + f_i1j) / 2)
            
            # c = (f(i,j) + f(i,j+1) + f(i+1,j) + f(i+1,j+1)) / 4
            new_matrix[2 * i + 1][2 * j + 1] = round((f_ij + f_ij1 + f_i1j + f_i1j1) / 4)
            
            # d = (f(i,j+1) + f(i+1,j+1)) / 2
            new_matrix[2 * i + 1][2 * j + 2] = round((f_ij1 + f_i1j1) / 2)
            
            # e = (f(i+1,j) + f(i+1,j+1)) / 2
            new_matrix[2 * i + 2][2 * j + 1] = round((f_i1j + f_i1j1) / 2)
    
    for j in range(old_width - 1):
        new_matrix[new_height - 1][2 * j] = matrix[old_height - 1][j]
        new_matrix[new_height - 1][2 * j + 1] = round((matrix[old_height - 1][j] + matrix[old_height - 1][j + 1]) / 2)
    new_matrix[new_height - 1][new_width - 1] = matrix[old_height - 1][old_width - 1]
    
    for i in range(old_height - 1):
        new_matrix[2 * i][new_width - 1] = matrix[i][old_width - 1]
        new_matrix[2 * i + 1][new_width - 1] = round((matrix[i][old_width - 1] + matrix[i + 1][old_width - 1]) / 2)

    return new_matrix
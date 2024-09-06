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
            new_matrix[i][j] = (top_left + top_right + bottom_left + bottom_right) / 4

    return new_matrix


#  ampliar a imagem por interpolação bilinear

def bilinear_interpolation_expand(matrix, scale_factor):
    old_height = len(matrix)
    old_width = len(matrix[0])

    # Novas dimensões da matriz ampliada
    new_height = old_height * scale_factor
    new_width = old_width * scale_factor

    # Cria uma nova matriz para a imagem ampliada
    new_matrix = np.zeros((new_height, new_width))

    for i in range(new_height):
        for j in range(new_width):
            # Coordenadas correspondentes na matriz original
            x = i / scale_factor
            y = j / scale_factor

            # Vizinhos mais próximos
            x1 = int(np.floor(x))
            y1 = int(np.floor(y))
            x2 = min(x1 + 1, old_height - 1)
            y2 = min(y1 + 1, old_width - 1)

            # Pesos baseados na distância fracionária
            dx = x - x1
            dy = y - y1

            # Interpolação linear entre os vizinhos
            pixel1 = (1 - dx) * matrix[x1][y1] + dx * matrix[x2][y1]
            pixel2 = (1 - dx) * matrix[x1][y2] + dx * matrix[x2][y2]
            new_pixel = (1 - dy) * pixel1 + dy * pixel2

            new_matrix[i][j] = new_pixel

    return new_matrix
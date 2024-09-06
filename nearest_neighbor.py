# Diminuir por vizinho mais próximo:
def reduce_matrix_nearest_neighbor(matrix):
    reduced_matrix = []

    # Mantém apenas as linhas pares
    for i in range(0, len(matrix), 2):
        row = []
        # Mantém apenas as colunas pares
        for j in range(0, len(matrix[0]), 2):
            row.append(matrix[i][j])
        reduced_matrix.append(row)

    return reduced_matrix

# Ampliar por vizinho mais próximo:

def expand_matrix_nearest_neighbor(matrix):
    expanded_matrix = []

    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            # Duplica o valor para simular a expansão
            row.append(matrix[i][j])
            row.append(matrix[i][j])
        
        # Duplica a linha inteira
        expanded_matrix.append(row)
        expanded_matrix.append(row.copy())

    return expanded_matrix

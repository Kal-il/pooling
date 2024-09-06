def read_matrix_from_txt(file_path):
    with open(file_path, 'r') as file:
        matrix = []
        for line in file:
            row = list(map(int, line.split()))  # Convertendo cada linha em uma lista de inteiros
            matrix.append(row)
    return matrix
from read_matrix import read_matrix_from_txt
from bilinear import bilinear_interpolation_reduce, bilinear_interpolation_expand
from nearest_neighbor import expand_matrix_nearest_neighbor, reduce_matrix_nearest_neighbor
import numpy as np 

def main():
    op = 6
    while op != 5:
        print("--------------------")
        try:
            op = int(input("Saudações, desejan \n 1 - Ampliar a imagem por vizinho mais próximo \n 2 - Ampliar a imagem por interpolação bilinear \n 3 - Reduzir a imagem por vizinho mais próximo \n 4 - Reduzir a imagem por interpolação bilinear \n 5 - Sair \n->"))
        except ValueError:
            print("Opção inválida. Por favor, insira um número entre 1 e 5.")
            continue

        if op == 1:
            print("Ampliar a imagem por vizinho mais próximo")
            new_matrix = expand_matrix_nearest_neighbor(matrix)
            print("Matriz resultante após interpolação bilinear:")
            print(np.array(new_matrix))
        elif op == 2:
            print("Ampliar a imagem por interpolação bilinear")
            scale_factor = 2
            new_matrix = bilinear_interpolation_expand(matrix)
            print("Matriz resultante após interpolação bilinear:")
            print(np.array(new_matrix))
        elif op == 3:
            print("Reduzir a imagem por vizinho mais próximo")
            new_matrix = reduce_matrix_nearest_neighbor(matrix)
            print("Matriz resultante após interpolação bilinear:")
            print(np.array(new_matrix))
        elif op == 4:
            print("Reduzir a imagem por interpolação bilinear")
            scale_factor = 0.8
            new_matrix = bilinear_interpolation_reduce(matrix)
            print("Matriz resultante após interpolação bilinear:")
            print(np.array(new_matrix))
        elif op == 5:
            print("Saindo...")
        else:
            print("Opção inválida. Por favor, insira um número entre 1 e 5.")


file_path = "matrix-2.txt"
matrix = read_matrix_from_txt(file_path)
new_matrix = []   
if __name__ == "__main__":
    main()
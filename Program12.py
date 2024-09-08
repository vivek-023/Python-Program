import numpy as np

def main():
    # Define two matrices
    matrix1 = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]])

    matrix2 = np.array([[9, 8, 7],
                        [6, 5, 4],
                        [3, 2, 1]])

    # Add the matrices
    matrix_sum = np.add(matrix1, matrix2)

    # Print the result
    print("Matrix 1:")
    print(matrix1)

    print("\nMatrix 2:")
    print(matrix2)

    print("\nSum of the matrices:")
    print(matrix_sum)

    # Find the transpose of matrix1
    matrix1_transpose = np.transpose(matrix1)

    # Print the transpose
    print("\nTranspose of Matrix 1:")
    print(matrix1_transpose)


if __name__ == "__main__":
    main()

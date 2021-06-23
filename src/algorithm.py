import numpy as np

"""
    Algorithm to find if the i/p matrix is nilpotent or not.
    Principle:
        A matrix is nilpotent iff:
            1. The matrix is square and all the eigenvalues are 0.
                                or
            2. A square matrix A such that A^n is the zero matrix 0 for some positive 
               integer matrix power n, known as the index.
    
"""


def check_nilpotency(matrix):
    np_array = np.array(matrix, dtype=complex)
    eigenval, eigenvec = np.linalg.eig(
        np_array
    )  # calculating eigenvalues of the matrix

    # eigenval is array with all the eigen values of matrix
    for x in eigenval:
        if x != 0:  # if an eigenvalue is not 0, then matrix is not nilpotent
            return eigenval, False

    return eigenval, True  # if all the eigenvalues are 0. then matrix is nilpotent


if __name__ == "__main__":

    size = int(input("Enter Matrix Size: "))
    matrix = [[input() for x in range(size)] for y in range(size)]
    print(check_nilpotency(matrix))
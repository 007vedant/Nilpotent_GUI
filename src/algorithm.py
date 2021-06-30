from sympy import Matrix
from pprint import pprint

"""
    Vedant Raghuwanshi(118EE0705)
    EE3302 Advanced Control System Project: Algorithm to find if the i/p matrix is nilpotent or not.
    Principle:
        A matrix is nilpotent iff:
            1. The matrix is square and all the eigenvalues are 0.
                                or
            2. A square matrix A such that A^n is the zero matrix 0 for some positive 
               integer matrix power n, known as the index.  
"""


def check_nilpotency(matrix):
    sp_matrix = Matrix(matrix)
    eigenvalues = sp_matrix.eigenvals()  # finding eigenvalues of the input matrix

    # eigenvalues is dictionary with eigen values of the matrix as keys and their multiplicity as dictionary values.

    for x in eigenvalues.keys():
        if (
            x != 0
        ):  # if any value other than 0 is present in keys then matrix is NOT nilpotent
            return eigenvalues, False

    return eigenvalues, True  # matrix is nilpotent


if __name__ == "__main__":

    size = int(input("Enter Matrix Size: "))
    matrix = []
    for i in range(size):
        row = list(map(complex, input().split()))
        matrix.append(row)

    print("Your input matrix is:")
    print(matrix)
    print()
    eigvalues, isnilp = check_nilpotency(matrix)
    print(f"The matrix is nilpotent: {isnilp}")
    print()
    print("The eigen values of the matrix and their corresponding multiplicity are: \n")
    pprint(eigvalues)

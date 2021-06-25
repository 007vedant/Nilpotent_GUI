from sympy import Matrix

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
    matrix = [[input() for x in range(size)] for y in range(size)]
    eigvalues, isnilp = check_nilpotency(matrix)
    print(isnilp)
    print(eigvalues)
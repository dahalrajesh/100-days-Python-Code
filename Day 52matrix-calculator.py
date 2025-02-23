import numpy as np

def matrix_input():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    print("Enter matrix elements row-wise:")
    matrix = [list(map(int, input().split())) for _ in range(rows)]
    return np.array(matrix)

def main():
    print("Matrix Operations: 1. Addition 2. Multiplication 3. Transpose 4. Determinant")
    choice = int(input("Enter choice: "))

    if choice in [1, 2]:  # Addition and Multiplication need two matrices
        print("Enter first matrix:")
        A = matrix_input()
        print("Enter second matrix:")
        B = matrix_input()

        if choice == 1:
            print("Sum:\n", A + B)
        else:
            print("Product:\n", np.dot(A, B))

    elif choice == 3:
        print("Enter matrix:")
        A = matrix_input()
        print("Transpose:\n", A.T)

    elif choice == 4:
        print("Enter square matrix:")
        A = matrix_input()
        if A.shape[0] == A.shape[1]:
            print("Determinant:", np.linalg.det(A))
        else:
            print("Determinant is only for square matrices.")

if __name__ == "__main__":
    main()


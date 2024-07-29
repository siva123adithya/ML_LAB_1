def input_matrix(rows, cols):
     
    matrix = []
    print(f"Enter the elements for a {rows}x{cols} matrix:")
    for i in range(rows):
        row = list(map(int, input().split()))
        if len(row) != cols:
            print("Error: Incorrect number of elements in the row.")
            return None
        matrix.append(row)
    return matrix

def print_matrix(matrix):
     
    for row in matrix:
        print(" ".join(map(str, row)))

def are_matrices_multiplicable(a, b):
     
    return len(a) == len(b) and len(a[0]) == len(b[0])

def multiply_matrices_elementwise(a, b):
     
    rows = len(a)
    cols = len(a[0])
    return [[a[i][j] * b[i][j] for j in range(cols)] for i in range(rows)]

def main():
    print("Matrix A:")
    rows_a = int(input("Enter number of rows for matrix A: "))
    cols_a = int(input("Enter number of columns for matrix A: "))
    matrix_a = input_matrix(rows_a, cols_a)
   
    if matrix_a is None:
        return

    print("Matrix B:")
    rows_b = int(input("Enter number of rows for matrix B: "))
    cols_b = int(input("Enter number of columns for matrix B: "))
    matrix_b = input_matrix(rows_b, cols_b)
   
    if matrix_b is None:
        return

    if rows_a != rows_b or cols_a != cols_b:
        print("Error: Matrices must be of the same dimensions for element-wise multiplication.")
        return

    result_matrix = multiply_matrices_elementwise(matrix_a, matrix_b)
   
    print("Matrix A:")
    print_matrix(matrix_a)
   
    print("Matrix B:")
    print_matrix(matrix_b)
   
    print("Result of element-wise multiplication:")
    print_matrix(result_matrix)

if __name__ == "__main__":
    main()

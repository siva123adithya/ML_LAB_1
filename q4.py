def get_matrix_input():
   
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = []
   
    print("Enter the matrix elements row by row:")
    for i in range(rows):
        row = list(map(int, input().split()))
        if len(row) != cols:
            print(f"Warning: Row {i+1} does not match the specified number of columns.")
        matrix.append(row)
   
    return matrix

def transpose_matrix(matrix):
   
    if not matrix or not matrix[0]:
        return []
   
    rows = len(matrix)
    cols = len(matrix[0])
   
    transposed = []
    for c in range(cols):
        new_row = [matrix[r][c] for r in range(rows)]
        transposed.append(new_row)
   
    return transposed

def print_matrix(matrix):
   
    for row in matrix:
        print(" ".join(map(str, row)))

def main():
   
    print("Matrix Transposition Program")
    matrix = get_matrix_input()
    transposed = transpose_matrix(matrix)
   
    print("Original Matrix:")
    print_matrix(matrix)
   
    print("Transposed Matrix:")
    print_matrix(transposed)

if __name__ == "__main__":
    main()

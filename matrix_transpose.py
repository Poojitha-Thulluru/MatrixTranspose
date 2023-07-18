def get_transpose_matrix(input_matrix: list, n_rows: int, n_columns: int) -> list:
    transpose_matrix = [[0 for _ in range(n_rows)] for _ in range(n_columns)]
    for row in range(n_rows):
        for column in range(n_columns):
            transpose_matrix[column][row] = input_matrix[row][column]
    return transpose_matrix


try:
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    matrix = [[int(input(f"Enter element ({y}, {x}) to insert into the matrix: ")) for x in range(columns)]
              for y in range(rows)]
    print("The transpose of the given matrix is:", get_transpose_matrix(matrix, rows, columns))
except ValueError:
    print("Invalid input. Please enter only integers.")

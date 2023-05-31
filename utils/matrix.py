def matrix_convertion(string):
    matrix = []
    rows = string.split('\n')

    for r in rows:
        numbers_s = r.split()
        numbers = [int(n) for n in numbers_s]

        matrix.append(numbers)

    return matrix

def matrix_mult(matrix1, matrix2):
    if len(matrix1) != 1:
        # Check if the matrices can be multiplied
        if len(matrix1[0]) != len(matrix2):
            return "Error"

        # Create an empty result matrix
        result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

        # Perform matrix multiplication
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]

        return result

    else:
        constant = matrix1[0][0]
        result = []

        for row in matrix2:
            multiplied_row = [constant * element for element in row]
            result.append(multiplied_row)

        return result

def matrix_sum(matrix1, matrix2):
    if len(matrix1) != 1:
        # Check if the matrices have the same dimensions
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            return "Error"

        # Create an empty matrix to store the result
        result = []

        # Iterate over the rows of the matrices
        for i in range(len(matrix1)):
            row = []
            # Iterate over the elements in the current row
            for j in range(len(matrix1[0])):
                # Add the corresponding elements from the matrices
                element_sum = matrix1[i][j] + matrix2[i][j]
                row.append(element_sum)
            result.append(row)

        return result

    else:
        constant = matrix1[0][0]
        result = []

        for row in matrix2:
            multiplied_row = [constant + element for element in row]
            result.append(multiplied_row)

        return result

def matrix_sub(matrix1, matrix2):
    if len(matrix1) != 1:
        # Check if the matrices have the same dimensions
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            return "Error"

        # Create an empty matrix to store the result
        result = []

        # Iterate over the rows of the matrices
        for i in range(len(matrix1)):
            row = []
            # Iterate over the elements in the current row
            for j in range(len(matrix1[0])):
                # Add the corresponding elements from the matrices
                element_sum = matrix1[i][j] - matrix2[i][j]
                row.append(element_sum)
            result.append(row)

        return result

    else:
        constant = matrix1[0][0]
        result = []

        for row in matrix2:
            multiplied_row = [constant - element for element in row]
            result.append(multiplied_row)

        return result

def matrix_traspose(matrix):
    # Get the number of rows and columns in the matrix
    rows = len(matrix)
    columns = len(matrix[0])

    # Create a new matrix with swapped rows and columns
    transpose = [[matrix[j][i] for j in range(rows)] for i in range(columns)]

    return transpose

def matrix_invert(matrix):
    # Get the dimensions of the matrix
    n = len(matrix)
    m = len(matrix[0])

    # Check if the matrix is square
    if n != m:
        return 'Error'

    # Create an augmented matrix [matrix | identity]
    augmented_matrix = [row + [int(i == j) for j in range(n)] for i, row in enumerate(matrix)]

    # Apply Gauss-Jordan elimination
    for i in range(n):
        # Find the pivot row
        pivot_row = max(range(i, n), key=lambda x: abs(augmented_matrix[x][i]))

        # Swap the current row with the pivot row
        augmented_matrix[i], augmented_matrix[pivot_row] = augmented_matrix[pivot_row], augmented_matrix[i]

        # Scale the pivot row to make the pivot element equal to 1
        pivot = augmented_matrix[i][i]
        augmented_matrix[i] = [element / pivot for element in augmented_matrix[i]]

        # Eliminate other rows
        for j in range(n):
            if j != i:
                factor = augmented_matrix[j][i]
                augmented_matrix[j] = [row_j - factor * row_i for row_i, row_j in
                                       zip(augmented_matrix[i], augmented_matrix[j])]

    # Extract the inverse matrix from the augmented matrix
    inverse_matrix = [row[n:] for row in augmented_matrix]

    return inverse_matrix

def matrix_determinant(matrix):
    # Get the dimensions of the matrix
    n = len(matrix)
    m = len(matrix[0])

    # Check if the matrix is square
    if n != m:
        raise ValueError("Input matrix must be square")

    # Base case: 2x2 matrix
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Recursive case: cofactor expansion
    determinant = 0
    for j in range(n):
        # Calculate the cofactor of the current element
        cofactor = (-1) ** j * matrix[0][j]

        # Calculate the submatrix by removing the first row and the j-th column
        submatrix = [[matrix[i][k] for k in range(n) if k != j] for i in range(1, n)]

        # Recursively calculate the determinant of the submatrix
        submatrix_determinant = matrix_determinant(submatrix)

        # Update the determinant with the cofactor expansion
        determinant += cofactor * submatrix_determinant

    return determinant

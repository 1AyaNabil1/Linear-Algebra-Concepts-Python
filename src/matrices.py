import numpy as np

# Function to Create a Matrix
def create_matrix(rows, cols, elements):
    """
    Creates a matrix with the specified number of rows and columns.

    Args:
        rows (int): Number of rows in the matrix.
        cols (int): Number of columns in the matrix.
        elements (list): A list of elements to fill the matrix.

    Returns:
        numpy.ndarray: Created matrix.
    """
    if len(elements) != rows * cols:
        raise ValueError("Number of elements does not match matrix dimensions.")
    matrix = np.array(elements).reshape(rows, cols)
    return matrix


# Function to Add Two Matrices
def add_matrices(A, B):
    """
    Adds two matrices element-wise.

    Args:
        A (numpy.ndarray): First matrix.
        B (numpy.ndarray): Second matrix.

    Returns:
        numpy.ndarray: Sum of the matrices.
    """
    if A.shape != B.shape:
        raise ValueError("Matrices must have the same shape for addition.")
    return np.add(A, B)


# Function to Subtract Two Matrices
def subtract_matrices(A, B):
    """
    Subtracts matrix B from matrix A element-wise.

    Args:
        A (numpy.ndarray): First matrix.
        B (numpy.ndarray): Second matrix.

    Returns:
        numpy.ndarray: Difference of the matrices.
    """
    if A.shape != B.shape:
        raise ValueError("Matrices must have the same shape for subtraction.")
    return np.subtract(A, B)


# Function for Matrix Multiplication
def multiply_matrices(A, B):
    """
    Multiplies two matrices using dot product.

    Args:
        A (numpy.ndarray): First matrix.
        B (numpy.ndarray): Second matrix.

    Returns:
        numpy.ndarray: Product of the matrices.
    """
    if A.shape[1] != B.shape[0]:
        raise ValueError("Number of columns in A must equal number of rows in B for multiplication.")
    return np.dot(A, B)


# Function to Transpose a Matrix
def transpose_matrix(A):
    """
    Transposes the given matrix.

    Args:
        A (numpy.ndarray): Matrix to transpose.

    Returns:
        numpy.ndarray: Transposed matrix.
    """
    return np.transpose(A)


# Function to Calculate Matrix Determinant
def matrix_determinant(A):
    """
    Calculates the determinant of a square matrix.

    Args:
        A (numpy.ndarray): Square matrix.

    Returns:
        float: Determinant of the matrix.
    """
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix must be square to calculate determinant.")
    return np.linalg.det(A)


# Function to Inverse a Matrix
def inverse_matrix(A):
    """
    Computes the inverse of a square matrix.

    Args:
        A (numpy.ndarray): Square matrix.

    Returns:
        numpy.ndarray: Inverse of the matrix.
    """
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix must be square to find its inverse.")
    if np.linalg.det(A) == 0:
        raise ValueError("Matrix is singular and cannot be inverted.")
    return np.linalg.inv(A)


# Example Usage
if __name__ == "__main__":
    # Creating matrices
    A = create_matrix(2, 2, [1, 2, 3, 4])
    B = create_matrix(2, 2, [5, 6, 7, 8])
    print("Matrix A:\n", A)
    print("Matrix B:\n", B)

    # Performing operations
    print("\nMatrix Addition:\n", add_matrices(A, B))
    print("\nMatrix Subtraction:\n", subtract_matrices(A, B))
    print("\nMatrix Multiplication:\n", multiply_matrices(A, B))
    print("\nTranspose of A:\n", transpose_matrix(A))
    print("\nDeterminant of A:", matrix_determinant(A))
    print("\nInverse of A:\n", inverse_matrix(A))

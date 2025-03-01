import numpy as np

# Define two matrices
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# Matrix operations
C = A + B  # Addition
D = A - B  # Subtraction
E = A * B  # Element-wise multiplication
F = np.dot(A, B)  # Dot product
A_T = A.T  # Transpose
det_A = np.linalg.det(A)  # Determinant

# Inverse if determinant is not zero
if det_A != 0:
    A_inv = np.linalg.inv(A)

# Display results
print("Matrix A:\n", A)
print("\nMatrix B:\n", B)
print("\nA + B:\n", C)
print("\nA - B:\n", D)
print("\nA * B (Element-wise):\n", E)
print("\nA · B (Dot Product):\n", F)
print("\nA Transpose:\n", A_T)
print("\nDeterminant of A:", det_A)
if det_A != 0:
    print("\nInverse of A:\n", A_inv)
else:
    print("\nMatrix A is singular and cannot be inverted.")

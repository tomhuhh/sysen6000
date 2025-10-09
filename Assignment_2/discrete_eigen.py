import numpy as np

# Define the system matrix A
A = np.array([
    [1, -1, 0],
    [-1, -3, 1],
    [0, 1, -1]
])

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Display results
print("Eigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)

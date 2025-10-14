import numpy as np
from pylab import *

J = np.array([
    [-1/3,-2/3],
    [-2/3,-1/3]
], dtype=float)

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(J)

# Display results
print("Eigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)
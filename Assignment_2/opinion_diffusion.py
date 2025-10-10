import numpy as np
import matplotlib.pyplot as plt

A = np.array([
    [1/3,1/3,1/3,0,0],
    [0,1/3,1/3,1/3,0],
    [0,0,1/3,1/3,1/3],
    [1/3,0,0,1/3,1/3],
    [1/3,1/3,0,0,1/3]
], dtype=float)

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Display results
print("Eigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)

def opinion_diffusion_visualization(A, steps=100, seed=None, save_path="./Assignment_2/results/opinion_diffusion.png"):
    # Initialize random initial values
    n = A.shape[0]
    rng = np.random.default_rng(seed)
    initial_values = rng.normal(size=n)

    # Simulate the system
    values_over_time = np.zeros((steps + 1, n))
    values_over_time[0] = initial_values
    for t in range(steps):
        values_over_time[t + 1] = A @ values_over_time[t]

    # Compute the long-term average (just as a reference line)
    avg_initial = np.mean(initial_values)

    # Visualization
    plt.rcParams['font.family'] = 'Arial'
    plt.rcParams['font.size'] = 18
    plt.figure(figsize=(10, 6))
    for i in range(n):
        plt.plot(values_over_time[:, i], label=f'Person {i + 1}')
    plt.axhline(avg_initial, linestyle='--', color='gray', linewidth=1, label='Average of initial values')
    plt.xlabel('Time step')
    plt.ylabel('Opinion Value')
    plt.title('Opinion Diffusion Over Time')
    plt.legend()
    plt.tight_layout()
    # Save as high-resolution PNG (300 dpi)
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()

opinion_diffusion_visualization(A, steps=100, seed=42)

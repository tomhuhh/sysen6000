import numpy as np
import matplotlib.pyplot as plt
from pylab import *

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

# v   : current state vector
# traj: list of states over time (each is a copy of v)
# time: list of integer time steps
v = None
traj = None
time = None

# v0 will be set externally in the plotting loops
v0 = None

def initialize():
    global v, traj, time
    # Start at the externally-provided v0
    v = v0.copy()
    traj = [v.copy()]
    time = [0]

def observe():
    global v, traj, time
    traj.append(v.copy())
    time.append(len(time))

def update():
    global v
    # Linear iteration: x(t+1) = A x(t)
    v = A @ v

# Visualization
mpl.rcParams['font.family'] = 'Arial'

figure(figsize=(10, 6))

rng = np.random.default_rng(42)
v0 = rng.normal(size=5)   # initial condition

# Simulate T steps using initialize/observe/update
initialize()             
T = 100                    
for t in range(T):
    update()
    observe()

for i in range(len(traj[0])): 
    plot(time, [state[i] for state in traj], label=f'Person {i+1}', alpha=0.9)

# Reference line: mean of initial values
avg_initial = sum(traj[0]) / len(traj[0])
axhline(avg_initial, linestyle='--', linewidth=1, label='Average of initial values')

grid(False)
xlabel('Time step', fontsize=16)        
ylabel('Opinion Value', fontsize=16)  
title('Opinion Diffusion Over Time', fontsize=18) 
legend(loc='best', fontsize=16)
tight_layout()

# Save figure
# save_path = "./results/opinion_time_series.png"
# os.makedirs(os.path.dirname(save_path), exist_ok=True)
# plt.savefig(save_path, dpi=300, bbox_inches='tight')
show()
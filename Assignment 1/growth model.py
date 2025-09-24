from pylab import *

# Parameters for logistic growth
r = 0.1  # growth rate
K = 100   # carrying capacity

def initialize():
    global x, result, time
    x = 2  # initial population
    result = [x]
    time = [0]

def observe():
    global x, result, time
    result.append(x)
    time.append(len(time))

def f(x):
    ''' Logistic growth function: x_(t+1) = x_t + r*x_t*(1 - x_t/K) '''
    return x + r * x * (1 - x / K)

def update():
    global x
    x = f(x)

# Initialize the model
initialize()

# Run simulation for 120 time steps
for t in range(120):
    update()
    observe()

# Plot population (x_t) against time (t)
mpl.rcParams['font.family'] = 'Arial'
figure(figsize=(10, 6))
plot(time, result, '-', color= '#89CFF0',  linewidth=2, marker='o', markersize=3)
axhline(y=K, color='#FFB6C1', linestyle='--', label=f'Carrying capacity K = {K}')
grid(True, alpha=0.3)
xlabel('Time (t)', fontsize=12)
ylabel('Population x$_t$', fontsize=12)
title(f'Logistic Growth Model', fontsize=14)
legend()
xlim(0, len(time)-1)
ylim(0, K*1.1)
grid(False)
show()
# plt.savefig("growth model.png", dpi=300, bbox_inches='tight')  # high-resolution

# Print final values
print(f"Initial population: {result[0]:.3f}")
print(f"Final population: {result[-1]:.3f}")
print(f"Carrying capacity: {K}")
print(f"Growth rate: {r}")
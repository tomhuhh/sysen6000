from pylab import *

# Parameters for logistic growth with and without Allee effect
r = 0.01  # growth rate
K = 100   # carrying capacity
r = 0.15  # growth rate
K = 800   # carrying capacity
A = 100     # Allee threshold (minimal population size)

def initialize():
    global x, y, result_f, result_g, time
    x = 60  # initial population for standard logistic model
    y = 60  # initial population for Allee effect model
    result_f = [x]  # results for f(x) or standard logistic
    result_g = [y]  # results for g(y) or Allee effect
    time = [0]

def observe():
    global x, y, result_f, result_g, time
    result_f.append(x)
    result_g.append(y)
    time.append(len(time))

def f(x):
    ''' Logistic growth function: x_(t+1) = x_t + r*x_t*(1 - x_t/K) '''
    return x + r * x * (1 - x / K)

def g(y):
    ''' Logistic growth with Allee effect: y_(t+1) = y_t + r*y_t*(1 - y_t/K)*(y_t - A) '''
    return y + r * y * (1 - y / K) * (y / A - 1)

def update():
    global x, y
    x = f(x)  # Standard logistic model
    y = g(y)  # Allee effect model

# Initialize the model
initialize()

# Run simulation for 60 time steps
for t in range(60):
    update()
    observe()

# Plot both models on the same graph
mpl.rcParams['font.family'] = 'Arial'
figure(figsize=(12, 8))
plot(time, result_f, '-', color='#89CFF0', linewidth=2, marker='o', markersize=3, label='Standard Logistic')
plot(time, result_g, '-', color='#00008B', linewidth=2, marker='s', markersize=3, label='Allee Effect')
axhline(y=K, color='#FFB6C1', linestyle='--', label=f'Carrying capacity K = {K}')
axhline(y=A, color='#FF6B6B', linestyle='--', label=f'Allee threshold A = {A}')
grid(True, alpha=0.3)
xlabel('Time (t)', fontsize=16)
ylabel('Population', fontsize=16)
title(f'Standard Logistic vs Allee Effect Models (x$_0$ = {result_f[0]:.0f})', fontsize=18)
legend(loc="upper left", bbox_to_anchor=(1, 1), fontsize=14)
xlim(0, len(time)-1)
ylim(0, K*1.5)
tight_layout() 
plt.savefig("growth model_60.png", dpi=300, bbox_inches='tight')  # high-resolution
show()
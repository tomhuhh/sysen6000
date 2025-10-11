from pylab import *
import os

# Parameters
beta  = 1.2    # virality (per time)
gamma = 0.4    # forgetting/boredom (per time)

dt    = 0.01
T_end = 100.0
steps = int(T_end / dt)

# Globals
S = None
I = None
R = None
t_hist = None
S_hist = None
I_hist = None
R_hist = None

# Initial fractions (must sum to 1)
S0 = 0.99
I0 = 0.01
R0 = 0.00

def initialize():
    global S, I, R, t_hist, S_hist, I_hist, R_hist
    S, I, R = S0, I0, R0
    t_hist = [0.0]
    S_hist = [S]
    I_hist = [I]
    R_hist = [R]

def observe():
    global S, I, R, t_hist, S_hist, I_hist, R_hist
    t_hist.append(t_hist[-1] + dt)
    S_hist.append(S)
    I_hist.append(I)
    R_hist.append(R)

def update():
    global S, I, R
    # dS/dt = -beta * S * I
    # dI/dt =  beta * S * I - gamma * I
    # dR/dt =  gamma * I
    dS = -beta * S * I
    dI =  beta * S * I - gamma * I
    dR =  gamma * I

    # Forward Euler step
    S_next = S + dt * dS
    I_next = I + dt * dI
    R_next = R + dt * dR

    # Keep nonnegative and re-normalize tiny drift
    S, I, R = max(S_next, 0.0), max(I_next, 0.0), max(R_next, 0.0)
    total = S + I + R
    if total > 0:
        S, I, R = S/total, I/total, R/total   # enforce S+I+R=1

# Visualization
mpl.rcParams['font.family'] = 'Arial'

figure(figsize=(10, 6))
initialize()
for _ in range(steps):
    update()
    observe()

plot(t_hist, S_hist, label='S(t): not yet into song')
plot(t_hist, I_hist, label='I(t): currently into song (popularity)', linewidth=2)
plot(t_hist, R_hist, label='R(t): moved on', linestyle='--')

grid(False)
xlabel('Time', fontsize=16)
ylabel('Fraction of audience', fontsize=16)
title('Dynamics for Song Popularity', fontsize=18)
legend(fontsize=16)
tight_layout()

os.makedirs('./results', exist_ok=True)
savefig('./results/song_popularity_SIR_fractions.png', dpi=300, bbox_inches='tight')
show()

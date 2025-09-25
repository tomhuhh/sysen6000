from pylab import *

# Base switching rate r 
r = 0.1 

def initialize():
    global p_c, p_l, p_n, results_c, results_l, results_n, time
    # Initial probabilities (must sum to 1)
    p_c = 1/3  # conservative probability
    p_l = 1/3  # liberal probability
    p_n = 1 - p_c - p_l  # neutral probability

    # Store results for plotting
    results_c = [p_c]
    results_l = [p_l]
    results_n = [p_n]
    time = [0]

def observe():
    global p_c, p_l, p_n, results_c, results_l, results_n, time
    results_c.append(p_c)
    results_l.append(p_l)
    results_n.append(p_n)
    time.append(len(time))

def switching_rate(p_from, p_to):
    """Calculate switching rate from opinion X to opinion Y"""
    if p_to > p_from:
        return r * (p_to - p_from)
    else:
        return 0.0

def update():
    global p_c, p_l, p_n
    
    # Store current probabilities
    p_c_old, p_l_old, p_n_old = p_c, p_l, p_n
    
    # Calculate all switching rates
    # From conservative to others
    rate_c_to_l = switching_rate(p_c_old, p_l_old)
    rate_c_to_n = switching_rate(p_c_old, p_n_old)
    
    # From liberal to others
    rate_l_to_c = switching_rate(p_l_old, p_c_old)
    rate_l_to_n = switching_rate(p_l_old, p_n_old)
    
    # From neutral to others
    rate_n_to_c = switching_rate(p_n_old, p_c_old)
    rate_n_to_l = switching_rate(p_n_old, p_l_old)
    
    # Update probabilities based on net flows
    # Conservative: gains from others, loses to others
    dp_c = (rate_l_to_c * p_l_old + rate_n_to_c * p_n_old) - (rate_c_to_l + rate_c_to_n) * p_c_old
    
    # Liberal: gains from others, loses to others  
    dp_l = (rate_c_to_l * p_c_old + rate_n_to_l * p_n_old) - (rate_l_to_c + rate_l_to_n) * p_l_old
    
    # Neutral: gains from others, loses to others
    dp_n = (rate_c_to_n * p_c_old + rate_l_to_n * p_l_old) - (rate_n_to_c + rate_n_to_l) * p_n_old
    
    # Apply changes
    p_c += dp_c
    p_l += dp_l
    p_n += dp_n

# Initialize the model
initialize()

# Run simulation for 100 time steps
for t in range(100):
    update()
    observe()

# Plot all three opinion probabilities over time
mpl.rcParams['font.family'] = 'Arial'
figure(figsize=(12, 8))
plot(time, results_c, '-', color='#FF6B6B', linewidth=2, marker='o', markersize=3, label='Conservative')
plot(time, results_l, '-', color='#3D8D7A', linewidth=2, marker='s', markersize=3, label='Liberal')
plot(time, results_n, '-', color='#45B7D1', linewidth=2, marker='^', markersize=3, label='Neutral')

grid(True, alpha=0.3)
xlabel('Time (t)', fontsize=16)
ylabel('Probability', fontsize=16)
title(f'Public Opinion Dynamics (Base Rate r = {r})', fontsize=18)
legend(loc="upper left", bbox_to_anchor=(1, 1), fontsize=14)
xlim(0, len(time)-1)
ylim(0, 1.05)
tight_layout()
plt.savefig("public opinion dynamics_tie.png", dpi=300, bbox_inches='tight')  # high-resolution
show()

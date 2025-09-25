from pylab import *

def initialize():
    global x, y, result_x, result_y, time
    x = x0  # initial value for x (must be > 0)
    y = y0  # initial value for y (must be > 0)
    result_x = [x] 
    result_y = [y]
    time = [0]

def observe():
    global x, y, result_x, result_y, time
    result_x.append(x)
    result_y.append(y)
    time.append(len(time))

def update():
    global x, y
    nextx = x + 0.1 * (x - x * y)
    nexty = y + 0.1 * (y - x * y)
    x, y = nextx, nexty

# Plot phase portrait with multiple initial conditions
mpl.rcParams['font.family'] = 'Arial'
figure(figsize=(10, 8))

for x0 in arange(0.1, 2, 0.2):
    for y0 in arange(0.1, 2, 0.2):
        initialize()
        x, y = x0, y0
        result_x, result_y = [x], [y]
        for t in range(30):
            update()
            observe()
        plot(result_x, result_y, color = '#89CFF0', alpha=0.7)

grid(True, alpha=0.3)
xlabel('x$_t$', fontsize=16)
ylabel('y$_t$', fontsize=16)
title('Phase Space', fontsize=18)
axis([0, 2, 0, 2])  # Zoom in to the area of interest

tight_layout()
plt.savefig("phase space.png", dpi=300, bbox_inches='tight')  # high-resolution
show()

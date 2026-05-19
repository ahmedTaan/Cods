import matplotlib.pyplot as plt
import numpy as np

# 1. Setup Simulation Grid (100x100)
grid_size = 100
U = np.full((grid_size, grid_size), 20.0) # Room temperature

# 2. Finite Difference Method (FDM) Algorithm
iterations = 3000
for i in range(iterations):
    U_old = U.copy()
    
    # Iterative update: average of 4 neighbors
    U[1:-1, 1:-1] = 0.25 * (U_old[2:, 1:-1] + U_old[:-2, 1:-1] + 
                            U_old[1:-1, 2:] + U_old[1:-1, :-2])
    
    # 3. Boundary Conditions & Heat Source
    # CPU in the center (90 C)
    U[40:60, 40:60] = 90.0
    
    # Cooled outer edges (20 C)
    U[:, 0] = 20.0
    U[:, -1] = 20.0
    U[0, :] = 20.0
    U[-1, :] = 20.0

# 4. Visualization (Thermal Camera Style)
fig, ax = plt.subplots(figsize=(8, 8))
contour = ax.imshow(U, cmap='hot', interpolation='bilinear', origin='lower')

ax.set_title("Steady-State Heat Distribution in a CPU Chip (FDM)")
ax.set_xlabel("X-axis (Position)")
ax.set_ylabel("Y-axis (Position)")
fig.colorbar(contour, ax=ax, shrink=0.8, label="Temperature (\u00b0C)")

plt.show()
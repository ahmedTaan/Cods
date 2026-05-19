import matplotlib
matplotlib.use('QtAgg') 
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# 1. Setup membrane dimensions (reduced grid to 40 for faster rendering)
a, b = 1.0, 1.0
x = np.linspace(0, a, 40)
y = np.linspace(0, b, 40)
X, Y = np.meshgrid(x, y)
c = 1.0

# 2. Wave Displacement Function
def u_wave(X, Y, t):
    w11 = c * np.pi * np.sqrt(1**2/a**2 + 1**2/b**2)
    mode1 = np.sin(1 * np.pi * X / a) * np.sin(1 * np.pi * Y / b) * np.cos(w11 * t)
    w22 = c * np.pi * np.sqrt(2**2/a**2 + 2**2/b**2)
    mode2 = 0.5 * np.sin(2 * np.pi * X / a) * np.sin(2 * np.pi * Y / b) * np.cos(w22 * t)
    return mode1 + mode2

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Setup axes once to reduce CPU load
ax.set_zlim(-1.5, 1.5)
ax.set_title("2D Vibrating Membrane")
ax.set_xlabel("Width (x)")
ax.set_ylabel("Length (y)")
ax.set_zlabel("Displacement (u)")

# Draw the initial surface and store it in a list to remove and update later
surf = [ax.plot_surface(X, Y, u_wave(X, Y, 0), cmap='viridis', edgecolor='none')]

def update_surface(t):
    surf[0].remove() # Remove only the old surface (keep axes)
    U = u_wave(X, Y, t)
    # Draw the new surface
    surf[0] = ax.plot_surface(X, Y, U, cmap='viridis', edgecolor='none', vmin=-1.5, vmax=1.5)
    return surf[0],

# Animation setup (interval=30 for smooth frames)
ani = animation.FuncAnimation(fig, update_surface, frames=np.linspace(0, 10, 150), interval=30, blit=False)

plt.show()

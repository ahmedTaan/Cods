import matplotlib.pyplot as plt
import numpy as np

# 1. Spatial and Temporal Domains
L = 2.0
x = np.linspace(0, L, 100)
t = np.linspace(0, 2.0, 100)
X, T = np.meshgrid(x, t)

# 2. Steady-State Component
U_steady = -50 * X + 100

# 3. Transient State Component (Fourier Series)
def u_transient_3d(X, T, terms=50):
    U_tr = np.zeros_like(X)
    for k in range(terms):
        n = 2 * k + 1
        coeff = 200 / (n * np.pi)
        spatial = np.sin((n * np.pi / 2) * X)
        temporal = np.exp(-3 * ((n**2 * np.pi**2) / 4) * T) 
        U_tr += coeff * spatial * temporal
    return U_tr

# 4. Total Temperature Distribution
U_total = U_steady + u_transient_3d(X, T)

# 5. 3D Surface Visualization
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, T, U_total, cmap='inferno', edgecolor='none')

ax.set_title("1D Heat Equation (3D Surface Plot)")
ax.set_xlabel("Position (x)")
ax.set_ylabel("Time (t)")
ax.set_zlabel("Temperature (U)")
fig.colorbar(surf, shrink=0.5, aspect=5, label="Temperature (\u00b0C)")

plt.show()
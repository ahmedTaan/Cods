import matplotlib.pyplot as plt
import numpy as np
from scipy.special import erfc

# 1. Simulation Parameters
C0 = 100.0  # Initial surface concentration (%)
D = 0.5     # Diffusion coefficient

# 2. Spatiotemporal Coordinates
x = np.linspace(0, 5, 100)    # Depth (mm)
t = np.linspace(0.1, 10, 100) # Time (Hours)
X, T = np.meshgrid(x, t)

# 3. Model Solution Formulation
Z_concentration = C0 * erfc(X / (2 * np.sqrt(D * T)))

# 4. Render 3D Concentration Profile
fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, T, Z_concentration, cmap='coolwarm', edgecolor='none')
ax.set_title("Spatiotemporal Drug Diffusion Profile")
ax.set_xlabel("Depth into Tissue (mm)")
ax.set_ylabel("Time (Hours)")
ax.set_zlabel("Drug Concentration (%)")
fig.colorbar(surf, shrink=0.5, aspect=10, label="Concentration (%)")
plt.show()
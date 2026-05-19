import matplotlib.pyplot as plt
import numpy as np
from scipy.special import beta

# 1. 2D Domain Meshgrid Setup
x_beta = np.linspace(0.5, 5, 50)
y_beta = np.linspace(0.5, 5, 50)
X_beta, Y_beta = np.meshgrid(x_beta, y_beta)
Z_beta = beta(X_beta, Y_beta)

# 2. 3D Surface Visualization
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X_beta, Y_beta, Z_beta, cmap='plasma', edgecolor='none')
ax.set_title("Beta Function Topology")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel(r'$B(x, y)$')
fig.colorbar(surf, shrink=0.5, aspect=10, label="Beta Value")
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# 1. Plate Dimensions (1x1)
x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)
X, Y = np.meshgrid(x, y)
U = np.zeros_like(X)

# 2. Fourier Series Evaluation (50 terms)
terms = 50 
for k in range(terms):
    n = 2 * k + 1  # Odd harmonics only
    coeff = 400 / (n * np.pi)
    
    # Hyperbolic and trigonometric components
    sinh_ratio = np.sinh(n * np.pi * Y) / np.sinh(n * np.pi)
    sin_x = np.sin(n * np.pi * X)
    
    U += coeff * sinh_ratio * sin_x

# 3. 2D Heatmap Visualization
fig, ax = plt.subplots(figsize=(8, 6))
contour = ax.contourf(X, Y, U, 100, cmap='inferno')

ax.set_title("2D Steady-State Heat Transfer (Laplace Equation)")
ax.set_xlabel("Width (x)")
ax.set_ylabel("Height (y)")
fig.colorbar(contour, ax=ax, label="Temperature (\u00b0C)")

plt.show()
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import gamma

# 1. Continuous Domain Evaluation
x_gamma = np.linspace(0.1, 5.5, 500)
y_gamma = gamma(x_gamma)

# 2. Integer Benchmarks for Factorials
n_values = np.array([1, 2, 3, 4, 5])
factorial_values = gamma(n_values)

# 3. Visualization Setup
fig, ax = plt.subplots(figsize=(7, 5))
ax.plot(x_gamma, y_gamma, 'b-', linewidth=2, label=r'$\Gamma(x)$')
ax.plot(n_values, factorial_values, 'ro', label=r'$\Gamma(n) = (n-1)!$')
ax.set_title("Gamma Function Evaluation")
ax.set_xlabel("x")
ax.set_ylabel(r'$\Gamma(x)$')
ax.set_ylim(0, 25)
ax.grid(True, linestyle='--')
ax.legend()
plt.show()
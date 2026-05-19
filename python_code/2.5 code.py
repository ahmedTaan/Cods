import numpy as np

# 1. Physical Parameters
L = 2.0
alpha_sq = 3.0  # c^2 in the heat equation

# 2. Mathematical Model Functions
def eigenvalue(n): 
    return (n * np.pi / L)**2

def eigenfunction(n, x): 
    return np.sin(n * np.pi * x / L)

def b_n(n): 
    return 0 if n % 2 == 0 else 200 / (n * np.pi)

def u_steady(x): 
    return -50 * x + 100

def u_total(x, t, terms=50):
    u_tr = 0
    for n in range(1, terms + 1):
        if n % 2 != 0:
            lam = eigenvalue(n)
            T_t = np.exp(-alpha_sq * lam * t)
            u_tr += b_n(n) * eigenfunction(n, x) * T_t
    return u_steady(x) + u_tr

# 3. Evaluating Eigenvalues
print("--- Evaluating Eigenvalues ---")
for n in range(1, 10, 2):
    print(f"Mode n={n}: Eigenvalue = {eigenvalue(n):.4f}")

# 4. Evaluating Solution at Various Points
print("\n--- Evaluating Solution at Various Points ---")
points_x = [0.5, 1.0, 1.5]
times_t = [0.01, 0.5, 2.0]

for t in times_t:
    print(f"\nTime t = {t}:")
    for x in points_x:
        print(f"  x = {x} -> Temp = {u_total(x, t):.2f} C")
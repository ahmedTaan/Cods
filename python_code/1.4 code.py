import numpy as np
import matplotlib.pyplot as plt

# 1. Signal Generation (Time Domain)
t = np.linspace(0, 2 * np.pi, 1000)
harmonics = [1, 3, 5, 7, 9, 11, 13, 15]
y = sum((1/n) * np.sin(n*t) for n in harmonics)

# 2. FFT Application (Frequency Domain)
n = len(t)
fft_result = np.fft.fft(y)
frequencies = np.fft.fftfreq(n, d=(t[1]-t[0])) 
angular_freqs = frequencies * (2 * np.pi)

# Extract positive half
pos_freqs = angular_freqs[:n//2]
amplitudes = np.abs(fft_result)[:n//2] / (n//2)

# 3. Visualization
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7))
ax1.plot(t, y, color='blue', linewidth=2)
ax1.set_title("Time Domain (Square Wave Approximation - 8 Harmonics)")
ax1.set_xlabel("Time (t)")
ax1.set_ylabel("Amplitude")
ax1.grid(True)

ax2.bar(pos_freqs, amplitudes, color='red', width=0.2)
ax2.set_xlim(0, 16) 
ax2.set_xticks(harmonics) 
ax2.set_title("Frequency Domain (FFT Analysis)")
ax2.set_xlabel("Angular Frequency (\u03c9)")
ax2.set_ylabel("Amplitude")
ax2.grid(True)

plt.tight_layout()
plt.show()

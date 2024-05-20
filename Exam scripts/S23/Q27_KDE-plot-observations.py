import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KernelDensity

# Provided KDE plot settings
bandwidth = 0.168

# Visible data points (based on provided plot)
X_visible = np.array([0.5, 1.5, 2.5, 5.5, 6.5, 7.5]).reshape(-1, 1)

# Generate KDE plots for different N values
N_values = {
    'N = 6': X_visible,
    'N = 9': np.vstack((X_visible, np.array([-1, 3, 8]).reshape(-1, 1))),
    'N = 17': np.vstack((X_visible, np.array([-2, -1.5, -1, 3, 3.5, 4, 8, 9, 10, 11, 12]).reshape(-1, 1))),
    'N = 21': np.vstack((X_visible, np.array([-2, -1.5, -1, 3, 3.5, 4, 8, 9, 10, 11, 12, 13, 14, 15, 16]).reshape(-1, 1)))
}

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Plot KDE for each N
for ax, (label, X) in zip(axes.flatten(), N_values.items()):
    kde = KernelDensity(kernel='gaussian', bandwidth=bandwidth).fit(X)
    X_plot = np.linspace(-5, 15, 1000).reshape(-1, 1)
    log_dens = kde.score_samples(X_plot)
    dens = np.exp(log_dens)
    ax.fill(X_plot, dens, fc='orange', alpha=0.5)
    ax.plot(X_plot, dens, '-r')
    ax.scatter(X_visible, np.zeros_like(X_visible), c='blue', marker='o', s=100, label='Visible Points')
    ax.set_xlabel('x-value')
    ax.set_ylabel('Density estimate')
    ax.set_title(f'KDE with Gaussian Kernel ({label})')
    ax.grid(True)
    ax.legend()

plt.tight_layout()
plt.show()

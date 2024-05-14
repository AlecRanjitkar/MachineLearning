import numpy as np # type: ignore
from scipy.stats import norm # type: ignore

# Given data
mu1 = np.array([0.77, -0.41])
sigma1_diag = np.array([0.29, 0.55])

mu2 = np.array([-0.91, 0.5])
sigma2_diag = np.array([0.32, 1.12])

x_test = np.array([0, 0.7])

# Priors
p_y1 = 0.53
p_y2 = 0.47

# Likelihoods using only diagonal elements
likelihood_y1 = (norm.pdf(x_test[0], mu1[0], np.sqrt(sigma1_diag[0])) *
                 norm.pdf(x_test[1], mu1[1], np.sqrt(sigma1_diag[1])))

likelihood_y2 = (norm.pdf(x_test[0], mu2[0], np.sqrt(sigma2_diag[0])) *
                 norm.pdf(x_test[1], mu2[1], np.sqrt(sigma2_diag[1])))

# Posteriors
posterior_y1 = likelihood_y1 * p_y1
posterior_y2 = likelihood_y2 * p_y2

print(f"Posterior probability for y=1: {posterior_y1:.6f}")
print(f"Posterior probability for y=2: {posterior_y2:.6f}")

# Classify based on higher posterior probability
if posterior_y1 > posterior_y2:
    classification = "y=1 (Low class)"
else:
    classification = "y=2 (High class)"

print(classification)

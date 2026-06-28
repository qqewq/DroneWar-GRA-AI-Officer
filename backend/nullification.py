import numpy as np
from scipy.linalg import null_space

class Nullifier:
    def __init__(self, dim=3):
        self.dim = dim
        # Resonance operator R
        self.R = np.eye(dim) - 0.1 * np.ones((dim, dim))
        self.R_dag = self.R.T

    def nullify(self, state: np.ndarray, perturbation: np.ndarray) -> np.ndarray:
        # projection onto kernel of R
        kernel = null_space(self.R)
        proj = kernel @ kernel.T
        return state + perturbation - proj @ perturbation

    def chiral_filter(self, signal: np.ndarray, friend_signature: np.ndarray):
        # phase-based friend/foe separation
        phase_diff = np.angle(signal) - np.angle(friend_signature)
        # cancel out-of-phase
        return signal * np.exp(-1j * phase_diff) * (np.cos(phase_diff) > 0.7)

import numpy as np
from backend.nullification import Nullifier

def test_nullify_zero_perturbation():
    nf = Nullifier()
    state = np.array([1.0, 0.0, 0.0])
    assert np.allclose(nf.nullify(state, np.zeros(3)), state)

def test_chiral_filter():
    nf = Nullifier()
    signal = np.exp(1j * np.array([0, np.pi, 0.5]))
    friend = np.exp(1j * np.array([0, 0, 0.4]))
    filtered = nf.chiral_filter(signal, friend)
    assert np.abs(filtered[0]) > 0.8  # in-phase retained
    assert np.abs(filtered[1]) < 0.2  # anti-phase cancelled

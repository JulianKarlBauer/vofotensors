import numpy as np
import sympy as sp


def get_mandel_base_sym():
    factor = sp.sqrt(2) / sp.S(2)

    DIM = 3
    DIM_MANDEL6 = 6
    B = np.zeros((DIM_MANDEL6, DIM, DIM), dtype=sp.Symbol)

    B[0, 0, 0] = sp.S(1)
    B[1, 1, 1] = sp.S(1)
    B[2, 2, 2] = sp.S(1)
    B[3, 1, 2] = B[3, 2, 1] = factor
    B[4, 0, 2] = B[4, 2, 0] = factor
    B[5, 0, 1] = B[5, 1, 0] = factor
    return B


mandel_base = get_mandel_base_sym()


def to_mandel(tensor4):
    tmp = np.tensordot(mandel_base, tensor4, axes=2)
    out = np.tensordot(tmp, np.einsum("bkl->klb", mandel_base), axes=2)
    return out

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import sympy as sp
from vofotensors.numbers import z, sqrt_two, two
from vofotensors.abc import (
    alpha,
    alpha1,
    alpha2,
    alpha3,
    la1,
    la2,
    la3,
    rho,
    rho1,
    rho2,
    rho3,
    d1,
    d2,
    d3,
    d4,
    d5,
    d6,
    d7,
    d8,
    d9,
)
from vofotensors import substitutions

##################
# N4


def F4_transv_1():
    return np.array(
        [
            [sp.S(8), -sp.S(4), -sp.S(4), z, z, z],
            [-sp.S(4), sp.S(3), sp.S(1), z, z, z],
            [-sp.S(4), sp.S(1), sp.S(3), z, z, z],
            [z, z, z, sp.S(2), z, z],
            [z, z, z, z, -sp.S(8), z],
            [z, z, z, z, z, -sp.S(8)],
        ],
        dtype=object,
    )


def F4_transv_2():
    return np.array(
        [
            [sp.S(3), -sp.S(4), sp.S(1), z, z, z],
            [-sp.S(4), sp.S(8), -sp.S(4), z, z, z],
            [sp.S(1), -sp.S(4), sp.S(3), z, z, z],
            [z, z, z, -sp.S(8), z, z],
            [z, z, z, z, sp.S(2), z],
            [z, z, z, z, z, -sp.S(8)],
        ],
        dtype=object,
    )


def F4_transv_3():
    return np.array(
        [
            [sp.S(3), sp.S(1), -sp.S(4), z, z, z],
            [sp.S(1), sp.S(3), -sp.S(4), z, z, z],
            [-sp.S(4), -sp.S(4), sp.S(8), z, z, z],
            [z, z, z, -sp.S(8), z, z],
            [z, z, z, z, -sp.S(8), z],
            [z, z, z, z, z, sp.S(2)],
        ],
        dtype=object,
    )


def dev4_transv_x_by_rho1():
    return rho1 * F4_transv_1()


def dev4_transv_y_by_rho2():
    return rho2 * F4_transv_2()


def dev4_transv_z_by_rho3():
    return rho3 * F4_transv_3()


def dev4_ortho_by_rho1_rho2_rho3():
    return dev4_transv_x_by_rho1() + dev4_transv_y_by_rho2() + dev4_transv_z_by_rho3()


def dev4_ortho_by_d1_d2_d3():
    return np.array(
        [
            [-(d1 + d2), d1, d2, z, z, z],
            [d1, -(d1 + d3), d3, z, z, z],
            [d2, d3, -(d2 + d3), z, z, z],
            [z, z, z, two * d3, z, z],
            [z, z, z, z, two * d2, z],
            [z, z, z, z, z, two * d1],
        ],
        dtype=object,
    )


def dev4_monoclinic_by_d1_d2_d3_d4_d5():
    return dev4_ortho_by_d1_d2_d3() + np.array(
        [
            [z, z, z, -(d4 + d5), z, z],
            [z, z, z, d4, z, z],
            [z, z, z, d5, z, z],
            [-(d4 + d5), d4, d5, z, z, z],
            [z, z, z, z, z, -sqrt_two * (d4 + d5)],
            [z, z, z, z, -sqrt_two * (d4 + d5), z],
        ],
        dtype=object,
    )


def copy_upper_triangle(matrix):
    r"""Copy upper triangle to lower triangle, i.e. make symmetric"""
    index_lower_triangle = np.tril_indices(6, -1)
    matrix[index_lower_triangle] = matrix.T[index_lower_triangle]
    return matrix


def dev4_triclinic_by_d():
    comp_03 = -sqrt_two * (d4 + d5)
    comp_14 = -sqrt_two * (d6 + d7)
    comp_25 = -sqrt_two * (d8 + d9)
    return copy_upper_triangle(
        np.array(
            [
                [-(d1 + d2), d1, d2, comp_03, sqrt_two * d6, sqrt_two * d8],
                [z, -(d1 + d3), d3, sqrt_two * d4, comp_14, sqrt_two * d9],
                [z, z, -(d2 + d3), sqrt_two * d5, sqrt_two * d7, comp_25],
                [z, z, z, sp.S(2) * d3, sqrt_two * comp_25, sqrt_two * comp_14],
                [z, z, z, z, sp.S(2) * d2, sqrt_two * comp_03],
                [z, z, z, z, z, sp.S(2) * d1],
            ],
            dtype=object,
        )
    )


def dev4_planar_alpha1_d0_d7():
    return np.array(
        sp.Matrix(dev4_triclinic_by_d()).subs(
            substitutions.substitutions["planar_alpha_d"]
        )
    )


def dev4_planar_la0_d0_d7():
    return np.array(
        sp.Matrix(dev4_triclinic_by_d()).subs(
            substitutions.substitutions["planar_la0_d"]
        )
    )


dev4s_parametric = {
    "planar": {
        "alpha1_d_0_d_7": dev4_planar_alpha1_d0_d7(),
        "la_0_d_0_d_7": dev4_planar_la0_d0_d7(),
    },
    "transv_isotropic": {
        "rho1": dev4_transv_x_by_rho1(),
        "rho2": dev4_transv_y_by_rho2(),
        "rho3": dev4_transv_z_by_rho3(),
    },
    "monoclinic": {
        "a_b_c_m_n_in_z_direction": dev4_monoclinic_by_d1_d2_d3_d4_d5(),
    },
}

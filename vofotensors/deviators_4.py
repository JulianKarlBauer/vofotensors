#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import sympy as sp
from vofotensors.numbers import z, half
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
    return (
        dev4_transv_x_by_rho1() + dev4_transv_y_by_rho2() + dev4_transv_z_by_rho3()
    )


def dev4_ortho_by_abc():
    return np.array(
        [
            [-(a + b), a, b, z, z, z],
            [a, -(a + c), c, z, z, z],
            [b, c, -(b + c), z, z, z],
            [z, z, z, sp.S(2) * c, z, z],
            [z, z, z, z, sp.S(2) * b, z],
            [z, z, z, z, z, sp.S(2) * a],
        ],
        dtype=object,
    )


def dev4_trigonal_by_def_z():
    return np.array(
        [
            [-(d + e), d, e, sqrt_two * f, z, z],
            [d, -(d + e), e, -sqrt_two * f, z, z],
            [e, e, -(e + e), z, z, z],
            [sqrt_two * f, -sqrt_two * f, z, two * e, z, z],
            [z, z, z, z, two * e, two * f],
            [z, z, z, z, two * f, two * d],
        ],
        dtype=object,
    )


def dev4_trigonal_by_def_x():
    return sb.actively_rotate_mandel(
        mandel=dev4_trigonal_by_def_z(),
        Q=sb.transformation.rotations["z_to_x"],
    )


def dev4_trigonal_by_def_y():
    return sb.actively_rotate_mandel(
        mandel=dev4_trigonal_by_def_z(),
        Q=sb.transformation.rotations["z_to_y"],
    )


def dev4_monoclinic_by_abcmn_z():
    return dev4_ortho_by_abc() + np.array(
        [
            [z, z, z, -(m + n), z, z],
            [z, z, z, m, z, z],
            [z, z, z, n, z, z],
            [-(m + n), m, n, z, z, z],
            [z, z, z, z, z, -sqrt_two * (m + n)],
            [z, z, z, z, -sqrt_two * (m + n), z],
        ],
        dtype=object,
    )


def copy_upper_triangle(matrix):
    r"""Copy upper triangle to lower triangle, i.e. make symmetric"""
    index_lower_triangle = np.tril_indices(6, -1)
    matrix[index_lower_triangle] = matrix.T[index_lower_triangle]
    return matrix


def dev4_triclinic_by_d():
    comp_03 = -sqrt_two * (d3 + d4)
    comp_14 = -sqrt_two * (d5 + d6)
    comp_25 = -sqrt_two * (d7 + d8)
    return copy_upper_triangle(
        np.array(
            [
                [-(d0 + d1), d0, d1, comp_03, sqrt_two * d5, sqrt_two * d7],
                [z, -(d0 + d2), d2, sqrt_two * d3, comp_14, sqrt_two * d8],
                [z, z, -(d1 + d2), sqrt_two * d4, sqrt_two * d6, comp_25],
                [z, z, z, sp.S(2) * d2, sqrt_two * comp_25, sqrt_two * comp_14],
                [z, z, z, z, sp.S(2) * d1, sqrt_two * comp_03],
                [z, z, z, z, z, sp.S(2) * d0],
            ],
            dtype=object,
        )
    )


def dev4_planar_alpha_x_d_0_d_7():
    return np.array(
        sp.Matrix(dev4_triclinic_by_d()).subs(substitutions["planar_alpha_d"])
    )


def dev4_planar_la_0_d_0_d_7():
    return np.array(
        sp.Matrix(dev4_triclinic_by_d()).subs(substitutions["planar_la0_d"])
    )


dev4s_parametric = {
    "planar": {
        "alpha_x_d_0_d_7": dev4_planar_alpha_x_d_0_d_7(),
        "la_0_d_0_d_7": dev4_planar_la_0_d_0_d_7(),
    },
    "transv_isotropic": {
        "rho1": dev4_transv_x_by_rho1(),
        "rho2": dev4_transv_y_by_rho2(),
        "rho3": dev4_transv_z_by_rho3(),
    },
    "trigonal": {
        "d_e_f_in_x_direction": dev4_trigonal_by_def_x(),
        "d_e_f_in_y_direction": dev4_trigonal_by_def_y(),
        "d_e_f_in_z_direction": dev4_trigonal_by_def_z(),
    },
    "monoclinic": {
        "a_b_c_m_n_in_z_direction": dev4_monoclinic_by_abcmn_z(),
    },
}

N4s_pairs = {
    "planar": {
        "alpha_x_d_0_d_7": {
            "D2": dev2_planar_by_alpha_x(),
            "D4": dev4_planar_alpha_x_d_0_d_7(),
        },
        "la_0_d_0_d_7": {
            "D2": dev2_planar_by_la_0(),
            "D4": dev4_planar_la_0_d_0_d_7(),
        },
    },
    "transv_isotropic": {
        "alpha_x_rho1": {"D2": dev2_by_alpha_x(), "D4": dev4_transv_x_by_rho1()},
        "alpha_y_rho2": {"D2": dev2_by_alpha_y(), "D4": dev4_transv_y_by_rho2()},
        "alpha_z_rho3": {"D2": dev2_by_alpha_z(), "D4": dev4_transv_z_by_rho3()},
    },
    "trigonal": {
        "alpha_z_def_z": {"D2": dev2_by_alpha_z(), "D4": dev4_trigonal_by_def_z()},
    },
    "orthotropic": {
        "a2_b2_a_b_c": {"D2": dev2_by_a2_b2(), "D4": dev4_ortho_by_abc()},
        "alpha_x_alpha_z_rho1_rho2_rho3": {
            "D2": dev2_by_alpha_x_alpha_z(),
            "D4": dev4_ortho_by_rho1_rho2_rho3(),
        },
        "alpha_x_alpha_z_a_b_c": {
            "D2": dev2_by_alpha_x_alpha_z(),
            "D4": dev4_ortho_by_abc(),
        },
    },
    "2transv_4orthotropic": {
        "alpha_x_a_b_c": {"D2": dev2_by_alpha_x(), "D4": dev4_ortho_by_abc()},
        "alpha_z_a_b_c": {"D2": dev2_by_alpha_z(), "D4": dev4_ortho_by_abc()},
    },
    "monoclinic": {
        "alpha_x_alpha_z_a_b_c_m_n": {
            "D2": dev2_by_alpha_x_alpha_z(),
            "D4": dev4_monoclinic_by_abcmn_z(),
        },
    },
    "triclinic": {
        "la_0_la_1_d_0_d_1_d_2_d_3_d_4_d_5_d_6_d_7_d_8": {
            "D2": dev2_by_la0_la1(),
            "D4": dev4_triclinic_by_d(),
        },
    },
}

N4s_parametric = {
    key: {
        key_sub: sb.special.combine_to_N4(**val_sub) for key_sub, val_sub in val.items()
    }
    for key, val in N4s_pairs.items()
}

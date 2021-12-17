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
from vofotensors import substitutions
from vofotensors.basic_tensors import N2_iso


##################
# N2


def F2_transv_1():
    return np.array(
        [
            [sp.S(1), z, z],
            [z, -half, z],
            [z, z, -half],
        ],
        dtype=object,
    )


def F2_transv_2():
    return np.array(
        [
            [-half, z, z],
            [z, sp.S(1), z],
            [z, z, -half],
        ],
        dtype=object,
    )


def F2_transv_3():
    return np.array(
        [
            [-half, z, z],
            [z, -half, z],
            [z, z, sp.S(1)],
        ],
        dtype=object,
    )


def dev2_transv_by_la1():
    half_reminder = (sp.S(1) - la1) / sp.S(2)
    N2 = np.array(
        [
            [la1, z, z],
            [z, half_reminder, z],
            [z, z, half_reminder],
        ],
        dtype=object,
    )
    return N2 - N2_iso


def dev2_by_alpha1():
    return alpha1 * F2_transv_1()


def dev2_by_alpha2():
    return alpha2 * F2_transv_2()


def dev2_by_alpha3():
    return alpha3 * F2_transv_3()


def dev2_by_alpha1_alpha3():
    return alpha1 * F2_transv_1() + alpha3 * F2_transv_3()


def dev2_by_alpha1_alpha2_alpha3():
    return dev2_by_alpha1_alpha3() + alpha2 * F2_transv_2()


def dev2_by_la1_la2():
    N2 = np.array(
        [
            [la1, z, z],
            [z, la2, z],
            [z, z, sp.S(1) - la1 - la2],
        ],
        dtype=object,
    )
    return N2 - N2_iso


def dev2_by_la1_la2_la3():
    N2 = np.array(
        [
            [la1, z, z],
            [z, la2, z],
            [z, z, la3],
        ],
        dtype=object,
    )
    return N2 - N2_iso


def dev2_planar_by_alpha1():
    return np.array(
        sp.Matrix(dev2_by_alpha1_alpha3()).subs(
            substitutions.substitutions["planar_alpha_d"]
        )
    )


def dev2_planar_by_la1():
    return np.array(
        sp.Matrix(dev2_by_la1_la2()).subs(substitutions.substitutions["planar_la1_d"])
    )

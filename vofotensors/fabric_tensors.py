#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import sympy as sp
import copy
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
from collections import defaultdict


def map_nested(dictionary, transformation):
    # https://stackoverflow.com/a/49897410/8935243
    for each in dictionary:
        if type(dictionary[each]) == dict:
            map_nested(dictionary[each], transformation)
        else:
            dictionary[each] = transformation(dictionary[each])


################################################
# Parametrizations

alpha1_in_la1 = sp.sympify("4/3") * la1 - sp.sympify("2/3")

substitutions = {
    "planar_alpha_d": {
        alpha3: alpha1 / sp.S(2) - sp.sympify("1/3"),
        d1: sp.sympify("1/140") * (-sp.S(15) * alpha1 - sp.S(6)),
        d2: sp.sympify("1/140") * (sp.S(15) * alpha1 - sp.S(6)),
        d3: z,
        d4: z,
        d5: z,
        d6: z,
        d8: -d7,
    },
    "planar_la1_d": {
        la2: sp.S(1) - la1,
        d1: sp.sympify("1/140") * (-sp.S(15) * alpha1_in_la1 - sp.S(6)),
        d2: sp.sympify("1/140") * (sp.S(15) * alpha1_in_la1 - sp.S(6)),
        d3: z,
        d4: z,
        d5: z,
        d6: z,
        d8: -d7,
    },
}


##################
# N2


def N2_iso():
    return sp.S(1) / sp.S(3) * np.array(sp.eye(3))


def dev2_to_N2(dev2):
    return N2_iso() + dev2


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
    return N2 - N2_iso()


def dev2_transv_x_by_la2():
    reminder = sp.S(1) - sp.S(2) * la2
    N2 = np.array(
        [
            [reminder, z, z],
            [z, la2, z],
            [z, z, la2],
        ],
        dtype=object,
    )
    return N2 - N2_iso()


def dev2_transv_z_by_la2():
    reminder = sp.S(1) - sp.S(2) * la2
    N2 = np.array(
        [
            [la2, z, z],
            [z, la2, z],
            [z, z, reminder],
        ],
        dtype=object,
    )
    return N2 - N2_iso()


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
    return N2 - N2_iso()


def dev2_by_la1_la2_la3():
    N2 = np.array(
        [
            [la1, z, z],
            [z, la2, z],
            [z, z, la3],
        ],
        dtype=object,
    )
    return N2 - N2_iso()


def dev2_planar_by_alpha1():
    return np.array(
        sp.Matrix(dev2_by_alpha1_alpha3()).subs(substitutions["planar_alpha_d"])
    )


def dev2_planar_by_la1():
    return np.array(sp.Matrix(dev2_by_la1_la2()).subs(substitutions["planar_la1_d"]))


dev2s_parametric = {
    "planar": {
        "alpha1": dev2_planar_by_alpha1(),
        "la1": dev2_planar_by_la1(),
    },
    "transv_isotropic": {
        "alpha1": dev2_by_alpha1(),
        "alpha2": dev2_by_alpha2(),
        "alpha3": dev2_by_alpha3(),
        "la1": dev2_transv_by_la1(),
        "la2_x": dev2_transv_x_by_la2(),
        "la2_z": dev2_transv_z_by_la2(),
    },
    "orthotropic": {
        "la1_la2": dev2_by_la1_la2(),
        "la1_la2_la3": dev2_by_la1_la2_la3(),
        "alpha1_alpha3": dev2_by_alpha1_alpha3(),
        "alpha1_alpha2_alpha3": dev2_by_alpha1_alpha2_alpha3(),
    },
}

N2s_parametric = copy.deepcopy(dev2s_parametric)
map_nested(dictionary=N2s_parametric, transformation=dev2_to_N2)

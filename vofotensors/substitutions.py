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
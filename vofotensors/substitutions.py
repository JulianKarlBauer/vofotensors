#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sympy as sp
from vofotensors.numbers import z
from vofotensors.abc import (
    alpha1,
    alpha3,
    la1,
    la2,
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
        d2: sp.sympify("1/140") * (-sp.S(15) * alpha1 - sp.S(6)),
        d3: sp.sympify("1/140") * (sp.S(15) * alpha1 - sp.S(6)),
        d4: z,
        d5: z,
        d6: z,
        d7: z,
        d9: -d8,
    },
    "planar_la1_d": {
        la2: sp.S(1) - la1,
        d2: sp.sympify("1/140") * (-sp.S(15) * alpha1_in_la1 - sp.S(6)),
        d3: sp.sympify("1/140") * (sp.S(15) * alpha1_in_la1 - sp.S(6)),
        d4: z,
        d5: z,
        d6: z,
        d7: z,
        d9: -d8,
    },
}
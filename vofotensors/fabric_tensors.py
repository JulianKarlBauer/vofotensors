#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import sympy as sp
import copy

from collections import defaultdict
from vofotensors import utils
from vofotensors import deviators_2


################################################
# Parametrizations

# Second order

dev2s_parametric = {
    "planar": {
        "alpha1": deviators_2.dev2_planar_by_alpha1(),
        "la1": deviators_2.dev2_planar_by_la1(),
    },
    "transv_isotropic": {
        "alpha1": deviators_2.dev2_by_alpha1(),
        "alpha2": deviators_2.dev2_by_alpha2(),
        "alpha3": deviators_2.dev2_by_alpha3(),
        "la1": deviators_2.dev2_transv_by_la1(),
    },
    "orthotropic": {
        "la1_la2": deviators_2.dev2_by_la1_la2(),
        "la1_la2_la3": deviators_2.dev2_by_la1_la2_la3(),
        "alpha1_alpha3": deviators_2.dev2_by_alpha1_alpha3(),
        "alpha1_alpha2_alpha3": deviators_2.dev2_by_alpha1_alpha2_alpha3(),
    },
}

N2s_parametric = copy.deepcopy(dev2s_parametric)
utils.map_nested(dictionary=N2s_parametric, transformation=utils.dev2_to_N2)

# Fourth order
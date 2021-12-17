#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import sympy as sp
import copy

from collections import defaultdict
from vofotensors import utils
from vofotensors import deviators_2
from vofotensors import deviators_4

################################################
# Parametrizations

#####################
# Second order


N2s_parametric = copy.deepcopy(deviators_2.dev2s_parametric)
utils.map_nested(dictionary=N2s_parametric, transformation=utils.dev2_to_N2)


#####################
# Fourth order


N4s_pairs = {
    "planar": {
        "alpha1_d1_d8": {
            "D2": deviators_2.dev2_planar_by_alpha1(),
            "D4": deviators_4.dev4_planar_alpha1_d1_d8(),
        },
        "la1_d1_d8": {
            "D2": deviators_2.dev2_planar_by_la1(),
            "D4": deviators_4.dev4_planar_la1_d1_d8(),
        },
    },
    "transv_isotropic": {
        "alpha1_rho1": {
            "D2": deviators_2.dev2_by_alpha1(),
            "D4": deviators_4.dev4_transv_x_by_rho1(),
        },
        "alpha2_rho2": {
            "D2": deviators_2.dev2_by_alpha2(),
            "D4": deviators_4.dev4_transv_y_by_rho2(),
        },
        "alpha3_rho3": {
            "D2": deviators_2.dev2_by_alpha3(),
            "D4": deviators_4.dev4_transv_z_by_rho3(),
        },
    },
    "orthotropic": {
        "la1_l2_d1_d2_d3": {
            "D2": deviators_2.dev2_by_la1_la2(),
            "D4": deviators_4.dev4_ortho_by_d1_d2_d3(),
        },
        "alpha1_alpha3_rho1_rho2_rho3": {
            "D2": deviators_2.dev2_by_alpha1_alpha3(),
            "D4": deviators_4.dev4_ortho_by_rho1_rho2_rho3(),
        },
        "alpha1_alpha3_d1_d2_d3": {
            "D2": deviators_2.dev2_by_alpha1_alpha3(),
            "D4": deviators_4.dev4_ortho_by_d1_d2_d3(),
        },
    },
    "monoclinic": {
        "alpha1_alpha3_d1_d2_d3_d4_d5": {
            "D2": deviators_2.dev2_by_alpha1_alpha3(),
            "D4": deviators_4.dev4_monoclinic_by_d1_d2_d3_d4_d5(),
        },
    },
    "triclinic": {
        "la1_la2_d1_d2_d3_d4_d5_d6_d7_d8_d9": {
            "D2": deviators_2.dev2_by_la1_la2(),
            "D4": deviators_4.dev4_triclinic_by_d(),
        },
    },
}

N4s_parametric = {
    key: {key_sub: utils.combine_to_N4(**val_sub) for key_sub, val_sub in val.items()}
    for key, val in N4s_pairs.items()
}

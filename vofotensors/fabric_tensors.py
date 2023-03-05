#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy as _copy
import vofotensors


################################################
# Parametrizations

#####################
# Second order


N2s_parametric = _copy.deepcopy(vofotensors.deviators_2.dev2s_parametric)
vofotensors.utils.map_nested(
    dictionary=N2s_parametric, transformation=vofotensors.utils.dev2_to_N2
)


#####################
# Fourth order

dev2s = vofotensors.deviators_2
dev4s = vofotensors.deviators_4

N4s_pairs = {
    "cubic": {
        "d1": {
            "D2": dev2s.dev2_cubic(),
            "D4": dev4s.dev4_cubic_d1(),
        }
    },
    "planar": {
        "alpha1_d1_d8": {
            "D2": dev2s.dev2_planar_by_alpha1(),
            "D4": dev4s.dev4_planar_alpha1_d1_d8(),
        },
        "la1_d1_d8": {
            "D2": dev2s.dev2_planar_by_la1(),
            "D4": dev4s.dev4_planar_la1_d1_d8(),
        },
    },
    "transv_isotropic": {
        "alpha1_rho1": {
            "D2": dev2s.dev2_by_alpha1(),
            "D4": dev4s.dev4_transv_x_by_rho1(),
        },
        "alpha2_rho2": {
            "D2": dev2s.dev2_by_alpha2(),
            "D4": dev4s.dev4_transv_y_by_rho2(),
        },
        "alpha3_rho3": {
            "D2": dev2s.dev2_by_alpha3(),
            "D4": dev4s.dev4_transv_z_by_rho3(),
        },
    },
    "tetragonal": {
        "alpha1_d1_d3": {
            "D2": dev2s.dev2_by_alpha1(),
            "D4": dev4s.dev4_tetragonal_by_d1_d3(),
        },
    },
    "trigonal": {
        "alpha1_d3_d9": {
            "D2": dev2s.dev2_by_alpha1(),
            "D4": dev4s.dev4_trigonal_by_d3_d9(),
        },
    },
    "orthotropic": {
        "la1_la2_d1_d2_d3": {
            "D2": dev2s.dev2_by_la1_la2(),
            "D4": dev4s.dev4_ortho_by_d1_d2_d3(),
        },
        "alpha1_alpha3_rho1_rho2_rho3": {
            "D2": dev2s.dev2_by_alpha1_alpha3(),
            "D4": dev4s.dev4_ortho_by_rho1_rho2_rho3(),
        },
        "alpha1_alpha3_d1_d2_d3": {
            "D2": dev2s.dev2_by_alpha1_alpha3(),
            "D4": dev4s.dev4_ortho_by_d1_d2_d3(),
        },
    },
    "monoclinic": {
        "alpha1_alpha3_d1_d2_d3_d4_d5": {
            "D2": dev2s.dev2_by_alpha1_alpha3(),
            "D4": dev4s.dev4_monoclinic_by_d1_d2_d3_d4_d5(),
        },
    },
    "triclinic": {
        "la1_la2_d1_d2_d3_d4_d5_d6_d7_d8_d9": {
            "D2": dev2s.dev2_by_la1_la2(),
            "D4": dev4s.dev4_triclinic_by_d(),
        },
    },
}

N4s_parametric = {
    key: {
        key_sub: vofotensors.utils.combine_to_N4(**val_sub)
        for key_sub, val_sub in val.items()
    }
    for key, val in N4s_pairs.items()
}

__all__ = ["N2s_parametric", "N4s_parametric", "N4s_pairs"]

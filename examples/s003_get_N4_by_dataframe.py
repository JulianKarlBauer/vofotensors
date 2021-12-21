#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import sympy as sp
import vofotensors as vot
from vofotensors.abc import alpha1, rho1
import pandas as pd

###################
# Create data

alphas = np.linspace(-1.0 / 3.0, 2.0 / 3.0, 10)
rho_top = alphas / 56.0 + 1.0 / 60.0
rho_bottom = alphas * alphas / 8.0 - alphas / 42.0 - 1.0 / 90.0

boundary = np.concatenate(
    [
        np.stack([alphas, rho_top], axis=1),
        np.stack([alphas, rho_bottom], axis=1)[1:-1],
    ],
    axis=0,
)


df = pd.DataFrame(boundary, columns=["alpha1", "rho1"])

###################
# Get parameterizations

parameterizations = vot.fabric_tensors.N4s_parametric
parameterization = parameterizations["transv_isotropic"]["alpha1_rho1"]

N4_func = sp.lambdify([alpha1, rho1], parameterization)

df["N4"] = df.apply(lambda row: N4_func(alpha1=row["alpha1"], rho1=row["rho1"]), axis=1)
print(df)

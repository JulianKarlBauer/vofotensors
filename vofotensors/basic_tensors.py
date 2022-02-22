#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sympy as sp
import numpy as np
from vofotensors.notation import to_mandel

N2_iso = sp.S(1) / sp.S(3) * np.array(sp.eye(3))


I2 = sp.eye(3)
P1 = to_mandel(sp.tensorproduct(I2, I2)) / sp.S(3)
P2 = sp.eye(6) - P1

N4_iso = sp.S(1) / sp.S(3) * P1 + sp.S(2) / sp.S(15) * P2

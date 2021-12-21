#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import vofotensors as vot


print("Available parameterizations of fourth order fiber orientation tensors:\n")
vot.utils.print_nested(vot.fabric_tensors.N4s_parametric)

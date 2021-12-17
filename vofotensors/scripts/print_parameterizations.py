#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import sympy as sp
import vofotensors as vot
from pprint import pprint


def print_nested(dictionary):
    for each in dictionary:
        if type(dictionary[each]) == dict:
            print("###")
            print("Group:", each)
            print_nested(dictionary[each])
        else:
            print(each)
            pprint(sp.Matrix(dictionary[each]))
            print()


print("Available parameterizations of second order fiber orientation tensors:\n")
print_nested(vot.fabric_tensors.N2s_parametric)

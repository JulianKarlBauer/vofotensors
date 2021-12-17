#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from vofotensors.basic_tensors import N2_iso, N4_iso, I2
from vofotensors import notation
import itertools
import numpy as np
import sympy as sp
from pprint import pprint


def dev2_to_N2(dev2):
    return N2_iso + dev2


def map_nested(dictionary, transformation):
    # https://stackoverflow.com/a/49897410/8935243
    for each in dictionary:
        if type(dictionary[each]) == dict:
            map_nested(dictionary[each], transformation)
        else:
            dictionary[each] = transformation(dictionary[each])


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


def sym(tensor):
    # Get symmetric part of fourth order tensor

    def _by_permutations(tensor, permutations):
        """Symmetrize tensor based on permutations"""
        return (
            sp.S(1)
            / len(permutations)
            * sum(tensor.transpose(perm) for perm in permutations)
        )

    return _by_permutations(
        tensor=np.array(tensor), permutations=list(itertools.permutations([0, 1, 2, 3]))
    )


def combine_to_N4(D2, D4):

    dev2_dyad_I2 = np.array(sp.tensorproduct(I2, sp.Array(D2)))

    part_D2 = notation.to_mandel(sp.S(6) / sp.S(7) * sym(dev2_dyad_I2))

    return N4_iso + part_D2 + D4

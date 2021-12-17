#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from vofotensors.basic_tensors import N2_iso


def dev2_to_N2(dev2):
    return N2_iso + dev2


def map_nested(dictionary, transformation):
    # https://stackoverflow.com/a/49897410/8935243
    for each in dictionary:
        if type(dictionary[each]) == dict:
            map_nested(dictionary[each], transformation)
        else:
            dictionary[each] = transformation(dictionary[each])

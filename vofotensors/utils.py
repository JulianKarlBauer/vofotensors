#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def map_nested(dictionary, transformation):
    # https://stackoverflow.com/a/49897410/8935243
    for each in dictionary:
        if type(dictionary[each]) == dict:
            map_nested(dictionary[each], transformation)
        else:
            dictionary[each] = transformation(dictionary[each])

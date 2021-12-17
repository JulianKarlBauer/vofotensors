#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sympy as sp


def real_symbol(arg):
    return sp.symbols(arg, real=True)


alpha, alpha1, alpha2, alpha3 = real_symbol("alpha alpha1 alpha2 alpha3")
la1, la2, la3 = real_symbol("la1 la2 la3")
rho, rho1, rho2, rho3 = real_symbol("rho rho1 rho2 rho3")
d1, d2, d3, d4, d5, d6, d7, d8, d9 = real_symbol("d1 d2 d3 d4 d5 d6 d7 d8 d9")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sympy as sp


def real_symbol(arg):
    return sp.symbols(arg, real=True)


alpha, alpha_1, alpha_2, alpha_3 = real_symbol("alpha alpha_1 alpha_2 alpha_3")
la1, la2, la3 = real_symbol("la1 la2 la3")
rho, rho_1, rho_2, rho_3 = real_symbol("rho rho_1 rho_2 rho_3")
d1, d2, d3, d4, d5, d6, d7, d8, d9 = real_symbol("d1 d2 d3 d4 d5 d6 d7 d8 d9")



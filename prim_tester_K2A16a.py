#!/usr/bin/python3
#! -*- coding: utf-8 -*-
import math

def prim_test(var):

    test_var = 0

    if var % 2 == 0 and var != 2:
        return False
    elif var == 2:
        return True

    for i in range(3, int(math.sqrt(var) + 1)):
        if var % i == 0:
            return False
    return True

test_case = int(input("Bitte geben sie die zu testende Zahl ein:\n"))

ans = prim_test(test_case)

print(ans)

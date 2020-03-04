#!/usr/bin/python3
#!-*- coding: utf-8 -*-

import time
import sys
import math as m

def fi_s(n):
    """
    Fibonacci in Rekursiv
    :param n: input int
    :return: x als Fibonacci Zahl
    """
    #zeit_g = time.time()

    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        x = fi_s(n - 1) + fi_s(n - 2)
        return x


def fi_f(n):
    """
    Fibonacci in Fast
    :param n: input int
    :return: x als Fibonacci Zahl von n
    """
    x = 1/m.sqrt(5) * (((1 + m.sqrt(5))**n) / 2 - ((1 - m.sqrt(5))**n) / 2 )
    return x

def eingabe():
    """
    Eingabe
    :return: trans
    """
    x = int(input("\nGeben sie eine Zahl ein: "))
    return x

if __name__ == "__main__":

    while True:
        case = input("Wollen sie fast [0] oder slow [1]? ")
        if case == "0":
            trans = eingabe()
            try:
                zeit_1 = time.time()
                ans = fi_f(trans)
                zeit_2 = time.time()
            except ValueError:
                print("Molch")

        elif case == "1":
            trans = eingabe()
            try:
                zeit_1 = time.time()
                ans = fi_s(trans)
                zeit_2 = time.time()
            except ValueError:
                print("Molch")
        else:
            print("[ABBRUCH]")
            sys.exit(12)

        zeit = round(zeit_2 - zeit_1, 6)

        print(f"Antwort: {ans}\nZeit: {zeit} Sekunden")
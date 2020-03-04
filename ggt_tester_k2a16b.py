#!/usr/bin/python3
#!-*- coding: utf-8 -*-



def ggT(a, b):

    print("A: {0}\tB: {1}" .format(a, b))
    Rest = a % b
    print("Rest: ",Rest)

    if Rest != 0:
        ggT(b, Rest)
    else:
        print("ggT:", b)
        return

Save = []
for i in range(0,2):
    Save.append(int(input("Geben sie die Zahlen ein: ")))

ggT(Save[0], Save[1])

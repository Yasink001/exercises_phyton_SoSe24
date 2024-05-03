# -*- coding: utf-8 -*-
"""
Created on Fri May  3 13:07:58 2024

@author: s_kilicm22
"""

## Übung 4.1
quad_zahl = []

for k in range(1,11):
    if k & 1:
        quad_zahl.append(k**2)
    else:
        quad_zahl.append(k)

print(quad_zahl)

## Übung 4.2
quad_zahl2 = [k**2 if k&1 else k for k in range(1,11)]
print(quad_zahl2)

import matplotlib.pyplot as plt
r = 0.5
a = 1
n = 10
summe = 0
s_n = []

for i in range(0,n):
    summe += a*r**i
    s_n.append(summe)

print(s_n)

plt.plot(s_n)
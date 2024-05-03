# -*- coding: utf-8 -*-
"""
Created on Fri May  3 14:39:33 2024

@author: s_kilicm22
"""

## Hausaufgabe
import matplotlib.pyplot as plt

def spar_funktion(AK=10000.00,SR=1000.00,i=0.01,lz=10):
    k = AK
    GK = []
    for k in range(1,lz+1):
        k = k*(1+i)+SR
        GK.append(k)
    return GK

print(spar_funktion())
plt.plot(spar_funktion())
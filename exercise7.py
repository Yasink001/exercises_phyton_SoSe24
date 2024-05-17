# -*- coding: utf-8 -*-
"""
# =============================================================================
# Created on Fri May 17 12:56:24 2024
# 
# @author: s_kilicm22
# """
# 
# def buchstaben_zählen(wort):
#     liste = list(wort)
#     x = len(liste)
#     print (x)
#     
# buchstaben_zählen("Hallo, Berlin")
# 
# =============================================================================
   def buchstaben_zählen_(wort):
       liste = list(wort)
       buchstaben = [i for i in liste if i.isalpha()]
       print(len(buchstaben))
       
buchstaben_zählen_("Hallo, Berlin!")
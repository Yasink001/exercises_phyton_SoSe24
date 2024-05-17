# -*- coding: utf-8 -*-
"""
Created on Fri May 17 14:11:07 2024

@author: s_kilicm22
"""

def vokon_zählen(wort):
    vokalen = "aeiou"
    wort_lower = wort.lower()
    
    bn = [i for i in wort_lower if i.isalpha()]
    vn = [k for k in wort_lower if k in vokalen]
    
    print(f"""Es gibt{len(vn)} Vokalen und {len(bn) -len(Vokalen)} Konsonanten. """)
    
    vokon_zählen("HI,&%/ BerliN!!")
    
    
            
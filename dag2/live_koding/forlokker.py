# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 17:53:54 2020

@author: Marie
"""

handleliste = ["melk", "egg", "sukker", "mel"]
prisliste = [28, 26, 22, 13, 40]

for vare, pris in zip(handleliste, prisliste):
    print(f"Vare: {vare}, Pris: {pris}")
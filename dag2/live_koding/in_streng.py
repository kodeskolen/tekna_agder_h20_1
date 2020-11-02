# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 18:36:08 2020

@author: Marie
"""

tekst = "Dette er litt normal tekst!"
tekst2 = "Her er en tekst som inneholder spam!"

if "spam" in tekst2:
    print("Spam detektert!")
else:
    print("Ingen spam!")
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 18:39:01 2020

@author: Marie
"""

filnavn = ["bilde1.jpeg", "program.exe", "bilde2.jpeg", "screenshot.png"]

for navn in filnavn:
    if ".exe" in navn:
        print(navn)
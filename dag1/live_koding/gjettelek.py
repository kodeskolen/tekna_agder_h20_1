# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 18:35:40 2020

@author: Marie
"""
from random import randint

riktig_tall = randint(0, 100)
maks_forsøk = 10

gjett = int(input("Gjett et tall mellom 0 og 100"))
forsøk = 1
while gjett != riktig_tall and forsøk < maks_forsøk:
    if gjett < riktig_tall:
        print("For lavt!")
    else:
        print("For høyt!")
    gjett = int(input("Gjett et tall mellom 0 og 100"))
    forsøk += 1

if gjett == riktig_tall:
    print("Det var riktig!")
    print("HURRA!!")
else:
    print(f"Du har brukt opp dine {forsøk} forsøk! GAME OVER!!")

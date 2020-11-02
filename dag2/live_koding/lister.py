# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 16:49:15 2020

@author: Marie
"""

navn1 = "Marie"
navn2 = "Hege"
navn3 = "Madeleine"

kule_kodere = ['Marie', "Hege", "Madeleine", "eirik", "Raphael"]

print(kule_kodere[4])

kule_kodere[3] = "Eirik"
print(kule_kodere)
n = len(kule_kodere)
print(kule_kodere[-2])

navn = "Marielle"
if navn in kule_kodere:
    print("Du er med! kult!")
else:
    print("Du er ikke med :(")
    
kule_kodere.append("Millad")
print(kule_kodere)



# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 19:28:33 2020

@author: Marie
"""

# Datamaskinen tenker på et hemmlig ord - LØST!
# Spilleren har et visst antall gjett - LØST!
# For hver runde skal spilleren gjette en bokstav - LØST
# Dersom bokstaven ikke er med i ordet, mister spilleren et av sine gjett -LØST!
# Dersom bokstaven er med i ordet, så får spilleren vite plasseringen til bokstaven - LØST!
# Spillet fortsetter til spilleren er tom for gjett eller det er ingen ukjente bokstaver igjen - LØST!
hemmelig_ord = "hemmelig"
gjett = 3
gjettede_bokstaver = ""
antall_ukjente = len(hemmelig_ord)

while gjett > 0 and antall_ukjente > 0:
    bokstavgjett = input("Gjett en bokstav")
    gjettede_bokstaver += bokstavgjett
    print(f"Gjett så langt: {gjettede_bokstaver}")
    if bokstavgjett not in hemmelig_ord:
        gjett -= 1
    else:
        print("RIKTIG!")
    print(f"Du har {gjett} gjett igjen")
    antall_ukjente = 0
    for bokstav in hemmelig_ord:
        if bokstav in gjettede_bokstaver:
            print(bokstav, end=" ")
        else:
            print("_", end=" ")
            antall_ukjente += 1




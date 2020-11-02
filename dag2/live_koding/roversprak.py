# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 18:41:43 2020

@author: Marie
"""

# Gå igjennom alle bokstavene i et ord - LØST :) 
# Dersom det er en konsonant, så si konsonanten + o + konsonanten - LØST :) 
# Dersom det er en vokal, så si bare vokal - LØST :) 

tekst = input("gi meg tekst:")
tekst = tekst.lower()
konsonanter = "bcdfghjklmnpqrstvwxz"
for bokstav in tekst:
    if bokstav in konsonanter:
        print(bokstav+"o"+bokstav, end="")
    else:
        print(bokstav, end="")

#help(print)

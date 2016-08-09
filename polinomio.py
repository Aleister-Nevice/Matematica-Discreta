#!/usr/bin/python3
#-*-coding: utf-8 -*-
"""
Se n é um inteiro positivo, então n² + n + 41 é primo
"""

import primo

def polinomio(n):
    
    poli = (n**2) + (n) + 41
    
    if not(primo.primo(poli)):
        print ('Não é válido para n = %d, pois %d não é primo' %(n, poli))

# Testa de 1 a 100

for x in range(101):
    polinomio(x)

#!/usr/bin/python3
#-*-coding: utf-8-*-

"""
Implementar uma função que retorne verdadeiro se o número for primo (falso caso contrário). Testar de 1 a 100

Definição de número primo: Um inteiro p é primo se p > 1 e se os únicos divisores positivos de p são 1 e p.
"""

def primo(p):
    if (p <= 1):
        return False
    for n in range (1, p):
        if (p % n == 0 and n != 1 and n != p):
            return False
    else:
        return True

# Teste
if ('__name__' == '__main__'):

    for x in range(1, 101):
        if (primo(x)):
            print (x)

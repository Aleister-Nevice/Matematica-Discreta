#!/usr/bin/python
#-*-coding: utf-8-*-

"""
Solução da questão 09 do capítulo 1

a) Há um número perfeito inferior a 28. Ache-o
b) Escreva um programa de computador para achar o número perfeito imediatamente superior a 28.

As questões podem ser resolvidas ao informar ao programa um número inferior a 28 (letra a) e o número 29 (letra b).

"""

def verifica_perfeito(n):
    
    divisores = []
    soma = 0

    for x in range(1,n):
        if (n%x == 0):
            divisores.append(x)

    for x in (divisores):
        soma = soma + x
     
    if (soma == n):
        print ("O número %d é perfeito" %n)
        #print ("Seus divisores são: " + divisores)
        
        return True

if __name__ == "__main__":
    
    x = input("Entre com o valor inicial de x: ")
    
    while True:
        if (verifica_perfeito(x) == True):
            break
        else:
            x = x + 1

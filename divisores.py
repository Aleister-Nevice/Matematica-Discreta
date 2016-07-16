#!/usr/bin/python
#-*-coding: utf-8-*-
"""
Programa para auxiliar a encontrar as soluçãos da questão 08 do capítulo 1
"""

n = input("Digite um número para saber quantos divisores tem: ")
divisores = []

for x in range (1, n):
    if (n % x == 0):
        divisores.append(x)

tamanho = len(divisores)

print("O número %d tem %d divisores" %(n, tamanho))

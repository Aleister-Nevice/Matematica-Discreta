#!/usr/bin/python
#-*-coding: utf-8-*-
"""
Programa para auxiliar a encontrar as soluçãos da questão 08 do capítulo 1

Obs: No Linux, é preciso dizer ao shell que o texto abaixo é um programa em python, para isso precisamos informar na primeira linha do arquivo o path do Python: usr/bin/python
Já o #-*-coding:utf-8-*- serve para que o interpretador reconheça os caracteres acentuados como à, á, ê, etc.
"""

# Recebe um valor fornecido pelo usuario e o atribui à variável n
n = input("Digite um número para saber quantos divisores tem: ")

# Cria uma lista vazia chamada divisores
divisores = []

# Cria uma variável x cujo valor irá variar de 1 a n-1 (o valor fornecido pelo usuário. ex: para n = 5, x irá variar de 1 a 4)
# O trecho de código dentro do for irá se repetir enquanto x for menor que n
for x in range (1, n):
    # Se o resto da divisão entre n e x for igual a 0 (Ex: para n=1 ocorrerá o seguinte: 5/1, 5/2, 5/3, 5/4 sendo o denominador o valor de x 
    if (n % x == 0):
        # Se o resto da divisão for igual a 0, n é divisível por x. Adicione x à lista divisores
        divisores.append(x)

# A função len() serve para "medir" o tamanho de uma lista. Por exemplo, para x = 6, temos 3 divisores: 1, 2 e 3
tamanho = len(divisores)

# Dentro do print podemos concatenar variáveis usando % , a letra que o segue identifica o tipo de variável
# %d para inteiros , %s para strings, %2.f para float (sendo 2 o número de casas decimais a serem exibidas após a vírgula)
print("O número %d tem %d divisores" %(n, tamanho))

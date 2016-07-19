#!/usr/bin/python
#-*-coding: utf-8-*-

"""
Solução da questão 09 do capítulo 1

a) Há um número perfeito inferior a 28. Ache-o
b) Escreva um programa de computador para achar o número perfeito imediatamente superior a 28.

As questões podem ser resolvidas ao informar ao programa um número inferior a 28 (letra a) e o número 29 (letra b).

"""

# Esstou definindo uma função chamada verifica perfeito que recebe uma variável n como argumento. Uma função é um código que será executado apenas quando chamado
def verifica_perfeito(n):
    
    # Cria uma lista vazia
    divisores = []
    # Cria uma variável soma e lhe atribui o valor 0
    soma = 0

    # O trecho de código dentro do for será executado enquanto x < n. Os valores de x irão variar de 1 a n-1
    for x in range(1,n):
        # Se o resto da divisão entre n e x for = 0
        if (n % x == 0):
            # então adicione x à lista de divisores
            divisores.append(x)
    # A variável x irá percorrer a lista divisores. Ou seja: x assumirá os valores contidos na lista
    for x in (divisores):
        # Aqui a variável soma terá seu próprio valor somado à variável x. (x por sua vez tem o valor de algum número da lista divisores)
        # Ex: Para x = 2 temos:
        # 0 = 0 + 2 -> soma = 2
        # Supondo que o próximo valor de x seja 4:
        # 2 = 2 + 4 -> soma = 6
        soma = soma + x
    
    # Se o total da soma for igual ao número n fornecido como argumento para a função
    if (soma == n):
        print ("O número %d é perfeito" %n)
        print ("Seus divisores são: " + divisores)
        
        # Toda função retorna algo. Neste caso, a função verifica_perfeito retorna uma variável booleana cujo valor é True
        return True

# Um programa Python pode ser executado de duas formas:
# I - Sendo importado por outro programa Python
# II - Sendo executado diretamente. 
# A linha abaixo diz que o trecho de código dentro do if deve ser executado apenas se este programa estiver sendo executado diretamente e não quando for importado por outro programa
if __name__ == "__main__":
    
    # Recebe um valor digitado pelo usuário e o atribui à variável v
    v = input("Entre com o valor inicial de v: ")
    
    # O trecho de código dentro do While irá se repetir infinitamente, pois a condição dada (True) é sempre verdadeira
    while True:
        # Chama a função verifica_perfeito() e envia como argumento a variável v cujo valor foi informado pelo usuário.
        # Se a função retornar True
        if (verifica_perfeito(v) == True):
            # Pare a repetição while
            break
        # Senão
        else:
            # Pegue o valor informado pelo usuário, some a 1 e repita o programa
            v = v + 1

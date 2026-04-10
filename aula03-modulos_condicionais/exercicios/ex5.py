'''
Faça um programa que leia 2 valores inteiros (A e B).
A seguir, o programa deve mostrar uma mensagem "São Múltiplos" ou "Não são Múltiplos", indicando
se os valores lidos são múltiplos entre si.
'''

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
aux = 0

if(num2 > num1):
    aux = num2
    num2 = num1
    num1 = aux

def verificar_multiplos(n1, n2):
    return n1 % n2 == 0

resultado = verificar_multiplos(num1, num2)

if(resultado):
    print(f"{num1} e {num2} são múltiplos.")
else:
    print(f"{num1} e {num2} NÃO são múltiplos.")
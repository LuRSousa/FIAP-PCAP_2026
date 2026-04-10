'''
Faça um programa que leia 3 valores que representam os lados de um triângulo A, B e C e ordene-os
em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o
tipo de triângulo que estes três lados formam, com base nos seguintes casos:
-Se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO;
-Se A² = B² + C² , apresente a mensagem: TRIANGULO RETANGULO;
-Se A² > B² + C² , apresente a mensagem: TRIANGULO OBTUSANGULO;
-Se A² < B² + C² , apresente a mensagem: TRIANGULO ACUTANGULO;
-Se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO;
-Se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES;
'''

ladoA = int(input("Digite o primeiro lado do triângulo: "))
ladoB = int(input("Digite o segundo lado do triângulo: "))
ladoC = int(input("Digite o terceiro lado do triângulo: "))

if(ladoB > ladoA):
    aux = ladoB
    ladoB = ladoA
    ladoA = aux
if(ladoC > ladoA):
    aux = ladoC
    ladoC = ladoA
    ladoA = aux

def calcular_angulo(a, b, c):
    if(a >= b + c):
        print("Não forma triângulo.")
    elif(a**2 == b**2 + c**2):
        print("Triângulo Retângulo")
    elif(a**2 > b**2 + c**2):
        print("Triângulo Obtusângulo")
    elif(a**2 < b**2 + c**2):
        print("Triângulo Acutângulo")

def calcular_lados(a, b, c):
    if(a >= b + c):
        print("Não forma triângulo.")
    elif(a == b and b == c):
        print("Triângulo Equilátero")
    elif(a == b or a == c or b == c):
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")

calcular_angulo(ladoA, ladoB, ladoC)
calcular_lados(ladoA, ladoB, ladoC)
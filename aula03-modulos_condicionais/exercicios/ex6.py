'''
Escreva um algoritmo que recebe dois números e um caractere (representando uma das operações
matemáticas (+, -, *, /)
O programa deve calcular o valor final de acordo com a operação selecionada.
Ou seja, se a entrada for 5, 6 e *, então seu programa dever mostrar 30.
'''

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
ope = input("Digite a operação a ser feita ('+', '-', '*', '/'): ")

def calculadora(n1, n2, o):
    if(o == "+"):
        print(f"{n1} + {n2} = {n1 + n2}")
    elif(o == "-"):
        print(f"{n1} - {n2} = {n1 - n2}")
    elif(o == "*"):
        print(f"{n1} * {n2} = {n1 * n2}")
    elif(o == "/"):
        print(f"{n1} / {n2} = {round(n1 / n2, 1)}")
    else:
        print("Digite uma operação válida.")

calculadora(num1, num2, ope)
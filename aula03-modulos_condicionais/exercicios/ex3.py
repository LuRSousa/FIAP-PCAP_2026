#Faça um programa que peça dois números e imprima o maior deles, e informe caso eles sejam iguais

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

def comparar_nums(num1, num2):
    if(num1 > num2):
        print(f"{num1} é maior que {num2}.")
    elif(num2 > num1):
        print(f"{num2} é maior que {num1}.")
    else:
        print(f"{num1} e {num2} são iguais.")

comparar_nums(num1, num2)
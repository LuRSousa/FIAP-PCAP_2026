#Faça um programa que peça dois números e imprima o maior deles, e informe caso eles sejam iguais

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

def comparar_nums(n1, n2):
    if(n1 > n2):
        print(f"{n1} é maior que {n2}.")
    elif(n2 > n1):
        print(f"{n2} é maior que {n1}.")
    else:
        print(f"{n1} e {n2} são iguais.")

comparar_nums(num1, num2)
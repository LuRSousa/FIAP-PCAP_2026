#Faça um programa que leia um número, e informe se ele é par ou impar

print("Verificador de Número Par ou Ímpar")
print()

num = int(input("Digite um número para verificação: "))

def verificador_par(num):
    return num % 2 == 0

resultado = verificador_par(num)

if(resultado):
    print(f"O número {num} é par!")
else:
    print(f"O número {num} é ímpar!")
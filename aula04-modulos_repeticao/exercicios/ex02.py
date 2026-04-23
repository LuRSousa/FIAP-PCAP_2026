#Escreva um programa que dadas duas notas de 0  10 calcula a média aritimética entre elas.
def validar_nota(nota):
    nota_aux = nota

    while nota_aux < 0 or nota_aux > 10:
        print("A nota deve estar entre 0 e 10!")
        nota_aux = float(input("Digite novamente a nota: "))
    
    return nota_aux



notaA = float(input("Digite a primeira nota: "))
notaA = validar_nota(notaA)

notaB = float(input("Digite a segunda nota: "))
notaB = validar_nota(notaB)

media = (notaA + notaB) / 2
print(f"A média é: {media}")
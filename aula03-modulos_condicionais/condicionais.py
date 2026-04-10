nota_final = 3

if nota_final < 6:
    print("Reprovado")

print("Fim")
print()

nota1 = float(input("Nota da CP 1: "))
nota2 = float(input("Nota da CP 2: "))
nota3 = float(input("Nota da CP 3: "))

def calcular_media(nota1, nota2, nota3):
    if(nota1 < 0 or nota2 < 0 or nota3 < 0):
        print("Nota não pode ser menor que 0!")
        return -1
    elif(nota1 > 10 or nota2 > 10 or nota3 > 10):
        print("Nota não pode ser maior que 10!")
        return -1
    
    return round((nota1 + nota2 + nota3) / 3, 2)

def resultado_final(media):
    print(f"Média: {media}")
    if(media < 0):
        print("Erro no cálculo da média")
    elif(0 <= media and media < 4):
        print("Status: Reprovado")
    elif(media <= 6):
        print("Status: Recuperação")
    elif(media <= 10):
        print("Aprovado")


media = calcular_media(nota1, nota2, nota3)
resultado_final(media)
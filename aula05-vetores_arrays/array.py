lista_frutas = ["Banana", "Maçã", "Morango"]

print(lista_frutas[1])

lista_frutas.append("Pera")
print(lista_frutas)

qnt_frutas = len(lista_frutas)
print("Qnt de frutas: ", qnt_frutas)

print()

for i in range(qnt_frutas):
    print(lista_frutas[i])

print()

for c in lista_frutas:
    print(c)
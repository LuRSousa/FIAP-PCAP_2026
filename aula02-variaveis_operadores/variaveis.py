print("Hello World 2")
print(7 + 4)
print("7 + 4")
print("7" + "4") #concatenando strings

'''
comentários 
de 
múltiplas 
linhas
'''

nome = "Lucas" #str
idade = 18 #int
peso = 64.5 #float

print(nome, idade, peso)

print(f"Bem Vindo, {nome}")

#Input

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
print(nome, idade, peso)

print(idade + 1)

ano_nascimento = 2007
ano_atual = 2026

idade = ano_atual - ano_nascimento
print(f"Sua idade é {idade}")
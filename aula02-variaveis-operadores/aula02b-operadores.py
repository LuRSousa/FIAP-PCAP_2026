num1 = 5
num2 = 2

print(type(num1), type(num2))

operacao = num1 + num2
print(operacao, type(operacao))

#operadores de atribuição
num = 15
print() #pula linha
print(num)

num = num + 2
print(num)

num *= 2
print(num)

#operadores relacionais
print()
print(6 > 2)
print(6 == 4)
print()

idade = 20
print(idade >= 21)

logado = True
print(logado, type(logado))

maior_idade = idade >= 18
print(maior_idade, type(maior_idade))
print()

#strings
nome1 = "Marcos"
nome2 = "marcos"

print(nome1 == nome2)
print(nome1.lower() == nome2.lower())
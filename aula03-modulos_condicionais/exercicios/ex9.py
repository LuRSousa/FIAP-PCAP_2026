'''
Faça um programa que recebe:
-o código do estado de origem da carga de um caminhão, supondo que é um número inteiro de 1 a 5
-o peso da carga do caminhão em toneladas
-o código da carga, supondo que é um número inteiro de 10 e 40

Seu programa deve calcular:
-o peso da carga do caminhão convertido em quilos
-o preço da carga do caminhão
-valor do imposto que e cobrado com base no preço da carga e do estado de origem
-o valor total transportado pelo caminhão (carga + impostos)

estado: 1, 2, 3, 4, 5
imposto: 35%, 25%, 15%, 5%, isento

codigo da carga: 10 a 20, 21 a 30, 31 a 40
preço: 100, 250, 340
'''

estado = int(input("Digite o código do estado de origem da carga (1 a 5): "))
peso_ton = float(input("Digite o peso da carga do caminhão em toneladas: "))
codigo_carga = int(input("Digite o código da carga (10 a 40): "))

peso_kg = peso_ton * 1000

def calcular_preco_carga(c):
    if(10 <= c and c <= 20):
        return peso_kg * 100
    elif(21 <= c and c <= 30):
        return peso_kg * 250
    elif(31 <= c and c <= 40):
        return peso_kg * 340
    else:
        return -1

def calcular_imposto(e):
    match (e):
        case 1:
            return 0.35
        case 2:
            return 0.25
        case 3:
            return 0.15
        case 4:
            return 0.05
        case 5:
            return 0
        case _:
            return -1

preco_carga = calcular_preco_carga(codigo_carga)
imposto = calcular_imposto(estado)

def calcular_total(p, i):
    valor_imposto = i * p
    total = valor_imposto + p

    print(f"Peso em Kg: {peso_kg}Kg \nPreço da Carga: R${preco_carga} \n Imposto: {i*100}% \n Valor do Imposto: R${valor_imposto} \n Valor Total: R${total}")

calcular_total(preco_carga, imposto)
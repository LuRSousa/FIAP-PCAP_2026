'''
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado
no salário atual:
Salários até R$ 280,00 (incluindo): aumento de 20%.
Salários entre R$ 280,00 e R$ 700,00: aumento de 15%.
Salários entre R$ 700,00 e R$ 1500,00: aumento de 10%.
Salários de R$ 1500,00 em diante: aumento de 5%.

Após o aumento ser realizado, informe na tela:
O salário antes do reajuste.
O percentual de aumento aplicado.
O valor do aumento.
O novo salário, após o aumento.
'''

salario_inicial = float(input("Digite o salário do colaborador em R$: "))

def calcular_aumento(s):
    porcento = 0

    if(s <= 280.00):
        porcento = 20
    elif(s < 700.00):
        porcento = 15
    elif(s < 1500.00):
        porcento = 10
    else:
        porcento = 5

    aumento = s * porcento / 100
    salario_final = s + aumento

    print(f"Salário Inicial: R${s} \nPercentual Aumentado: {porcento}% \nAumento: R${aumento} \nSalário Final: R${salario_final}")

calcular_aumento(salario_inicial)


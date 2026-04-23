#Faça um programa que receba a quant. de produtos que o usuário deseja

qnt_produtos = int(input("Digie a quantidade de produtos: "))

for i in range(qnt_produtos):
    print(f"Produto: {i+1}")
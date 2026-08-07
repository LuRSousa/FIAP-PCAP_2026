endpoints = ["/login", "/produtos", "/pedidos"]
 
status = [
    [200, 200, 401, 200, 500],
    [200, 200, 200, 200, 200],
    [201, 500, 502, 201, 500]
]
 
def validador(stat):
    if stat >= 200 and stat <= 299:
        return 1
    else:
        return 0
 
endpoints_criticos = []
endpoints_estaveis = []
endpoints_instaveis = []

for e in range(len(status)):
    #1.
    tamanho_endpoint = len(status[e])
    qnt_sucessos = 0
    for i in range(tamanho_endpoint):
        if(validador(status[e][i])):
            qnt_sucessos += 1
            
    porcentagem_acertos = qnt_sucessos/tamanho_endpoint * 100
    
    print(f"Endpoint: '{endpoints[e]}' teve {porcentagem_acertos}% das requisições bem-sucedidas.")
    
    #2.
    menor_porcentagem = 100
    endpoint_pior = -1
    
    if(porcentagem_acertos < menor_porcentagem):
        menor_porcentagem = porcentagem_acertos
        endpoint_pior = e
    #3.
    for f in range(tamanho_endpoint - 1):
        if(not(validador(status[e][f])) and not(validador(status[e][f+1]))):
            endpoints_criticos.append(e)
            
    if(porcentagem_acertos >= 80):
        endpoints_estaveis.append(e)
    elif(porcentagem_acertos < 80):
        endpoints_instaveis.append(e)
        
print("")
print(f"O endpoint com mais erros é o: {endpoints[endpoint_pior]}")
 
print("")
print("O(s) seguinte(s) endpoint(s) tiveram 2 erros seguidos: ")
for g in endpoints_criticos:
    print(f"-{endpoints[g]}")
    
print("")
print("Endpoint estáveis: ")
for p in endpoints_estaveis:
    print(f"-{endpoints[p]}")
    
print("Endpoint instáveis: ")
for q in endpoints_instaveis:
    print(f"-{endpoints[q]}")

print("Endpoint críticos: ")
for r in endpoints_criticos:
    print(f"-{endpoints[r]}")


    

